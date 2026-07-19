# General Agentic Memory (GAM): JIT-Based Lossless Context Management

> **Source:** [General Agentic Memory Via Deep Research (Nov 2025)](https://youtube.com/watch?v=IM2jnfVU3us)
> **Channel:** AI Paper Slop · **Published:** 2025-11-28 · **Ingested:** 2026-07-19
> **Relevance score:** 9/10

## Summary

GAM replaces ahead-of-time (AOT) memory compression with just-in-time (JIT) retrieval, maintaining a lossless universal page store indexed by lightweight summaries. A dual-agent architecture (memorizer + researcher) enables dynamic context assembly on-demand without information loss or static structure constraints.

## Key Takeaways

- Flip from compression-centric to search-centric memory: store complete raw history losslessly, use lightweight summaries as retrieval maps only
- Dual-agent system: memorizer handles incremental paging + indexing in background; researcher performs iterative deep research (plan → search → reflect) at query time using page store
- Eliminates three AOT failure modes: information loss from compression, rigid pre-computed structure, and heavy heuristics dependence; scales to massive histories without degradation
- Deep research loop uses chain-of-thought planning to identify needed pages, parallel search execution, and reflection to determine if context is sufficient before responding

## ArchonOS Applicability

Core pattern for ArchonOS agent memory: implement page store as indexed task/interaction history with semantic headers, use lightweight embeddings for retrieval guidance, and wire researcher loop into main agent planning. Enables long-running homlab agents to retain full context without recompression overhead while supporting arbitrary future queries.

---

`#memory-systems` `#auto-ingested` `#youtube`
