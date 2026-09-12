# Why LLMs get dumb (Context Windows Explained)

**URL:** https://youtube.com/watch?v=TeQDr4DkLYo
**Added:** 2026-09-05
**Relevance:** ⭐⭐⭐ (3/5)

## Key Takeaways
- **🧠 Context Windows** — LLMs (Large Language Models) have a short-term memory limit known as the context window, which affects their ability to maintain conversation coherence over time.…
- **🔍 Token Counting** — LLMs measure input in tokens, which can vary in size. For example, a sentence might count as multiple tokens depending on the model.…
- **⚠️ Memory Limitations** — As conversations extend beyond the context window (e.g., 2048 tokens), LLMs may forget earlier parts or become slower.…
- **🔄 Memory Expansion** — Increasing the context window (e.g., to 4096 or 128,000 tokens) can help LLMs remember more but requires significantly more GPU resources.…
- **⚙️ Resource Management** — Running large context windows demands high VRAM and computational power, leading to potential performance issues.…

## Apply to ArchonOS
- Cross-cutting reference: useful framing for future architecture discussions
- Save for FOCUS-card context when planning cross-archon changes

## TubeOnAI Summary
> - 🧠 Context Windows  
  - LLMs (Large Language Models) have a short-term memory limit known as the context window, which affects their ability to maintain conversation coherence over time.

- 🔍 Token Counting  
  - LLMs measure input in tokens, which can vary in size. For example, a sentence might count as multiple tokens depending on the model.

- ⚠️ Memory Limitations  
  - As conversations extend beyond the context window (e.g., 2048 tokens), LLMs may forget earlier parts or become slower.

- 🔄 Memory Expansion  
  - Increasing the context window (e.g., to 4096 or 128,000 tokens) can help LLMs remember more but requires significantly more GPU resources.

- ⚙️ Resource Management  
  - Running large context windows demands high VRAM and computational power, leading to potential performance issues.

- 💤 Attention Problems  
  - LLMs show a U-shaped accuracy curve, with better performance at the start and end of conversations, but a drop-off in the middle, akin to losing focus.

- 📈 Attention Mechanisms  
  - LLMs use self-attention mechanisms to weigh the importance of words in context, but this computation becomes more complex with longer dialogues.

- 🆕 Optimization Techniques  
  - New techniques like flash attention and KC/V cache are being developed to improve LLM efficiency and reduce memory usage.

- 🛡️ Security Concerns  
  - Larger context windows increase the attack surface for potential vulnerabilities, making it easier for malicious inputs to bypass safety measures.

- ✨ Future Developments  
  - Upcoming models, like Google's Gemini with 2 million tokens, aim to enhance memory and attention capabilities, but challenges remain in processing speed and accuracy.

## Tags
#general #general #memory
