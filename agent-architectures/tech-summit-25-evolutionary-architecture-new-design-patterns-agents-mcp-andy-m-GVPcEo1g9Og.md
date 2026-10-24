# Tech Summit '25 - Evolutionary Architecture - New design patterns, Agents & MCP (Andy Masters)

**URL:** https://www.youtube.com/watch?v=GVPcEo1g9Og
**Added:** 2026-10-24
**Relevance:** ⭐⭐⭐⭐ (4/5)

## Key Takeaways
- Clarify the problem before deciding whether an MCP server is the right solution.…
- Break the problem into building blocks, then define the server’s specialist functions, tools, and resources.…
- Make the server’s metadata clear and self-describing so AI hosts can understand its capabilities.…
- Track changes to the MCP specification to avoid breakage as new features are added.…
- Review MCP server code and verify its source before trusting it, because MCP does not prevent malicious or tainted software.…
- Manage the number of tools and servers exposed to a model; group them into nested systems if the model is overwhelmed.…
- Try Claude for Desktop or build an MCP server and tools to experiment with the protocol.…

## Apply to ArchonOS
- Tool use: check against the ArchonOS MCP catalog — if this pattern needs a new tool surface, it belongs in the shared MCP layer rather than inside one archon. _(from: "Clarify the problem before deciding whether an MCP server is the right solution.…")_

## TubeOnAI Summary
> MCP lets AI hosts discover and use self-describing tools and data sources, which can make integrations more adaptable and reduce the effort of connecting legacy systems. Masters recommends experimenting with MCP while treating security, reliability, and the fast-changing specification as real concerns.

Advice
- Clarify the problem before deciding whether an MCP server is the right solution.
- Break the problem into building blocks, then define the server’s specialist functions, tools, and resources.
- Make the server’s metadata clear and self-describing so AI hosts can understand its capabilities.
- Track changes to the MCP specification to avoid breakage as new features are added.
- Review MCP server code and verify its source before trusting it, because MCP does not prevent malicious or tainted software.
- Manage the number of tools and servers exposed to a model; group them into nested systems if the model is overwhelmed.
- Try Claude for Desktop or build an MCP server and tools to experiment with the protocol.
Mentioned
- Protocols: Model Context Protocol (MCP), Agent-to-Agent protocol (A2A)
- Products: Claude for Desktop, ChatGPT, Claude, Gemini 2.5
- Tools: FastMCP, MCP Inspector, Visual Studio Code, Ollama
- Companies: Anthropic, AWS, Customd
- Sources: modelcontextprotocol.io
Numbers to remember
- Late 2024: Anthropic launched MCP.
- Three: MCP servers offer tools, resources, and prompts, each described with metadata.
- Seven versus 70: Masters compares managing seven people with managing 70 to explain how too many servers or tools can overwhelm a model.
- One to one: Masters describes A2A as connecting agents directly, in contrast with MCP’s coordination across multiple tools or agents.

## Tags
`#agent` `#architecture` `#orchestration` `#memory` `#rag` `#mcp`
