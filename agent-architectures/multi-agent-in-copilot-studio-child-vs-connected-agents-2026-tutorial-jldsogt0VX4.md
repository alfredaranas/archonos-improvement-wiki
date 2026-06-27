# Multi-Agent in Copilot Studio: Child vs Connected Agents — 2026 Tutorial

**URL:** https://www.youtube.com/watch?v=jldsogt0VX4
**Channel:** Corporate Programming
**Added:** 2026-06-27
**Published:** 8 days ago
**Duration:** 23m 58s
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- **🔧 Architecture and flow** — Multi-agent orchestration with a Parent agent and two Child agents (Technical, Billing); parent detects intent, routes to the right child, then consolidates and refines the child’s answer.…
- **🗂 Knowledge base design** — SharePoint list fields include Category and Content; categories drive agent routing and retrieval.…
- **🧭 Instruction design (critical for routing and answer quality)** — Parent instructions define: intent detection, routing rules (when to invoke Technical vs Billing), sequence for handling queries, and response formatting rules.…
- **🛠 Build steps (end-to-end)** — Step 1: Create a blank parent agent; select an LLM (Copilot Studio offers OpenAI and Claude; example uses Claude Sonnet 4.6).…
- **🤝 Child vs Connected agents** — New child agent: created within the parent; configured specifically for this solution.…

## Apply to ArchonOS
- Replace single-agent tool-heavy patterns with a Parent + Child routing architecture — supervisor agent detects intent, child agents own domain-specific tools, parent consolidates and refines the response.
- Adopt a cognitive anatomy for agents: planning / memory / tools / actions layers with explicit boundaries, mirroring the 2026 production-grade framework comparison.
- Push from chatbot-style reactive flows to proactive orchestration: agents that decompose problems, delegate to specialists, and iterate to completion autonomously.

## Subjects
- Multi-Agent Systems
- Agent Orchestration
- RAG
- Tool Use
- Context Engineering
- Planning Patterns
- Copilot Studio

## TubeOnAI Summary
> - 🔧 Architecture and flow     – Multi-agent orchestration with a Parent agent and two Child agents (Technical, Billing); parent detects intent, routes to the right child, then consolidates and refines the child’s answer.     – Knowledge solely from a SharePoint list used as the KB; no public web search.     – Categories in KB: Technical, Billing, General; child agents filter by category via their instructions. - 🗂 Knowledge base design     – SharePoint list fields include Category and Content; categories drive agent routing and retrieval.     – Child agents are instructed to search only their category-specific KB (e.g., Technical KB, Billing KB).     – Disable Web search so responses come exclusively from internal articles/policies. - 🧭 Instruction design (critical for routing and answer quality)     – Parent instructions define: intent detection, routing rules (when to invoke Technical …

## Tags
`#multi-agent` `#rag` `#context-engineering` `#orchestration` `#copilot-studio` `#archonos` `#agent-architectures`
