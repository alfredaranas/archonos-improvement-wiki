# Tool Calling Explained: How AI Agents Use APIs and Tools

**URL:** https://www.youtube.com/watch?v=mCnsIHja5cw
**Added:** 2026-09-19
**Relevance:** ⭐⭐⭐ (3/5)

## Key Takeaways
- Tool calling lets a model request live information or actions without executing code itself. The application runs the requested tool, returns its result, and asks the model to produce an answer grounded in that data.…
- - Treat tool descriptions and input schemas like prompts, because they determine when and how the model uses each tool.
- Keep the model as the decision maker and let application code execute tools and handle their results.
- Inject cheap, static facts such as
- - Products: Amazon Bedrock, Claude, ChatGPT
- Tools: get weather, get current date time
- Software: Converse API, Python standard library
- Companies: Anthropic, GitHub, Slack
- Protocols: Model Context Protocol (MCP), USB-C
- Sources: Anthropic release notes


## Apply to ArchonOS
- Tool calling lets a model request live information or actions without executing code itself.
- The application runs the requested tool, returns its result, and asks the model to produce an answer grounded in that data.
- Advice

- Treat tool descriptions and input schemas like prompts, because they determine when and how the model uses each tool.

## TubeOnAI Summary
> Tool calling lets a model request live information or actions without executing code itself. The application runs the requested tool, returns its result, and asks the model to produce an answer grounded in that data.

Advice

- Treat tool descriptions and input schemas like prompts, because they determine when and how the model uses each tool.
- Keep the model as the decision maker and let application code execute tools and handle their results.
- Inject cheap, static facts such as the current date into the model's context instead of maintaining a separate tool.
- Use tools for live information such as weather, because the application cannot know in advance which changing facts a question will require.
- Define every input a tool needs in its schema, and create a different tool when the task requires an input the existing tool does not support.
- When an application has many tools across several services, use Model Context Protocol rather than hand-wiring every integration.
- Treat a multi-step sequence of tool calls as an agent when the model must inspect results and choose the next action.

Mentioned

- Products: Amazon Bedrock, Claude, ChatGPT
- Tools: get weather, get current date time
- Software: Converse API, Python standard library
- Companies: Anthropic, GitHub, Slack
- Protocols: Model Context Protocol (MCP), USB-C
- Sources: Anthropic release notes
- Related episodes: Episode 2, the next episode on building an agent with Strands

Numbers to remember

- 4 steps make

## Tags
`#agents` `#mcp` `#claude` `#context`
