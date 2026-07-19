# Deferred Tool Loading & Programmatic Tool Calling: Context-Efficient Agent Patterns

> **Source:** [Anthropic Just Changed How Agents Call Tools. I Stole It for My Qwen3.5 Agent](https://youtube.com/watch?v=R7OCrqyGMeY)
> **Channel:** The AI Automators · **Published:** 2026-03-07 · **Ingested:** 2026-07-19
> **Relevance score:** 9/10

## Summary

Two design patterns from Anthropic's beta features reduce token bloat in agent systems: tool search (deferred loading of tool schemas on-demand) and programmatic tool calling (executing tool sequences as executable code rather than sequential LLM calls). These patterns achieve ~85% token reduction and work across any LLM/framework—not Claude-exclusive.

## Key Takeaways

- Deferred tool loading: Don't load all tool schemas upfront. Implement a tool-search tool that agents query by name/keyword to load only needed schemas into context, reducing baseline context from 13K to 6.3K tokens in demonstrated example.
- Programmatic tool calling: When tool execution is deterministic/scriptable (e.g., iterate over results from one tool to feed into another), let agent generate and execute code instead of sequential LLM→tool→LLM→tool chains. Reduces redundant context bloat from intermediate responses.
- Framework-agnostic patterns: Both patterns are architectural designs, not API-specific. Implementable with any LLM (tested with Qwen 3.5) and any agent framework by managing tool registries and sandboxed code execution.

## ArchonOS Applicability

ArchonOS can implement deferred MCP tool loading to handle large tool catalogs without baseline context explosion, and use programmatic calling for multi-step MCP operations (e.g., sequential filesystem or GitHub queries). Critical for resource-constrained homelab deployments where context window is precious.

---

`#tool-use` `#auto-ingested` `#youtube`
