# Building MCP Apps With GraphQL Patterns You Already Know - Jerel Miller, Apollo GraphQL

**URL:** https://www.youtube.com/watch?v=IeRjaphHOeA
**Added:** 2026-07-19
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)
**Channel:** GraphQL TV
**Published:** 2 weeks ago
**Duration:** 29:05

## Key Takeaways
- **💡 What MCP apps are** — MCP app = an interactive UI rendered inside an MCP-compatible host such as Claude Desktop, ChatGPT, VS Code, Cursor, or similar tools.
- **🔥 How UI gets rendered from an MCP server** — A tool definition can include a UI resource URI in _meta.ui.
- **🧩 Apollo’s approach for MCP apps** — Apollo provides an AI apps package that adapts Apollo Client for MCP environments.
- **The host remains the security boundary** — MCP app iframes communicate through host-mediated messages rather than connecting directly to the MCP server.
## Apply to ArchonOS
- Treat interactive MCP resources as untrusted iframes mediated by the host; do not allow direct UI-to-server privilege escalation.
- Reuse schema-first GraphQL habits for MCP resources: typed payloads, explicit mutations, predictable errors, and subscriptions only when needed.
- Add host-level policy and telemetry for every UI-originated tool call so interactive apps remain auditable.

## TubeOnAI Summary
> 💡 What MCP apps are – MCP app = an interactive UI rendered inside an MCP-compatible host such as Claude Desktop, ChatGPT, VS Code, Cursor, or similar tools. – Instead of returning only text from a tool call, the host can render a full UI inside an iframe. – Core architecture has four pieces: user, host/agent, MCP app iframe, and MCP server. – The host is the orchestrator: the app iframe does not communicate directly with the MCP server. – Communication between the host and the iframe is primarily message passing via window.postMessage, usually abstracted by a library rather than used directly. 🔥 How UI gets rendered from an MCP server – A tool definition can include a UI resource URI in _meta.ui. – When the host requests that resource, the server returns: – the URI – a MIME type of text/html+skybridge-style MCP app HTML profile (the transcript references the MCP app HTML profile MIME…

## Tags
`#mcp` `#tool-use` `#schemas` `#agents` `#archonos-improvement`
