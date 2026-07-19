# Agentic Memory Part 1: What is Agentic Memory & Types

**URL:** https://www.youtube.com/watch?v=9ta1cawyVsU
**Added:** 2026-07-11
**Relevance:** ⭐⭐⭐⭐ (4/5)
**Channel:** Divesh Jadhwani
**Published:** 6 days ago
**Duration:** 1h 2m

## Key Takeaways
- **🔥 No-memory baseline: each query is treated independently** — The agent only sees the system prompt and the current user message…
- **🪟 Sliding window memory keeps only the most recent N messages or turns** — Once the window is full, older items are evicted from active memory…
- **📝 Summary memory compresses prior conversation into a running summary** — After each interaction, the system updates a summary such as: user identity, preferences, and major prior requests…
- **🔀 Summary buffer memory combines recent raw messages with a summarized older history** — Recent exchanges are preserved verbatim in a small buffer for precise short-term recall…
- **🧭 Vector store memory retrieves relevant past information by semantic similarity** — User messages and possibly responses are embedded and stored in a vector database…

## Apply to ArchonOS
- Adopt the video's memory taxonomy (working/episodic/semantic/procedural) in SupaBrain entries and tag by type.
- Compare current retrieval (BM25 + vector) against the video's hybrid/re-ranking approach and document the gap.
- Watch the full talk (Agentic Memory Part 1: What is Agentic Memory & Types) and add a SupaBrain entry per concrete memory pattern.

## TubeOnAI Summary
> 💡 Agentic memory is the mechanism that lets AI agents retain and use prior interaction context across conversations and tasks – It improves performance, reliability, and usability by preserving conversational flow and task continuity – Without memory, an AI system acts more like a one-shot content generator than a persistent assistant, coding partner, or workflow tool – Examples used: recalling a user’s name, a prior goal like learning agentic AI, or retrieving an earlier message from a long chat 🧠 A basic AI agent loop consists of user input, system instructions, tool outputs, and AI response – User message: the query or request from the user – System message: hidden instructions defining behavior, role, format, and constraints – Tool message: context retrieved from external systems such as databases or APIs – AI message: the final response returned to the user – One full cycle of these…

## Tags
`#memory` `#context-engineering` `#tools` `#workflow` `#archonos-improvement`
