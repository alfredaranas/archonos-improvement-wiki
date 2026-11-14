# AI System Design Tutorial

**URL:** https://youtube.com/watch?v=S6jy0T85DFs
**Channel:** codebasics
**Added:** 2026-11-07
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- Define functional requirements and measurable limits before designing, including latency, budget, privacy, and uptime targets.
- Estimate daily traffic, peak throughput, and token use; do not treat 10,000 users as 10,000 concurrent requests.
- Add authentication, rate limits, and an API gateway to control access, limit usage, and filter suspicious traffic.
- Use input and output guardrails, and have legal and compliance teams decide what the chatbot must never say or disclose.
- Cache only stable knowledge answers; exclude user-specific actions and changing information such as live prices. Invalidate affected cache entries when source data changes.

## Apply to ArchonOS
- Check the cost lever against the current TubeOnAI and fleet LLM spend on Oracle's node.
- Measure the saving on a real workload before changing defaults.
- Document the trade-off in the ArchonOS cost notes.

## TubeOnAI Summary
> A production AI system needs more than an LLM call: it needs clear requirements, safeguards, cost controls, resilience, and monitoring. Start with the simplest approach that meets the need, then add complexity only where the task requires it.
> 
> ## Advice
> - Define functional requirements and measurable limits before designing, including latency, budget, privacy, and uptime targets.
> - Estimate daily traffic, peak throughput, and token use; do not treat 10,000 users as 10,000 concurrent requests.
> - Add authentication, rate limits, and an API gateway to control access, limit usage, and filter suspicious traffic.
> - Use input and output guardrails, and have legal and compliance teams decide what the chatbot must never say or disclose.
> - Cache only stable knowledge answers; exclude user-specific actions and changing information such as live prices. Invalidate affected cache entries when source data changes.
> - Route emotionally sensitive or high-stakes cases, such as cancellation disputes, to a human.
> - Use the least costly approach that can handle each task, from rules and classifiers to smaller or more capable language models.…

## Tags
`#agents` `#production-ai` `#archonos`
