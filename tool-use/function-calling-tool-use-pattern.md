# Function Calling & Tool Use Pattern: LLM Agent Interface Design

> **Source:** [Agentic Patterns Tool Use | OpenAI Function Calling](https://youtube.com/watch?v=WoF1BuoVAWA)
> **Channel:** AI TL;DR · **Published:** 2025-11-28 · **Ingested:** 2026-08-02
> **Relevance score:** 8/10

## Summary

Tool use (function calling) is the architectural pattern that bridges LLM reasoning with external system execution. The LLM generates structured JSON requests for tools; application code executes them and returns results back to the model, creating a closed-loop agentic cycle. Clear JSON schema definitions—especially descriptive parameter fields—determine whether the model correctly identifies and invokes the right tool.

## Key Takeaways

- LLM never executes code directly; it generates structured JSON (typically) signaling intent. Your application code parses and executes the actual function—this is a hard security boundary.
- Tool manifest (JSON schema definitions) is the contract. The description field is critical for model reasoning; vague or missing descriptions cause incorrect tool selection.
- Six-step closed loop: user prompt → LLM decides tool needed → structured request generated → application parses & executes → result returned → LLM generates final answer with context.
- Tool use transforms a text generator into an agent by enabling read operations (live APIs, databases) and write operations (email, calendar events, state changes) in external systems.

## ArchonOS Applicability

ArchonOS agents depend on tool use to break free from static knowledge and act on homelab systems. Design the tool manifest carefully—clear schemas for system calls (Docker, Kubernetes, file I/O, monitoring APIs) determine whether the agent reliably orchestrates infrastructure or fails silently.

---

`#tool-use` `#auto-ingested` `#youtube`
