# Plan Before You Build: Deterministic Planning Patterns for AI Agents by Dan Dobrin @ Spring I/O 26

**URL:** https://www.youtube.com/watch?v=0fH-tWLvDC4
**Added:** 2026-06-13
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)
**Channel:** Spring I/O
**Published:** 1 day ago
**Duration:** 46m 48s

## Key Takeaways
- **💡 Core thesis: plan before building AI agents** — – Many agent systems are built by connecting an LLM to tools and letting it improvise, which creates unpredictable execution paths, weak testability, unclear debugging, and uncontrolled cost.
- **🧠 Model variability is a central architectural problem** — – The same system prompt and user prompt can produce materially different answers across models.
- **👥 LLM council pattern: use multiple models as a deliberative committee** — – Based on the idea that no single model is best across all tasks.
- **🏗️ Design principles for the council architecture** — – Anonymity: models evaluate content rather than model identity.
- **⚠️ Trade-offs of the LLM council pattern** — – API costs multiply with each participating model.

## Apply to ArchonOS
- Memory: review the hybrid memory approach for gaps in current SupaBrain design
- Retrieval: hybrid search (BM25 + vector) + re-ranking layer for SupaBrain
- Consider GraphRAG for relationship-aware recall in cross-archon knowledge
- Agent architecture: separate planning, execution, verification roles in dispatch layer
- Planning: consider deterministic plan-then-execute pattern over free-form agent loops

## TubeOnAI Summary

> 💡 Core thesis: plan before building AI agents – Many agent systems are built by connecting an LLM to tools and letting it improvise, which creates unpredictable execution paths, weak testability, unclear debugging, and uncontrolled cost. – Traditional software assumptions no longer hold: code is no longer the only source of truth; agent reasoning and tool choices also need to be observed and constrained. – Key operational risks include model variability, infinite loops, hidden token-cost multipliers, and lack of a clear explanation for why an agent chose a path. 🔍 Observability for agents differs from traditional application monitoring – Standard metrics like CPU, memory, and latency remain useful, but agent systems require additional telemetry: – tool call sequence – reasoning path – decision quality – time to first token – token consumption and token efficiency – Distributed tracing be...

## Tags
`#memory` `#agents` `#rag` `#context-engineering` `#tools` `#orchestration` `#planning` `#graphrag` `#java` `#claude` `#archonos`
