# Async Agents in Production: Failure Modes and Fixes — Seb Ringrose | AI in Production 2026

**URL:** https://www.youtube.com/watch?v=rdbdM_RnLCk
**Added:** 2026-07-19
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)
**Channel:** Jumping Rivers
**Published:** 13 days ago
**Duration:** 20:01

## Key Takeaways
- **Key insight** — Long-running agentic tasks are increasingly feasible: earlier models handled tasks lasting seconds, while current top coding models can often complete tasks lasting hours without follow-up.
- **🔥 Case study: an autonomous pull request review agent** — The use case is a PR review bot triggered by a GitHub webhook.
- **🧰 Tooling strategy: reuse existing coding-agent infrastructure instead of building from scratch** — A major challenge is giving the agent the right tools to inspect code and operate on repositories.
- **🤖 Model selection is a first-order production decision** — Suitable model families for this kind of work include:
- **Long-running agents need durable checkpoints** — Background work should persist progress outside model context and expose cancellation, retry, timeout, and partial-result semantics.
## Apply to ArchonOS
- Persist async job state and checkpoints outside the model so long-running work survives client timeouts and gateway restarts.
- Give every background run a wall cap, cancellation path, progress artifact, and direct-ID recovery path.
- Schedule model work by cost, context size, and expected duration; surface partial completion instead of retrying the whole workflow.

## TubeOnAI Summary
> 💡 Core thesis: async agents are becoming practical, but production use is constrained by model choice, tooling, context growth, cost, and scheduling – Long-running agentic tasks are increasingly feasible: earlier models handled tasks lasting seconds, while current top coding models can often complete tasks lasting hours without follow-up. – This shift makes background agents more useful for production workflows such as coding, review, research, and enterprise automation. – The main engineering question is no longer whether agents can act autonomously, but how to run them economically and reliably. 🔥 Case study: an autonomous pull request review agent – The use case is a PR review bot triggered by a GitHub webhook. – Requirements: – Read and grep the codebase – Search the web for supporting research and best practices – Run a multi-step reasoning loop – Return a code review back to…

## Tags
`#production-ai` `#reliability` `#governance` `#agents` `#archonos-improvement`
