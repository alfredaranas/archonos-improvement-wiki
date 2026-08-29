# Bevor du KI-AGENTEN nutzt: Das musst du WIRKLICH wissen!

**URL:** https://www.youtube.com/watch?v=GgYBe6I4aHQ
**Added:** 2026-08-29
**Relevance:** ⭐⭐⭐ (3/5)
**Model:** `azure/gpt-5-mini`
**Channel:** Christoph Magnussen

## Key Takeaways
- **🔥 Agents vs chatbots** — Agents act autonomously, run in loops, and use tools to perform tasks on your computer, while chatbots only generate responses.…
- **💾 Local vs cloud** — desktop apps (e.g., Codex, Claude Code) run locally and can access local projects, whereas web agents run in the cloud and depend on provider infrastructure.…
- **💾 Global memory & agent files** — AGENTS. md / CLAUDE.…

## Apply to ArchonOS
- Reconcile the fleet's MCP lifecycle paths (in-process SDK vs STDIO vs HTTP) and document which ArchonOS tools use which — `references/tubeonai-prompt-output-shapes.md` already shows the operational cost when MCP server output shapes drift.
- SupaBrain's MCP-mediated cross-archon recall (Oracle writes, Yoda/Bathy read) is the Oracle-native equivalent of the Claude Chat 'import memory' workflow; document the round-trip so future archons know to use it instead of duplicating fetches.

## TubeOnAI Summary
> 🔥 Agents vs chatbots: Agents act autonomously, run in loops, and use tools to perform tasks on your computer, while chatbots only generate responses. 💾 Local vs cloud: desktop apps (e.g., Codex, Claude Code) run locally and can access local projects, whereas web agents run in the cloud and depend on provider infrastructure. 💾 Global memory & agent files: AGENTS.md / CLAUDE.md store persistent context, personal/project memories, and working rules that shape agent behavior. – These files are plain text/Markdown, typically created or updated by the agent itself and can be enabled or disabled. 🧩 Skills: Skills are standardized instruction files the model recognizes and may auto-select to perform tasks without explicit prompts. – Skills are text files in a defined format and can be shared or centrally deployed. 🔗 Model Context Protocol (MCP): MCP is the tool "manual" standard that tells agents how to use external tools and services via MCP servers. – MCP servers should be trusted, and anyone can theoretically run one. 📦 Plugins: Plugins bundle skills, an MCP server, and tools into an organized package that agents can use and administrators can distribute. – Plugins help manage many skil…

## Tags
`#MCP` `#memory` `#agents` `#tool-use` `#workflows`
