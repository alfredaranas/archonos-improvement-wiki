# Agentic AI E04 Agentic Design Patterns: ReAct, Planning, Reflection, Orchestrator & Evaluator

**URL:** https://youtube.com/watch?v=QUdPxZmhQh8
**Channel:** RoboSathi
**Added:** 2026-11-07
**Relevance:** ⭐⭐⭐⭐ (4/5)

## Key Takeaways
- Use deterministic workflows for steps that are known in advance, and agentic patterns when the model needs to decide actions at run time.
- Set limits on agent loops, searches, fetches, model calls, time, and revision rounds so the agent cannot run indefinitely or waste tokens.
- In a ReAct loop, check that the final answer matches tool results; a model's reasoning is not evidence, and repeated or duplicate actions can signal a stuck loop.
- Use reflection when a second review is affordable, but cap the rounds because a model can be biased toward its own work.
- Give evaluator-optimizers clear rubrics, and keep the evaluator independent with a different model and fresh context.

## Apply to ArchonOS
- Test the technique against Oracle's Ollama lanes (:11434 CUDA / :11436 iGPU) and measure context length + latency before adopting.
- A/B the change on a real wiki-summary workload and record the quality/throughput delta in the ArchonOS notes.
- Check whether the ArchonOS inference router needs a lane-specific setting rather than a global one.

## TubeOnAI Summary
> An agentic pattern gives the language model at least one decision about what to do next, whether work is good enough, or how to split a task. Each decision needs a fence, such as a step limit, budget, or independent review, to prevent wasted work and cost.
> 
> ## Advice
> - Use deterministic workflows for steps that are known in advance, and agentic patterns when the model needs to decide actions at run time.
> - Set limits on agent loops, searches, fetches, model calls, time, and revision rounds so the agent cannot run indefinitely or waste tokens.
> - In a ReAct loop, check that the final answer matches tool results; a model's reasoning is not evidence, and repeated or duplicate actions can signal a stuck loop.
> - Use reflection when a second review is affordable, but cap the rounds because a model can be biased toward its own work.
> - Give evaluator-optimizers clear rubrics, and keep the evaluator independent with a different model and fresh context.
> - Decompose tasks up front when their structure is predictable; use an orchestrator when subtasks or assignments need to be determined at run time.…

## Tags
`#agents` `#agent-architectures` `#archonos`
