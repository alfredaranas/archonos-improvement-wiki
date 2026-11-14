# AI Engineering PART3:  Dataset Engineering, Inference Optimization, and AI Engineering Architecture.

**URL:** https://youtube.com/watch?v=9TgICIKp5wo
**Channel:** Shahanawaj Mulla
**Added:** 2026-11-07
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- Prioritize high-quality training examples over raw data volume, and ensure they cover varied tasks such as math, coding, and creative writing.
- Use synthetic data when human-written examples are too costly, but avoid training a model blindly on its own outputs because errors can compound into model collapse.
- Clean training data by removing duplicates, irrelevant HTML, and personally identifiable information, then format it consistently so user and assistant messages are distinct.
- Use batching to raise hardware throughput, while accounting for the possible increase in time to the first token.
- Consider quantization to reduce memory use and bandwidth demands, and speculative decoding to speed generation without reducing output quality.

## Apply to ArchonOS
- Test the technique against Oracle's Ollama lanes (:11434 CUDA / :11436 iGPU) and measure context length + latency before adopting.
- A/B the change on a real wiki-summary workload and record the quality/throughput delta in the ArchonOS notes.
- Check whether the ArchonOS inference router needs a lane-specific setting rather than a global one.

## TubeOnAI Summary
> AI systems depend on the engineering around the model: carefully curated data, efficient inference, and orchestration. The discussion draws on Chip Huyen’s *AI Engineering* to explain how these pieces improve quality, speed, and cost.
> 
> ## Advice
> - Prioritize high-quality training examples over raw data volume, and ensure they cover varied tasks such as math, coding, and creative writing.
> - Use synthetic data when human-written examples are too costly, but avoid training a model blindly on its own outputs because errors can compound into model collapse.
> - Clean training data by removing duplicates, irrelevant HTML, and personally identifiable information, then format it consistently so user and assistant messages are distinct.
> - Use batching to raise hardware throughput, while accounting for the possible increase in time to the first token.
> - Consider quantization to reduce memory use and bandwidth demands, and speculative decoding to speed generation without reducing output quality.
> - Build orchestration around the model: retrieve relevant company information, apply safety checks, route tasks to appropriately sized models, and use caching or agents where useful.

## Tags
`#agents` `#production-ai` `#archonos`
