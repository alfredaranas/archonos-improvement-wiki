# Google ADK Context Engineering - Compaction, Caching & Artifacts (Cut LLM Costs ) ( Tutorial- 10 )

**URL:** https://youtube.com/watch?v=MtBJw4cG6SI
**Channel:** AI Tech With Ravi
**Added:** 2026-11-07
**Relevance:** ⭐⭐⭐⭐ (4/5)

## Key Takeaways
- Use compaction when long chat histories consume too many tokens or make responses slower; summarize older turns while preserving information useful in future replies.
- Set a compaction interval and overlap size to control how often history is summarized and how much recent context carries forward.
- Use context caching for large, stable content that agents repeatedly need, such as a company policy document.
- Configure a minimum token threshold, time to live, and cache-use interval for cached context.
- Store text or binary content such as images and PDFs as artifacts, then load it when needed instead of keeping it in the prompt.

## Apply to ArchonOS
- Test the technique against Oracle's Ollama lanes (:11434 CUDA / :11436 iGPU) and measure context length + latency before adopting.
- A/B the change on a real wiki-summary workload and record the quality/throughput delta in the ArchonOS notes.
- Check whether the ArchonOS inference router needs a lane-specific setting rather than a global one.

## TubeOnAI Summary
> Google Agent Development Kit (ADK) can reduce context use and repeated work through compaction, caching, and artifacts. The tutorial demonstrates saving and loading text and image artifacts, summarizing older conversation history, and reusing cached policy data.
> 
> ## Advice
> - Use compaction when long chat histories consume too many tokens or make responses slower; summarize older turns while preserving information useful in future replies.
> - Set a compaction interval and overlap size to control how often history is summarized and how much recent context carries forward.
> - Use context caching for large, stable content that agents repeatedly need, such as a company policy document.
> - Configure a minimum token threshold, time to live, and cache-use interval for cached context.
> - Store text or binary content such as images and PDFs as artifacts, then load it when needed instead of keeping it in the prompt.
> - Use artifact listing and version methods to inspect stored files and versions.

## Tags
`#agents` `#agent-architectures` `#archonos`
