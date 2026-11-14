# Who governs an AI SRE agent that fixes production?

**URL:** https://youtube.com/watch?v=da-XUVimLYk
**Channel:** AgentGlass, Inc.
**Added:** 2026-11-07
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- Keep deterministic safety rules outside the language model, rather than relying on prompts such as “never delete data.”.
- Avoid asking humans to approve every action. Reserve approvals for consequential changes so repeated prompts do not cause approval fatigue.
- Verify fixes with an independent system, not the agent that made the change.
- Treat each production action as a transaction: capture a restore point, test the blast radius, start with a canary, check service-level objectives, then promote or roll back.
- Use a policy gateway to validate agent identity, limit its scope, and stop repeated attempts, such as after three retries.

## Apply to ArchonOS
- Compare the described control against ArchonOS's existing approval gate and note the gap.
- Check whether the policy applies to service restarts and fleet-wide config changes (the Tier-2/Tier-3 escalation rules).
- Record the comparison in the ArchonOS governance notes.

## TubeOnAI Summary
> AI SRE agents can repair production systems, but organizations remain responsible for failures. Safe autonomy requires deterministic policy checks, independent verification, risk-based human oversight, and staged changes with rollback.
> 
> ## Advice
> - Keep deterministic safety rules outside the language model, rather than relying on prompts such as “never delete data.”
> - Avoid asking humans to approve every action. Reserve approvals for consequential changes so repeated prompts do not cause approval fatigue.
> - Verify fixes with an independent system, not the agent that made the change.
> - Treat each production action as a transaction: capture a restore point, test the blast radius, start with a canary, check service-level objectives, then promote or roll back.
> - Use a policy gateway to validate agent identity, limit its scope, and stop repeated attempts, such as after three retries.
> - Route actions by reversibility, blast radius, and freshness of system state. Require human approval for high-risk actions, allow a timed veto for medium-risk ones, and automate only low-risk actions.…

## Tags
`#agents` `#production-ai` `#archonos`
