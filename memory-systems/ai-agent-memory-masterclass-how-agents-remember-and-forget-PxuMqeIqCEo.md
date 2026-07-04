# AI Agent Memory Masterclass | How Agents Remember and Forget

**URL:** https://www.youtube.com/watch?v=PxuMqeIqCEo
**Added:** 2026-07-04
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- Agent memory is not the model remembering on its own; it is an external architecture that stores and reassembles relevant state into the prompt at the right time.
- Working memory is the current context window, which is limited, temporary, and shared by instructions, chat history, retrieved snippets, and tool outputs.
- Episodic memory stores past events such as investigations, sessions, tool calls, logs, and approval outcomes, typically with timestamps and session IDs.
- Semantic memory stores standing facts such as repository layout, project rules, assignee mappings, and user or workflow preferences, but requires updates and conflict handling to avoid staleness.
- Procedural memory encodes how work should be done through runbooks, skills, tool schemas, orchestration code, and approval-gated workflows.
- The context builder is the key mechanism: durable memory remains inert until the system retrieves, ranks, and injects the right material into the active context.

## Apply to ArchonOS
- Audit an existing agent by classifying its state into working, episodic, semantic, and procedural memory, then identify where each type is stored and how it enters the prompt.
- Design a context builder that explicitly ranks current user request, visible conversation, project rules, past sessions, tool results, and workflow runbooks before prompt assembly.
- Create a test case with conflicting issue state, such as approval absent in one session and present in a later one, to evaluate whether the agent resolves current truth correctly.
- Implement memory hygiene policies: temporal decay for old items, contradiction handling for updated facts, and summarization pipelines that compress session logs into reusable facts or procedures.
- Separate critical project rules and approval gates into curated semantic or procedural memory files rather than relying only on automatic extraction from logs.

## Subjects
Agent, Working, Episodic, Semantic

## TubeOnAI Summary
> The video explains that AI agents do not remember by changing model weights between sessions; memory is created by surrounding systems that store, retrieve, update, and forget information across time. It distinguishes four memory types: working memory for what is currently in the context window, episodic memory for past events and sessions, semantic memory for stable facts and project rules, and procedural memory for reusable workflows, runbooks, tools, and orchestration. A recurring example uses a project called Cricket and an issue workflow where the agent must investigate a bug, respect repository constraints, map human-friendly assignee names, and wait for an approval comment such as "codex implement" before editing code. The central architectural claim is that durable memory stores only matter when a context builder selects the right slices and injects them into the current context window, since the model can only act on what it actually sees. The video also argues that memory failures are often state-management failures rather than retrieval failures, especially when old and current facts conflict, such as an issue previously lacking approval but later gaining it. Forgetting is presented as a necessary maintenance function through temporal decay, contradiction handling, compression, and manual curation so stale facts and procedures do not outrank current truth. The overall framing connects memory to harness engineering: memory is a harness primitive that governs what state survives and shapes future actions, similar in importance to tools, sandboxing, and workflow controls.

## Tags
`#ai-agents` `#2026` `#memorysystems` `#archonos-improvement`
