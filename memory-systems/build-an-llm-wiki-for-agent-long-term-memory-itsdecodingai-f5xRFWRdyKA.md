# Build an LLM Wiki for Agent Long-Term Memory - @itsdecodingai

**URL:** https://youtube.com/watch?v=f5xRFWRdyKA
**Added:** 2026-10-10
**Relevance:** ⭐⭐⭐ (score 3/5)
**Source:** TubeOnAI summarization, see references/tubeonai-summary-extraction-2026-07-cascade.md

## Key Takeaways
- An LLM wiki turns a collection of source material into linked, searchable memory for an agent, using ordinary Markdown files rather than a database. The agent follows those links to find relevant evidence instead of loading every source into its context at o

## Apply to ArchonOS
- Patterns worth porting into SupaBrain (our shared fleet memory) — see the four-mechanism memory pattern in wiki/memory-systems.
- Multi-agent orchestration takeaways apply to FOCUS card executor and the autonomous kanban system.

## TubeOnAI Summary
> - An LLM wiki turns a collection of source material into linked, searchable memory for an agent, using ordinary Markdown files rather than a database. The agent follows those links to find relevant evidence instead of loading every source into its context at once. - The wiki separates immutable raw files from generated pages. Each source gets a summary page with key claims and links to extracted concepts and entities, which are then combined into their own pages when they appear often enough; the example used a threshold of two mentions. - Indexes enable progressive disclosure: a master index points to indexes for sources, concepts, and entities, which point to individual pages. The agent starts with these compact summaries and reads deeper only when a question requires it, making the approach a lightweight form of graph retrieval. - Concepts and entities serve different purposes: concepts are abstract ideas such as orchestration or agent memory, while entities are identifiable things such as tools, frameworks, or people. The taxonomy is adjustable, but overly narrow categories can limit extraction and overly broad ones can produce noise. - New data types can be added with source-specific adapters that fetch and normalize material into Markdown, such as web articles, code repositories, or video transcripts. Repository pages can begin with a compact architecture overview, with the agent exploring specific files only when needed. - For large collections, ingestion can run in…

## Tags
#archonos-improvement #memory-systems #memory #agents
