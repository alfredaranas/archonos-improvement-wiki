# Design Your Multi-Agent System

**URL:** https://www.youtube.com/watch?v=elRW5G4dr4k
**Added:** 2026-09-19
**Relevance:** ⭐⭐⭐ (3/5)

## Key Takeaways
- Annie argues that production multi-agent systems should combine AI agents with deterministic workflows, so teams gain flexibility without sacrificing reliability, testability, traceability, or cost control.…
- Advice
- Start with the business process, identify its specialists, and decide which steps require AI before designing agents.
- Use deterministic code for fixed rules and known sequences instead of asking a model to perform every step.
- Use routing when a re
- Mentioned
- Frameworks and tools: Google Agent Development Kit, Google Cloud, Google Cloud Agent Platform, Cloud Run, Cloud Trace, BigQuery
- Companies and sources: Google, Anthropic, Anthropic’s multi-agent research system blog post
- Concepts: single-agent s

## Apply to ArchonOS
- Advice
- Start with the business process, identify its specialists, and decide which steps require AI before designing agents.
- - Use deterministic code for fixed rules and known sequences instead of asking a model to perform every step.
- - Use routing when a request must be sent to a specialist, and prefer explicit rules when the routing conditions are clear.

## TubeOnAI Summary
> Annie argues that production multi-agent systems should combine AI agents with deterministic workflows, so teams gain flexibility without sacrificing reliability, testability, traceability, or cost control.

Advice
- Start with the business process, identify its specialists, and decide which steps require AI before designing agents.
- Use deterministic code for fixed rules and known sequences instead of asking a model to perform every step.
- Use routing when a request must be sent to a specialist, and prefer explicit rules when the routing conditions are clear.
- Use sequential workflows for fixed-order tasks and parallel workflows for independent tasks that can run at the same time.
- Use model-generated workflows for open-ended research when the required steps cannot be known in advance.
- Add evaluators, judges, gates, or voting systems when the system must check and improve its own output.
- Set a maximum iteration count or an explicit stopping condition to prevent infinite loops.
- Add tracing and observability to each workflow step so teams can audit results and troubleshoot failures.

Mentioned
- Frameworks and tools: Google Agent Development Kit, Google Cloud, Google Cloud Agent Platform, Cloud Run, Cloud Trace, BigQuery
- Companies and sources: Google, Anthropic, Anthropic’s multi-agent research system blog post
- Concepts: single-agent systems, multi-agent orchestration, routing, sequential workflows, parallel workflows, map over item, plan-executor workflows, dele

## Tags
`#agents` `#orchestration` `#production` `#multi-agent` `#frameworks`
