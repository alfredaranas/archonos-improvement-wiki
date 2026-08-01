# 5 Advanced RAG Context Expansion Techniques

**URL:** https://www.youtube.com/watch?v=3pR4i0_UDtU
**Added:** 2026-08-01
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- **💡 Basic vector search with simple chunking can reduce RAG accuracy** — The issue is especially relevant for structured documents, where meaning often depends on headings, surrounding sections, and document hierarchy.
- **🔥 1. Full document expansion** — The agent receives the entire document as context for answering a query.
- **🍳 2. Neighbor expansion** — After retrieving a chunk from the vector store, the system also includes adjacent chunks.
- **🧩 3. Section expansion** — Retrieval uses the document’s structure to include sibling chunks and child chunks tied to the matched section.
- **🌳 4. Parent expansion** — Instead of only returning the matched chunk, the system retrieves all chunks under the parent heading.
- **🤖 5. Agentic expansion** — An agent dynamically traverses the document structure to determine which parts are needed for the question.
- **📈 Dynamic retrieval improves answer accuracy** — The core recommendation is to move from static chunk retrieval to structure-aware, dynamically expanded context.

## Apply to ArchonOS
- (See takeaways — adapt patterns to Oracle/SupaBrain/MCP/lane-routing context.)

## TubeOnAI Summary
> 💡 Basic vector search with simple chunking can reduce RAG accuracy   – The issue is especially relevant for structured documents, where meaning often depends on headings, surrounding sections, and document hierarchy.   – The remedy is context expansion: retrieving more than the initially matched chunk so the model has enough surrounding information to answer accurately.  🔥 1. Full document expansion   – The agent receives the entire document as context for answering a query.   – This is the broadest strategy and is most useful when relevant information may be distributed across the file or when document size is still manageable.  🍳 2. Neighbor expansion   – After retrieving a chunk from the vector store, the system also includes adjacent chunks.   – This helps when the answer spans chunk boundaries or when nearby paragraphs provide necessary definitions, qualifiers, or examples.  🧩 3. Section expansion   – Retrieval uses the document’s structure to include sibling chunks and child chunks tied to the matched section.   – This is useful for documents organized by headings and subheadings, where related content is grouped semantically rather than only by proximity.  🌳 4. Parent expansion   – Instead of only returning the matched chunk, the system retrieves all chunks under the parent heading.   – This captures the complete context of a subsection, which can prevent partial or misleading answers caused by isolated chunk retrieval.  🤖 5. Agentic expansion   – An agent dynamically 

## Tags
`#ai-agents` `#production`
