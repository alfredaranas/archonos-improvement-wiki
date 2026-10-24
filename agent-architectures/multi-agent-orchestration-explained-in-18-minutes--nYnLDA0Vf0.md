# Multi Agent Orchestration Explained in 18 Minutes

**URL:** https://www.youtube.com/watch?v=-nYnLDA0Vf0
**Added:** 2026-10-24
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- Split work at real boundaries in expertise, data, permissions, tools, or evaluation needs, not simply by organizational department.…
- Design the decision flow before creating agents: define dependencies, parallel work, conflict handling, and points where authority changes.…
- Give each specialist narrow context, instructions, outputs, and authority; grant only the access it needs.…
- Define the orchestrator’s response format, approval policy, and rules for missing or unverified evidence.…
- Do not finalize a recommendation when required evidence is missing; retry, use a verified fallback, request documentation, or route the decision to a person.…
- Evaluate the full business outcome, not just each agent’s accuracy.…
- Set human approval boundaries as part of the architecture, distinguishing what the system can recommend from what it can approve or execute.…

## Apply to ArchonOS
- Architecture: compare against the fleet's existing orchestration (A2A bus, Hermes runner, Kanban) — port the pattern only if it beats what we already run. _(from: "Design the decision flow before creating agents: define dependencies, parallel work, conflict handling, and points where authority changes.…")_
- Reliability: apply to the cron/retry layer — Hermes crons and the fleet health watchdogs already need a documented recovery path. _(from: "Do not finalize a recommendation when required evidence is missing; retry, use a verified fallback, request documentation, or route the decision to a…")_
- Governance: map to the existing approval gate (hermes-approvals) rather than inventing a parallel review mechanism. _(from: "Define the orchestrator’s response format, approval policy, and rules for missing or unverified evidence.…")_

## TubeOnAI Summary
> Multi-agent orchestration divides enterprise decisions across specialists with distinct expertise and authority, then uses an orchestrator to reconcile their findings, manage uncertainty, and produce one accountable recommendation.

Advice
- Split work at real boundaries in expertise, data, permissions, tools, or evaluation needs, not simply by organizational department.
- Design the decision flow before creating agents: define dependencies, parallel work, conflict handling, and points where authority changes.
- Give each specialist narrow context, instructions, outputs, and authority; grant only the access it needs.
- Define the orchestrator’s response format, approval policy, and rules for missing or unverified evidence.
- Do not finalize a recommendation when required evidence is missing; retry, use a verified fallback, request documentation, or route the decision to a person.
- Evaluate the full business outcome, not just each agent’s accuracy.
- Set human approval boundaries as part of the architecture, distinguishing what the system can recommend from what it can approve or execute.
Mentioned
- Products: Agentforce, Agentforce Studio
- Roles: renewal orchestrator, customer relationship agent, pricing and margin agent, risk agent, contract agent
Numbers to remember
- The example renewal is $10 million, due in 30 days, with a requested 20% discount.
- The pricing agent considers 8% to 10% defensible if the customer gives something meaningful in return.
- The proposed offer is 10% off in exchange for a three-year renewal, plus an executive recovery plan for open support issues.
- Example approval limits are 5% for an account executive and 10% for a regional leader; larger discounts require finance or deal desk approval.
- The orchestrator’s six responsibilities are decomposition, routing, context management, state tracking, reconciliation, and governance.

*(summary truncated)*

## Tags
`#agent` `#architecture` `#orchestration` `#memory` `#rag` `#mcp`
