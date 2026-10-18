# Context Window Limits & Stateless LLM API Calls

> **Source:** [How Memory is stored in AI Agents | Mastering Memory for AI](https://youtube.com/watch?v=gvhVtaEA1z8)
> **Channel:** Piyush Garg · **Published:** 2025-08-22 · **Ingested:** 2026-10-18
> **Relevance score:** 8/10

## Summary

LLM API calls (OpenAI, etc.) are stateless—they don't retain conversation history between requests. As conversation history grows, it must be resent with each call, but LLMs have fixed context windows (128k-1M tokens) that create a sliding window problem: older messages get dropped when new ones exceed the limit. This requires explicit memory management to avoid losing critical context.

## Key Takeaways

- Stateless API calls mean you must resend entire conversation history with every request—no automatic retention
- Context windows are fixed and finite; exceeding them causes older messages to fall outside the processable range, creating information loss
- Long-running conversations require a memory layer (short-term + long-term storage) to compress, summarize, or selectively replay conversation history rather than naively appending all messages

## ArchonOS Applicability

ArchonOS agents interacting with LLM APIs must implement explicit memory management: maintain a conversation buffer, implement summarization for old messages, and use semantic memory (embeddings) to retrieve relevant context without bloating the context window. This prevents token waste and preserves agent continuity across long-running tasks.

---

`#memory-systems` `#auto-ingested` `#youtube`
