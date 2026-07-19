# CompactionRL: Reinforcement Learning with Context Compaction for Long-Horizon Agents (Jul 2026)

**URL:** https://www.youtube.com/watch?v=-HPThjYR_jA
**Added:** 2026-07-19
**Relevance:** ⭐⭐⭐ (3/5)
**Channel:** AI Paper Slop
**Published:** 8 days ago
**Duration:** 18:08

## Key Takeaways
- **💡 Core idea of CompactionRL** — Addresses the context window bottleneck in long-horizon agents, especially for coding and terminal tasks where logs, tool outputs, and reasoning quickly exceed available tokens.
- **🔥 Why standard RL fails under compaction** — Methods such as PPO, GRPO (Group Relative Policy Optimization), and RLOO assume a rollout is a continuous sequence from prompt to terminal outcome.
- **🍳 Why the summarizer must be part of the policy** — A frozen external summarizer changes downstream performance substantially, showing that summary quality directly affects agent capability.
## Apply to ArchonOS
- Treat context compaction as a policy that can be evaluated and optimized, not a fixed summarization prompt.
- Score compacted state by downstream task success and retained tool facts, with rollback when the summary loses critical constraints.
- Prototype training-free A/B tests first: compare current summaries against task-aware compaction on long Hermes runs.

## TubeOnAI Summary
> 💡 Core idea of CompactionRL – Addresses the context window bottleneck in long-horizon agents, especially for coding and terminal tasks where logs, tool outputs, and reasoning quickly exceed available tokens. – Standard workaround is context compaction: pause the rollout, summarize prior history, discard raw history, and continue from the summary plus recent context. – The paper’s claim is that standard RL methods break when a single rollout is split into variable-length compacted segments. – CompactionRL treats summarization itself as a learned action within the policy, optimized jointly with execution using the same terminal task reward. 🔥 Why standard RL fails under compaction – Methods such as PPO, GRPO (Group Relative Policy Optimization), and RLOO assume a rollout is a continuous sequence from prompt to terminal outcome. – Under compaction, one rollout may remain a single…

## Tags
`#memory` `#context-engineering` `#retrieval` `#agents` `#archonos-improvement`
