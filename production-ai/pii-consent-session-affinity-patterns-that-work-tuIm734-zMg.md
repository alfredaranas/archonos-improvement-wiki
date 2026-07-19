# PII, Consent & Session Affinity Patterns That Work

**URL:** https://www.youtube.com/watch?v=tuIm734-zMg
**Added:** 2026-07-19
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)
**Channel:** Agentic AI Foundation
**Published:** 3 weeks ago
**Duration:** 19:54

## Key Takeaways
- **💡 Core architecture: 4-layer production pattern for MCP-based banking systems** — UI layer: React-based interface for customers and partners.
- **🔥 Main production issue: session affinity breaks when MCP runs on Kubernetes at scale** — A local POC worked because everything ran on a single machine with implicit state.
- **🧭 Solution for scaling: route requests using MCP session identity** — The practical fix was to introduce an MCP gateway, in this case Microsoft’s MCP Gateway.
- **🔐 PII handling pattern: keep sensitive data out of the LLM** — Banking workflows often include SSNs, dates of birth, account data, and other PII.
- **Consent and session affinity are state, not prose** — Identity, consent, and routing metadata must survive agent handoffs without being inferred again from natural-language history.
## Apply to ArchonOS
- Place a policy gateway between agents and sensitive MCP servers for identity, consent, routing, filtering, and audit logging.
- Propagate session affinity and user identity as typed metadata, not as natural-language context that can be lost during handoff.
- Redact or tokenize PII before it enters model context and verify the same schemas at UI, gateway, and server boundaries.

## TubeOnAI Summary
> 💡 Core architecture: 4-layer production pattern for MCP-based banking systems – UI layer: React-based interface for customers and partners. – Agent layer: LangChain/LangGraph orchestration handles workflow, tool calling, and error handling. – Gateway layer: used between agents and MCP servers to manage routing, security, filtering, and observability. – MCP server layer: contains the core business logic and backend tool implementations. – The same schema definitions should be enforced across layers, such as Pydantic in Python and Zod in TypeScript, to catch validation issues early. 🔥 Main production issue: session affinity breaks when MCP runs on Kubernetes at scale – A local POC worked because everything ran on a single machine with implicit state. – In production, multiple Kubernetes pods caused follow-up requests to land on different replicas. – MCP interactions that depended on…

## Tags
`#production-ai` `#reliability` `#governance` `#agents` `#archonos-improvement`
