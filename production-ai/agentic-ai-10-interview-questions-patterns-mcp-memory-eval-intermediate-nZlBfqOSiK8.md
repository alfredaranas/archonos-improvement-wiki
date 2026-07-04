# Agentic AI  10 Interview Questions (Patterns, MCP, Memory & Eval)  Intermediate

**URL:** https://www.youtube.com/watch?v=nZlBfqOSiK8
**Added:** 2026-07-04
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- Agent design should match the task pattern: ReAct for adaptive stepwise interaction, plan-and-execute for long structured goals, and reflection for retryable tasks with a clear pass/fail signal.
- Planning quality depends on useful task decomposition, explicit dependencies, parallel execution of independent steps, and replanning when new observations invalidate the current plan.
- Tool use at scale requires retrieval of only relevant tools and standardization via MCP so agents do not carry hundreds of schemas or rely on bespoke integrations.
- Reliable tool calling is layered: constrained outputs, schema validation, self-repair on malformed arguments, defensive tool implementation, idempotency, and time-bounded execution.
- Agent memory should be engineered as a write path and read path, combining episodic, semantic, and procedural memory while budgeting the context window intentionally.
- Orchestration frameworks become useful when systems need branching, retries, checkpointing, observability, pause/resume behavior, and durable state rather than a simple loop.

## Apply to ArchonOS
- Map one current agent workflow to the ReAct, plan-and-execute, and reflection framework, then test which combination gives the best tradeoff of cost, latency, and task completion.
- Create a planner that decomposes one business task into tool-sized steps, annotates dependencies, and runs independent steps in parallel with explicit replanning checks.
- Prototype tool retrieval by indexing tool descriptions and surfacing only the top relevant tools per user goal instead of exposing the full tool list.
- Implement structured tool calling with strict schemas, JSON mode, schema validation, and a single self-repair retry loop that feeds validation errors back to the model.
- Audit all external tools for idempotency, readable structured errors, and timeouts; add per-tool retry caps and a circuit breaker for repeated failures.

## Subjects
Agent, Planning, Tool, Reliable

## TubeOnAI Summary
> This intermediate-level overview focuses on building production-grade AI agents that are reliable, affordable, and measurable rather than simple demos. It explains when to use ReAct, plan-and-execute, and reflection patterns, recommending ReAct for short reactive tasks, planning for longer structured work, and reflection when there is a clear success check such as tests passing. It covers planning and task decomposition through dependency graphs, parallel execution of independent steps, and replanning when observations invalidate the current plan. For tool use at scale, it recommends retrieving only relevant tools instead of exposing all schemas at once, and adopting the Model Context Protocol (MCP) as a standard host-client-server interface for reusable tool integrations. It also outlines production reliability practices including structured outputs, JSON mode, schema validation, self-repair loops, idempotent tools, timeouts, bounded retries, memory design with episodic/semantic/procedural layers, and orchestration frameworks such as LangGraph, OpenAI Agents SDK, and CrewAI. Three scenarios illustrate agentic RAG, failure handling for flaky APIs, and cost-latency optimization through routing, caching, context trimming, and parallelism. The final emphasis is that evaluation is the key production differentiator, requiring outcome, trajectory, efficiency, and safety metrics, ideally scored with calibrated LLM-as-judge workflows over a private eval set in continuous integration.

## Tags
`#ai-agents` `#2026` `#productionai` `#archonos-improvement`
