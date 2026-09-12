# How to Use Agentic AI: LLMs, AI Agents & Prompt Engineering in Action

**URL:** https://youtube.com/watch?v=bwvfdFWR1RI
**Added:** 2026-09-05
**Relevance:** ⭐⭐⭐ (3/5)

## Key Takeaways
- **🍳 Example** — two inputs—items not included in the order and employee notes; goal is to ensure an explanation exists for each item, with missing ones output as "Item - No explanation".
- **🪜 Typical agentic workflow layout** — P1 extract items with explanations; P2 validate each reason; P3 compare results with the original list; P4 generate the final text.…
- **🧭 Prompts function as distinct tasks** — extraction, classification/validation, comparison, and generation; this structuring clarifies responsibilities and reduces cognitive load on the LLM.

## Apply to ArchonOS
- Adopt hub-and-spoke coordinator pattern for cross-archon orchestration (Oracle ↔ Yoda ↔ Jarvis)
- Add durable-execution primitives (Temporal-style) to ArchonOS so workflows survive crashes
- Use task-decomposition + parallel-sub-agent pattern for long-running research tasks

## TubeOnAI Summary
> - 🔥 If the largest LLM cannot solve a task with a single prompt, adopt an agentic workflow to decompose the problem into multiple prompts or functions.
  - Breaks the work into specialized steps (extraction, validation, generation) to reduce model confusion.

- 🍳 Example: two inputs—items not included in the order and employee notes; goal is to ensure an explanation exists for each item, with missing ones output as "Item - No explanation".
  - The process demonstrates feed-forward chaining where each step relies on the previous outputs.

- 💡 A single prompt often fails due to edge cases and task complexity; dividing the work avoids the model trying to do everything at once.
  - Each step has a focused objective (extraction, validation, comparison, final output).

- 🪜 Typical agentic workflow layout: P1 extract items with explanations; P2 validate each reason; P3 compare results with the original list; P4 generate the final text.
  - The design can use three or four prompts, or non-prompt functions for certain steps.

- 🧭 Prompts function as distinct tasks: extraction, classification/validation, comparison, and generation; this structuring clarifies responsibilities and reduces cognitive load on the LLM.
  - The approach can mix prompts and other text functions to implement the workflow.

## Tags
#agentarchitectures #agent #agents
