# Sliding Window Memory in LangChain Explained | Build Production-Ready AI Chat Memory

**URL:** https://www.youtube.com/watch?v=Rxn1qGJ3fYc
**Added:** 2026-08-29
**Relevance:** ⭐⭐⭐ (3/5)
**Model:** `azure/gpt-5`
**Channel:** Code & Canvas

## Key Takeaways
- **🧠 Implementation outline (LangChain)** — a custom memory tracks each message with its token count, maintains totals/peaks, and triggers pruning while tokens exceed the max_tokens.…

## Apply to ArchonOS
- ArchonOS session context can flood with 50+ SupaBrain lookups per run; switch from LRU to relevance scoring so high-importance lookups persist regardless of recency. The `~/.hermes/state/archonos-improvement-sources.json` file already grew past the simple-LRU threshold.
- Apply sliding-window discipline to Hermes per-turn context: keep the last N SupaBrain entries verbatim, summarize the prior N→2N band, archive the rest with tag `archived`. The `archonos-improvement-researcher` cron generates 200+ wiki entries of exactly this kind and benefits first.
- Move SupaBrain semantic search from a single FTS5 column to a hybrid BM25 + dense + RRF pipeline. Current `search` works at 200-entry improvement-wiki scale; at the 5k+ entry mark, single-retriever recall drops sharply.

## TubeOnAI Summary
> - 🔎 LLM context windows are finite, so long chats can exceed the token limit, causing earlier context to be dropped and responses to degrade. – Context limits vary by model (e.g., GPT, Claude, Gemini) from tens of thousands up to hundreds of thousands or even ~1M tokens in some models. - 🧰 Approaches to manage context include sliding window, summarization, pruning, token budgeting, hybrid memory, state extraction, importance scoring, and adaptive context budgeting. – This session focuses on the simplest: sliding window. - 🪟 Sliding window memory keeps only the most recent messages under a max token threshold to fit the context window. – When total tokens exceed the limit, it prunes the oldest messages, optionally preserving at least a minimum number of messages and archiving pruned entries. - 🧮 Token counting should use the model’s tokenizer in production for accurate counts; a demo approximation used 1 token ≈ 4 characters. – Different models tokenize differently, so counts vary across tokenizers. - 🧠 Implementation outline (LangChain): a custom memory tracks each message with its token count, maintains totals/peaks, and triggers pruning while tokens exceed the max_tokens. – User/…

## Tags
`#memory` `#RAG` `#production` `#langgraph`
