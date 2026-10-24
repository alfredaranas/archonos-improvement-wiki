# Agentic AI System Design Crash Course

**URL:** https://www.youtube.com/watch?v=TDReumVAUmI
**Added:** 2026-10-24
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- Keep context focused and within the model’s context-window limit; excess or irrelevant context can cause errors or off-topic responses.…
- Use a strong system prompt to define the agent’s role, scope, behavior, and boundaries; add examples, instructions on what to avoid, and relevant user history when needed.…
- Give an agent tools for the actions it must perform, such as searching the web, writing files, or posting messages.…
- Use loops with checklists, review, and clear stopping conditions to complete multi-step tasks without running indefinitely.…
- Connect specialized agents when a task spans domains, and design how their work passes between them.…
- Add input and output guardrails to detect unsafe or out-of-scope requests, prompt injection, and sensitive information leaks.…
- Instrument agent runs with traces of inputs, outputs, tool calls, token use, and handoffs so failures can be investigated.…

## Apply to ArchonOS
- Prompting/context: test against the Hermes system-prompt layering and the context compaction path before adopting. _(from: "Use a strong system prompt to define the agent’s role, scope, behavior, and boundaries; add examples, instructions on what to avoid, and relevant…")_

## TubeOnAI Summary
> A production agent needs more than a capable language model: it needs tools, orchestration, safeguards, observability, and evaluation. The course presents agent development as system design, with those surrounding components built and coordinated by engineers.

Advice
- Keep context focused and within the model’s context-window limit; excess or irrelevant context can cause errors or off-topic responses.
- Use a strong system prompt to define the agent’s role, scope, behavior, and boundaries; add examples, instructions on what to avoid, and relevant user history when needed.
- Give an agent tools for the actions it must perform, such as searching the web, writing files, or posting messages.
- Use loops with checklists, review, and clear stopping conditions to complete multi-step tasks without running indefinitely.
- Connect specialized agents when a task spans domains, and design how their work passes between them.
- Add input and output guardrails to detect unsafe or out-of-scope requests, prompt injection, and sensitive information leaks.
- Instrument agent runs with traces of inputs, outputs, tool calls, token use, and handoffs so failures can be investigated.
- Evaluate outputs, including with a separate language model acting as a judge, and use user feedback to improve the system.
Mentioned
- Models: large language models, Claude, ChatGPT, GPT-5.5
- Tools: web search, local code search, file writing, filesystem tools, computer-use tools, weather tools
- Software: Langfuse, Pydantic Logfire
- Platforms: Twitter, WhatsApp, LinkedIn
- Examples: coding agent, cooking agent, fitness agent
Numbers to remember
- 128K tokens: An example context-window size; the transcript’s spoken number is garbled, so the exact figure is uncertain.
- 1 million tokens: A context-window size attributed to newer models; the speaker says engineers still need to keep context focused.

*(summary truncated)*

## Tags
`#agent` `#architecture` `#orchestration` `#memory` `#rag` `#mcp`
