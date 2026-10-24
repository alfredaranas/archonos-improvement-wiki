# Designing a Production RAG System from Scratch | Structured + Unstructured Data | System Design

**URL:** https://www.youtube.com/watch?v=21JTfX-d9S0
**Added:** 2026-10-24
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- Use a planner and router to choose structured retrieval, unstructured retrieval, parallel retrieval, dependent retrieval, or clarification when the question is ambiguous.…
- Keep structured and unstructured retrieval in separate services, and let a tool executor carry out the planner’s decisions.…
- Retrieve only relevant table and column schemas before generating SQL; validate SQL as read-only, restrict it to allowed tables and columns, enforce tenant filters, and apply query limits and timeouts.…
- Use hybrid document search: combine keyword search with vector search, fuse the ranked results, then rerank candidates before sending only the strongest evidence to the language model.…
- Build a compact prompt from the question, relevant conversation history, evidence, and source references; avoid sending the entire history or every retrieved result.…
- Persist conversation state, execution IDs, completed steps, and tool outputs so another worker can resume after a failure.…
- Evaluate routing, SQL generation, retrieval, reranking, and final answer quality separately.…

## Apply to ArchonOS
- Memory: fold this into the Oracle vault + SupaBrain layer — decide whether it needs a new retrieval path, a new store, or just a better index over what already exists. _(from: "Use hybrid document search: combine keyword search with vector search, fuse the ranked results, then rerank candidates before sending only the…")_
- Architecture: compare against the fleet's existing orchestration (A2A bus, Hermes runner, Kanban) — port the pattern only if it beats what we already run. _(from: "Use a planner and router to choose structured retrieval, unstructured retrieval, parallel retrieval, dependent retrieval, or clarification when the…")_
- Prompting/context: test against the Hermes system-prompt layering and the context compaction path before adopting. _(from: "Build a compact prompt from the question, relevant conversation history, evidence, and source references; avoid sending the entire history or every…")_
- Reliability: apply to the cron/retry layer — Hermes crons and the fleet health watchdogs already need a documented recovery path. _(from: "Persist conversation state, execution IDs, completed steps, and tool outputs so another worker can resume after a failure.…")_

## TubeOnAI Summary
> A production retrieval-augmented generation (RAG) system should route questions to structured data, unstructured documents, or both, then ground answers in retrieved evidence and return citations. The design separates planning, retrieval, evidence handling, and answer generation so components can scale and recover independently.

Advice
- Use a planner and router to choose structured retrieval, unstructured retrieval, parallel retrieval, dependent retrieval, or clarification when the question is ambiguous.
- Keep structured and unstructured retrieval in separate services, and let a tool executor carry out the planner’s decisions.
- Retrieve only relevant table and column schemas before generating SQL; validate SQL as read-only, restrict it to allowed tables and columns, enforce tenant filters, and apply query limits and timeouts.
- Use hybrid document search: combine keyword search with vector search, fuse the ranked results, then rerank candidates before sending only the strongest evidence to the language model.
- Build a compact prompt from the question, relevant conversation history, evidence, and source references; avoid sending the entire history or every retrieved result.
- Persist conversation state, execution IDs, completed steps, and tool outputs so another worker can resume after a failure.
- Evaluate routing, SQL generation, retrieval, reranking, and final answer quality separately.
- Validate answer grounding, citations, and output correctness before returning a response.
Mentioned
- Products: OpenSearch, PostgreSQL, DynamoDB, Redis, Amazon Cognito, Amazon Bedrock
- Tools: API Gateway, BM25, reciprocal rank fusion (RRF)
- Software: AWS Lambda, Amazon ECS, OpenAI, Claude
- Sources: the creator’s earlier videos on RAG ingestion and RAG evaluation
Numbers to remember
- 8 to 10 seconds: suggested target for 95th-percentile query latency.

*(summary truncated)*

## Tags
`#memory` `#rag` `#retrieval` `#eval` `#tool`
