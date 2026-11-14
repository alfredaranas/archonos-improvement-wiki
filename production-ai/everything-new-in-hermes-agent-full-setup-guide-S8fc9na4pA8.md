# Everything New in Hermes Agent (Full Setup Guide)

**URL:** https://youtube.com/watch?v=S8fc9na4pA8
**Channel:** Tech With Tim
**Added:** 2026-11-14
**Relevance:** ⭐⭐⭐⭐ (4/5)

## Key Takeaways
- Run Hermes on a virtual private server if you want it available around the clock; the creator says this is easier to secure and manage than dedicated local hardware.
- Choose and configure a model provider with `Hermes setup model`; the creator recommends using a subscription provider for value, while noting that other providers and local models are options.
- Connect the desktop app to the remote Hermes installation rather than using a separate local agent, which would only run while the computer is on and could access local files.
- Review skills before installing them from the catalog, because some may be malicious.
- Use separate bots or profiles when you want different personalities, models, tools, or permissions.

## Apply to ArchonOS
- Test the technique against Oracle's Ollama lanes (:11434 CUDA / :11436 iGPU) and measure context length + latency before adopting.
- A/B the change on a real wiki-summary workload and record the quality/throughput delta in the ArchonOS notes.
- Check whether the ArchonOS inference router needs a lane-specific setting rather than a global one.

## TubeOnAI Summary
> Hermes Agent is a configurable, persistent AI agent that can use different models and tools, remember user preferences, improve reusable skills, and run scheduled tasks. The guide recommends hosting it on a virtual private server and shows how to configure it, connect interfaces, and create specialized bots.
> 
> ## Advice
> - Run Hermes on a virtual private server if you want it available around the clock; the creator says this is easier to secure and manage than dedicated local hardware.
> - Choose and configure a model provider with `Hermes setup model`; the creator recommends using a subscription provider for value, while noting that other providers and local models are options.
> - Connect the desktop app to the remote Hermes installation rather than using a separate local agent, which would only run while the computer is on and could access local files.
> - Review skills before installing them from the catalog, because some may be malicious.
> - Use separate bots or profiles when you want different personalities, models, tools, or permissions.
> - Set up messaging integrations such as Telegram if you want to chat with Hermes from your phone.
> - Use scheduled jobs for recurring tasks, and specify the intended time zone.

## Tags
`#agents` `#production-ai` `#archonos`
