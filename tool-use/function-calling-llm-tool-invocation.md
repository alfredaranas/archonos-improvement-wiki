# Function Calling: LLM Tool Invocation Pattern

> **Source:** [Function Calling Explained Simply | How LLMs Use Tools | Agentic AI Series](https://youtube.com/watch?v=Y8t4fYqIDgs)
> **Channel:** Coding with Neeraj · **Published:** 2026-08-19 · **Ingested:** 2026-10-11
> **Relevance score:** 8/10

## Summary

Function calling is a mechanism where LLMs request execution of predefined functions/external tools rather than generating raw text responses. The LLM reasons about which tool to invoke, the application executes it (API calls, DB queries, etc.), and returns results for the LLM to format into human-readable responses. Core to agentic AI systems that need real-time data or external system access.

## Key Takeaways

- LLMs don't execute functions—they only request them. Execution happens in external systems (APIs, databases, services)
- Functions are registered in a tool registry as JSON schemas; the LLM selects tools based on semantic understanding of user queries
- Flow: user query → LLM selects tool → application executes → results returned to LLM → formatted response. Enables real-time weather, bookings, calculations without knowledge cutoff
- Tool registry allows selective access (100 available tools, agent uses 5-6) and supports future auth/RBAC (e.g., CEDAR policies)

## ArchonOS Applicability

ArchonOS agents need function calling for homelab automation—invoking VM management APIs, querying Prometheus, executing system commands, accessing local DBs. Implement tool registry for device-specific capabilities and restrict execution scope per agent role.

---

`#tool-use` `#auto-ingested` `#youtube`
