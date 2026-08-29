# A Meta Engineer's Agentic Engineering Workflow

**URL:** https://www.youtube.com/watch?v=Ukju3maxbEQ
**Added:** 2026-08-29
**Relevance:** ⭐⭐⭐ (3/5)
**Model:** `azure/gpt-5`
**Channel:** Jason Ku

## Key Takeaways
- **🔧 Workflow overview** — Uses a Level 4 agentic engineering approach—multiple coding agents orchestrated in parallel, with tasks bundled by code area for token efficiency.…
- **🧭 Product context** — Building Altitude, an AI coding tutor that guides users through project-based learning, maintains a knowledge graph, and uses spaced repetition.…
- **🛠️ UI demo scope** — Onboarding chat fixes—Enter sends, Shift+Enter adds newline, auto-scroll to bottom, streamed responses, and loading spinners for slow operations.…

## Apply to ArchonOS
- Each fleet archon should declare (in `DUTIES_<archon>.md` or SupaBrain self-summary) which 'level' of agentic autonomy it operates at: routing (L1), supervised tool-use (L2), short-task delegation (L3), long-running multi-step orchestration (L4). Today we have an implicit layer; making it explicit helps with the next permission-scoping pass.

## TubeOnAI Summary
> - 🔧 Workflow overview: Uses a Level 4 agentic engineering approach—multiple coding agents orchestrated in parallel, with tasks bundled by code area for token efficiency. – Keeps a running backlog and scopes work so a single orchestrator can handle related changes. - 🧭 Product context: Building Altitude, an AI coding tutor that guides users through project-based learning, maintains a knowledge graph, and uses spaced repetition. - 🛠️ UI demo scope: Onboarding chat fixes—Enter sends, Shift+Enter adds newline, auto-scroll to bottom, streamed responses, and loading spinners for slow operations. – Requests agents to generate HTML UI variations to quickly select designs before implementation. - 🗣️ Input acceleration: Uses speech-to-text to reduce typing and speed up multi-agent orchestration. - 🧪 Dev process automation: Each feature runs in a separate git worktree; follows TDD (write failing tests first) and adds end-to-end tests for browser interactions. - 🧰 Design method: For complex changes, runs a “grill” session to co-design via structured Q&A, producing precise specs. – After design, performs a compact to retain only essentials and lower context/token load before building. - 🤖 Multi…

## Tags
`#agents` `#workflows` `#multi-agent` `#failure-modes`
