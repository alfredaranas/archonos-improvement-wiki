# Road to NODES AI: Graph-Based Long-Term Memory: How Agentic Workflows Adapt Thro

**URL:** https://www.youtube.com/watch?v=U_sA6S_jBxE
**Added:** 2026-07-04
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- Standard agents often behave like stateless systems across sessions: they can access tools and knowledge but do not reliably retain lessons from previous failures, successes, or user feedback unless a memory mechanism is added.
- A context graph can capture the full decision story of an agentic workflow, including what was attempted, why it was attempted, what evidence was found, what was missing, and how the final answer was judged.
- Long-term memory is more useful when distilled into reusable strategies, patterns, and lessons learned rather than storing every prior interaction as another retrieval corpus.
- Agentic RAG is well suited to complex document intelligence problems because retrieval decisions happen during reasoning, allowing iterative use of vector search, full-text search, and page navigation rather than relying on one-shot retrieval.
- Separating retrieval strategy from retrieval execution and retrieval evaluation creates better observability and more precise opportunities for learned guidance than a monolithic ReAct agent.
- Playbooks should be compact, continuously refined, and scoped to relevant task categories, such as separate playbooks for retrieval versus answer generation and separate playbooks for different question classes.

## Apply to ArchonOS
- Recreate the demonstrated pipeline with Neo4j, LangGraph, OCR, semantic chunking, embeddings, vector search, full-text search, and a page retrieval tool, then compare one-shot RAG versus agentic RAG on a domain dataset.
- Model a context graph that stores questions, retrieval iterations, answer iterations, tool calls, chunk provenance, feedback, and playbook updates, then inspect whether it improves debugging and explainability.
- Split playbooks by workflow phase, at minimum retrieval and answer generation, and test whether specialized guidance performs better than a single shared prompt memory.
- Add question classification so each task type has its own playbooks, then compare results against a global playbook across heterogeneous question families.
- Run ablation studies on embedding models, chunk formats, guidance generation, and retrieval tools to identify which components most affect final answer quality.

## Subjects
Standard, Long, Agentic RAG

## TubeOnAI Summary
> This workshop presents a pattern for adding graph-based long-term memory to agentic workflows so they can learn from prior executions and human feedback without immediate fine-tuning. The implementation is demonstrated on a complex financial document intelligence task using an agentic RAG system that separates retrieval strategy, tool execution, retrieval evaluation, answer generation, and answer evaluation, with iterative loops when evidence or reasoning is insufficient. A central idea is to store the full execution trace in a Neo4j-based context graph, including questions, retrieval attempts, reasoning summaries, tool calls, answer steps, chunk provenance, and feedback, so the system remains auditable and explainable. From that graph, a reflector extracts lessons learned from each run, and a creator updates compact evolving playbooks that capture reusable retrieval and answering strategies by question class rather than storing raw conversation history alone. The system also generates focused guidance from those playbooks for the current question, reducing irrelevant context and helping the agent choose better retrieval tactics and domain-specific calculation rules. Document preprocessing is intentionally simpler than GraphRAG-style pipelines, relying on OCR, semantic chunking, chunk summaries, embeddings, full-text indexes, and page-level retrieval tools rather than full entity-relationship extraction. Reported benchmark results on a FinanceBench-based setup show that vanilla one-shot RAG performed worst, agentic RAG improved multi-document reasoning, and adding the learning loop further improved domain-relevant financial reasoning, especially on tasks requiring user- or domain-specific interpretation such as capital intensity thresholds.

## Tags
`#ai-agents` `#2026` `#memorysystems` `#archonos-improvement`
