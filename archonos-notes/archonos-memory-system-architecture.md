# ArchonOS Memory System — Complete Architecture

> 🎨 **Visual diagram available**: [archonos-memory-system-architecture.html](archonos-memory-system-architecture.html) — SVG architecture diagram with cyberpunk color scheme showing all 6 layers with data flow paths.

**Last updated:** 2026-05-31
**Source:** archonos-mcp.py, Hermes config.yaml, filesystem audit, Supabase schema

---

## What This Covers

Before we can improve the memory system, we need an exact inventory of what exists. This document catalogs every memory store in ArchonOS — where data lives, how it's searched, who writes to it, and the gaps.

---

## Layer 1 — SupaBrain Cloud (Supabase)

**Database:** `jpputhjyrnrqwzphjywq.supabase.co`
**Access:** REST API via ArchonOS MCP server

### suprabrain — Long-Term Knowledge Store

- **Schema:** id (UUID), title (text), content (text), agent_id (text), source (text), tags (jsonb), created_at, updated_at
- **Search:** PostgreSQL `ILIKE` pattern matching — simple substring matching, no vector search, no FTS
- **Writers:** All archons (Oracle, Yoda, Sentinel), Claude.ai via MCP, cron jobs
- **Readers:** Claude.ai via MCP tools (`supabrain_search`, `supabrain_recent`)
- **Use case:** Persistent cross-session knowledge — research findings, system notes, improvement ideas

### agent_memory — Working Memory / Audit Trail

- **Schema:** Similar to suprabrain (title, content, agent_id, source, created_at)
- **Search:** Same ILIKE pattern matching
- **Writers:** MCP server auto-logs (yoda_shell audit, service restarts, boot events), archon processes
- **Use case:** Transient operational logging — shell command history, service events, run tracking

**Key gap:** No vector embeddings (pgvector available in Supabase but unused). No FTS tsvector indexes. Search is limited to exact substring matches.

---

## Layer 2 — Hermes Agent Local Memory (SQLite)

**Location:** `~/.hermes/state.db` (146 MB)
**Access:** Hermes Agent runtime, injected into agent context every turn

### Agent Memory — Durable Notes

- **Storage:** SQLite table
- **Limit:** 2,200 characters per entry
- **Behavior:** Injected into every agent turn as context
- **Nudge interval:** Every 10 turns Hermes prompts to save a memory
- **Flush:** Every 6 turns (minimum) to persist

### User Profile — Identity & Preferences

- **Storage:** SQLite table (same state.db)
- **Limit:** 1,375 characters
- **Behavior:** Injected every turn alongside agent memory
- **Content:** User name, role, preferences, environment facts, conventions

### Session Store — Chat History

- **Storage:** SQLite with **FTS5** full-text search index
- **Size:** 1,000+ sessions stored
- **Search:** `session_search` tool — FTS5 with boolean operators, phrase matching, role filtering
- **Features:** Discovery (query → best session), Scroll (window around a message), Browse (recent sessions list)
- **This is the only store with proper full-text search**

---

## Layer 3 — Local Vault (Filesystem)

**Location:** `~/vault/` on Oracle (nucbox)
**Sync:** Git → `alfredaranas/vault-private` (GitHub) → Obsidian pulls on Surface
**Writer:** Oracle only (via vault-write skill)
**Reader:** Alfred via Obsidian

### Directory Structure

| Directory | Purpose |
|-----------|---------|
| `_meta/` | Capture guide, task list, sort log |
| `archonos/` | System documentation, architecture |
| `claude-artifacts/` | Chat session exports |
| `pentest/` | Recon, writeups, lab notes (recon/, writeups/, lab/) |
| `openfusion/` | OpenFusion project notes |
| `secrets/` | Encrypted secrets (not visible in git) |

**Search:** ripgrep via `search_files` tool — fast regex, context lines, file name search

---

## Layer 4 — State Files (JSON)

**Location:** `~/.hermes/state/`
**Access:** Cron jobs and scripts read/write

Contains ~50 JSON files tracking:
- Research pipeline state (archonos-improvement-sources.json)
- Predictive history tracker state
- Vault-Notion mirror state
- TubeOnAI batch ingestion state
- Data center geopolitics tracker state

**Search:** Manual file reading only — no search index, no SQLite

---

## Layer 5 — Kanban Database (SQLite)

**Location:** `~/.hermes/kanban.db` (106 KB)
**Access:** Hermes Kanban dashboard UI at `http://100.86.195.121:9122/kanban`

Stores task workflow state across boards (Improvement Wiki, etc.).

**Search:** Dashboard UI with filter cards, tenant/profile filters, column grouping

---

## Layer 6 — Response Store (SQLite)

**Location:** `~/.hermes/response_store.db` (20 KB)
**Access:** Internal Hermes caching

---

## Critical Gaps Summary

| Gap | Impact |
|-----|--------|
| No vector search on SupaBrain | Can't do semantic similarity — "find memories similar to this concept" doesn't work |
| No FTS on SupaBrain | Cloud search is substring-only — slow, inexact, no relevance ranking |
| No memory consolidation cron | Agent_memory (working) never compresses into suprabrain (long-term) |
| No hit-rate telemetry | Can't measure whether memory retrieval improves agent outputs |
| No cross-layer search | Vault (ripgrep), sessions (FTS5), SupaBrain (ILIKE) — three different interfaces |
| Tags unused | Tags column exists but inconsistently populated — no tag browsing |

---

## Data Flow Diagram

See the [visual HTML architecture diagram](archonos-memory-system-architecture.html) for an SVG-based view with the cyberpunk color scheme.

```text
┌─────────────────────────────────────────────┐
│              Claude.ai (user)               │
│  reads: suprabrain, sessions, vault          │
│  writes: suprabrain, agent_memory            │
└──────────┬──────────────────────┬────────────┘
           │ MCP                  │ Hermes
     ┌─────┴──────┐        ┌──────┴──────┐
     │  Supabase  │        │   SQLite    │
     │  Cloud     │        │   Local     │
     │ suprabrain │        │ agent memory│
     │ agent_mem  │        │ user profile│
     │ ILIKE only │        │ session FTS5│
     └────────────┘        └─────────────┘

┌──────────────────────┐   ┌──────────────────┐
│   ~/vault/ (Oracle)  │   │ ~/.hermes/state/ │
│   ripgrep search    │   │   JSON files     │
│   git sync → GH     │   │   no index       │
└──────────────────────┘   └──────────────────┘
```

## Tags

`#archonos` `#memory` `#architecture` `#supabase` `#supabrain` `#hermes` `#vault` `#knowledge-base` `#improvement`