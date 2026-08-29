# Memory Pruning in LangChain | Importance-Based Context Management for Production AI

**URL:** https://www.youtube.com/watch?v=OZKKQg8nhSU
**Added:** 2026-08-29
**Relevance:** ⭐⭐⭐⭐ (4/5)
**Model:** `azure/gpt-5`
**Channel:** Code & Canvas

## Key Takeaways
- **🔧 Problem framing: context management** — Sliding window can drop early important instructions; summarization can preserve irrelevant chatter.…
- **🧮 Heuristic demo: importance scoring** — Estimate tokens via len(text)/4; store in a MemoryEntry with message, tokens, importance.…
- **🤖 LLM-integrated scoring (production-ready)** — Replace hardcoded rules with an LLM that outputs a structured evaluation: importance (1–10), category, should_keep (bool), reason.…

## Apply to ArchonOS
- ArchonOS session context can flood with 50+ SupaBrain lookups per run; switch from LRU to relevance scoring so high-importance lookups persist regardless of recency. The `~/.hermes/state/archonos-improvement-sources.json` file already grew past the simple-LRU threshold.
- Apply sliding-window discipline to Hermes per-turn context: keep the last N SupaBrain entries verbatim, summarize the prior N→2N band, archive the rest with tag `archived`. The `archonos-improvement-researcher` cron generates 200+ wiki entries of exactly this kind and benefits first.

## TubeOnAI Summary
> - 🔧 Problem framing: context management – Sliding window can drop early important instructions; summarization can preserve irrelevant chatter. – Introduces importance-based pruning that retains only high-value messages. - 🧮 Heuristic demo: importance scoring – Estimate tokens via len(text)/4; store in a MemoryEntry with message, tokens, importance. – Assign importance by keyword rules (e.g., name/decisions = high; greetings = low). – When over max tokens, sort messages by importance (asc), then tokens (asc) and remove the first repeatedly. – Effect: low-value items like “hi/thanks” are pruned first; critical facts and decisions persist regardless of order. - 🤖 LLM-integrated scoring (production-ready) – Replace hardcoded rules with an LLM that outputs a structured evaluation: importance (1–10), category, should_keep (bool), reason. – Prompt maps categories to scores: – 10: permanent user facts (name, age, location, profession) – 9: critical decisions, architecture, requirements – 8: preferences, goals, current projects – 7: useful technical discussions – 5: general conversation – 3: temporary info – 1: greetings/small talk – Implementation via LangChain “with structured output” to …

## Tags
`#memory` `#production` `#langgraph` `#failure-modes`
