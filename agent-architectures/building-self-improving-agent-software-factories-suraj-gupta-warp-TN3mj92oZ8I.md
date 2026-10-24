# Building Self-Improving Agent Software Factories — Suraj Gupta, Warp

**URL:** https://www.youtube.com/watch?v=TN3mj92oZ8I
**Added:** 2026-10-24
**Relevance:** ⭐⭐⭐⭐ (4/5)

## Key Takeaways
- Software factories can self-improve by adding outer-loop automation that updates how agents work over time, rather than leaving “factory maintenance” as manual engineering work.…
- For agent procedures, use skills (procedural memory) but assume they will go stale as humans give feedback and agents encounter new situations.…
- Improve stale skills with an outer-loop agent that watches an inner-loop agent’s runs, detects mistakes, and incorporates human feedback signals such as thumbs up or down and issue comments.…
- Warp’s example is a GitHub issue triage workflow where every new issue triggers an inner-loop triage agent, then an outer-loop agent synthesizes what went wrong or what feedback arrived and updates the triage skill.…
- Skill updates are shipped via a pull request, so changes are versioned in Git and reviewed by a human to prevent the outer loop from degrading the inner-loop agent’s performance.…
- For non-procedural reuse, add persistent memory as an agent-scoped fact store so agents do not re-gather the same context and can reuse root-cause learnings on similar future issues.…
- In Warp’s Oz platform, agents can attach memory stores, memories are created primarily by agents, can be versioned and edited or deleted by humans, and are traceable back to the run they came from; the example sentry-style agent later reports which…

## Apply to ArchonOS
- Memory: fold this into the Oracle vault + SupaBrain layer — decide whether it needs a new retrieval path, a new store, or just a better index over what already exists. _(from: "For agent procedures, use skills (procedural memory) but assume they will go stale as humans give feedback and agents encounter new situations.…")_
- Production AI: measure on the local inference lanes (:11434 CUDA / :11436 iGPU) before claiming a win — the router decides whether this changes lane routing. _(from: "Skill updates are shipped via a pull request, so changes are versioned in Git and reviewed by a human to prevent the outer loop from degrading the…")_

## TubeOnAI Summary
> Software factories can self-improve by adding outer-loop automation that updates how agents work over time, rather than leaving “factory maintenance” as manual engineering work.

- For agent procedures, use skills (procedural memory) but assume they will go stale as humans give feedback and agents encounter new situations.
- Improve stale skills with an outer-loop agent that watches an inner-loop agent’s runs, detects mistakes, and incorporates human feedback signals such as thumbs up or down and issue comments.
- Warp’s example is a GitHub issue triage workflow where every new issue triggers an inner-loop triage agent, then an outer-loop agent synthesizes what went wrong or what feedback arrived and updates the triage skill.
- Skill updates are shipped via a pull request, so changes are versioned in Git and reviewed by a human to prevent the outer loop from degrading the inner-loop agent’s performance.
- For non-procedural reuse, add persistent memory as an agent-scoped fact store so agents do not re-gather the same context and can reuse root-cause learnings on similar future issues.
- In Warp’s Oz platform, agents can attach memory stores, memories are created primarily by agents, can be versioned and edited or deleted by humans, and are traceable back to the run they came from; the example sentry-style agent later reports which five memories it used to speed up a new triage.
- Self-improvement also applies to cost and performance through model routing, because running simple factory tasks on an expensive model like Opus can become prohibitively costly, so Warp uses routing rules plus an eval sidecar that tries multiple models per prompt with a “best-at-k” approach to learn, for example, that some UI tasks work well on GLM instead of Opus.

## Tags
`#agent` `#architecture` `#orchestration` `#memory` `#rag` `#mcp`
