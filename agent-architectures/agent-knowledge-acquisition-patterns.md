# Four Knowledge Acquisition Patterns for AI Agents: Skills, MCP, RAG, Memory

> **Source:** [Skills vs MCP vs RAG vs Memory: What AI Agents Need to Know](https://youtube.com/watch?v=X4FVEEegCbk)
> **Channel:** IBM Technology · **Published:** 2026-09-03 · **Ingested:** 2026-09-27
> **Relevance score:** 9/10

## Summary

AI agents require structured approaches to access knowledge beyond training data. Skills provide procedural guidance, MCP enables external system integration, RAG retrieves curated documents on-demand, and Memory captures learned experience. Each pattern solves different knowledge acquisition problems and should be combined based on use case requirements.

## Key Takeaways

- Skills: Structured procedures with judgment gates—use for repeatable workflows with escalation logic. Solves 'what steps should the agent take' but not 'how to access external systems'
- MCP (Model Context Protocol): Standardized agent-to-service connectivity without proprietary integrations. Solves 'how does the agent reach external APIs/dashboards/systems' via protocol-based servers
- RAG: Retrieve human-curated documents (manuals, runbooks, dependency maps) on-demand via semantic search. Solves 'how does the agent access domain knowledge someone already documented'
- Memory: Agent-stored experience from past executions. Solves 'how does the agent capture and reuse non-documented solutions discovered through experience'

## ArchonOS Applicability

ArchonOS homelab agents should layer all four: Skills define homelab management procedures (backups, deployments), MCP connects to local services (Docker, metrics, git), RAG indexes homelab documentation/configs, and Memory accumulates troubleshooting patterns. Critical for evolving agent autonomy from manual runbooks to learned operational expertise.

---

`#agent-architectures` `#auto-ingested` `#youtube`
