# Multi-Agent Architecture \u0026 Orchestration - Omar Elcircevi | AI Agents Bootcamp

**URL:** https://youtube.com/watch?v=NryqsRd48Mc
**Added:** 2026-10-10
**Relevance:** ⭐⭐⭐ (score 3/5)
**Source:** TubeOnAI summarization, see references/tubeonai-summary-extraction-2026-07-cascade.md

## Key Takeaways
- Multi-agent systems help when a single agent’s growing prompt becomes hard to test and maintain: a change to one instruction can affect unrelated behavior. The speaker recommends starting with one agent and splitting only when the task calls for it.
- An age

## Apply to ArchonOS
- Multi-agent orchestration takeaways apply to FOCUS card executor and the autonomous kanban system.

## TubeOnAI Summary
> - Multi-agent systems help when a single agent’s growing prompt becomes hard to test and maintain: a change to one instruction can affect unrelated behavior. The speaker recommends starting with one agent and splitting only when the task calls for it. - An agent combines a model, plain-language instructions, and tools, then loops through reasoning, tool use, and observation until it can answer. In the date demo, the model guessed the date without a tool; adding a Python date function let it return the actual current date. - Tools can be ordinary Python functions. The framework uses their names, type hints, and docstrings to describe them to the model, so the docstring should clearly state what the function does and when to use it. - The session state acts as a shared workspace between agents. An agent writes its result under an output key, and later agents can use that value in their instructions; parallel agents need distinct keys to avoid overwriting one another’s results. - A sequential workflow runs agents in a developer-defined order. The example sends research notes from a researcher to a writer, which uses the shared state to produce a brief. - Parallel workflows suit independent tasks: three researchers cover background, current conditions, and future outlook at the same time, then a writer combines their results. A trace view shows their overlapping execution and the writer starting after they finish. - A critic-and-revision loop has one agent assess a draft and a…

## Tags
#archonos-improvement #agent-architectures #agents
