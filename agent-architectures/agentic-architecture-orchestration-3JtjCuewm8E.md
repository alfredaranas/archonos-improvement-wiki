# Agentic Architecture & Orchestration

**URL:** https://www.youtube.com/watch?v=3JtjCuewm8E
**Added:** 2026-10-18
**Relevance:** ⭐⭐⭐ (3/5)

## Key Takeaways
- An agentic application uses repeated observe, reason, and act cycles to complete tasks, rather than answering in one pass.
- The application must control when the loop ends and preserve the conversation context between model calls.
- Advice End the loop based on the API’s stop_reason, not on response text that says the model is finished.
- When stopreason is tooluse, execute the requested tool, append its result to the conversation, and continue; when it is end_turn, return the response.
- Set safety limits for repeated tool failures, but do not use a fixed number of passes as the normal stopping rule.
- Maintain the conversation history in the application and provide the relevant context with every Messages API request.

## Apply to ArchonOS
- Idea from `- An agentic application uses repeated observe, reason, and act cycles to comple`
- Idea from `- The application must control when the loop ends and preserve the conversation `
- Idea from `- Advice End the loop based on the API’s stop_reason, not on response text that `

## TubeOnAI Summary
> An agentic application uses repeated observe, reason, and act cycles to complete tasks, rather than answering in one pass. The application must control when the loop ends and preserve the conversation context between model calls.

Advice
- End the loop based on the API’s stop_reason, not on response text that says the model is finished.
- When stopreason is tooluse, execute the requested tool, append its result to the conversation, and continue; when it is end_turn, return the response.
- Set safety limits for repeated tool failures, but do not use a fixed number of passes as the normal stopping rule.
- Maintain the conversation history in the application and provide the relevant context with every Messages API request.
- Append tool results to the conversation history so the model can use them in later passes.
- Use non-agentic systems for fixed workloads with known paths, and agentic systems for open-ended or variable tasks.
- Review the five architectural points presented for exam preparation.

Mentioned
- Products and APIs: Claude API, Messages API, OpenAI API, ChatGPT
- Tools and concepts: agentic loop, harness, system message, user message, assistant message, stopreason, endturn, tool_use
- Examples: web search, database query, file reading and writing, API calls, customer orders, order status, delivery status

Numbers to remember
- Three agent components: the LLM reasons

## Tags
`#agent` `#context` `#orchestr`
