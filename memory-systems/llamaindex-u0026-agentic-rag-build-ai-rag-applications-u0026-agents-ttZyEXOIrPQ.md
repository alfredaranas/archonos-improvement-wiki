# LlamaIndex & Agentic RAG: Build AI RAG Applications & Agents

**URL:** https://youtube.com/watch?v=ttZyEXOIrPQ
**Channel:** Tech With Mala
**Added:** 2026-11-14
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- Use RAG when an application needs answers grounded in documents, especially when there are too many documents to fit in an LLM’s context window.
- For a basic RAG pipeline, load documents, split them into chunks, choose an LLM and embedding model, create a vector index and query engine, then ask questions.
- For agentic RAG, expose query engines as tools so the agent can choose a retrieval method and repeat retrieval when it needs more information.
- Add a summary index and summary query engine for high-level questions, and a vector query engine for specific details.
- Write detailed agent instructions that explain when to use each tool and include examples of the kinds of questions it should handle.

## Apply to ArchonOS
- Map the memory/retrieval design onto the ArchonOS vault + SupaBrain layer and identify which layer owns each fact.
- Check whether the described decay/compaction behaviour explains any current recall gaps in fleet knowledge queries.
- Prototype on Oracle's node and measure the delta against the existing retrieval path.

## TubeOnAI Summary
> Agentic retrieval-augmented generation (RAG) lets an agent iteratively retrieve information and use external tools, rather than relying on a single retrieval step. The tutorial builds RAG and agentic RAG applications with LlamaIndex, using a McKinsey report as the example document.
> 
> ## Advice
> - Use RAG when an application needs answers grounded in documents, especially when there are too many documents to fit in an LLM’s context window.
> - For a basic RAG pipeline, load documents, split them into chunks, choose an LLM and embedding model, create a vector index and query engine, then ask questions.
> - For agentic RAG, expose query engines as tools so the agent can choose a retrieval method and repeat retrieval when it needs more information.
> - Add a summary index and summary query engine for high-level questions, and a vector query engine for specific details.
> - Write detailed agent instructions that explain when to use each tool and include examples of the kinds of questions it should handle.
> - Add external tools when the agent needs information beyond the documents, such as web searches or research-paper searches.
> - Provide a Brave Search API key to use its search tool, and store the key securely.
> - Experiment with different LLMs, embedding models, tools, and prompts to suit the application and improve responses.

## Tags
`#agents` `#memory-systems` `#archonos`
