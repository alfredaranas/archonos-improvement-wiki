# Route Tools Without Context Bloat

**URL:** https://www.youtube.com/watch?v=PgI7uJmwoAY
**Added:** 2026-09-19
**Relevance:** ⭐⭐⭐ (3/5)

## Key Takeaways
- Agents should receive MCP tools just in time instead of loading every available tool into each prompt. Hugo recommends combining identity-based filtering, an MCP registry, and gateway policies to reduce token use, latency, and reasoning errors.…
- - Give agents only the tools required for the current request, rather than exposing tools “just in case.”
- Put an MCP gateway between agents and MCP servers to centralize authentication, authorization, access controls, and observability.
- Use agent identitie
- - People: Hugo (Kong product team), Dedre
- Companies: Kong
- Tools: Jira, GitHub, Confluence, Slack, Insomnia, Visual Studio Code, Cloud Code, Codex
- Software: MCP, MCP gateway, MCP registry, LLM router, Context Mesh, Volcano SDK
- Services: GitHub MCP serve

## Apply to ArchonOS
- Agents should receive MCP tools just in time instead of loading every available tool into each prompt.
- Hugo recommends combining identity-based filtering, an MCP registry, and gateway policies to reduce token use, latency, and reasoning errors.
- - Use agent identities to filter available tools, so read-only users cannot access destructive operations such as deleting branches or repositories.

## TubeOnAI Summary
> Agents should receive MCP tools just in time instead of loading every available tool into each prompt. Hugo recommends combining identity-based filtering, an MCP registry, and gateway policies to reduce token use, latency, and reasoning errors.

Advice

- Give agents only the tools required for the current request, rather than exposing tools “just in case.”
- Put an MCP gateway between agents and MCP servers to centralize authentication, authorization, access controls, and observability.
- Use agent identities to filter available tools, so read-only users cannot access destructive operations such as deleting branches or repositories.
- Use an MCP registry for service discovery and endpoint resolution instead of hard-coding every server into the agent.
- Expose the registry through an MCP server so agents can search for and connect to services themselves.
- Maintain separate registries or catalogs for groups such as partners, developers, regular users, internal networks, and policy-compliant services.
- Use gateway policies for reasoning traffic, including personally identifiable information sanitization, text-based caching, and semantic routing.

Mentioned

- People: Hugo (Kong product team), Dedre
- Companies: Kong
- Tools: Jira, GitHub, Confluence, Slack, Insomnia, Visual Studio Code, Cloud Code, Codex
- Software: MCP, MCP gateway, MCP registry, LLM router, Context Mesh, Volcano SDK
- Services: GitHub MCP server, Jira MCP server, Chuck Norris jokes MCP server
- Standards: O

## Tags
`#agents` `#mcp` `#context`
