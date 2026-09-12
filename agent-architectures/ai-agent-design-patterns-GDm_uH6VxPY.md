# AI agent design patterns

**URL:** https://youtube.com/watch?v=GDm_uH6VxPY
**Added:** 2026-09-05
**Relevance:** ⭐⭐⭐⭐ (4/5)

## Key Takeaways
- **🧠 Single Agent pattern** — A single agent uses tools and the model’s reasoning to plan and execute multi-step tasks.…
- **🔗 Sequential Agent pattern** — A fixed-order pipeline of specialized sub-agents where each output feeds the next, like an assembly line.…
- **⚡ Parallel Agent pattern** — Multiple specialized agents run concurrently on independent subtasks.…
- **🧭 When to use which** — Single: simple or loosely structured tasks needing quick setup.…
- **🔜 Upcoming patterns** — Loop/critique for self-correction, coordinator/orchestrator for dynamic routing, and agent-as-tool for modular reuse.…

## Apply to ArchonOS
- Adopt hub-and-spoke coordinator pattern for cross-archon orchestration (Oracle ↔ Yoda ↔ Jarvis)
- Add durable-execution primitives (Temporal-style) to ArchonOS so workflows survive crashes
- Use task-decomposition + parallel-sub-agent pattern for long-running research tasks

## TubeOnAI Summary
> 🧠 Single Agent pattern  
– A single agent uses tools and the model’s reasoning to plan and execute multi-step tasks.  
– Pros: simple to implement, flexible for straightforward tasks.  
– Cons: limited control and reliability for complex workflows due to nondeterminism and growing prompt/tool complexity.

🔗 Sequential Agent pattern  
– A fixed-order pipeline of specialized sub-agents where each output feeds the next, like an assembly line.  
– Mechanism: shares data via a shared session state (short-term memory).  
– Pros: predictable, controlled, and reliable for structured, repeatable tasks.  
– Cons: rigid and inflexible, poorly suited to dynamic or branching scenarios.

⚡ Parallel Agent pattern  
– Multiple specialized agents run concurrently on independent subtasks.  
– Composition: typically followed by an aggregator step to synthesize results.  
– Pros: significantly reduces latency for independent tasks.  
– Cons: higher initial cost and added coordination/merging complexity.

🧭 When to use which  
– Single: simple or loosely structured tasks needing quick setup.  
– Sequential: highly structured, repeatable workflows needing control.  
– Parallel: independent subtasks where speed matters, often with a final aggregation step.

🔜 Upcoming patterns  
– Loop/critique for self-correction, coordinator/orchestrator for dynamic routing, and agent-as-tool for modular reuse.

## Tags
#agentarchitectures #agent #agents
