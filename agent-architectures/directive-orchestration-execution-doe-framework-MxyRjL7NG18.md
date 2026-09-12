# Directive Orchestration Execution (DOE Framework)

**URL:** https://youtube.com/watch?v=MxyRjL7NG18
**Added:** 2026-09-12
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- **🔥 Agentic workflows — definition, business significance, and framing** — Agentic workflow: an LLM-based system that plans, uses tools, retains memory, reflects, and orchestrates actions autonomously to perform business tasks end-to-end.…
- **💡 Three technical enablers now making agentic workflows practical** — Intelligence: frontier LLMs (Anthropic Claude, OpenAI, Google Gemini, etc.) score highly on engineering benchmarks (roughly ~80% on software engineering benchmarks) and handle complex code and reasoning tasks
- **🧭 Agent runtime loop (five components: PTMRO)** — Planning: decomposes high-level objectives into ordered executable steps and revises plans as new info arrives; recommended human focus area because early planning errors compound.…
- **🛠 Separation of concerns: where to use LLM vs deterministic code** — Directive (what to do): written in natural language markdown (SOPs → directives).
- **🍳 DO framework (Directive — Orchestration — Execution): concrete workspace pattern** — Workspace layout: top-level folders /directives (markdown SOPs) and /executions (scripts, typically Python).

## Apply to ArchonOS
- prefer lower temperature and stricter schemas where determinism required.
- keep orchestrator out of long-running cloud services; deploy deterministic execution scripts as cloud functions (Modal, trigger.
- keep spawning depth limited (parent → subagents; avoid unchecked recursive spawning).

## TubeOnAI Summary
> 🔥 Agentic workflows — definition, business significance, and framing – Agentic workflow: an LLM-based system that plans, uses tools, retains memory, reflects, and orchestrates actions autonomously to perform business tasks end-to-end. – Economic claim: agentic workflows produce large horizontal leverage by automating ~…

## Tags
`#agents` `#archonos`
