# I Tested Buzz by Block: Multi-Agent Orchestration

**URL:** https://youtube.com/watch?v=L5gXr2TghgA
**Added:** 2026-07-25
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- **💡 Buzz overview** — Buzz is an open-source, Apache 2.
- **🔥 Core test: agent-to-agent conversation can loop indefinitely** — A simple prompt asking one agent (Honey) to talk to another (Fizz) caused both to repeatedly @mention each other.…
- **🧠 Main argument: Buzz is not implementing deep agent orchestration yet** — The system supports multi-agent communication, but not robust, built-in orchestration logic.…
- **📊 Four orchestration families used as evaluation criteria** — Central orchestration: a controller manages workers and delegates tasks directly.…
- **🧪 Second test: prompt-created manager/worker setup** — Manager: instructed to split work between two agents and wait for both before replying.…

## Apply to ArchonOS
- Document this orchestration pattern in `archonos-notes/improvement-todo.md` under multi-agent design.
- File this pattern in the appropriate category README for cross-reference.
- Add a search-hook keyword derived from 'I Tested Buzz by Block: Multi-Agent Orch' to the wiki sidebar.

## TubeOnAI Summary
> 💡 Buzz overview
  – Buzz is an open-source, Apache 2.0 licensed project from Block positioned as a shared workspace where humans and AI agents collaborate.
  – It resembles a chat workspace with channels, threads, agents, teams, routing, event storage, and tools for agent interaction.
  – Agents communicate primarily through @mentions, which trigger responses from other agents.

🔥 Core test: agent-to-agent conversation can loop indefinitely
  – A simple prompt asking one agent (Honey) to talk to another (Fizz) caused both to repeatedly @mention each other.
  – Because each reply became the next prompt, the system entered an ongoing reply loop with dozens of messages until manually interrupted.
  – This behavior reflects a known failure mode in multi-agent systems: no enforced stopping rule.
  – The loop only ended after a direct human instruction: “Please stop your conversation.”

🧠 Main argument: Buzz is not implementing deep agent orchestration yet
  – The system supports multi-agent communication, but not robust, built-in orchestration logic.
  – What appears to be orchestration is largely driven by prompt instructions given to language models, not by a formal workflow engine enforcing task completion.
  – Buzz provides the communication layer, while the agents themselves are trusted to manage delegation and coordination correctly.
  – This means successful coordination depends heavily on LLM compliance, which is inherently unreliable in more complex workflows.

📊 Four orc

## Tags
`#ai-agents` `#archonos` `#agentarchitectures`
