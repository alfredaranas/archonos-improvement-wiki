# Building a Network Troubleshooting Agent: Architecture, Tools, Guardrails, and Lessons Learned

**URL:** https://youtube.com/watch?v=eC-W7yGgXC4
**Channel:** NANOG
**Added:** 2026-11-14
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- Keep model reasoning separate from the harness, so changing models does not change operational policies or authority.
- Expose only typed, approved diagnostic tools; validate the target, device compatibility, arguments, rate, concurrency, failure limits, and call and token budgets before each operation.
- Require exact, unexpired human approval for write operations, bound to the approver, target, action, and argument digest; verify fresh device state before executing.
- Stop and escalate when a diagnosis exceeds the agent’s scope, reaches a policy boundary, or remains uncertain.
- Record requests, policy decisions, tool results, failures, approvals, evidence, and outcomes for audit and replay; do not rely on storing private reasoning.

## Apply to ArchonOS
- Apply the pattern to the fleet MCP server catalogue and check it against the Hermes approval-gate semantics.
- Validate the tool-call contract against a live fleet tool invocation before shipping changes.
- Document the pattern in the ArchonOS tool-use reference notes.

## TubeOnAI Summary
> A production network troubleshooting agent should gather fresh evidence through a controlled harness, not receive broad device access. Keep its tools, policies, and authority fixed across models, and require human approval for changes.
> 
> ## Advice
> - Keep model reasoning separate from the harness, so changing models does not change operational policies or authority.
> - Expose only typed, approved diagnostic tools; validate the target, device compatibility, arguments, rate, concurrency, failure limits, and call and token budgets before each operation.
> - Require exact, unexpired human approval for write operations, bound to the approver, target, action, and argument digest; verify fresh device state before executing.
> - Stop and escalate when a diagnosis exceeds the agent’s scope, reaches a policy boundary, or remains uncertain.
> - Record requests, policy decisions, tool results, failures, approvals, evidence, and outcomes for audit and replay; do not rely on storing private reasoning.
> - Use only verified, completed incidents as memory, filter them by compatible device and software and playbook versions, and treat them as hints for ordering reads, not as evidence or permission.
> - Prefer deterministic APIs or specific CLI commands over arbitrary shell access.

## Tags
`#agents` `#tool-use` `#archonos`
