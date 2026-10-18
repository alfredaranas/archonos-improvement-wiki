# Building the Document Context Layer for AI Agents — Jerry Liu, LlamaIndex

**URL:** https://www.youtube.com/watch?v=RQi7x-navxU
**Added:** 2026-10-18
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- Document systems for AI agents should combine fast parsing, deeper visual analysis when needed, structured extraction, and search tools.
- Liu argues that this context layer lets agents work with enterprise documents at scale while balancing accuracy, cost, and speed.
- Advice Use a fast parser for an initial scan, then call a vision-language-model parser when a page’s tables, charts, or values need closer inspection.
- Choose document-processing settings to match the task: prioritize accuracy for regulated or high-risk extraction, and cost for large-scale indexing where agents can revisit documents.
- For extracted data, use source citations and confidence scores, and flag uncertain values before sending them to downstream systems.
- Give agents a broader document-search toolkit, including keyword search, vector search, reading, and scrolling.

## Apply to ArchonOS
- Idea from `- Document systems for AI agents should combine fast parsing, deeper visual anal`
- Idea from `- Liu argues that this context layer lets agents work with enterprise documents `
- Idea from `- Advice Use a fast parser for an initial scan, then call a vision-language-mode`

## TubeOnAI Summary
> Document systems for AI agents should combine fast parsing, deeper visual analysis when needed, structured extraction, and search tools. Liu argues that this context layer lets agents work with enterprise documents at scale while balancing accuracy, cost, and speed.

Advice
- Use a fast parser for an initial scan, then call a vision-language-model parser when a page’s tables, charts, or values need closer inspection.
- Choose document-processing settings to match the task: prioritize accuracy for regulated or high-risk extraction, and cost for large-scale indexing where agents can revisit documents.
- For extracted data, use source citations and confidence scores, and flag uncertain values before sending them to downstream systems.
- Give agents a broader document-search toolkit, including keyword search, vector search, reading, and scrolling.

Mentioned
- Products: LlamaParse, LightParse, ParseBench
- Software: Claude Code, Claude Code Work, Codex, OpenClaw, PyPDF, PyMuPDF
- Platforms: SharePoint, Box, Dropbox, Amazon S3, Snowflake, Databricks
- Sources: Hugging Face, Kaggle

Numbers to remember
- 10 trillion-plus pages of human-created knowledge are said to be stored in documents such as PDFs, PowerPoints, Word files, and Excel sheets.
- 2,000 human-verified pages make up ParseBench, which evaluates tables, charts, content faithfulness, and semantic formatting.
- About 50 mod

## Tags
`#agent` `#tool` `#context`
