# RAG Strategy Selection & Composition Framework

> **Source:** [Every RAG Strategy Explained in 13 Minutes (No Fluff)](https://youtube.com/watch?v=tLMViADvSNE)
> **Channel:** Cole Medin · **Published:** 2025-11-03 · **Ingested:** 2026-10-11
> **Relevance score:** 8/10

## Summary

RAG effectiveness depends on combining 3-5 specialized strategies rather than single approaches. Core strategies include re-ranking (filter irrelevant chunks), agentic RAG (agent-controlled search selection), knowledge graphs (entity relationship queries), and contextual retrieval (LLM-enriched chunk context). Strategy selection trades cost, latency, and relevance against complexity.

## Key Takeaways

- Re-ranking is foundational: retrieve broadly (20-50 chunks), then use specialized cross-encoder to filter to most relevant before LLM consumption—prevents context overwhelm with minimal cost increase
- Agentic RAG enables flexible search: let agents choose between semantic search, full-document reads, or relationship traversal based on query intent; requires clear decision boundaries to avoid unpredictability
- Knowledge graphs excel for interconnected data: combine vector search with graph database entity relationship queries, but expect 2-3x latency/cost penalty due to LLM-driven extraction during indexing
- Contextual retrieval (Anthropic): prepend LLM-generated context to each chunk describing document fit; measurable relevance gains but requires per-chunk LLM pass during prep phase
- Optimal solutions combine strategies: rarely use single approach; typical production RAG stacks layer re-ranking + agentic selection + contextual enrichment based on data structure and query patterns

## ArchonOS Applicability

For ArchonOS agent knowledge augmentation, start with re-ranking + contextual retrieval for cost-efficient homelab operation. Add agentic RAG when agent needs flexible document traversal (e.g., meeting notes vs. action items). Reserve knowledge graphs for later optimization when interconnected domain models justify preprocessing overhead.

---

`#memory-systems` `#auto-ingested` `#youtube`
