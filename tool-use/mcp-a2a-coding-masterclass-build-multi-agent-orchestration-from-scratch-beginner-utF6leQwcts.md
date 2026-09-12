# MCP + A2A Coding Masterclass: Build multi-agent orchestration from scratch (Beginner to Pro)

**URL:** https://youtube.com/watch?v=utF6leQwcts
**Added:** 2026-09-05
**Relevance:** ⭐⭐⭐⭐ (4/5)

## Key Takeaways
- **🔧 Build MCP servers** — Terminal server: FastMCP stdio tool run_command via subprocess in a fixed workspace; main block runs mcp.run with transport "stdio".
- **🛠️ Configure clients (Claude Desktop and local)** — Claude Desktop: stdio server via uv run; streamable HTTP via MCP Remote (npx) to http://localhost:3000/mcp/ with trailing slash.…
- **🔍 MCP discovery and connector** — MCPDiscovery reads mcp_config.json and exposes the MCP servers map (name → command/args).
- **🧪 Test MCP tools** — Terminal tool can create/edit files in the workspace; arithmetic tool returns result and expression with structured input/output.…
- **🤖 Build A2A remote agent (Website Builder)** — Agent loads instructions/description from files, builds LLMAgent (ADK) with model Gemini 2.

## Apply to ArchonOS
- MCP server surface: expose ArchonOS tools via streamable-HTTP MCP for external agents
- Document MCP 'transport' choices (stdio vs streamable-http) in our internal tool-use guide
- Implement A2A-style remote agent invocation so archons can call sister-archon tools natively

## TubeOnAI Summary
> 🔧 Build MCP servers
  – Terminal server: FastMCP stdio tool run_command via subprocess in a fixed workspace; main block runs mcp.run with transport "stdio".
  – Streamable HTTP server: FastMCP with statelesshttp=True on port 3000, Pydantic ArithmeticInput/Output, async tool addnumbers, transport "streamable-http".

🛠️ Configure clients (Claude Desktop and local)
  – Claude Desktop: stdio server via uv run; streamable HTTP via MCP Remote (npx) to http://localhost:3000/mcp/ with trailing slash.
  – Local mcpconfig.json: mark HTTP servers with command "streamablehttp" and URL arg; keep stdio entries as uv run with command/args.

🔍 MCP discovery and connector
  – MCPDiscovery reads mcp_config.json and exposes the MCP servers map (name → command/args).
  – MCPConnector builds MCPToolSet per server using Google ADK adapters (StreamableHttpServerParams or StdioConnectionParams); async get_tools() returns toolsets for agent use.

🧪 Test MCP tools
  – Terminal tool can create/edit files in the workspace; arithmetic tool returns result and expression with structured input/output.

🤖 Build A2A remote agent (Website Builder)
  – Agent loads instructions/description from files, builds LLMAgent (ADK) with model Gemini 2.5, no external tools.
  – Runner uses in-memory artifact/session/memory services; invoke yields streaming dicts: {is_task_complete, updates|content}.

🧩 Implement A2A Agent Executor and Server
  – AgentExecutor exposes async execute/cancel with RequestContext and EventQ; uses TaskUpdater to send TaskState updates and final result.
  – Starlette A2A server publishes AgentCard via DefaultRequestHandler; default port 10000.

🗂️ Agent registry, discovery, and connector (A2A)
  – agentregistry.json lists base URLs; AgentDiscovery fetches AgentCards via .well-known/agent.json* using httpx and A2ACardResolver.
  – AgentConnector wraps A2AClient; send_task builds SendMessageRequest with message parts and returns the response text.

🧠 Build Host Orchestrator Agent
  – HostAgent loads MCP tools via MCPConnector and routes to A2A agents via AgentDiscovery + AgentConnector.
  – Exposes tools: list_agents() (returns AgentCard dumps) and delegate_task(agent_name, message) (match by name/id, send via AgentConnector); A2A server on 10001.

🖥️ CLI app to talk to Host Agent
  – cmd.py prompts user, resolves Host AgentCard (A2ACardResolver), sends messages via AgentConnector; supports custom session id and quit flow.

🔐 Environment and models
  – .env with GOOGLE_API_KEY; load via load_dotenv before agent creation.
  – Use Gemini 2.5 for both agents; observe free limits (e.g., 10 RPM, 500 RPD).

⚙️ Key async/refactor fixes
  – Make HostAgent.buildagent and MCPConnector.gettools async; add HostAgent.create() and HostAgentExecutor.create() to await discovery.
  – AgentConnector payload uses messageId (not sessionId); MCPConnector loads tools per-server with try/except; use dict .items() when iterating servers.

▶️ Run and verify
  – Start: MCP HTTP server on 3000; Website Builder A2A on 10000; Host Agent A2A on 10001; CLI app connects to Host by default.
  – End-to-end: Host delegates HTML generation to Website Builder, writes file via Terminal MCP; arithmetic tool computes sums via HTTP MCP.

📁 Notable files/dirs
  – mcp/servers/{terminalserver.py, streamablehttp_server.py}
  – utilities/{mcpconfig.json, mcpdiscovery.py, mcpconnect.py, a2a/agentregistry.json, a2a/agentdiscovery.py, a2a/agentconnect.py, common/file_loader.py}
  – agents/{websitebuildersimple, hostagent}/{agent.py, agentexecutor.py, main.py}
  – app/cmd/{init.py, cmd.py}

## Tags
#tooluse #tool #mcp
