# Bhavin Parikh: Context Engineering for AI Agents: A Practical Architecture for Production Systems

**URL:** https://www.youtube.com/watch?v=J-L2jFwNJcU
**Added:** 2026-10-18
**Relevance:** ⭐⭐⭐ (3/5)

## Key Takeaways
- Production agents need curated, task-specific context, not the longest possible context window.
- Parikh’s incident-management platform shows how to assemble current, relevant information for each agent call while keeping humans involved in validation and decisions.
- Advice Keep the core context small, and retrieve other information only when the task requires it.
- For a high-volume model call, inspect its context, classify each item as core, on-demand, or removable, then compare answer quality and token use against the original.
- Use adaptive agent loops so agents can retrieve additional evidence and adjust their next steps instead of following a fixed workflow.
- Store large tool responses outside the context window, and give agents short references they can expand when needed.

## Apply to ArchonOS
- Idea from `- Production agents need curated, task-specific context, not the longest possibl`
- Idea from `- Parikh’s incident-management platform shows how to assemble current, relevant `
- Idea from `- Advice Keep the core context small, and retrieve other information only when t`

## TubeOnAI Summary
> Production agents need curated, task-specific context, not the longest possible context window. Parikh’s incident-management platform shows how to assemble current, relevant information for each agent call while keeping humans involved in validation and decisions.

Advice
- Keep the core context small, and retrieve other information only when the task requires it.
- For a high-volume model call, inspect its context, classify each item as core, on-demand, or removable, then compare answer quality and token use against the original.
- Use adaptive agent loops so agents can retrieve additional evidence and adjust their next steps instead of following a fixed workflow.
- Store large tool responses outside the context window, and give agents short references they can expand when needed.
- Retrieve conversation history by intent, using recent messages, summaries, and relevant prior decisions rather than loading the full conversation.
- Include the user’s role, permissions, and preferences when selecting and presenting information.
- Match model size and reasoning effort to task complexity; use smaller models for structured tasks and larger ones for deep reasoning.
- Track information source, owner, version, and freshness; flag conflicting information for human validation before replacing outdated context.

Mentioned
- Companies: Comcast, Google, OpenAI, Anthropic
- Tools: LiteLLM
- R

## Tags
`#agent` `#context` `#production`
