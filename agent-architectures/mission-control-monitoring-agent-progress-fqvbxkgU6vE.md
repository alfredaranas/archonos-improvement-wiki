# Mission control: Monitoring agent progress

**URL:** https://youtube.com/watch?v=fqvbxkgU6vE
**Added:** 2026-09-12
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- **🔥 Caution: prefer single agent + tools unless tasks are complex** — Single agent with well-designed tools often suffices; multi-agent patterns add complexity and are recommended only as task complexity increases.…
- **🧭 Scoring criteria (used to compare architectures)** — Distributed development: can different teams maintain components/agents independently?
- **🕹️ Supervisor pattern (aka subagents)** — Main supervisor agent coordinates subagents as tools; all message routing passes through the main agent.…
- **🔁 Handoffs pattern** — Agents use tool-calling to hand off control to one another; entry agent receives the user request and agents can pass control (A → B → C) and generate final responses.…
- **🧩 Skills / Progressive disclosure (quasi multi-agent)** — Single controlling agent loads specialized prompts/knowledge (“skills”) on demand; called “progressive disclosure” for context management.…

## Apply to ArchonOS
- Review the agent architectures patterns described and map to current ArchonOS architecture.
- Note any tooling/evaluation improvements that could be applied to existing pipelines.

## TubeOnAI Summary
> 🔥 Caution: prefer single agent + tools unless tasks are complex – Single agent with well-designed tools often suffices; multi-agent patterns add complexity and are recommended only as task complexity increases. 🧭 Scoring criteria (used to compare architectures) – Distributed development: can different teams maintain co…

## Tags
`#agents` `#archonos`
