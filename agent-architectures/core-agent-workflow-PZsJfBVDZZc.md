# Core Agent Workflow

**URL:** https://youtube.com/watch?v=PZsJfBVDZZc
**Added:** 2026-09-12
**Relevance:** ⭐⭐⭐⭐ (4/5)

## Key Takeaways
- Reflection and reasoning improve quality by generate–critique–refine with separate generator and critic iterating to a target score; a variant saves “lessons” to memory for future retries, and self-discover composes a custom reasoning recipe from thinking modules before solving.
- Sampling and search generate multiple candidates and pick the best: tree of thoughts proposes different next thoughts, scores them 1 to 5, and expands the best path, while a mental loop simulates candidate actions, though both suffer from mid-range score collapse.
- The host argues that knowing the 35 agentic design patterns across eight families lets builders pick the right workflow shape, which boosts reliability and results, and even naming a pattern in a prompt can steer coding agents, especially on smaller local models.
- LaTS searches over reasoning moves with Monte Carlo tree search, proposing different next steps, applying deterministic checks for progress, completeness, loop avoidance, and confidence, and propagating rewards to prune weak branches.
- The host advises choosing the smallest shape that works, starting with React tool use, adding reflection for quality, adding planning when steps are unknown, and using teams only when tasks are truly parallel or need specialists.

## Apply to ArchonOS
- Review the agent architectures patterns described and map to current ArchonOS architecture.
- Note any tooling/evaluation improvements that could be applied to existing pipelines.

## TubeOnAI Summary
> - The host argues that knowing the 35 agentic design patterns across eight families lets builders pick the right workflow shape, which boosts reliability and results, and even naming a pattern in a prompt can steer coding agents, especially on smaller local models. - Tools and actions center on a loop where the model t…

## Tags
`#agents` `#archonos`
