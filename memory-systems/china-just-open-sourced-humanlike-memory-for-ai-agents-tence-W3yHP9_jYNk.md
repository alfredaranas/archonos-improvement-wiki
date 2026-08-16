# China Just Open-Sourced Humanlike Memory for AI Agents (Tencent DB)

**URL:** https://youtube.com/watch?v=W3yHP9_jYNk
**Added:** 2026-08-16
**Relevance:** ⭐⭐⭐⭐ (4/5)

## Key Takeaways
- **🔥 Core problem: agents lack persistent memory, and long transcripts hurt performance** — Agents are a model with no memory + a loop that re-injects the transcript; when it overflows, compaction summarizes and discards detail, degrading results.…
- **💡 Tencent’s open-source approach: better results with fewer tokens** — Released by Tencent Cloud’s database team under MIT, ~10k GitHub stars in ~4 months.…
- **📈 Benchmarks for the compression layer (wide factual tasks and beyond)** — Wide factual QA (ByteDance “Wide-Search” style set): 33% → 50% pass; tokens 221M → 86M (~61% reduction).
- **🧠 Idea 2 — Long-term memory via humanlike consolidation (multi-layer architecture)** — Based on memory theory: episodic → semantic consolidation (Tulving, 1972); forgetting as compression (Ebbinghaus, 1885); hippocampal replay as a mechanism.…
- **🛠️ Implementation and developer ergonomics** — Local-first: SQLite, runs on-device; no API key required; nothing leaves the laptop unless configured.…

## Apply to ArchonOS
- Add to SupaBrain enrichment pipeline: episodic→semantic consolidation layer: Agents are a model with no memory + a loop that re-injects the transcript; when it overflows, compaction summarizes and 
- Apply to ArchonOS domain knowledge: Released by Tencent Cloud’s database team under MIT, ~10k GitHub stars in ~4 months.…
- Apply to ArchonOS domain knowledge: Wide factual QA (ByteDance “Wide-Search” style set): 33% → 50% pass; tokens 221M → 86M (~61% reduction)

## TubeOnAI Summary
> 🔥 Core problem: agents lack persistent memory, and long transcripts hurt performance  
  – Agents are a model with no memory + a loop that re-injects the transcript; when it overflows, compaction summarizes and discards detail, degrading results.  
  – On long runs, models re-read files, repeat questions, and re-propose rejected fixes because prior context was compacted.  
  – Example burn: 3.5B tokens for 50 coding tasks in one session.  
  – Larger context windows aren’t a cure: a multi-model …

## Tags
`#ai-agents` `#archonos-improvement`
