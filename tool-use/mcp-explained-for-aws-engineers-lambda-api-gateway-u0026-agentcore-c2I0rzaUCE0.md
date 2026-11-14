# MCP Explained for AWS Engineers: Lambda, API Gateway & AgentCore

**URL:** https://youtube.com/watch?v=c2I0rzaUCE0
**Channel:** Dear AWS
**Added:** 2026-11-07
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- Standardize on MCP to reduce the integrations needed as models and tools are added.
- Use stateless HTTP and optional sessions to support scalable, serverless MCP services.
- Put an agent gateway between agents and internal systems to manage identity, credentials, tool discovery, and policy enforcement.
- Enforce governance through policies outside the model, not through system prompts.
- Carry the user's identity with each request, authorize access before contacting downstream systems, and log actions for audit.

## Apply to ArchonOS
- Apply the pattern to the fleet MCP server catalogue and check it against the Hermes approval-gate semantics.
- Validate the tool-call contract against a live fleet tool invocation before shipping changes.
- Document the pattern in the ArchonOS tool-use reference notes.

## TubeOnAI Summary
> MCP could become the standard for connecting AI models to tools because it replaces separate model-to-tool integrations with a shared protocol. The presenter argues that stateless HTTP makes MCP practical at cloud scale, while AgentCore Gateway can provide a central layer for identity, security, governance, and tool discovery.
> 
> ## Advice
> - Standardize on MCP to reduce the integrations needed as models and tools are added.
> - Use stateless HTTP and optional sessions to support scalable, serverless MCP services.
> - Put an agent gateway between agents and internal systems to manage identity, credentials, tool discovery, and policy enforcement.
> - Enforce governance through policies outside the model, not through system prompts.
> - Carry the user's identity with each request, authorize access before contacting downstream systems, and log actions for audit.
> - Return only the data needed to answer a request, rather than copying full customer records into the AI platform.
> - Secure the boundaries around the model, since the model itself cannot guarantee access control.…

## Tags
`#agents` `#tool-use` `#archonos`
