---
kind: structural
provenance_note: "Internal TODO — derived from fleet daily review"
provenance_classified_at: 2026-07-10
---

# ArchonOS Improvement TODO

> Live implementation tracker — sourced from the [Memory System Roadmap](memory-system-current-vs-improvements.md).  
> Update status as items complete. Last updated: 2026-06-08.

---

## P0 — Quick Wins (Hours)

| # | Item | Status | Notes |
|---|------|--------|-------|
| P0-A | Enable `pgvector` extension on SupaBrain Supabase (`jpputhjyrnrqwzphjywq`) | ⬜ TODO | One SQL statement — `CREATE EXTENSION IF NOT EXISTS vector;` |
| P0-B | Add FTS `tsvector` column + GIN index on `suprabrain` table | ⬜ TODO | Generated column, auto-updates on write |
| P0-C | Add `embedding` vector(768) column to `suprabrain` | ⬜ TODO | Depends on P0-A |
| P0-D | Tag backfill — LLM assigns 2-4 tags to all existing suprabrain entries | ⬜ TODO | One-shot script |
| P0-E | Memory consolidation cron — `agent_memory` → `suprabrain` weekly | ⬜ TODO | Runs on Yoda, grouped by topic |

---

## P1 — Moderate Builds (Days)

| # | Item | Status | Notes |
|---|------|--------|-------|
| P1-A | Embedding pipeline cron — backfill + ongoing (nomic-embed-text 768d via Bathy) | ⬜ TODO | Depends on P0-C |
| P1-B | Memory entry lifecycle — `status` column: `active / consolidated / archived` | ⬜ TODO | Depends on P0-E |
| P1-C | Memory telemetry — `memory_query_log` table, MCP writes per search call | ⬜ TODO | |
| P1-D | Memory compressor cron — LLM dedupes + compresses redundant entries | ⬜ TODO | Reduces context token burn |
| P1-E | `supabrain_tags()` MCP tool — tag cloud with counts | ⬜ TODO | Depends on P0-D |

---

## P2 — Significant (Weeks)

| # | Item | Status | Notes |
|---|------|--------|-------|
| P2-A | Unified cross-layer search gateway — `memory_search(query, layers=[...])` | ⬜ TODO | Fans out to SupaBrain + Vault + Sessions |
| P2-B | Memory impact measurement — A/B with/without retrieval | ⬜ TODO | Research-grade, needs experimental design |

---

## P3 — Strategic (Months)

| # | Item | Status | Notes |
|---|------|--------|-------|
| P3-A | Cross-archon memory sync — dual-write local SQLite + SupaBrain on all archons | ⬜ TODO | Oracle + Yoda + Sentinel unified memory |

---

## Status Key

| Symbol | Meaning |
|--------|---------|
| ⬜ TODO | Not started |
| 🔄 IN PROGRESS | Active work this session |
| ✅ DONE | Complete — update with date |
| ⏸ BLOCKED | Waiting on dependency |

---

## SQL Reference — P0 Commands

```sql
-- P0-A: Enable pgvector
CREATE EXTENSION IF NOT EXISTS vector;

-- P0-B: FTS column + index
ALTER TABLE suprabrain
  ADD COLUMN search_vector tsvector
  GENERATED ALWAYS AS (to_tsvector('english', title || ' ' || content)) STORED;

CREATE INDEX suprabrain_fts_idx ON suprabrain USING GIN(search_vector);

-- P0-C: Embedding column
ALTER TABLE suprabrain ADD COLUMN embedding vector(768);
CREATE INDEX suprabrain_embed_idx ON suprabrain USING ivfflat (embedding vector_cosine_ops);
```

---

## Related

- [Memory System Architecture](archonos-memory-system-architecture.md)
- [Memory: Current vs. Improvements](memory-system-current-vs-improvements.md)
- FOCUS card: `archonos/docs/focus/FOCUS_SUPABRAIN.md`
- SupaBrain project: `jpputhjyrnrqwzphjywq`

`#archonos` `#todo` `#memory` `#pgvector` `#supabrain` `#roadmap`
