# Inside Freshworks' MCP Gateway

**URL:** https://www.youtube.com/watch?v=GVB-1mTmBOU
**Added:** 2026-07-11
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)
**Channel:** Agentic AI Foundation
**Published:** 2 weeks ago
**Duration:** 21m

## Key Takeaways
- **💡 Core premise: MCP is a protocol, not a full enterprise platform** — Model Context Protocol (MCP) standardizes agent-to-tool communication, but enterprise deployments still need platform capabilities around it.…
- **🏢 Freshworks’ context and motivation** — Freshworks serves 75,000+ customers and already had a mature integration and marketplace platform.…
- **🛠️ Why MCP fit their architecture** — Freshworks already had the business logic running as serverless remote functions in an event-driven architecture.…
- **📅 Implementation timeline** — Early 2025: tracked MCP while the spec was evolving from a mostly local pattern to remote MCP.
- **🚪 Gateway as the central architectural pattern** — The main pattern presented is an MCP gateway that acts as a control plane, not merely a request proxy.…

## Apply to ArchonOS
- Evaluate the talk's gateway pattern as a candidate for the ArchonOS MCP gateway layer.
- Surface the talk's top 3 production patterns to other archons via SupaBrain or FOCUS card.
- Schedule a 30-min walkthrough of the talk with one other archon to confirm we're aligned.

## TubeOnAI Summary
> 💡 Core premise: MCP is a protocol, not a full enterprise platform – Model Context Protocol (MCP) standardizes agent-to-tool communication, but enterprise deployments still need platform capabilities around it. – For support and IT service workflows, agents must operate across many business systems such as Shopify, Stripe, Shiprocket, Datadog, and PagerDuty. – The main problem is not only exposing tools to AI agents, but doing so with security, tenancy, routing, reliability, and governance. 🏢 Freshworks’ context and motivation – Freshworks serves 75,000+ customers and already had a mature integration and marketplace platform. – Existing apps already contained the core business logic needed for tool execution, such as issuing refunds or retrieving subscription details. – Instead of building a separate MCP stack from scratch, MCP was added as a layer on top of the existing platform to reuse…

## Tags
`#mcp` `#context-engineering` `#tools` `#enterprise` `#workflow` `#archonos-improvement`
