# Agent Orchestration Frameworks

**URL:** https://youtube.com/watch?v=TtzBQmOk2TE
**Added:** 2026-07-25
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- **💡 Core architecture of an AI agent** — A modern agent typically combines an LLM, a system prompt, a user prompt, tool access, and a surrounding harness.…
- **🧩 Harness engineering vs. orchestration** — Harness engineering focuses on how a single agent operates: what tools it can use, what memory it has, and how it is evaluated.…
- **🏗️ Three-layer stack** — Orchestration layer: decides which agent runs, when, and how work is handed off.…
- **🧠 Memory is a key part of the harness** — Short-term memory is usually the prompt context itself.…
- **🔌 MCP: Model Context Protocol** — MCP is a standardized way for agents to connect to tools, data sources, APIs, databases, and prompts.…

## Apply to ArchonOS
- Add a memory-layer hook to capture this pattern in `archonos-memory-system-architecture.md`.
- Document this orchestration pattern in `archonos-notes/improvement-todo.md` under multi-agent design.
- Map the pattern to the existing MCP/tool-use taxonomy in `tool-use/README.md`.
- Cross-link to the relevant entry in `agent-architectures/README.md`.

## TubeOnAI Summary
> 💡 Core architecture of an AI agent
  – A modern agent typically combines an LLM, a system prompt, a user prompt, tool access, and a surrounding harness.
  – The harness is the scaffolding around the model: tools, memory, permissions, context management, evaluation loops, and task-specific skills.
  – Agents may also contain sub-agents that perform specialized tasks under a lead agent.

🧩 Harness engineering vs. orchestration
  – Harness engineering focuses on how a single agent operates: what tools it can use, what memory it has, and how it is evaluated.
  – Orchestration focuses on how multiple agents coordinate: task routing, sequencing, retries, failure handling, and state sharing.
  – A useful analogy is an orchestra: orchestration decides who plays when; the harness determines how well each musician performs.
  – In practice, many frameworks do both at once.

🏗️ Three-layer stack
  – Orchestration layer: decides which agent runs, when, and how work is handed off.
  – Harness layer: gives each agent tools, memory, permissions, and local evaluation logic.
  – Model layer: the underlying LLM such as Claude Opus, GPT, or Gemini.
  – Failures can happen at any of these layers, so debugging agent systems is more complex than debugging a plain chatbot.

🧠 Memory is a key part of the harness
  – Short-term memory is usually the prompt context itself.
  – External memory can include vector databases, flat files, markdown notes, or session logs.
  – Some systems also use episodic 

## Tags
`#ai-agents` `#archonos` `#tooluse`
