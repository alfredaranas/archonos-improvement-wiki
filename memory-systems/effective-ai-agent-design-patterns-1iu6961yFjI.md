# Effective AI agent design patterns

**URL:** https://www.youtube.com/watch?v=1iu6961yFjI
**Added:** 2026-08-01
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- **💡 Core problem: context rot** — Long-running agents often perform well initially, then degrade after 15–20 minutes: repeating work, forgetting prior decisions, contradicting themselves, hallucinating, and increasing token usage.
- **🧠 Mental model shift: from chatbots to distributed systems** — Generation 1: prompt + model, suitable for short tasks only.
- **🔥 Pattern 1: sub-agents for context isolation** — Break work into separate workers such as research, coding, testing, planning, or review.
- **🗂️ Pattern 2: planner-executor split** — Separate planning from execution instead of mixing both in one loop.
- **📄 Pattern 3: artifact-centric design** — Agents should read the relevant artifact instead of replaying long conversation histories.
- **🧱 Pattern 4: external state management** — The key rule is: state should never live only in the conversation.
- **🏛️ Pattern 5: layered memory** — Not all information should be stored the same way.
- **📝 Pattern 6: episodic summaries** — Long histories should be periodically compressed into structured summaries.

## Apply to ArchonOS
- (See takeaways — adapt patterns to Oracle/SupaBrain/MCP/lane-routing context.)

## TubeOnAI Summary
> 💡 Core problem: context rot   – Long-running agents often perform well initially, then degrade after 15–20 minutes: repeating work, forgetting prior decisions, contradicting themselves, hallucinating, and increasing token usage.   – The root cause is treating context like memory.   – Context is temporary working space inside the prompt window; it grows with each exchange and becomes noisy and expensive.   – Memory is persistent, structured, searchable, and survives across sessions.   – When state is kept in chat history instead of external systems, agents become fragile, costly, and unreliable.  🧠 Mental model shift: from chatbots to distributed systems   – Agent design is framed in three generations:   – Generation 1: prompt + model, suitable for short tasks only.   – Generation 2: tools + loop, more capable but still tied to one growing conversation.   – Generation 3: orchestrated systems with sub-agents, external state, memory layers, and durable artifacts.   – Modern agents are closer to distributed software systems than chat interfaces.   – The engineering challenge is not only prompting, but designing state flow, isolation, persistence, and recovery.  🔥 Pattern 1: sub-agents for context isolation   – Break work into separate workers such as research, coding, testing, planning, or review.   – Each worker operates in its own isolated context window and returns only a compressed result.   – The main benefit is not specialization alone, but isolation of context.   – Example

## Tags
`#ai-agents` `#production`
