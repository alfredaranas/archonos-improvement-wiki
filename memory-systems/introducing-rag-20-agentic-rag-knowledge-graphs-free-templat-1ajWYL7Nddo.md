# Introducing RAG 2.0: Agentic RAG + Knowledge Graphs (FREE Template)

**URL:** https://www.youtube.com/watch?v=1ajWYL7Nddo
**Added:** 2026-08-01
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- **💡 Core idea: RAG 2.0 combines Agentic RAG with Knowledge Graphs** — The system uses an AI agent to decide which retrieval source is most appropriate for a question.
- **🗂️ Two parallel representations of the same data** — A document containing information about large technology companies, their AI initiatives, and partnerships is stored in two forms.
- **🔎 How the agent chooses tools** — For questions about a single company, the agent uses the vector database.
- **🧠 Agentic behavior** — The agent uses its system prompt to determine whether to call vector search, graph search, or both.
- **🔄 Using both sources together** — The agent can be instructed to query both the vector database and the knowledge graph for a broader answer.
- **🛠️ Implementation stack mentioned** — The build process is described as using Claude Code to assist development; “Cloud Code” in the transcript appears to be a transcription error.

## Apply to ArchonOS
- (See takeaways — adapt patterns to Oracle/SupaBrain/MCP/lane-routing context.)

## TubeOnAI Summary
> 💡 Core idea: RAG 2.0 combines Agentic RAG with Knowledge Graphs   – The system uses an AI agent to decide which retrieval source is most appropriate for a question.   – It combines vector search for semantic document retrieval with a knowledge graph for relationship-based queries.   – The goal is to improve answer quality by routing queries based on the type of information needed.  🗂️ Two parallel representations of the same data   – A document containing information about large technology companies, their AI initiatives, and partnerships is stored in two forms.   – In the vector pipeline, the document is chunked, embedded, and stored in PostgreSQL with the pgvector extension.   – The transcript refers to Neon as the serverless PostgreSQL platform.   – In the graph pipeline, the same information is stored in a knowledge graph, described as using Neo4j; the transcript’s “Neoforj” is a mispronunciation of Neo4j.   – “Graffiti” is mentioned as part of the graph workflow, likely referring to a graph extraction or graph-building tool.  🔎 How the agent chooses tools   – For questions about a single company, the agent uses the vector database.   – Example: asking about Google’s AI initiatives triggers vector search because the answer is likely contained in descriptive document chunks.   – For questions about relationships between companies, the agent uses the knowledge graph.   – Example: relationship-style queries can identify links such as Anthropic hosting models on Amazon/AWS in

## Tags
`#ai-agents` `#production`
