# From Chaos to Choreography: Multi-Agent Orchestration Patterns That Actually Work — Sandipan Bhaumik

**URL:** https://www.youtube.com/watch?v=2czYyrTzILg
**Added:** 2026-08-01
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- **💡 A central design choice is choreography vs. orchestration.** — Choreography is event-driven and decentralized: agents publish and consume events independently, which improves autonomy and extensibility.
- **🧭 Orchestration is the safer default for complex production workflows.** — A central orchestrator controls execution order, parallelism, retries, state, and logging; agents only process inputs and return outputs.
- **⚠️ Shared mutable state is a primary source of bugs.** — Letting multiple agents read and write the same records can cause lost updates, stale cache reads, and inconsistent decisions.
- **🧱 Use immutable state snapshots with versioning.** — Each agent should receive an immutable state, produce a new version, and append it rather than update shared records in place.
- **📐 Enforce data contracts between agents.** — Each agent should declare a typed input/output schema and validate handoffs at the boundary.
- **🛑 Design for failure with circuit breakers.** — Wrap every agent call in a circuit breaker so repeated failures trigger fast-fail behavior instead of repeated timeouts and cascading load.
- **🔁 Use compensation or saga patterns for rollback.** — Each agent should implement both execute and compensate operations so the orchestrator can undo prior work when a later step fails.
- **🏗️ A production-grade architecture centers on an orchestrator, versioned state, and observability.** — Agents do not call each other directly; all coordination flows through the orchestrator, which stores state versions, manages execution, and triggers compensation.

## Apply to ArchonOS
- (See takeaways — adapt patterns to Oracle/SupaBrain/MCP/lane-routing context.)

## TubeOnAI Summary
> 🔥 Multi-agent AI systems are distributed systems, not just collections of prompts and tools.     – Moving from 1 agent to 5 agents creates coordination, state, and failure-management problems that grow roughly with the number of inter-agent relationships.     – Common production failures come from architecture issues such as race conditions, stale reads, and partial failures, not from model quality.  💡 A central design choice is choreography vs. orchestration.     – Choreography is event-driven and decentralized: agents publish and consume events independently, which improves autonomy and extensibility.     – It is suitable when workflows are naturally event-based and agents change often, but it requires strong observability and delivery guarantees to debug failures.  🧭 Orchestration is the safer default for complex production workflows.     – A central orchestrator controls execution order, parallelism, retries, state, and logging; agents only process inputs and return outputs.     – This pattern is preferred when workflows have complex dependencies, rollback needs, audit requirements, or strict debugging needs, especially in regulated domains.  ⚠️ Shared mutable state is a primary source of bugs.     – Letting multiple agents read and write the same records can cause lost updates, stale cache reads, and inconsistent decisions.     – Default database behavior is often insufficient unless teams explicitly use transactions, locking, and strong isolation.  🧱 Use immutable state

## Tags
`#ai-agents` `#production`
