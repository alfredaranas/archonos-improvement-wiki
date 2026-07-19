# Agent Loop: Observe-Think-Act Pattern

> **Source:** [Building AI Agents that actually work (Full Course)](https://youtube.com/watch?v=eA9Zf2-qYYM)
> **Channel:** Greg Isenberg · **Published:** 2026-03-17 · **Ingested:** 2026-07-19
> **Relevance score:** 8/10

## Summary

Agents operate via iterative loops (observe-think-act) that persist until task completion, unlike chat models which answer single queries. The loop continuously gathers context, plans next steps, executes actions, and feeds results back until predefined success criteria are met.

## Key Takeaways

- Agent = goal-to-result; chat = question-to-answer. Agents loop until task completion vs. single request-response.
- Observe-Think-Act cycle: check available context/files → reason about next action → execute → loop until task parameters satisfied.
- Agent harness (Claude Code, Codex, OpenAI Code, etc.) is the platform that facilitates the loop; LLM + loop + tools + context are the four core components.
- Success criteria in prompt determines loop termination (e.g., 'compile 10 sources, deliver PowerPoint')—agent won't stop until satisfied.

## ArchonOS Applicability

ArchonOS should implement persistent observe-think-act loops for department-level agents (marketing, finance, ops). Each agent needs explicit success criteria in system prompts and must recursively pull context from memory systems and tools until task completion, eliminating need for human babysitting between steps.

---

`#agent-architectures` `#auto-ingested` `#youtube`
