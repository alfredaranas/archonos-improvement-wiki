# Tool Use in LLMs: How AI Agents Call Tools | AI Engineering Design Patterns S01 E01

**URL:** https://youtube.com/watch?v=HUPiSv_b3dw
**Channel:** Gensoku Devs
**Added:** 2026-11-07
**Relevance:** ⭐⭐⭐ (3/5)

## Key Takeaways
- Replace regular-expression parsing of model replies with registered tools that have names, descriptions, input schemas, and handlers.
- Authenticate tool actions against the request context, and check that the order belongs to the requesting user before returning order details or issuing a refund.
- Validate tool inputs, reject unknown tool names or invalid arguments, and return errors to the model so it can correct its request.
- Return only the fields the model needs, not entire internal objects.
- Support multiple tool calls in one response, and match each result to its call using the tool-call ID.

## Apply to ArchonOS
- Apply the pattern to the fleet MCP server catalogue and check it against the Hermes approval-gate semantics.
- Validate the tool-call contract against a live fleet tool invocation before shipping changes.
- Document the pattern in the ArchonOS tool-use reference notes.

## TubeOnAI Summary
> Tool use lets an AI model request defined backend actions without relying on fragile text matching. The system should validate each request, enforce user ownership, and limit back-and-forth with the model.
> 
> ## Advice
> - Replace regular-expression parsing of model replies with registered tools that have names, descriptions, input schemas, and handlers.
> - Authenticate tool actions against the request context, and check that the order belongs to the requesting user before returning order details or issuing a refund.
> - Validate tool inputs, reject unknown tool names or invalid arguments, and return errors to the model so it can correct its request.
> - Return only the fields the model needs, not entire internal objects.
> - Support multiple tool calls in one response, and match each result to its call using the tool-call ID.
> - Handle response content by block type and stop reason rather than assuming the first block is text.
> - Limit model-tool back-and-forth with a maximum-turn setting, and handle the limit being exceeded.
> - Review generated code for edge cases and implementation practices instead of assuming it is correct.

## Tags
`#agents` `#tool-use` `#archonos`
