# The Four Types of Memory Every AI Agent Needs

**URL:** https://www.youtube.com/watch?v=BacJ6sEhqMo
**Added:** 2026-06-13
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)
**Channel:** IBM Technology
**Published:** 2 weeks ago
**Duration:** 10m 41s

## Key Takeaways
- **🔥 Four core memory types for AI agents** — – Working, semantic, procedural, and episodic memory mirror human short-term memory, factual knowledge, learned skills, and personal experience.
- **💡 Working memory = context window** — – Represents everything the agent can “see” now: current conversation, system prompts, loaded files, and data.
- **📚 Semantic memory = knowledge base** — – Stores facts, rules, documentation, and conventions, implemented via vector databases, knowledge graphs, or simple files like Markdown (.
- **🛠 Procedural memory = skills** — – Encodes how to perform tasks using structured “skills” (e.
- **🧠 Episodic memory = experience over time** — – Captures what happened in past interactions and what was learned, beyond simple transcript storage.

## Apply to ArchonOS
- Memory taxonomy: implement the four-type split (working / semantic / procedural / episodic) in SupaBrain
- Retrieval: hybrid search (BM25 + vector) + re-ranking layer for SupaBrain
- Consider GraphRAG for relationship-aware recall in cross-archon knowledge
- Agent architecture: separate planning, execution, verification roles in dispatch layer
- Context window: implement structured summarization and sliding-window history

## TubeOnAI Summary

> 🔥 Four core memory types for AI agents – Working, semantic, procedural, and episodic memory mirror human short-term memory, factual knowledge, learned skills, and personal experience. – Not every agent needs all four; the mix depends on task complexity. 💡 Working memory = context window – Represents everything the agent can “see” now: current conversation, system prompts, loaded files, and data. – It is fast, volatile, and size-limited, similar to RAM; very large contexts still have practical ceilings and performance tradeoffs. 📚 Semantic memory = knowledge base – Stores facts, rules, documentation, and conventions, implemented via vector databases, knowledge graphs, or simple files like Markdown (.md). – Typically loaded into the context at session start, giving the agent persistent project and domain knowledge to avoid repeating mistakes. 🛠 Procedural memory = skills – Encodes how to p...

## Tags
`#memory` `#agents` `#rag` `#context-engineering` `#production` `#graphrag` `#archonos`
