# AI Agent Memory Explained (Why Your AI Agent Forgets You)

**URL:** https://youtube.com/watch?v=ZnRKU7kyV8Y
**Channel:** AI Build Along
**Added:** 2026-11-07
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- Save long-term memory outside chat histories, then include relevant facts in a new chat’s context.
- Use compaction to replace old messages with a summary when a chat grows too large; consider removing old tool results with context editing.
- Ask customers what they agree to save, and save only after they consent.
- Do not store children’s names, health facts, or payment details.
- Keep each customer’s memory separate, and check every path so memory commands cannot access another customer’s files.

## Apply to ArchonOS
- Map the memory/retrieval design onto the ArchonOS vault + SupaBrain layer and identify which layer owns each fact.
- Check whether the described decay/compaction behaviour explains any current recall gaps in fleet knowledge queries.
- Prototype on Oracle's node and measure the delta against the existing retrieval path.

## TubeOnAI Summary
> An AI agent forgets between chats because the model keeps nothing between requests; the app must save useful facts and send them back. Memory should be limited, consent-based, isolated by customer, and easy to delete.
> 
> ## Advice
> - Save long-term memory outside chat histories, then include relevant facts in a new chat’s context.
> - Use compaction to replace old messages with a summary when a chat grows too large; consider removing old tool results with context editing.
> - Ask customers what they agree to save, and save only after they consent.
> - Do not store children’s names, health facts, or payment details.
> - Keep each customer’s memory separate, and check every path so memory commands cannot access another customer’s files.
> - Let customers view and delete their memory, and provide a settings button rather than relying only on the model.
> - To reduce prompt-injection risks, consider read-only memory, review saved content, and keep notes short.

## Tags
`#agents` `#memory-systems` `#archonos`
