# From Training to Tokens Revolutionizing AI Inference with In Network Compute

**URL:** https://youtube.com/watch?v=8UzNifcZsZE
**Channel:** Open Compute Project
**Added:** 2026-11-07
**Relevance:** ⭐⭐⭐ (3/5)

## Key Takeaways
- Prioritize low total latency for distributed general matrix multiplication, which performs repeated, latency-sensitive partial-product reductions.
- Support dynamic multicast groups for mixture-of-experts workloads, where each token can be routed to different experts.
- Build in-network collectives on efficient write-based protocols rather than read-based protocols.
- Design configuration and management to coordinate collective groups across multiple switches, not just within one switch.
- Develop a standards-based in-network collective protocol through industry collaboration.

## Apply to ArchonOS
- Test the technique against Oracle's Ollama lanes (:11434 CUDA / :11436 iGPU) and measure context length + latency before adopting.
- A/B the change on a real wiki-summary workload and record the quality/throughput delta in the ArchonOS notes.
- Check whether the ArchonOS inference router needs a lane-specific setting rather than a global one.

## TubeOnAI Summary
> In-network collectives can reduce latency in AI inference by moving reductions, replication, and synchronization into fabric switches. Making this work across growing clusters requires low-latency, standards-based support and collective libraries that can use the switch functions.
> 
> ## Advice
> - Prioritize low total latency for distributed general matrix multiplication, which performs repeated, latency-sensitive partial-product reductions.
> - Support dynamic multicast groups for mixture-of-experts workloads, where each token can be routed to different experts.
> - Build in-network collectives on efficient write-based protocols rather than read-based protocols.
> - Design configuration and management to coordinate collective groups across multiple switches, not just within one switch.
> - Develop a standards-based in-network collective protocol through industry collaboration.
> - Update accelerator collective libraries to call the in-network functions available in switches.
> - Use static preconfiguration where possible, but plan for runtime reconfiguration when expert combinations exceed available configuration slots.

## Tags
`#agents` `#production-ai` `#archonos`
