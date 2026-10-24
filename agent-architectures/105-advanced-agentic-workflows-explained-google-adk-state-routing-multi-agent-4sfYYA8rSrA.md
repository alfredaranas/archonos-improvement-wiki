# 105 | Advanced Agentic Workflows Explained | Google ADK | State, Routing & Multi-Agent Workflows

**URL:** https://www.youtube.com/watch?v=4sfYYA8rSrA
**Added:** 2026-10-24
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- Use state for complex workflows involving external APIs, bookings, payments, or other multi-step transactions; ordinary read/write workflows may not need it.…
- Save relevant transaction details in state as each tool completes, then have later steps retrieve them from state rather than chat history.…
- Structure state fields clearly so agents use the correct customer, booking, and payment data instead of an older transaction.…
- For cancellations, check the applicable policy before cancelling and calculating a refund.…
- Watch the earlier tutorials on the employee travel multi-agent system and state before following this implementation.…
- 7 Cloud Functions support the example: Book Flight, Book Hotel, Cancel Order, My Trips, Payment History, Process Payment, and Process Refund.…
- 4 specialist agents handle travel, support, finance, and cancellation-policy retrieval, with a root agent routing requests.…

## Apply to ArchonOS
- Architecture: compare against the fleet's existing orchestration (A2A bus, Hermes runner, Kanban) — port the pattern only if it beats what we already run. _(from: "Watch the earlier tutorials on the employee travel multi-agent system and state before following this implementation.…")_

## TubeOnAI Summary
> Stateful multi-agent workflows use structured state, rather than chat history, to pass transaction data between steps and reduce errors in complex tasks. Google’s Agent Development Kit manages that state as tools and specialist agents update it.

Advice
- Use state for complex workflows involving external APIs, bookings, payments, or other multi-step transactions; ordinary read/write workflows may not need it.
- Save relevant transaction details in state as each tool completes, then have later steps retrieve them from state rather than chat history.
- Structure state fields clearly so agents use the correct customer, booking, and payment data instead of an older transaction.
- For cancellations, check the applicable policy before cancelling and calculating a refund.
- Watch the earlier tutorials on the employee travel multi-agent system and state before following this implementation.
Mentioned
- Products Google Agent Development Kit (ADK), Vertex AI, Firestore, Google Cloud Run
- Tools adk create, adk web, Get Current State
- Software ChatGPT
- Related videos YouTube 15 (employee travel multi-agent system), YouTube 102 (architecture and Cloud Functions), YouTube 105 (this workflow), the earlier state tutorial, the cancellation-policy retrieval-augmented generation tutorial
Numbers to remember
- 7 Cloud Functions support the example: Book Flight, Book Hotel, Cancel Order, My Trips, Payment History, Process Payment, and Process Refund.
- 4 specialist agents handle travel, support, finance, and cancellation-policy retrieval, with a root agent routing requests.
- 5 of 10 workflow steps is the example of an external API call that may take long enough for a network failure or app crash to interrupt processing.
- November 15 and 17, 2026 are the example dates for booking an outbound flight and then a return flight using saved state.

*(summary truncated)*

## Tags
`#agent` `#architecture` `#orchestration` `#memory` `#rag` `#mcp`
