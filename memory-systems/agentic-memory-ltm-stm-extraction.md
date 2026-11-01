# Agentic Memory: Long-Term vs Short-Term Memory Architecture

> **Source:** [AI Agentic Memory System Design](https://youtube.com/watch?v=2zdWI2SYB9I)
> **Channel:** Piyush Garg · **Published:** 2026-07-27 · **Ingested:** 2026-11-01
> **Relevance score:** 9/10

## Summary

Context windows are fundamentally limited; LLMs require dual-tier memory: short-term (sliding conversation history) and long-term (extracted facts stored in persistent DB). Use a secondary LLM to extract factual, semantic, and episodic memories from each message, persisting to a database to prevent information loss beyond the sliding window.

## Key Takeaways

- Short-term memory (STM) = sliding conversation context window; information older than window depth is lost to LLM unless explicitly stored
- Long-term memory (LTM) requires separate extraction pipeline: run lightweight LLM on each message to extract facts (e.g., 'user_name=Piyush', 'user_age=27'), persist to queryable DB (SQL/vector), inject relevant facts back into context before inference
- Memory types matter: factual (names, facts), semantic (preferences, patterns), episodic (event summaries); design extraction prompts for each type to minimize hallucination and cost
- Even with 1M+ token context windows, don't bloat context with full history—extraction + targeted retrieval keeps tokens/cost low and reduces hallucinations

## ArchonOS Applicability

ArchonOS agents need persistent user/environment state across sessions. Implement dual-memory: ephemeral sliding window for active task reasoning, persistent fact store (PostgreSQL + vector DB) for user preferences, past decisions, and system configuration. Inject relevant memories into context via retrieval before each LLM call.

---

`#memory-systems` `#auto-ingested` `#youtube`
