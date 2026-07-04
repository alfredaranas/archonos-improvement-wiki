# ð¨ð¥Building an AI Threat Modeling Agent Claude Code + STRIDE + MCP for Auto

**URL:** https://www.youtube.com/watch?v=zBU1ovXgDTU
**Added:** 2026-07-04
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- claude.md functions as a policy layer that defines security guardrails and prohibited behaviors for an AI agent before it performs security tasks.
- skills.md functions as a procedural layer, and the STRIDE framework can be encoded there as a repeatable threat-modeling method.
- STRIDE is operationalized as six recurring security questions: spoofing, tampering, repudiation, information disclosure, denial of service, and elevation of privilege.
- MCP is used as the integration layer that lets an AI client access external tools and resources such as a Snyk server for dependency vulnerability scanning.
- A practical workflow is shown on OWASP Juice Shop: define policy, define procedure, generate a threat model, then run an automated dependency scan.
- Threat-model outputs are structured into actors, trust boundaries, architecture/data flows, threat maps, risk tables, and prioritized remediation guidance.

## Apply to ArchonOS
- Create a claude.md file for a test project that defines system context, data sensitivity, banned patterns, approved libraries, and a pre-completion checklist.
- Encode a STRIDE workflow into a new skills.md file and test whether the agent consistently produces the same threat-model sections across multiple applications.
- Run the workflow against OWASP Juice Shop and compare the generated threat model with known Juice Shop weaknesses to evaluate coverage and false negatives.
- Set up a Snyk account, authenticate a Snyk MCP server, keep the server running in a separate terminal, and prompt Claude to scan project dependencies.
- Review the generated dependency vulnerability report and map findings to remediation actions such as version upgrades, package replacement, or compensating controls.

## Subjects
AI, STRIDE, STRIDE, MCP

## TubeOnAI Summary
> The video demonstrates a workflow for building an AI-assisted security review process using Claude Code, a security policy file in claude.md, a STRIDE-based procedure file in skills.md, and an MCP server for vulnerability scanning. The setup begins with defining guardrails in claude.md, including rules such as never hardcoding secrets, preferring HTTPS over HTTP, using secure hashing instead of MD5, validating and sanitizing inputs, and limiting generated code to approved libraries and patterns. A STRIDE threat-modeling procedure is then created in skills.md so the agent can systematically evaluate spoofing, tampering, repudiation, information disclosure, denial of service, and elevation of privilege risks in the OWASP Juice Shop application. The generated threat model includes actors, trust boundaries, architecture/data-flow context, threat mapping, a threat table with likelihood and impact, key risks, and recommended controls. For dependency scanning, the workflow connects Claude to a Snyk MCP server, authenticates, starts the server in a separate terminal, and prompts Claude to scan the project's open-source dependencies, producing a dependency vulnerability report. The broader point is that security agents can be constrained by policy, guided by repeatable procedures, and extended through MCP tools to automate parts of threat modeling, asset discovery, and vulnerability analysis. The video also briefly frames main agents, sub-agents, hooks, tools, and resources as composable elements for larger security automation workflows, while noting cost considerations for multi-agent setups.

## Tags
`#ai-agents` `#2026` `#tooluse` `#archonos-improvement`
