# Engineering Agentic RAG as a Tool (Part 2) #AgenticRAG #AIAgents #LLMOps #VectorEmbeddings

**URL:** https://www.youtube.com/watch?v=54C8GzErOPE
**Channel:** Unfold Data Science
**Added:** 2026-06-20
**Published:** 4 days ago
**Duration:** 21m 47s
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- This lecture argues that retrieval-augmented generation is more effective inside an agent when implemented as an explicit tool rather than as a mandatory step on every query.
- It contrasts traditional standalone RAG pipelines with an agentic design in which the model decides whether to call a knowledge-search tool, reducing unnecessary retrieval when the question does not require local documents.
- The explanation breaks RAG into indexing and retrieval, then maps those concepts directly to code: chunking documents, creating embeddings, storing vectors, retrieving by similarity, and exposing the search function as an additional tool within an existing tutor agent.

## Core Thesis
RAG should be added to an AI agent as a callable tool so the agent can decide when retrieval is needed instead of searching documents on every query.

## Subjects
- Agentic RAG
- Tool Calling
- Vector Embeddings
- Document Chunking
- Similarity Search
- Knowledge Base
- AI Agent Design

## TubeOnAI Summary
> This lecture argues that retrieval-augmented generation is more effective inside an agent when implemented as an explicit tool rather than as a mandatory step on every query. It contrasts traditional standalone RAG pipelines with an agentic design in which the model decides whether to call a knowledge-search tool, reducing unnecessary retrieval when the question does not require local documents. The explanation breaks RAG into indexing and retrieval, then maps those concepts directly to code: chunking documents, creating embeddings, storing vectors, retrieving by similarity, and exposing the search function as an additional tool within an existing tutor agent. The implementation uses a custom local vector store instead of an external vector database to clarify the mechanics of embedding storage and similarity matching, and it also shows how prompt wording influences tool selection between concept explanation and knowledge-base lookup.

## Key Quotes
- "my rag is also embedded as one of the tool."
- "The problem with this rag is if you don't define this as a tool, right? What happens is for everything user is asking, the system will try to find something here."
- "The meaning of agentic AI is agent should decide when to call which tool, when to take what action, and when to bring what result."

## Tags
`#agentic-rag` `#tool-calling` `#vector-embeddings` `#document-chunking` `#similarity-search` `#knowledge-base` `#ai-agent-design` `#archonos` `#ai-agents` `#tool-use`
