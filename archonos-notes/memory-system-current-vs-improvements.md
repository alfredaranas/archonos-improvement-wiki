# ArchonOS Memory System — Current State vs. Improvement Roadmap

> **Prerequisite:** Read [Memory System Architecture](archonos-memory-system-architecture.md) first — this document builds on the full 6-layer inventory.

**Last updated:** 2026-05-31

---

## Overview

This document maps every memory gap identified in the architecture audit to a concrete improvement suggestion, prioritized by impact and effort. Each row shows: what exists now → what's missing → what to build.

---

## Priority Rankings

| Priority | Label | Effort | Impact |
|----------|-------|--------|--------|
| P0 | Quick win | Hours | High |
| P1 | Moderate build | Days | High |
| P2 | Significant | Weeks | Very high |
| P3 | Strategic | Months | Transformative |

---

## 1. Search Gap — SupaBrain Cloud

**Current state:** PostgreSQL `ILIKE` pattern matching only. No vector embeddings, no FTS tsvector/tsquery indexes on suprabrain or agent_memory.

| Dimension | Current | Target |
|-----------|---------|--------|
| Search type | Substring match (`ILIKE %query%`) | Semantic + FTS hybrid |
| Relevance ranking | None (chronological order) | Vector similarity + tsvector rank |
| Query flexibility | Exact terms only | Synonyms, concepts, fuzzy |
| Speed on 10K rows | ~50ms (sequential scan) | ~5ms (indexed) |

### Improvement Path

**P0 — Deploy pgvector index** (hours)
```sql
-- Extension already available in Supabase, just needs enabling
CREATE EXTENSION IF NOT EXISTS vector;

-- Add embedding column
ALTER TABLE suprabrain ADD COLUMN embedding vector(1536);

-- Create index
CREATE INDEX ON suprabrain USING ivfflat (embedding vector_cosine_ops);

-- Backfill: embed existing entries via a cron job
```

**P0 — Add FTS tsvector column** (hours)
```sql
ALTER TABLE suprabrain ADD COLUMN search_vector tsvector
  GENERATED ALWAYS AS (to_tsvector('english', title || ' ' || content)) STORED;

CREATE INDEX suprabrain_fts_idx ON suprabrain USING GIN(search_vector);
```

**P1 — Embedding pipeline cron** (days)
- Cron job: every 6 hours, find entries without embeddings, call Ollama/API to generate embeddings, update row
- Starting point: `nomic-embed-text` on local Ollama (free, fast, 768d) or OpenAI `text-embedding-3-small` (1536d, $0.02/1M tokens)

---

## 2. Memory Consolidation Gap

**Current state:** `agent_memory` accumulates entries indefinitely. Each archon writes working memory logs (yoda_shell, service events, boot records) but nothing ever distills them into long-term `suprabrain` entries.

| Dimension | Current | Target |
|-----------|---------|--------|
| Working → Long-term | Never happens | Weekly consolidation cron |
| Duplicate detection | None | Dedup by content hash |
| Compression | Each entry standalone | Summarize repeated patterns |
| Entry lifecycle | Created once, never updated | Created → refined → promoted → archived |

### Improvement Path

**P0 — Memory consolidation cron** (hours)
```python
# Pseudocode for the consolidation cron
# Runs weekly, reads agent_memory from last 7 days
# Groups by topic (title similarity, source)
# For each group: LLM summarizes into a single suprabrain entry
# Tags with source="consolidation" and agent_id="memory-cron"
```

**P1 — Entry lifecycle** (days)
- Add `status` column to agent_memory: `active | consolidated | archived`
- After consolidation, mark source entries as `consolidated`
- After 30 days, move `consolidated` entries to an archive table
- Add `source_entry_ids` JSON field to suprabrain showing which agent_memory entries fed into it

---

## 3. Telemetry Gap

**Current state:** Zero metrics track whether SupaBrain lookups change agent behavior. No way to measure if memory retrieval is actually helping.

| Dimension | Current | Target |
|-----------|---------|--------|
| Memory hit rate | No measurement | Track per-query hit/miss |
| Impact on output | No measurement | Track whether retrieved memory altered response |
| A/B testing | Impossible | Compare ILIKE vs vector vs hybrid |
| Dashboard | None | Grafana panel on memory performance |

### Improvement Path

**P1 — Memory telemetry** (days)
- Add a `memory_query_log` table in Supabase:
  ```sql
  CREATE TABLE memory_query_log (
    id UUID PRIMARY KEY,
    query_text TEXT,
    search_type TEXT,       -- 'iliKE', 'vector', 'hybrid'
    result_count INT,
    top_result_id UUID,
    top_score FLOAT,
    latency_ms INT,
    agent_id TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
  );
  ```
- MCP `supabrain_search` writes a log row every call
- Weekly cron analyzes: average latency, result count distribution, zero-result rate

**P2 — Impact measurement** (weeks)
- Log the full conversation context before and after memory injection
- Compare: does the agent's response change when memory is present vs absent?
- This is a research project — needs careful experimental design

---

## 4. Cross-Layer Search Gap

**Current state:** Three separate search interfaces with no unified query.

| Store | Search Tool | Interface |
|-------|------------|-----------|
| Vault | `search_files` (ripgrep) | Terminal regex |
| Sessions | `session_search` (FTS5) | Tool call |
| SupaBrain | `supabrain_search` (ILIKE) | MCP tool |

**Target:** A single `memory_search(query, layers=[...])` tool that queries selected layers and returns merged, deduplicated results.

### Improvement Path

**P2 — Unified search gateway** (weeks)
- Build a Python MCP tool that:
  1. Accepts query + layer filter + limit
  2. Fans out to each selected layer in parallel
  3. Merges results (dedup by content hash)
  4. Ranks by a combined score
  5. Returns unified JSON

```python
@mcp.tool
async def memory_search(
    query: str,
    layers: list[str] = ["supabrain", "vault", "sessions"],
    limit: int = 5
) -> str:
    """Unified search across memory layers."""
    results = []
    tasks = []
    if "supabrain" in layers:
        tasks.append(search_supabrain(query, limit))
    if "vault" in layers:
        tasks.append(search_vault(query, limit))
    if "sessions" in layers:
        tasks.append(search_sessions(query, limit))
    for r in await asyncio.gather(*tasks):
        results.extend(r)
    results.sort(key=lambda x: x["score"], reverse=True)
    return json.dumps(results[:limit], indent=2)
```

---

## 5. Tag Utilization Gap

**Current state:** `tags` column exists in suprabrain schema (JSONB) but is inconsistently populated. No tag browsing, filtering, or autocomplete.

| Dimension | Current | Target |
|-----------|---------|--------|
| Tag usage | Optional, inconsistent | Mandatory for new entries |
| Tag browser | None | Sidebar or filter UI |
| Autocomplete | None | Suggest tags from existing corpus |
| Tag hierarchy | Flat | Optional nested tags (memory/vector, agent/archon) |

### Improvement Path

**P0 — Tag hygiene** (hours)
- Backfill existing entries via a one-shot script: LLM reads each entry and assigns 2-4 tags
- Add a MCP tool helper that validates tags before write

**P1 — Tag browser** (days)
- Supabase materialized view: `SELECT tags, COUNT(*) FROM suprabrain GROUP BY tags`
- Simple MCP tool: `supabrain_tags()` returns tag cloud with counts
- Claude.ai can use this to build a dynamic filter

---

## 6. Memory Compression Gap

**Current state:** Every Hermes memory entry is injected into the agent's context every turn. No dedup, no compression, no expiry.

| Dimension | Current | Target |
|-----------|---------|--------|
| Context injection | Full raw entries | Compressed, deduped |
| Duplicate prevention | None | Hash-based dedup on write |
| Entry expiry | Never | Auto-expire after N days |
| Priority | All equal | Rank by recency + relevance + access count |

### Improvement Path

**P1 — Memory compressor** (days)
- Cron job: read all memory entries, ask an LLM to compress similar entries into one
- For example: 5 entries about "prefers concise responses" → 1 entry "communication: concise"
- Reduces context token consumption
- Implementation: same pattern as the consolidation cron

---

## 7. Cross-Archon Synchronization Gap

**Current state:** Oracle, Yoda, and Sentinel each run their own Hermes instance with their own local memory stores. No mechanism syncs learnings between them.

| Dimension | Current | Target |
|-----------|---------|--------|
| Shared learning | Manual (write to suprabrain) | Automatic sync via suprabrain |
| Archon-specific memory | Local SQLite only | Local + cloud dual-write |
| Conflict resolution | N/A | Timestamp-based last-write-wins |

### Improvement Path

**P3 — Cross-archon memory sync** (months)
- When an archon saves a memory note, dual-write to local SQLite + suprabrain
- Each archon's session boot reads: local memories + relevant suprabrain entries
- Suprabrain stores per-archon preferences with `agent_id` field

---

## Priority Implementation Order

```
WEEK 1 (P0 — hours each)
├── Deploy pgvector extension on Supabase
├── Add FTS tsvector column to suprabrain
├── Backfill tags on existing suprabrain entries
└── Create memory consolidation cron

WEEK 2-3 (P1 — days each)
├── Embedding pipeline cron (backfill + ongoing)
├── Memory entry lifecycle (status, archive)
├── Memory telemetry logging
├── Memory compressor cron
└── Tag browser MCP tool

MONTH 2 (P2 — weeks each)
├── Unified search gateway (cross-layer)
└── Memory impact measurement

MONTH 3+ (P3 — strategic)
└── Cross-archon memory sync
```

---

## Immediate Next Step (P0 — today)

The single highest-impact, lowest-effort improvement: **enable pgvector on Supabase**.

```sql
-- One SQL statement. Supabase supports it natively.
CREATE EXTENSION IF NOT EXISTS vector;
```

This unlocks semantic search — "find memories like this one" — which is the foundation for almost everything else on this roadmap. Everything else builds on this capability.

---

## Tags

`#memory` `#improvement` `#roadmap` `#archonos` `#pgvector` `#consolidation` `#cross-layer-search`
