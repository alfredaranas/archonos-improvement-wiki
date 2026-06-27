# EP02: The Agentic Loop: Where 27% of the Claude Certification Lives

**URL:** https://www.youtube.com/watch?v=LTgjnnkYOtA
**Channel:** Vivek Amilkanthawar
**Added:** 2026-06-27
**Published:** 2 weeks ago
**Duration:** 8m 30s
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- **🔥 Agentic loop overview (core to the exam)** — An agent is a repeating 4-step loop: send conversation + tool definitions → get model response → run requested tools → append results and repeat.…
- **🧠 Statelessness and history management** — The API is stateless; the only memory is the message history you send each turn.…
- **🛠️ Tool execution and result protocol** — For every tooluse block, create exactly one toolresult with a matching id (one-to-one mapping).…
- **🧭 Decision-making location** — Prefer model-driven decisions: the model decides which tool to call next based on context.…
- **🚫 Exam-tested anti-patterns** — Parsing natural language to decide completion (e.g., searching for “task complete”).…

## Apply to ArchonOS
- Adopt the 4-step agentic loop pattern (send conversation + tools → get response → run tools → append results) as the canonical execution cycle for every ArchonOS agent invocation.
- Surface `stop_reason` from every LLM call as the canonical termination signal — `end_turn` ends the loop, `tool_use` continues it.
- Treat function/tool-calling as the *only* external-system boundary: every API, DB, or service call must go through a registered tool definition rather than freeform prompt instructions.

## Subjects
- Multi-Agent Systems
- Agent Orchestration
- Memory Systems
- Tool Use
- Context Engineering
- Agent Loops

## Key Quotes
- ".  
  – If stop_reason == "
- ", the model is requesting a tool; your code executes it (the model never runs tools itself).  
  – Other values: "
- " = truncation (not completion); "

## TubeOnAI Summary
> 🔥 Agentic loop overview (core to the exam)     – An agent is a repeating 4-step loop: send conversation + tool definitions → get model response → run requested tools → append results and repeat.     – Check the response field stop_reason every turn; it is the termination signal source.     – Loop ends only when stop_reason == "end_turn".     – If stop_reason == "tool_use", the model is requesting a tool; your code executes it (the model never runs tools itself).     – Other values: "max_tokens" = truncation (not completion); "pause_turn" = server-side pause; continue by sending the response back. 🧠 Statelessness and history management     – The API is stateless; the only memory is the message history you send each turn.     – Always append the entire assistant response, including its tool_use blocks, to history before running tools.     – Dropping tooluse blocks breaks the next call beca…

## Tags
`#memory` `#context-engineering` `#tools` `#orchestration` `#agent-loop` `#tool-use` `#agentic-loop` `#claude` `#patterns` `#archonos`
