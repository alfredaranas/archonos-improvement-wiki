# Coordinator Subagent Orchestration in Claude Agent SDK — How Multi-Agent Delegation Actually Works

**URL:** https://www.youtube.com/watch?v=RfB1ju3Wks4
**Added:** 2026-09-19
**Relevance:** ⭐⭐⭐ (3/5)

## Key Takeaways
- The coordinator-subagent design uses a hub-and-spoke model: one coordinator delegates work, manages communication, checks for gaps, and combines sourced results from isolated subagents.…
- - Let the coordinator handle routing, error handling, delegation, and result aggregation instead of doing research directly.
- Select subagents according to the query instead of running the full pipeline every time.
- Partition the topic before assigning tasks
- - Tools: Task, web search, web fetching, read, grep
- Software: Claude Agent SDK, ChatGPT, Claude, Gemini, Mistral, Kimi
- Topics: music, writing, film, visual arts, games
- Architecture: hub-and-spoke orchestration, isolated context, subagent invocation, cont

## Apply to ArchonOS
- The coordinator-subagent design uses a hub-and-spoke model: one coordinator delegates work, manages communication, checks for gaps, and combines sourced results from isolated subagents.
- Advice

- Let the coordinator handle routing, error handling, delegation, and result aggregation instead of doing research directly.
- - Select subagents according to the query instead of running the full pipeline every time.

## TubeOnAI Summary
> The coordinator-subagent design uses a hub-and-spoke model: one coordinator delegates work, manages communication, checks for gaps, and combines sourced results from isolated subagents.

Advice

- Let the coordinator handle routing, error handling, delegation, and result aggregation instead of doing research directly.
- Select subagents according to the query instead of running the full pipeline every time.
- Partition the topic before assigning tasks so subagents do not duplicate work or miss entire areas.
- Restrict each subagent to a narrow topic and tool set through its description, prompt, and allowed tools.
- Pass every required piece of context directly in the subagent prompt because new subagents do not inherit prior conversation or shared memory.
- Keep claims attached to source metadata by passing structured findings, including URLs and publication dates, into synthesis.
- Have the coordinator evaluate the synthesis for thin or missing topics, then issue targeted follow-up tasks before finishing.
- Give subagents goals and quality requirements while allowing them to adapt, rather than forcing rigid step-by-step scripts.

Mentioned

- Tools: Task, web search, web fetching, read, grep
- Software: Claude Agent SDK, ChatGPT, Claude, Gemini, Mistral, Kimi
- Topics: music, writing, film, visual arts, games
- Architecture: hub-and-spoke orchestration, isolated context, subagent invocation, context passing
- Sources: JSON findings, URLs, publication dates, source-to-claim m

## Tags
`#memory` `#agents` `#orchestration` `#claude` `#context`
