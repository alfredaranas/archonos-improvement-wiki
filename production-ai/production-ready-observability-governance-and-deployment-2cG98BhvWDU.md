# Production Ready: Observability, Governance and Deployment

**URL:** https://www.youtube.com/watch?v=2cG98BhvWDU
**Added:** 2026-10-24
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- Record agent requests, tool calls, and results, but do not store prompts, tool payloads, secrets, or file contents in traces.…
- Screen generated content before displaying or streaming it, and apply the same policies to subagents as to the parent agent.…
- Set explicit boundaries for tool use, including approval steps for actions that need human authorization.…
- Keep a baseline evaluation and rerun it as the agent changes so regressions are visible.…
- For local models, choose one that supports tool calling if the agent needs to use tools.…
- Before deploying to a hosted environment, check whether local files, shell access, and memory are available; connect external memory or use the host's tools when needed.…
- To deploy a hosted agent in Microsoft Foundry, containerize it and support the Foundry Responses or Invocations protocol.…

## Apply to ArchonOS
- Memory: fold this into the Oracle vault + SupaBrain layer — decide whether it needs a new retrieval path, a new store, or just a better index over what already exists. _(from: "Before deploying to a hosted environment, check whether local files, shell access, and memory are available; connect external memory or use the…")_
- Tool use: check against the ArchonOS MCP catalog — if this pattern needs a new tool surface, it belongs in the shared MCP layer rather than inside one archon. _(from: "Set explicit boundaries for tool use, including approval steps for actions that need human authorization.…")_
- Production AI: measure on the local inference lanes (:11434 CUDA / :11436 iGPU) before claiming a win — the router decides whether this changes lane routing. _(from: "To deploy a hosted agent in Microsoft Foundry, containerize it and support the Foundry Responses or Invocations protocol.…")_
- Governance: map to the existing approval gate (hermes-approvals) rather than inventing a parallel review mechanism. _(from: "Set explicit boundaries for tool use, including approval steps for actions that need human authorization.…")_

## TubeOnAI Summary
> Production readiness for an agent harness requires four things: trace its behavior, govern what it can do, evaluate its quality for regressions, and deploy it in an environment suited to its tools and memory.

Advice
- Record agent requests, tool calls, and results, but do not store prompts, tool payloads, secrets, or file contents in traces.
- Screen generated content before displaying or streaming it, and apply the same policies to subagents as to the parent agent.
- Set explicit boundaries for tool use, including approval steps for actions that need human authorization.
- Keep a baseline evaluation and rerun it as the agent changes so regressions are visible.
- For local models, choose one that supports tool calling if the agent needs to use tools.
- Before deploying to a hosted environment, check whether local files, shell access, and memory are available; connect external memory or use the host's tools when needed.
- To deploy a hosted agent in Microsoft Foundry, containerize it and support the Foundry Responses or Invocations protocol.
Mentioned
- Software: Microsoft Agent Framework, Microsoft.Extensions.AI, Microsoft Agent Framework Purview library, Foundry Local, Microsoft Foundry
- Tools: Model Context Protocol (MCP), Microsoft Learn MCP server, OpenTelemetry, Aspire dashboard, Azure CLI, Bicep
- Models: Qwen 2.5, Llama 4
- Libraries: Microsoft CMCP SDK, Foundry evaluator, local evaluator
- People: Bruno Cap, Pablo Piano, Jose Luis Lator
- Sources: Microsoft Agent Framework financial advisor blog series, FreeCodeCamp Ccourse, roadmap.sh, Codewars
Numbers to remember
- 3 core trace elements: agent requests, tool calls, and results; together they help show what happened during a run.
- 4 production concerns: observability, governance, evaluation, and hosting.
- 265 output tokens: the limit configured in the local-model demonstration.

*(summary truncated)*

## Tags
`#production` `#reliability` `#agents` `#memory` `#rag` `#context`
