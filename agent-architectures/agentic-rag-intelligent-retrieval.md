# Agentic RAG: LLM-Driven Data Source Selection

> **Source:** [What is Agentic RAG?](https://youtube.com/watch?v=0z9_MhcYvcY)
> **Channel:** IBM Technology · **Published:** 2024-10-28 · **Ingested:** 2026-08-02
> **Relevance score:** 8/10

## Summary

Agentic RAG extends standard RAG by using the LLM as a decision-making agent that selects optimal data sources, determines response formats, and handles out-of-scope queries. Unlike passive RAG pipelines that retrieve and generate in fixed sequence, agentic RAG leverages the LLM's language understanding to intelligently route queries to multiple vector databases or failsafes based on semantic context.

## Key Takeaways

- LLM acts as router: Uses semantic understanding to select between multiple vector databases (internal docs, public knowledge, external APIs) rather than querying a single source
- Response format decisions: Agent can determine whether to return text, charts, code snippets, or structured data based on query context—not just text by default
- Graceful degradation: Agent recognizes out-of-scope queries and routes to failsafes instead of hallucinating, improving reliability over vanilla RAG

## ArchonOS Applicability

For ArchonOS, agentic RAG enables intelligent task decomposition where the agent dynamically selects from multiple memory/knowledge sources (user preferences, system state, learned patterns, external APIs) based on request semantics. This supports multi-tenant homelab scenarios where different queries need different knowledge domains—e.g., routing smart home queries to local sensor data vs. routing general tech questions to a web-search capability.

---

`#agent-architectures` `#auto-ingested` `#youtube`
