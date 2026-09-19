# Code Mode: Why AI Agents Are Ditching Tool Calls for Code

**URL:** https://www.youtube.com/watch?v=IXe48aIw_X4
**Added:** 2026-09-19
**Relevance:** ⭐⭐⭐ (3/5)

## Key Takeaways
- Code mode lets agents write and execute code that composes tools, handles complex operations quickly, and extends software through defined interfaces. It is most useful when ordinary tool calls create too many round trips or overwhelm the context window.…
- Advice
- Use code mode when an agent needs to discover and compose dozens of tools, especially across services such as Slack, GitHub, email, and social platforms.
- Use code mode when an agent must traverse or modify complex data structures, such as a YJS CRDT
- Mentioned
- Products: Code Mode, Bash, MCP, Open Code, BAML, CodeX harness, Claude Code harness
- Tools and l…

## Apply to ArchonOS
- Code mode lets agents write and execute code that composes tools, handles complex operations quickly, and extends software through defined interfaces.
- It is most useful when ordinary tool calls create too many round trips or overwhelm the context window.
- Advice
- Use code mode when an agent needs to discover and compose dozens of tools, especially across services such as Slack, GitHub, email, and social platforms.

## TubeOnAI Summary
> Code mode lets agents write and execute code that composes tools, handles complex operations quickly, and extends software through defined interfaces. It is most useful when ordinary tool calls create too many round trips or overwhelm the context window.

Advice
- Use code mode when an agent needs to discover and compose dozens of tools, especially across services such as Slack, GitHub, email, and social platforms.
- Use code mode when an agent must traverse or modify complex data structures, such as a YJS CRDT document, rather than exposing a large custom tool schema.
- Let agents use familiar JavaScript or TypeScript SDKs when those libraries are already well represented in their training data.
- Execute sequences of operations as code when repeated model calls could make the underlying data change before the agent finishes.
- Sandbox untrusted generated code in multi-tenant systems, deny network, file, shell, and reflection access by default, and impose memory and time limits.
- Inject narrow bindings or wrappers instead of exposing backend objects and credentials directly to generated code.
- Add compile-time interface checks when dynamically generated code must satisfy application contracts, and return clear compiler or runtime errors to the agent.
- Avoid code mode when the problem does not need tool composition, dynamic discovery, or fast multi-step execution.

Mentioned
- Products: Code Mode, Bash, MCP, Open Code, BAML, CodeX harness, Claude Code harness
- Tools and l

## Tags
`#memory` `#agents` `#mcp` `#claude` `#context`
