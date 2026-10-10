# Anthropic Claude Certified Architect - Professional Exam Prep | RAG, MCP, EVAL | Complete Guide

**URL:** https://youtube.com/watch?v=PcYZzatbhbk
**Added:** 2026-10-10
**Relevance:** ⭐⭐⭐⭐ (score 4/5)
**Source:** TubeOnAI summarization, see references/tubeonai-summary-extraction-2026-07-cascade.md

## Key Takeaways
- The exam rewards architectural reasoning, not memorized answers: identify the scenario’s main constraint, locate the system layer responsible, and favor least privilege, measurable controls, evidence-based decisions, auditability, and clear ownership.
- For

## Apply to ArchonOS
- MCP wiring patterns apply to hermes_runner / FastMCP server architecture.
- Retrieval/RAG patterns apply to wiki content augment and hallucination guard.
- Claude-specific patterns apply to Hermes profile config and assistant tool routing.

## TubeOnAI Summary
> - The exam rewards architectural reasoning, not memorized answers: identify the scenario’s main constraint, locate the system layer responsible, and favor least privilege, measurable controls, evidence-based decisions, auditability, and clear ownership. - For policy or compliance assistants, use an authoritative controlled corpus with targeted retrieval and citations. This grounds answers, helps users verify them, and can reduce token use and latency compared with searching the open internet. - Treat retrieved documents and web content as untrusted input. Prompt instructions alone are not a security boundary; restrict tools and permissions so injected content cannot gain unauthorized access or actions. - Choose integration patterns by their job: use a direct API for a simple stateless request, MCP when multiple AI clients need a shared tool interface, and an agent handoff for specialized or longer-running work. For database access, enforce read-only access in the database identity rather than relying on prompts or keyword filters. - Limit tool sprawl through progressive discovery instead of loading every tool definition into every request. Keep shared security rules in project-level configuration, while machine-specific and personal settings belong in local or user-level configuration. - Select models and optimize cost using representative workload evidence. Lighter models such as Haiku can handle clear, high-volume tasks, with harder cases routed to larger models; for cos…

## Tags
#archonos-improvement #tool-use #mcp #rag #claude
