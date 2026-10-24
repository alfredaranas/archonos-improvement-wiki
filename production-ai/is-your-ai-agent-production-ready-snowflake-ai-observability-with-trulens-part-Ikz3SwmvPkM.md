# Is Your AI Agent Production Ready? Snowflake AI Observability with TruLens | Part 2

**URL:** https://www.youtube.com/watch?v=Ikz3SwmvPkM
**Added:** 2026-10-24
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- Instrument retrieval and generation separately so traces show whether a weak answer comes from search or from the prompt and response.…
- Evaluate RAG with context relevance, groundedness, and answer relevance rather than relying on a smoke test alone.…
- Compare runs when changing prompts or retrieval settings, and investigate tradeoffs instead of assuming stricter grounding always improves quality.…
- Inspect individual traces, retrieved context, and evaluation criteria to understand scores and diagnose problems.…
- Suspend or delete the Snowflake service when finished, and clean up the database and schema to avoid ongoing charges.…
- Use Snowflake Copilot’s “Add to chat” option to get help fixing notebook errors.…
- 3 metrics: Context relevance measures whether retrieved material fits the query, groundedness whether the answer is supported by that material, and answer relevance whether it addresses the query.…

## Apply to ArchonOS
- Memory: fold this into the Oracle vault + SupaBrain layer — decide whether it needs a new retrieval path, a new store, or just a better index over what already exists. _(from: "Evaluate RAG with context relevance, groundedness, and answer relevance rather than relying on a smoke test alone.…")_
- Prompting/context: test against the Hermes system-prompt layering and the context compaction path before adopting. _(from: "Instrument retrieval and generation separately so traces show whether a weak answer comes from search or from the prompt and response.…")_

## TubeOnAI Summary
> Production readiness for a retrieval-augmented generation (RAG) agent requires tracing its behavior and measuring quality across changes, so teams can identify failures and improve performance against their criteria.

Advice
- Instrument retrieval and generation separately so traces show whether a weak answer comes from search or from the prompt and response.
- Evaluate RAG with context relevance, groundedness, and answer relevance rather than relying on a smoke test alone.
- Compare runs when changing prompts or retrieval settings, and investigate tradeoffs instead of assuming stricter grounding always improves quality.
- Inspect individual traces, retrieved context, and evaluation criteria to understand scores and diagnose problems.
- Suspend or delete the Snowflake service when finished, and clean up the database and schema to avoid ongoing charges.
- Use Snowflake Copilot’s “Add to chat” option to get help fixing notebook errors.
Mentioned
- Products: Snowflake Cortex Search, Cortex Complete, Snowflake AI Observability
- Tools: TruLens, Snowflake Copilot
- Software: Python 3.12, Snowflake ML Python, pandas, PyArrow, Pydantic
- Sources: TruLens documentation, GitHub cleanup script
Numbers to remember
- 3 metrics: Context relevance measures whether retrieved material fits the query, groundedness whether the answer is supported by that material, and answer relevance whether it addresses the query.
- 25 questions: The shared evaluation dataset is used to test both RAG versions.
- 3 chunks: The baseline retrieves up to three chunks and uses no strict-grounding instructions.
- 4 chunks: The grounded version retrieves at least four chunks and uses strict instructions to rely only on supplied clinical-trial context, avoid medical advice, and state when the context lacks an answer.

*(summary truncated)*

## Tags
`#production` `#reliability` `#agents` `#memory` `#rag` `#context`
