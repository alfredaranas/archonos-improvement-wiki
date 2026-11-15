# Session State & Persistence Tiers for Agent Fleets

> **Source:** [Running Agents at Scale - Session State and Persistence](https://youtube.com/watch?v=VAI6FA1_rUQ)
> **Channel:** Plain Systems · **Published:** 2026-11-03 · **Ingested:** 2026-11-15
> **Relevance score:** 9/10

## Summary

Agents at scale require explicit partitioning of three data classes: scratch (ephemeral logs/temps on disposable overlay), shared read-only assets (base images, toolchains, package caches mounted once per host), and persistent user workspace (versioned volumes surviving across sessions). LangGraph separates execution checkpoints (per-thread) from long-term memory (cross-thread semantic storage).

## Key Takeaways

- Partition state by lifetime: scratch dies with session (overlay), shared assets are curated once per host (RO mounts), workspace persists with explicit TTL (durable volume)
- Memory/storage scales through sharing: read-only base layers and package caches live once per host, forked via CoW snapshots across thousands of agent instances
- Brain-side split matters: LangGraph checkpoints are execution traces (thread-scoped, rebuild cost on drop), long-term memory is semantic store (thread-agnostic, follows user across conversations)
- Every persisted byte has ops cost: storage, cleanup duty, privacy liability for user data—mature fleets decide per data class intentionally

## ArchonOS Applicability

ArchonOS agents need explicit session lifecycle: scratch dirs on tmpfs/overlay, shared tool/library mounts (base Python, MCP servers), and user workspace volumes with versioning. Implement checkpointing for multi-turn tasks (survives agent restarts) separate from semantic memory (user facts, preferences).

---

`#production-ai` `#auto-ingested` `#youtube`
