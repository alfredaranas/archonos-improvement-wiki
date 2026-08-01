# AI Agentic Memory System Design

**URL:** https://www.youtube.com/watch?v=2zdWI2SYB9I
**Added:** 2026-08-01
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- **💡 Core problem: LLMs have limited context windows** — Chat models maintain a sliding window of recent messages, not permanent memory.
- **🧠 Short-term memory = conversation thread** — The running chat history acts as short-term memory.
- **📚 Long-term memory is needed to retain useful information across time** — A separate memory system can extract durable information from messages and store it outside the LLM context.
- **⚙️ Basic memory-engine architecture** — During conversation, each user message can be passed through an additional model or extraction step.
- **🔎 Why naive long-term memory loading does not scale** — Long-term memory grows continuously over time.
- **🧩 Semantic retrieval with a vector database** — Instead of storing memory only in a relational database such as PostgreSQL, memory can be embedded and stored in a vector database such as Qdrant.
- **🗂️ Three main long-term memory types** — Stores stable user facts and preferences as key-value style data.
- **🔄 Memory extraction itself is LLM-driven** — The system uses an LLM to interpret incoming messages and decide what should be stored.

## Apply to ArchonOS
- (See takeaways — adapt patterns to Oracle/SupaBrain/MCP/lane-routing context.)

## TubeOnAI Summary
> 💡 Core problem: LLMs have limited context windows   – Chat models maintain a sliding window of recent messages, not permanent memory.   – As a conversation grows, earlier messages fall out of context.   – Even with very large context windows, sending everything is inefficient because it increases token cost, latency, and risk of irrelevant context.  🧠 Short-term memory = conversation thread   – The running chat history acts as short-term memory.   – It preserves recent turns while the conversation is active.   – This is similar to how humans remember the flow of a recent discussion but not every exact sentence.   – Example: if a user says “My name is Piyush” early in a long chat, that detail may be lost once it slides out of the active context window.  📚 Long-term memory is needed to retain useful information across time   – A separate memory system can extract durable information from messages and store it outside the LLM context.   – This memory can then be reloaded during later queries, including in a new chat session.   – Example: if the user later asks “What is my name?”, the system can answer by retrieving stored memory rather than relying only on recent chat history.  ⚙️ Basic memory-engine architecture   – During conversation, each user message can be passed through an additional model or extraction step.   – That step identifies information worth storing as long-term memory.   – Extracted memory is written to a database.   – At query time, the system combines:     – 

## Tags
`#ai-agents` `#production`
