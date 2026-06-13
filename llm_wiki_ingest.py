#!/usr/bin/env python3
"""
llm_wiki_ingest.py — LLM Wiki arXiv ingester (Oracle)
Pipeline:
  arXiv API → new papers → SQLite dedup → Anthropic score (skip < 7)
  → Anthropic summarize + categorize → markdown to llm-wiki/ → DB record

Cron: Sunday 04:00 CT
  0 4 * * 0 python3 -u ~/llm-wiki/scripts/llm_wiki_ingest.py >> ~/logs/llm_wiki_ingest.log 2>&1
"""

import os, sys, json, re, time, sqlite3, textwrap, requests
from pathlib import Path
from datetime import datetime, timezone
import arxiv

WIKI_DIR  = Path.home() / "llm-wiki"
DB_PATH   = WIKI_DIR / "llm-wiki.db"
LOG_DIR   = Path.home() / "logs"
RELEVANCE_THRESHOLD = 7

SEARCH_QUERIES = [
    "large language model agents memory",
    "multi-agent LLM orchestration",
    "model context protocol MCP tool use",
    "transformer inference optimization",
    "retrieval augmented generation RAG",
    "LLM alignment RLHF DPO fine-tuning",
    "mixture of experts sparse LLM",
    "LLM quantization inference efficiency",
    "autonomous AI agents planning",
    "LLM context window long context",
]

CATEGORIES = {
    "memory-systems":      "vector DBs, RAG, memory, embeddings, KV cache",
    "agent-architectures": "agents, planning, multi-agent, orchestration, tool use",
    "concepts":            "core LLM techniques, architectures, training methods",
    "entities":            "specific models, tools, frameworks, organizations",
    "comparisons":         "side-by-side analysis of two or more approaches",
    "general":             "LLM research not fitting other categories",
}

FOLDER_MAP = {
    "memory-systems":      "concepts",
    "agent-architectures": "concepts",
    "concepts":            "concepts",
    "entities":            "entities",
    "comparisons":         "comparisons",
    "general":             "concepts",
}

def load_env(path):
    p = Path(path)
    if not p.exists(): return
    for line in p.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line: continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

load_env(Path.home() / "archonos/.env")
load_env(Path.home() / ".env")

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

def check_deps():
    missing = []
    if not ANTHROPIC_API_KEY: missing.append("ANTHROPIC_API_KEY")
    if not DB_PATH.exists():  missing.append(f"DB: {DB_PATH}")
    if missing:
        print(f"[FAIL] {', '.join(missing)}")
        sys.exit(1)

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def paper_exists(conn, arxiv_id):
    return conn.execute("SELECT 1 FROM papers WHERE arxiv_id=?", (arxiv_id,)).fetchone() is not None

def insert_paper(conn, data):
    conn.execute("""
        INSERT OR IGNORE INTO papers
        (arxiv_id,title,authors,abstract,published,category,
         relevance_score,summary,key_concepts,archonos_applicability,md_path)
        VALUES (:arxiv_id,:title,:authors,:abstract,:published,:category,
                :relevance_score,:summary,:key_concepts,:archonos_applicability,:md_path)
    """, data)
    conn.commit()

def search_arxiv(query, max_results=15):
    client = arxiv.Client(page_size=max_results, delay_seconds=2)
    search = arxiv.Search(query=query, max_results=max_results,
                          sort_by=arxiv.SortCriterion.SubmittedDate)
    results = []
    for r in client.results(search):
        results.append({
            "arxiv_id": r.entry_id.split("/")[-1],
            "title":    r.title,
            "authors":  ", ".join(a.name for a in r.authors[:5]),
            "abstract": r.summary.replace("\n", " "),
            "published": r.published.strftime("%Y-%m-%d"),
        })
    return results

def discover_new_papers(conn):
    seen, all_papers = set(), []
    for query in SEARCH_QUERIES:
        print(f"  [search] {query}")
        try:
            for p in search_arxiv(query):
                aid = p["arxiv_id"]
                if aid not in seen and not paper_exists(conn, aid):
                    seen.add(aid)
                    all_papers.append(p)
            time.sleep(1)
        except Exception as e:
            print(f"  [WARN] {e}")
    print(f"  [discover] {len(all_papers)} new papers")
    return all_papers

def anthropic_call(messages, system, max_tokens=1000):
    r = requests.post("https://api.anthropic.com/v1/messages",
        headers={"x-api-key": ANTHROPIC_API_KEY,
                 "anthropic-version": "2023-06-01",
                 "content-type": "application/json"},
        json={"model": "claude-haiku-4-5-20251001", "max_tokens": max_tokens,
              "system": system, "messages": messages},
        timeout=60)
    r.raise_for_status()
    return r.json()["content"][0]["text"].strip()

def score_paper(paper):
    system = (
        "Score this arXiv paper 1-10 for relevance to ArchonOS — a homelab AI agent OS "
        "with distributed agents, pgvector memory, MCP tools, LLM orchestration. "
        "10=agent memory/MCP/inference optimization, 7-9=core LLM techniques, "
        "4-6=general ML, 1-3=unrelated. Respond with ONLY a single integer."
    )
    prompt = f"Title: {paper['title']}\nAuthors: {paper['authors']}\n\nAbstract:\n{paper['abstract']}"
    try:
        result = anthropic_call([{"role": "user", "content": prompt}], system, max_tokens=10)
        return min(10, max(1, int(re.search(r'\d+', result).group())))
    except Exception as e:
        print(f"  [WARN] score: {e}")
        return 0

def summarize_paper(paper):
    cat_desc = "\n".join(f"  - {k}: {v}" for k, v in CATEGORIES.items())
    system = ("You write concise wiki entries for LLM research. "
              "Audience: experienced ML engineer. Direct, specific, no fluff.")
    prompt = textwrap.dedent(f"""
        Paper: "{paper['title']}"
        Authors: {paper['authors']} | Published: {paper['published']}
        arXiv: https://arxiv.org/abs/{paper['arxiv_id']}

        Abstract: {paper['abstract']}

        Return ONLY valid JSON (no fences):
        {{
          "category": "<memory-systems|agent-architectures|concepts|entities|comparisons|general>",
          "slug": "<kebab-case>",
          "title": "<concise wiki title>",
          "summary": "<2-3 sentence technical summary>",
          "key_concepts": ["<c1>","<c2>","<c3>"],
          "archonos_applicability": "<1-2 sentences>"
        }}

        Categories:
        {cat_desc}
    """).strip()
    result = None
    try:
        result = anthropic_call([{"role": "user", "content": prompt}], system, max_tokens=600)
        result = re.sub(r'^```json\s*', '', result).rstrip('`').strip()
        return json.loads(result)
    except Exception as e:
        print(f"  [WARN] summarize: {e} | {str(result)[:80] if result else ''}")
        return None

def build_markdown(paper, entry, score):
    concepts = "\n".join(f"- {c}" for c in entry.get("key_concepts", []))
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return f"""---
arxiv_id: "{paper['arxiv_id']}"
authors: "{paper['authors']}"
published: "{paper['published']}"
ingested: "{today}"
score: {score}
category: "{entry['category']}"
---

# {entry['title']}

> **Paper:** [{paper['title']}](https://arxiv.org/abs/{paper['arxiv_id']})
> **Authors:** {paper['authors']} · **Published:** {paper['published']} · **Score:** {score}/10

## Summary

{entry['summary']}

## Key Concepts

{concepts}

## ArchonOS Applicability

{entry['archonos_applicability']}

## Abstract

{paper['abstract']}

---

`#{entry['category']}` `#arxiv` `#auto-ingested`
"""

def update_sidebar(entry):
    sidebar_path = WIKI_DIR / "_sidebar.md"
    if not sidebar_path.exists(): return
    folder = FOLDER_MAP.get(entry["category"], "concepts")
    new_line = f"  - [{entry['title']}]({folder}/{entry['slug']}.md)"
    sidebar = sidebar_path.read_text()
    if new_line in sidebar: return
    display = {"memory-systems": "Memory Systems", "agent-architectures": "Agent Architectures",
               "concepts": "Concepts", "entities": "Entities",
               "comparisons": "Comparisons", "general": "General"}.get(
               entry["category"], entry["category"].title())
    lines = sidebar.splitlines()
    insert_at = None
    for i, line in enumerate(lines):
        if f"**{display}**" in line:
            for j in range(i+1, len(lines)):
                if lines[j].strip().startswith("- ["):
                    if not lines[j].startswith("  "): break
                    insert_at = j + 1
            if insert_at is None: insert_at = i + 1
            break
    if insert_at is None: insert_at = len(lines)
    lines.insert(insert_at, new_line)
    sidebar_path.write_text("\n".join(lines) + "\n")
    print(f"  [sidebar] updated")

def main():
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    print(f"[llm_wiki_ingest] {datetime.now().strftime('%Y-%m-%d %H:%M CT')}")
    check_deps()
    conn = get_db()

    print("[1] Discovering papers ...")
    papers = discover_new_papers(conn)
    if not papers:
        print("[OK] No new papers.")
        conn.close()
        return

    ingested = skipped_score = skipped_error = 0

    for i, paper in enumerate(papers):
        aid = paper["arxiv_id"]
        print(f"\n[{i+1}/{len(papers)}] {paper['title'][:55]} ({aid})")

        score = score_paper(paper)
        print(f"  [score] {score}/10")

        if score < RELEVANCE_THRESHOLD:
            insert_paper(conn, {**paper, "category": "skipped", "relevance_score": score,
                                "summary": None, "key_concepts": None,
                                "archonos_applicability": None, "md_path": None})
            skipped_score += 1
            continue

        print(f"  [summarize] ...")
        entry = summarize_paper(paper)
        if not entry:
            skipped_error += 1
            continue

        folder = FOLDER_MAP.get(entry["category"], "concepts")
        md_path = WIKI_DIR / folder / f"{entry['slug']}.md"
        md_path.parent.mkdir(parents=True, exist_ok=True)
        raw_path = WIKI_DIR / "raw" / f"{aid}.md"

        try:
            md = build_markdown(paper, entry, score)
            md_path.write_text(md)
            raw_path.write_text(md)
            update_sidebar(entry)
            insert_paper(conn, {**paper, "category": entry["category"],
                                "relevance_score": score, "summary": entry["summary"],
                                "key_concepts": json.dumps(entry.get("key_concepts",[])),
                                "archonos_applicability": entry["archonos_applicability"],
                                "md_path": str(md_path)})
            ingested += 1
            print(f"  [OK] {md_path}")
        except Exception as e:
            print(f"  [FAIL] {e}")
            skipped_error += 1

        time.sleep(1)

    conn.close()
    print(f"\n[done] {ingested} ingested · {skipped_score} low score · {skipped_error} errors")

if __name__ == "__main__":
    main()
