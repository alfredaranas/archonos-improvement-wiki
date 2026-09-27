# Streaming Tool Events for Agent Responsiveness

> **Source:** [5 Tips for Deploying AI Agents to Production](https://youtube.com/watch?v=j1wfE0SOBbE)
> **Channel:** AWS Developers · **Published:** 2026-06-02 · **Ingested:** 2026-09-27
> **Relevance score:** 8/10

## Summary

Stream three event types (text deltas, tool start/end) back to frontend during agent execution to prevent UI spinners during long tool calls. Iterate over agent.stream() events and emit as server-sent events, keeping users informed of activity even during 10+ second operations.

## Key Takeaways

- Emit tool_start and tool_end events alongside text deltas to show user activity during long tool execution, eliminating perceived unresponsiveness
- Use invocation_state to pass authenticated user ID to tools without exposing it to the model, maintaining security across the streaming pipeline
- Implement event-driven UI updates via Server-Sent Events rather than blocking on final agent response to improve perceived latency

## ArchonOS Applicability

ArchonOS agents serving homelab dashboards should stream tool execution events to prevent timeout perception and allow real-time status updates during long-running operations like database queries or external service calls.

---

`#production-ai` `#auto-ingested` `#youtube`
