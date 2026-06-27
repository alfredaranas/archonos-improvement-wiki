# Samuel Jaja - Building Production Multi-Agent RAG Systems on Serverless AWS | Pydata London 26

**URL:** https://www.youtube.com/watch?v=M4j1otT6Leg
**Channel:** PyData
**Added:** 2026-06-27
**Published:** 11 days ago
**Duration:** 22m 47s
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- **📈 Enterprise adoption context** — Moving from pilots to production requires architecture beyond demos.…
- **🔥 Limits of single-agent systems** — Context overload and degraded reasoning as one agent handles everything.…
- **🧩 Multi-agent system design (Prime project)** — Portfolio Risk Investment Management engine with five agents: Planner, Tagger, Reporter, Charter, Retirement.…
- **🏗️ Serverless AWS architecture (high-level)** — Agents implemented as AWS Lambda functions; choose serverless based on workload patterns and trade-offs.…
- **📨 Decoupling and resilience with SQS** — API requests publish to Amazon SQS; the API does not call the Planner directly (pub/sub decoupling).…

## Apply to ArchonOS
- Adopt enterprise adoption context as the north-star metric: ArchonOS should optimize for moving agents from pilot to production, not demo-to-demo.
- Use the multi-agent RAG on serverless pattern as a reference architecture for parallelizing context-overloaded single-agent tasks (LLM Router + child agents).
- Treat agent-safe data (Lakebase-style separation of storage from compute, schema-validated writes, agent identity propagation) as a first-class production requirement.

## Subjects
- Multi-Agent Systems
- Agent Orchestration
- Memory Systems
- RAG
- Tool Use
- Production Deployment
- AWS Serverless
- Enterprise Workflows

## TubeOnAI Summary
> 📈 Enterprise adoption context     – Moving from pilots to production requires architecture beyond demos.     – Cited figures: ~62% of enterprises are experimenting with agents; ~25% have production deployments (Gartner). 🔥 Limits of single-agent systems     – Context overload and degraded reasoning as one agent handles everything.     – Latency bottlenecks and lack of parallelism; hard to scale.     – Debugging complexity rises without clear separation of concerns. 🧩 Multi-agent system design (Prime project)     – Portfolio Risk Investment Management engine with five agents: Planner, Tagger, Reporter, Charter, Retirement.     – Planner = orchestrator that coordinates all other agents; others are specialized.     – Only selected agents get RAG capabilities (avoid blanket RAG). 🏗️ Serverless AWS architecture (high-level)     – Agents implemented as AWS Lambda functions; choose serverless b…

## Tags
`#memory` `#multi-agent` `#rag` `#context-engineering` `#tools` `#production` `#orchestration` `#graphrag` `#enterprise` `#aws`
