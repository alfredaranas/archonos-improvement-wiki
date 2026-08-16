# How Does Claude Code Actually Work? Let's Make Our Own

**URL:** https://youtube.com/watch?v=vp6Dlx5aHDU
**Added:** 2026-08-16
**Relevance:** ⭐⭐⭐ (3/5)

## Key Takeaways
- **🔧 What Claude Code (an agent) actually is** — An agent = an LLM “brain” plus a software harness that runs a loop, manages state, and executes actions.…
- **🧠 LLM fundamentals** — The model is a stateless next‑token predictor; it has no goals or memory on its own.…
- **🛠️ Tools: types and how they are used** — Built-in I/O tools: read/write files, edit, bash/command execution, search, etc.…
- **🗃️ Memory as files (not model weights)** — Persistent info is stored in files (e.g., claw.md, a memory/ folder, “skills” markdowns).
- **🧾 Context window composition** — System prompt (role and rules).

## Apply to ArchonOS
- Update archonOS agent orchestrator to share this pattern: An agent = an LLM “brain” plus a software harness that runs a loop, manages state, and executes actions.…
- Add to SupaBrain enrichment pipeline: episodic→semantic consolidation layer: The model is a stateless next‑token predictor; it has no goals or memory on its own.…
- Apply to ArchonOS tool registry: standardize via this pattern: Built-in I/O tools: read/write files, edit, bash/command execution, search, etc.…

## TubeOnAI Summary
> - 🔧 What Claude Code (an agent) actually is
  - An agent = an LLM “brain” plus a software harness that runs a loop, manages state, and executes actions.
  - Core building blocks: model, tools, memory, context, guardrails.

- 🧠 LLM fundamentals
  - The model is a stateless next‑token predictor; it has no goals or memory on its own.
  - It only “knows” the context window provided at inference time.
  - Outputs can be plain text or structured tokens (e.g., JSON for tool calls). The harness interpre…

## Tags
`#ai-agents` `#archonos-improvement`
