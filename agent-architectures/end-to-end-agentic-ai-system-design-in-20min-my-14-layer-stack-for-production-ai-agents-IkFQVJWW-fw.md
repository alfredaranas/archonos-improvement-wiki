# End-to-End Agentic AI System Design in 20min: My 14-Layer Stack for Production AI Agents

**URL:** https://youtube.com/watch?v=IkFQVJWW-fw
**Channel:** Dr. Maryam Miradi
**Added:** 2026-11-14
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- Define product requirements by outcomes, boundaries, constraints, and the respective responsibilities and authority of agents and people.
- Design an explicit workflow that assigns ownership of progress, routing, and handoffs; use deterministic steps where appropriate.
- Split agents by responsibility only when doing so reduces reasoning complexity without adding unnecessary architectural complexity. The speaker says five or six agents are often enough.
- Build context for each decision instead of passing the agent all available information.
- Keep knowledge, context, memory, and workflow state distinct, and store each kind of information according to how it will be used.

## Apply to ArchonOS
- Map the orchestration pattern onto ArchonOS archon delegation boundaries and the demiurge/archon split.
- Check the pattern against the fleet's 26-archon topology — does it assume a single coordinator that ArchonOS does not have?
- Add the pattern to the ArchonOS architecture reference notes.

## TubeOnAI Summary
> A production agent system needs separate designs for product goals, orchestration, agent boundaries, context, state, knowledge, actions, authority, tools, runtime, recovery, evaluation, observability, and learning. The speaker’s central advice is to assign each responsibility to the simplest component that can handle it, then make execution durable, measurable, and improvable.
> 
> ## Advice
> - Define product requirements by outcomes, boundaries, constraints, and the respective responsibilities and authority of agents and people.
> - Design an explicit workflow that assigns ownership of progress, routing, and handoffs; use deterministic steps where appropriate.
> - Split agents by responsibility only when doing so reduces reasoning complexity without adding unnecessary architectural complexity. The speaker says five or six agents are often enough.
> - Build context for each decision instead of passing the agent all available information.
> - Keep knowledge, context, memory, and workflow state distinct, and store each kind of information according to how it will be used.
> - Match retrieval to the question: use similarity search for suitable queries and graph or spatial data when relationships and routes matter.
> - Apply stronger execution safeguards to higher-risk actions. Validate and log writes, and require authorization and duplicate-execution prevention for consequential actions.…

## Tags
`#agents` `#agent-architectures` `#archonos`
