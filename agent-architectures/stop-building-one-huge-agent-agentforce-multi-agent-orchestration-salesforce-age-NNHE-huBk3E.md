# Stop Building One Huge Agent! Agentforce Multi-Agent Orchestration | Salesforce | Agentscript

**URL:** https://youtube.com/watch?v=NNHE-huBk3E
**Added:** 2026-10-10
**Relevance:** ⭐⭐⭐ (score 3/5)
**Source:** TubeOnAI summarization, see references/tubeonai-summary-extraction-2026-07-cascade.md

## Key Takeaways
- Multi-agent orchestration keeps a customer-facing experience unified while splitting business capabilities across specialized agents. An orchestrator routes each request to the agent best suited to handle it.
- The design applies separation of responsibiliti

## Apply to ArchonOS
- Multi-agent orchestration takeaways apply to FOCUS card executor and the autonomous kanban system.

## TubeOnAI Summary
> - Multi-agent orchestration keeps a customer-facing experience unified while splitting business capabilities across specialized agents. An orchestrator routes each request to the agent best suited to handle it. - The design applies separation of responsibilities: each agent has its own instructions, knowledge, and actions, making it easier to maintain or expand one capability without changing a single oversized agent. - The tutorial’s example uses three active agents: a soft drink agent for orders and order status, a lead management agent for creating and updating leads, and a case management agent for creating and updating cases. - To assemble the orchestrator in Agentforce, create an agent, then connect the active specialized agents as subagents. Each connected agent is referenced by its API name, and its description helps the orchestrator decide when to route a request to it. - The orchestrator can pass inputs to a connected agent through input variables. For example, it could capture a customer name or order number and pass that value to the specialized agent. - In the preview, a request to create a lead routes to lead management, which asks for required details such as last name and company, then creates the lead after receiving them. - Requests to check an order or create a support case likewise route to the soft drink or case agent. The speaker notes that the order-status interaction asked for confirmation multiple times, but still returned the order’s status.

## Tags
#archonos-improvement #agent-architectures #agents
