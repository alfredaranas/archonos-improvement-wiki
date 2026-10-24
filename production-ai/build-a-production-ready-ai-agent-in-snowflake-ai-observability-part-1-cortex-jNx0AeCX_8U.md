# Build a Production-Ready AI Agent in Snowflake | AI Observability Part 1 | Cortex Search + RAG

**URL:** https://www.youtube.com/watch?v=jNx0AeCX_8U
**Added:** 2026-10-24
**Relevance:** ⭐⭐⭐⭐ (4/5)

## Key Takeaways
- Use Snowflake’s LAYOUT parsing mode when preserving tables and other document structure matters; OCR mode extracts text without preserving that structure.…
- Split parsed documents into meaningful chunks before sending them to search, rather than indexing entire long PDFs.…
- Use recursive character splitting so text is divided at paragraph breaks first, then at smaller separators when needed to meet the character limit.…
- Add chunk overlap to reduce the risk of losing context when a split falls mid-sentence.…
- Evaluate the agent against questions paired with ground-truth answers, and add more questions as needed.…
- 5 PDFs were uploaded to the document stage for parsing.…
- 1,400 characters was the chunk size limit used in the recursive text split.…

## Apply to ArchonOS
- G
- e
- n
- e

## TubeOnAI Summary
> The tutorial builds a Snowflake retrieval-augmented generation application over clinical study PDFs and prepares a 25-question evaluation dataset for assessing its answers.

Advice
- Use Snowflake’s LAYOUT parsing mode when preserving tables and other document structure matters; OCR mode extracts text without preserving that structure.
- Split parsed documents into meaningful chunks before sending them to search, rather than indexing entire long PDFs.
- Use recursive character splitting so text is divided at paragraph breaks first, then at smaller separators when needed to meet the character limit.
- Add chunk overlap to reduce the risk of losing context when a split falls mid-sentence.
- Evaluate the agent against questions paired with ground-truth answers, and add more questions as needed.
Mentioned
- Products Snowflake Cortex Search, Cortex AI PARSEDOCUMENT, SPLITTEXTRECURSIVECHARACTER
- Tools Snowflake worksheets and stages
- Data clinical study PDFs, evaluation dataset, trial protocol, data monitoring committee documents
Numbers to remember
- 5 PDFs were uploaded to the document stage for parsing.
- 1,400 characters was the chunk size limit used in the recursive text split.
- 200 characters of overlap was used between chunks to help preserve context.
- 78 chunks were created from the five PDFs.
- 25 questions with ground-truth answers made up the initial evaluation dataset.
- 2 parts make up the series: this part builds the application and dataset; the next examines traces and compares evaluations across application versions.

## Tags
`#production` `#reliability` `#agents` `#memory` `#rag` `#context`
