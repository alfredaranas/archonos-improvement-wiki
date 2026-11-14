# Where Your AI Agent's Memory Goes When You Walk Away: KV Cache Serving Deep Dive

**URL:** https://youtube.com/watch?v=w_i1b0QGf9I
**Channel:** XOR
**Added:** 2026-11-07
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- Keep agent cache hit rates high; the Manus team calls this the most important production-agent metric, and Claude Code’s team alerts when it falls.
- Pin a cache during tool calls for a duration suited to the tool, then evict it if the tool takes too long.
- Trade cache lifetime against storage: retain caches longer when likely reuse justifies the extra memory.
- Move idle caches to CPU memory, SSDs, or shared storage rather than discarding them when reloading is faster than recomputation.
- Route requests to replicas with the longest matching prefix, while accounting for queue length to avoid overloading a hot replica.

## Apply to ArchonOS
- Map the memory/retrieval design onto the ArchonOS vault + SupaBrain layer and identify which layer owns each fact.
- Check whether the described decay/compaction behaviour explains any current recall gaps in fleet knowledge queries.
- Prototype on Oracle's node and measure the delta against the existing retrieval path.

## TubeOnAI Summary
> Agent memory is the model’s KV cache: it makes repeated reads of a conversation cheaper, but consumes large amounts of memory while people and tools wait. Serving systems can keep it briefly, move it to cheaper storage, and route the next request to it; caches expire when retaining them costs more than recomputing them.
> 
> ## Advice
> - Keep agent cache hit rates high; the Manus team calls this the most important production-agent metric, and Claude Code’s team alerts when it falls.
> - Pin a cache during tool calls for a duration suited to the tool, then evict it if the tool takes too long.
> - Trade cache lifetime against storage: retain caches longer when likely reuse justifies the extra memory.
> - Move idle caches to CPU memory, SSDs, or shared storage rather than discarding them when reloading is faster than recomputation.
> - Route requests to replicas with the longest matching prefix, while accounting for queue length to avoid overloading a hot replica.
> - Pay for an hour-long cache only when you expect to return after five minutes but within the hour.
> - Preserve prompt prefixes across turns: trimming earlier messages, switching models, or changing effort level can break cache reuse.…

## Tags
`#agents` `#memory-systems` `#archonos`
