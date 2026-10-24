# 2,000+ Hours of Learning Agentic AI System Design in 20 Minutes

**URL:** https://www.youtube.com/watch?v=Mv7eiQFQQ1E
**Added:** 2026-10-24
**Relevance:** ⭐⭐⭐⭐ (4/5)

## Key Takeaways
- Make assumptions explicit about data, inputs, operating constraints, and action risks. The example assumes a few thousand mostly English help articles, short customer questions that may include exact IDs, thousands of customers per day, answers…
- The architecture framework is know, act, remember, coordinate. For knowledge, start with hybrid retrieval that combines semantic search and keyword search, then rerank results; avoid complex multi-document retrieval unless evaluation shows that…
- Choose memory based on the task rather than using every type by default. The support agent needs working memory for the current conversation and may benefit from episodic memory of prior cases; persistent customer facts can help, while procedural…

## Apply to ArchonOS
- Memory: fold this into the Oracle vault + SupaBrain layer — decide whether it needs a new retrieval path, a new store, or just a better index over what already exists. _(from: "The architecture framework is know, act, remember, coordinate. For knowledge, start with hybrid retrieval that combines semantic search and keyword…")_

## TubeOnAI Summary
> Strong AI system design starts with scope, not technology choices. For a customer support agent, define the user’s problem, the outcome to improve, which tasks AI should handle, and how much autonomy it gets; routine answers and low-risk actions can be automated, while refunds may require a policy check or human approval.

- Make assumptions explicit about data, inputs, operating constraints, and action risks. The example assumes a few thousand mostly English help articles, short customer questions that may include exact IDs, thousands of customers per day, answers needed within seconds, and actions with varying risk.
- The architecture framework is know, act, remember, coordinate. For knowledge, start with hybrid retrieval that combines semantic search and keyword search, then rerank results; avoid complex multi-document retrieval unless evaluation shows that answers often need it.
- Give the agent narrowly scoped tools and design each around permissions, blast radius, failure handling, and trust boundaries. For example, order lookup should only access the authenticated customer’s orders, while higher-risk actions need deterministic controls; treat user messages, retrieved documents, and tool outputs as untrusted.
- Choose memory based on the task rather than using every type by default. The support agent needs working memory for the current conversation and may benefit from episodic memory of prior cases; persistent customer facts can help, while procedural memory is not needed initially.
- Build observability around logs and actionable evaluations. Track model inputs and outputs, retrieved content, tool calls and arguments, retries, latency, and cost; measure retrieval quality, groundedness, tool accuracy and success, resolution rate, latency, cost per resolution, and customer satisfaction.

*(summary truncated)*

## Tags
`#agent` `#architecture` `#orchestration` `#memory` `#rag` `#mcp`
