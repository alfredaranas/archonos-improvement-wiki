# Claude Architect Track — Month 2: Tool Design \u0026 MCP

**URL:** https://youtube.com/watch?v=eEF-wHXjHso
**Added:** 2026-07-25
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- **💡 Month 2 focus: from prompt architecture to system-integrated agents via MCP** — Month 1 covered how Claude reasons: system prompts, context injection, and conversation structure.…
- **🔥 MCP mental model: client-server protocol for Claude tool use** — The client is Claude Desktop, an API integration, or a custom host app.…
- **🛠️ Transport modes and when to use each** — stdio: subprocess-style local integration using stdin/stdout.…
- **🍳 Tool definition quality is the main driver of correct tool selection** — Keep it short, machine-readable, and snake_case.…

## Apply to ArchonOS
- Map the pattern to the existing MCP/tool-use taxonomy in `tool-use/README.md`.
- Cross-link to the relevant entry in `agent-architectures/README.md`.
- Cross-link to the Claude-related entries in `archonos-notes/hermes-agentic-os-just-watch.md`.

## TubeOnAI Summary
> 💡 Month 2 focus: from prompt architecture to system-integrated agents via MCP
  – Month 1 covered how Claude reasons: system prompts, context injection, and conversation structure.
  – Month 2 covers how Claude acts: connecting to live databases, APIs, and queues through the Model Context Protocol (MCP).
  – The session’s goals are to design production-ready tool definitions, implement resources, connect backend systems, choose between tools vs context vs system prompts, and audit for security risks.

🔥 MCP mental model: client-server protocol for Claude tool use
  – The client is Claude Desktop, an API integration, or a custom host app.
  – The server is an MCP server that exposes tools and resources.
  – Message lifecycle:
    – initialize handshake for capability and transport negotiation.
    – tools/list to return tool definitions.
    – Claude reads all names, descriptions, and schemas before deciding what to call.
    – tools/call executes backend logic and returns either content or isError: true.
    – Claude can also read URI-based resources directly for bulk data access.
  – Server-Sent Events (SSE) in MCP means the MCP server pushes events to the client over a long-lived connection; it is not an external webhook mechanism.

🛠️ Transport modes and when to use each
  – stdio: subprocess-style local integration using stdin/stdout.
    – Best for local development and desktop tooling.
    – No network overhead or port management.
  – SSE: HTTP server with long-lived co

## Tags
`#ai-agents` `#archonos` `#tooluse`
