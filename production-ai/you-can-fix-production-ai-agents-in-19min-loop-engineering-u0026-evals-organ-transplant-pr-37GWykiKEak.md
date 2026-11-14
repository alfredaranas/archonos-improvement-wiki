# You Can Fix Production AI Agents in 19min: Loop Engineering & Evals | Organ Transplant Project

**URL:** https://youtube.com/watch?v=37GWykiKEak
**Channel:** Dr. Maryam Miradi
**Added:** 2026-11-14
**Relevance:** ⭐⭐⭐⭐ (4/5)

## Key Takeaways
- Use expert-approved medical definitions, map synonyms and abbreviations to concepts, verify units and timestamps, and test ambiguous terms.
- Apply deterministic rules and clinical review to critical decisions.
- Require fresh evidence for each loop iteration, and track repeated errors rather than treating the agent’s earlier estimates as evidence.
- Define what counts as improvement, set iteration limits and stop conditions, and separate planning from authorized actions.
- Compare transport options before committing, and control tool actions with approvals, retries, and idempotency.

## Apply to ArchonOS
- Test the technique against Oracle's Ollama lanes (:11434 CUDA / :11436 iGPU) and measure context length + latency before adopting.
- A/B the change on a real wiki-summary workload and record the quality/throughput delta in the ArchonOS notes.
- Check whether the ArchonOS inference router needs a lane-specific setting rather than a global one.

## TubeOnAI Summary
> Production transplant agents need domain-aware semantics, evidence-grounded loops, and risk-based evaluations; otherwise, they can misread medical records, compound guesses, take conflicting actions, or pass flawed safety tests.
> 
> ## Advice
> - Use expert-approved medical definitions, map synonyms and abbreviations to concepts, verify units and timestamps, and test ambiguous terms.
> - Apply deterministic rules and clinical review to critical decisions.
> - Require fresh evidence for each loop iteration, and track repeated errors rather than treating the agent’s earlier estimates as evidence.
> - Define what counts as improvement, set iteration limits and stop conditions, and separate planning from authorized actions.
> - Compare transport options before committing, and control tool actions with approvals, retries, and idempotency.
> - Evaluate task completion, safety, escalation, and latency together; do not reward a policy simply for escalating every case.
> - Test routine, critical, and adversarial cases separately, track critical recall and false negatives, and block releases when critical gates fail.
> - Run regression tests to detect changes and drift.

## Tags
`#agents` `#production-ai` `#archonos`
