# Local Agentic Coding: VRAM-Constrained Model Selection

> **Source:** [The Best LOCAL Agentic Coding Workflow (Complete Guide)](https://youtube.com/watch?v=hfba9dAT6xE)
> **Channel:** Tech With Tim · **Published:** 2026-06-10 · **Ingested:** 2026-07-26
> **Relevance score:** 8/10

## Summary

Local model performance is strictly bounded by available VRAM (Windows GPU) or unified memory (Mac). Practical model size ceiling is 75-80% of available memory after OS overhead. Windows dedicated GPUs provide 2x+ memory throughput advantage over Mac despite unified memory appearing larger.

## Key Takeaways

- Windows: Calculate max model size from discrete GPU VRAM (RTX 4090 = 24GB usable). Mac: Use unified memory minus 10-15% system overhead (M5 Max 64GB → ~54GB usable). This hard limit determines whether you run Sonnet-class or Haiku-class models locally.
- Memory throughput matters as much as capacity—RTX 4090 (1008 GB/s) vs M4 Max (546 GB/s). Higher throughput = more tokens/sec despite Mac's larger theoretical pool. Prioritize GPU memory bandwidth for inference speed in production agents.
- Zero-cost inference at scale—local models eliminate per-token fees, enabling unlimited agentic loops (file writes, bash execution, tool calling) without subscription models (Cursor, Claude API, CloudCode). Trade-off: Sonnet/Opus-level reasoning unavailable; suitable for routine coding tasks, not complex problem solving.

## ArchonOS Applicability

ArchonOS should profile host hardware on init (VRAM/unified memory, throughput) to auto-select optimal model tier and quantization strategy. Enables purely offline agentic execution for file operations, bash tasks, and tool integration without cloud dependencies—critical for homelab reliability.

---

`#archonos-notes` `#auto-ingested` `#youtube`
