# Building AI Agents in Pure Python - Beginner Course

**URL:** https://www.youtube.com/watch?v=c9AnqCeyxbI
**Added:** 2026-09-19
**Relevance:** ⭐⭐⭐ (3/5)

## Key Takeaways
- The instructor argues that an AI agent is a small software system built from a language model, tools, and a loop. Building those parts directly in Python helps developers understand how agents reason, retain context, and perform tasks.…
- Advice
- Choose a language model that fits the project, using either a local API or a hosted provider such as OpenAI.
- Mentioned
- Products: OpenAI API, GPT-5 Mini, Claude Code, Cursor, Codex, Pygame
- Tools: UV, Whisper Flow, Docker Model Runner, LM Studio, Ollama, Model Context Protocol (MCP)
- Software: LangChain, Python, subprocess
- Companies: OpenAI, Anthropic, HubSpot
-

## Apply to ArchonOS
- The instructor argues that an AI agent is a small software system built from a language model, tools, and a loop.
- Building those parts directly in Python helps developers understand how agents reason, retain context, and perform tasks.
- Advice
- Choose a language model that fits the project, using either a local API or a hosted provider such as OpenAI.

## TubeOnAI Summary
> The instructor argues that an AI agent is a small software system built from a language model, tools, and a loop. Building those parts directly in Python helps developers understand how agents reason, retain context, and perform tasks.

Advice
- Choose a language model that fits the project, using either a local API or a hosted provider such as OpenAI.
- Keep conversation history and pass it back to the model, because language models do not remember previous messages by themselves.
- Write clear tool names, descriptions, and parameter schemas so the model knows when and how to request each tool.
- Let the agent software execute tool calls, rather than assuming the language model performs actions directly.
- Add user approval before running potentially destructive tools such as shell commands or file-writing functions.
- Before building an agent, test whether the task is repetitive, uses structured data, allows about 90% accuracy, and has measurable success criteria. Keep a human involved if it fails those checks.
- Use environment variables for API keys instead of placing raw keys directly in source code.

Mentioned
- Products: OpenAI API, GPT-5 Mini, Claude Code, Cursor, Codex, Pygame
- Tools: UV, Whisper Flow, Docker Model Runner, LM Studio, Ollama, Model Context Protocol (MCP)
- Software: LangChain, Python, subprocess
- Companies: OpenAI, Anthropic, HubSpot
- Sources: HubSpot’s AI Agents Unleashed playbook, HubSpot’s “Is This an Agent Job?” decision tree
- Projects: mini c

## Tags
`#agents` `#mcp` `#claude` `#context` `#langchain`
