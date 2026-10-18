# Multi-Agent Orchestrator with Jev, LangGraph & OpenAI

**URL:** https://www.youtube.com/watch?v=Ugj5GjWA-ww
**Added:** 2026-10-18
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- A discriminative decision model can handle agent routing and verification, while OpenAI language models do the work; this can reduce routing latency and avoid relying on a language model to check its own output.
- Advice Use a decision model for routing or other narrow decisions instead of asking a general-purpose language model to choose an agent.
- Keep each agent’s routing description separate from its system prompt so routing criteria and response behavior can be tuned independently.
- Give the decision model clear state and structured questions, with defined choices, scores, or yes-or-no answers.
- Use a language model for generative tasks such as writing email or code; the decision model is not meant to generate text.
- Consider involving a human when a decision’s probability is below 0.5, as in the speaker’s example.

## Apply to ArchonOS
- Idea from `- A discriminative decision model can handle agent routing and verification, whi`
- Idea from `- Advice Use a decision model for routing or other narrow decisions instead of a`
- Idea from `- Keep each agent’s routing description separate from its system prompt so routi`

## TubeOnAI Summary
> A discriminative decision model can handle agent routing and verification, while OpenAI language models do the work; this can reduce routing latency and avoid relying on a language model to check its own output.

Advice
- Use a decision model for routing or other narrow decisions instead of asking a general-purpose language model to choose an agent.
- Keep each agent’s routing description separate from its system prompt so routing criteria and response behavior can be tuned independently.
- Give the decision model clear state and structured questions, with defined choices, scores, or yes-or-no answers.
- Use a language model for generative tasks such as writing email or code; the decision model is not meant to generate text.
- Consider involving a human when a decision’s probability is below 0.5, as in the speaker’s example.
- Add real tools to agents when adapting the pattern, such as test execution for a coding agent or browsing for a research agent.

Mentioned
- Products: Z (TypeSafe AI decision model), OpenAI
- Tools: LangGraph, LangChain, FastAPI, Next.js, MCP
- Companies: TypeSafe AI
- Languages and interfaces: Python SDK, TypeScript SDK, Java SDK, HTTP API

Numbers to remember
- 3 agents: the example routes requests to coding, research, or writing agents.
- $5: the speaker says this is the minimum amount to add to get started with the decision model API.
- $0.004 input c

## Tags
`#mcp` `#agent` `#tool` `#orchestr` `#multi-agent` `#langgraph`
