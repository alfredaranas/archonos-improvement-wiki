# Maximizar la Ventana de Contexto en Qwen Code 🚀 Cómo Optimizar el Procesamiento de TOKENS

**URL:** https://www.youtube.com/watch?v=sS7ZtHtCIGE
**Added:** 2026-10-24
**Relevance:** ⭐⭐⭐ (3/5)

## Key Takeaways
- Set the context window in Continue’s settings.json as well as in the model’s execution parameters; changing only the execution parameters is not enough.…
- If the conversation reaches the context limit, either start a new conversation and rerun the tests or compress the existing conversation before it runs out of room.…
- Increase batch size when faster preprocessing matters and the smaller context window still fits the conversation.…
- Keep the vision component enabled when the workflow, such as Playwright testing, may need screenshots.…
- For local inference where token-generation speed matters, the presenter would choose an RTX 5090 over an Nvidia DGX Spark at a similar price.…
- Use another model for specific tasks where Qwen falls short; the presenter used Gemini to handle a few issues.…
- 262,144 tokens: The model’s context can be expanded to this size, though the presenter describes it as beyond the model’s native context window.…

## Apply to ArchonOS
- Prompting/context: test against the Hermes system-prompt layering and the context compaction path before adopting. _(from: "Set the context window in Continue’s settings.json as well as in the model’s execution parameters; changing only the execution parameters is not…")_
- Production AI: measure on the local inference lanes (:11434 CUDA / :11436 iGPU) before claiming a win — the router decides whether this changes lane routing. _(from: "For local inference where token-generation speed matters, the presenter would choose an RTX 5090 over an Nvidia DGX Spark at a similar price.…")_

## TubeOnAI Summary
> Qwen Code can handle large software projects, but reaching the context limit forces a choice: compress or restart, or enlarge the context window at the cost of memory and slower prompt processing. Increasing batch size can make preprocessing much faster, but may reduce how much conversation fits.

Advice
- Set the context window in Continue’s settings.json as well as in the model’s execution parameters; changing only the execution parameters is not enough.
- If the conversation reaches the context limit, either start a new conversation and rerun the tests or compress the existing conversation before it runs out of room.
- Increase batch size when faster preprocessing matters and the smaller context window still fits the conversation.
- Keep the vision component enabled when the workflow, such as Playwright testing, may need screenshots.
- For local inference where token-generation speed matters, the presenter would choose an RTX 5090 over an Nvidia DGX Spark at a similar price.
- Use another model for specific tasks where Qwen falls short; the presenter used Gemini to handle a few issues.
Mentioned
- Products: Qwen Code, Qwen 2.5 32B, Qwen 2.5 Coder 32B, Qwen 3.5 4B, GLM 5.1, Nvidia DGX Spark, RTX 5090, Gemini
- Tools: Continue, Llama.cpp, Playwright, Context 7, ComfyUI
- Places: Mexico
- Files: settings.json
Numbers to remember
- 262,144 tokens: The model’s context can be expanded to this size, though the presenter describes it as beyond the model’s native context window.
- 131,072 tokens: The conversation size that had to be reprocessed after the model server was closed and reopened.
- 512 tokens: The batch size used to reprocess the prior conversation in blocks.
- 239 tokens per second: Average preprocessing speed with the smaller batch setting.

*(summary truncated)*

## Tags
`#production` `#reliability` `#agents` `#memory` `#rag` `#context`
