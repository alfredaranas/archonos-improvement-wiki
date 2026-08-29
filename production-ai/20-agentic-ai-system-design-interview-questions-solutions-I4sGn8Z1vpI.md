# 20 Agentic AI System Design Interview Questions & Solutions

**URL:** https://www.youtube.com/watch?v=I4sGn8Z1vpI
**Added:** 2026-08-29
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)
**Model:** `azure/gpt-5`
**Channel:** Keerti Purswani

## Key Takeaways
- **🔥 RAG at scale: design for speed and citations** — Split into ingestion (dedup, semantic chunking, rich metadata, batch embeddings to ANN index) and query (hybrid BM25 + dense retrieval, merge, rerank top-K).
- **🧭 Debugging wrong answers: isolate retrieval vs generation** — If correct passages aren’t in top-K, fix retrieval (query rewrite, chunking, embeddings, metadata filters, hybrid config).
- **🛠️ Tool misuse in agents: improve toolability** — Audit full agent trajectory (plan → selection → args → tool output → final).

## Apply to ArchonOS
- Move SupaBrain semantic search from a single FTS5 column to a hybrid BM25 + dense + RRF pipeline. Current `search` works at 200-entry improvement-wiki scale; at the 5k+ entry mark, single-retriever recall drops sharply.

## TubeOnAI Summary
> 🔥 RAG at scale: design for speed and citations – Split into ingestion (dedup, semantic chunking, rich metadata, batch embeddings to ANN index) and query (hybrid BM25 + dense retrieval, merge, rerank top-K). – Ensure stable doc/chunk IDs and character offsets for citations; apply metadata filters early, bound reranking, and cache hot queries; trade off recall vs latency/noise. 🧭 Debugging wrong answers: isolate retrieval vs generation – If correct passages aren’t in top-K, fix retrieval (query rewrite, chunking, embeddings, metadata filters, hybrid config). – If context is correct but answers are wrong, fix generation (prompt grounding, context order, reduce distractors); build evals on real queries. 🛠️ Tool misuse in agents: improve toolability – Audit full agent trajectory (plan → selection → args → tool output → final). – Clarify tool scopes, tighten schemas/validation, add few-shot selection examples, and guardrails for high-risk tools; constraints raise reliability but add cost/latency. 🧪 Training parallel, inference sequential – LLMs are autoregressive: inference depends on prior tokens, so decoding is sequential. – Training sees full sequences (teacher forcing), enabling para…

## Tags
`#memory` `#RAG` `#agents` `#tool-use` `#production`
