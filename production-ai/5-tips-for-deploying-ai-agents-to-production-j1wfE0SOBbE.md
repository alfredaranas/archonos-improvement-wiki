# 5 Tips for Deploying AI Agents to Production

**URL:** https://youtube.com/watch?v=j1wfE0SOBbE
**Added:** 2026-09-12
**Relevance:** ⭐⭐⭐⭐ (4/5)

## Key Takeaways
- Replace raw SQL tools with typed tools that enforce contracted query shapes and tenant isolation, for example an enum status filter (pending, shipped, delivered), a limit capped at 50, parameterized queries, and user ID sourced from invocation state set by the verified JWT.
- Control cost with model routing: send simple requests to a cheaper model like Amazon Nova Micro based on message length or a lightweight classifier, and reserve a more expensive model for harder queries; Nova Micro supports tool use via the Converse API.
- The host lays out five production practices for TypeScript AI agents to prevent open endpoints, runaway costs, tenant data leaks, and poor observability.

## Apply to ArchonOS
- Review the production ai patterns described and map to current ArchonOS architecture.
- Note any tooling/evaluation improvements that could be applied to existing pipelines.

## TubeOnAI Summary
> - The host lays out five production practices for TypeScript AI agents to prevent open endpoints, runaway costs, tenant data leaks, and poor observability. - Stream three event types to the UI so users see activity during slow tool calls: token-by-token text deltas, tool start, and tool end, using Strands agent.stream…

## Tags
`#agents` `#archonos`
