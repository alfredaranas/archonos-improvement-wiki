# The Ultimate AI Agent Memory Guide (2026) | Working vs Semantic vs Episodic vs Procedural Memory

**URL:** https://www.youtube.com/watch?v=G2NiVhoBq1c
**Added:** 2026-08-01
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- **💡 Core problem** — A common symptom is inconsistent recall: an agent forgets recent details but remembers older facts.
- **🧠 Four distinct memory types** — Working memory: information relevant to the current interaction, limited by the model’s context window/token budget.
- **🌲 Decision tree for placing information in the right memory layer** — 1.
- **🗂️ Working vs long-term memory** — Working memory handles short-term continuity inside the current conversation.
- **🔎 Retrieval strategy depends on storage size and shape** — Small fact sets can be fully injected into context at the start of a session.
- **🔁 Procedural memory is about distilled improvement, not replay** — Repeated tasks should result in a stored procedure that captures what worked.
- **🛠️ Architecture examples** — Working memory for current edits and active session state.
- **🚨 Common failure modes and fixes** — Symptom: the agent asks again for details given a few minutes earlier.

## Apply to ArchonOS
- (See takeaways — adapt patterns to Oracle/SupaBrain/MCP/lane-routing context.)

## TubeOnAI Summary
> 💡 Core problem: most AI memory failures come from using one storage approach for all information   – A common symptom is inconsistent recall: an agent forgets recent details but remembers older facts.   – The underlying issue is usually treating facts, events, active context, and learned routines as if they belong in the same database.   – Memory design should be treated as a first-class part of agent architecture, alongside orchestration and tool use.  🧠 Four distinct memory types   – Working memory: information relevant to the current interaction, limited by the model’s context window/token budget.   – Used for session continuity, such as details of an active support ticket or what tools were called during the current chat.   – Semantic memory: persistent, stable knowledge stored in canonical form instead of being repeatedly inferred.   – Suitable for facts such as a user’s name, role, preferences, or subscription tier.   – Episodic memory: a timeline of specific past events and interactions.   – Useful for retrieving historical sequences, such as a customer’s complaints last month or prior decisions in an ongoing case.   – Procedural memory: distilled know-how for recurring task patterns.   – Stores successful routines or workflows, such as the best sequence for handling a refund, rather than raw transcripts.  🌲 Decision tree for placing information in the right memory layer   – 1. Does it persist beyond the current turn?   – If not, it may need no memory layer at all; the

## Tags
`#ai-agents` `#production`
