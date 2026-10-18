# Agent Loop & Harness: The 80% Beyond the Model

> **Source:** [How AI Agents Actually Work (Every Piece Explained &amp; Built)](https://youtube.com/watch?v=HzGOWq5UyjY)
> **Channel:** Tech With Tim · **Published:** 2026-09-03 · **Ingested:** 2026-10-18
> **Relevance score:** 8/10

## Summary

An AI agent is fundamentally a model placed in an execution loop where it observes goals, selects actions, executes them in reality, and feeds results back—iterating until task completion. The harness is the runtime orchestrator that manages this loop, handling prompt routing, tool execution, context windowing, and state persistence across restarts.

## Key Takeaways

- Model ≠ Agent: The model is ~20% of an agent; the other 80% is the orchestration layer (harness), tools, skills, and sandbox infrastructure
- Harness is the orchestrator: Manages the agent loop lifecycle, sends prompts to the model, executes tool calls, manages context windows, maintains state for long-running tasks, and abstracts model provider (model-agnostic)
- Agent loop pattern: Model observes goal → selects action → harness executes action in real environment → result fed back to model → repeat until completion

## ArchonOS Applicability

ArchonOS needs a production harness (like TrueForge) to orchestrate its agent loop reliably across homelab workloads. Understanding the harness-as-runtime enables ArchonOS to swap model providers, maintain task state through restarts, and manage resource-constrained execution in a home environment.

---

`#agent-architectures` `#auto-ingested` `#youtube`
