# Optimizar Ollama con IA 🚀 Configuración CORRECTA de Contexto y GPUs

**URL:** https://www.youtube.com/watch?v=cbeJtLuh47o
**Added:** 2026-10-24
**Relevance:** ⭐⭐⭐ (3/5)

## Key Takeaways
- Keep the number of simultaneous responses at one for typical use; raise it to two or four only for parallel requests and when memory allows.…
- Avoid setting parallel responses too high for a large model, since memory pressure can push work into system RAM and slow generation.…
- Split a model across GPUs when handling simultaneous requests; for a single response, splitting may reduce speed because of communication overhead between cards.…
- Set context length to what conversations actually need, since larger windows consume more memory and may slow startup and token generation.…
- Check Ollama’s serve output for environment-variable errors after configuring it.…
- Use ollama ls to check downloaded models and ollama ps to check running models.…
- 4,096 tokens: Ollama’s default context length, which the presenter says is enough for many conversations.…

## Apply to ArchonOS
- Memory: fold this into the Oracle vault + SupaBrain layer — decide whether it needs a new retrieval path, a new store, or just a better index over what already exists. _(from: "Keep the number of simultaneous responses at one for typical use; raise it to two or four only for parallel requests and when memory allows.…")_
- Architecture: compare against the fleet's existing orchestration (A2A bus, Hermes runner, Kanban) — port the pattern only if it beats what we already run. _(from: "Keep the number of simultaneous responses at one for typical use; raise it to two or four only for parallel requests and when memory allows.…")_
- Prompting/context: test against the Hermes system-prompt layering and the context compaction path before adopting. _(from: "Set context length to what conversations actually need, since larger windows consume more memory and may slow startup and token generation.…")_

## TubeOnAI Summary
> Ollama performance depends on matching GPU splitting, simultaneous request capacity, and context length to available memory. The presenter recommends keeping defaults where possible and increasing settings only when the workload justifies the extra memory use.

Advice
- Keep the number of simultaneous responses at one for typical use; raise it to two or four only for parallel requests and when memory allows.
- Avoid setting parallel responses too high for a large model, since memory pressure can push work into system RAM and slow generation.
- Split a model across GPUs when handling simultaneous requests; for a single response, splitting may reduce speed because of communication overhead between cards.
- Set context length to what conversations actually need, since larger windows consume more memory and may slow startup and token generation.
- Check Ollama’s serve output for environment-variable errors after configuring it.
- Use ollama ls to check downloaded models and ollama ps to check running models.
Mentioned
- Products: Ollama, LM Studio, Claude, Qwen 2, Qwen 2.5 Coder 32B, Gemma 2
- Tools: llama.cpp, TensorRT
- Commands: ollama serve, ollama ls, ollama ps
Numbers to remember
- 4,096 tokens: Ollama’s default context length, which the presenter says is enough for many conversations.
- 32,768 tokens: The context length the presenter chooses for his setup, though he says he usually uses at most about 2,000 tokens per conversation.
- 256,000 tokens: A Qwen 2.5 Coder 32B model at this context length used about 50 GB of system RAM in his test.
- 1 million tokens: The same model at this context length used 108 GB of RAM on his 128 GB system.
- 70 versus 40 tokens per second: Splitting across two GPUs reduced his observed speed, but he still considered 40 tokens per second fast.

*(summary truncated)*

## Tags
`#production` `#reliability` `#agents` `#memory` `#rag` `#context`
