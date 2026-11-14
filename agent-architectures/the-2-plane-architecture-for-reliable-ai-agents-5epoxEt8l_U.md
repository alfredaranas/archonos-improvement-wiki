# The 2-Plane Architecture for Reliable AI Agents

**URL:** https://youtube.com/watch?v=5epoxEt8l_U
**Channel:** Shikha Bahirani - The AI Architect
**Added:** 2026-11-14
**Relevance:** ⭐⭐⭐⭐ (4/5)

## Key Takeaways
- Design the workflow as two planes: execution proposes state changes, while a separate assertion plane checks them.
- Write runtime invariants in deterministic code and validate proposed changes against ground-truth systems, such as databases or contracts.
- Have agent code, not individual workflow steps, call the assertion plane before applying changes to shared state.
- Run invariants after steps with probabilistic risk, such as model steps and tool calls; checks are not needed after every step.
- Place a final invariant gate before irreversible external actions. Commit only after checks pass; otherwise reject the change and retry, use a fallback, or escalate to a human.

## Apply to ArchonOS
- Map the orchestration pattern onto ArchonOS archon delegation boundaries and the demiurge/archon split.
- Check the pattern against the fleet's 26-archon topology — does it assume a single coordinator that ArchonOS does not have?
- Add the pattern to the ArchonOS architecture reference notes.

## TubeOnAI Summary
> Reliable AI agents should separate model-driven execution from deterministic checks against ground truth, and never let an unchecked probabilistic proposal change production state.
> 
> ## Advice
> - Design the workflow as two planes: execution proposes state changes, while a separate assertion plane checks them.
> - Write runtime invariants in deterministic code and validate proposed changes against ground-truth systems, such as databases or contracts.
> - Have agent code, not individual workflow steps, call the assertion plane before applying changes to shared state.
> - Run invariants after steps with probabilistic risk, such as model steps and tool calls; checks are not needed after every step.
> - Place a final invariant gate before irreversible external actions. Commit only after checks pass; otherwise reject the change and retry, use a fallback, or escalate to a human.
> - For a local, fixable assertion failure, retry with the error feedback rather than rolling back the whole run.
> - Keep assertion checks independent of the execution path's prior outputs and model reasoning.

## Tags
`#agents` `#agent-architectures` `#archonos`
