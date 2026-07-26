# Two-Tier Self-Hosted AI Lab Architecture: Always-On + Compute Separation

> **Source:** [Why Build Your Own AI Lab? (Self-Hosted AI, Explained)](https://youtube.com/watch?v=dzDV7fUzFJA)
> **Channel:** The Smart Workshop · **Published:** 2026-07-22 · **Ingested:** 2026-07-26
> **Relevance score:** 8/10

## Summary

Practical homelab AI design splitting infrastructure into Tier 1 (always-on ARM SBCs for memory, MCP, automations, nervous system) and Tier 2 (Apple Silicon Mac with unified memory for model inference). Handoff between tiers over local network eliminates cloud dependency, persistent memory, and offline-first capability.

## Key Takeaways

- Tier 1 (SBCs): 3-5W constant power, runs persistent memory store, MCP connectors, service mesh, automations—never sleeps. Tier 2 (Mac mini): Wakes for heavy inference only, leverages unified memory for efficient model loading.
- GPU memory bandwidth is the bottleneck for LLM inference, not CPU count—ARM board stacks won't substitute for Apple Silicon or discrete GPU. CPU boards excel at low-latency orchestration and tool routing.
- Avoid cloud lock-in and subscription meters: persistent context lives in your memory system; models are swappable; privacy is enforced by network topology (data never leaves house); offline operation via local network routing.
- Start minimal: Tier 1 only on day one with small quantized model for end-to-end proof. Upgrade to Tier 2 when ready for capability—don't scale horizontally with more boards, scale vertically with better GPU.

## ArchonOS Applicability

Core reference architecture for ArchonOS: Tier 1 maps to homelab service backbone (memory, MCP orchestration, log ingestion); Tier 2 maps to inference acceleration node. The handoff pattern is the critical design—small persistent systems ask big smart systems, both inside walls, enabling privacy-first agent operation with local fallback.

---

`#archonos-notes` `#auto-ingested` `#youtube`
