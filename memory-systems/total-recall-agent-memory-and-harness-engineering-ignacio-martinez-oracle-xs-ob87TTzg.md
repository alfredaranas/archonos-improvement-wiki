# Total Recall: Agent Memory and Harness Engineering — Ignacio Martinez, Oracle

**URL:** https://youtube.com/watch?v=xs-ob87TTzg
**Added:** 2026-10-10
**Relevance:** ⭐⭐⭐ (score 3/5)
**Source:** TubeOnAI summarization, see references/tubeonai-summary-extraction-2026-07-cascade.md

## Key Takeaways
- Reliable agents depend less on changing model weights than on the harness around a model. The harness combines memory, tools, perception, and context management to make a model’s variable outputs more predictable and useful.
- The agent stack has five layers

## Apply to ArchonOS
- Patterns worth porting into SupaBrain (our shared fleet memory) — see the four-mechanism memory pattern in wiki/memory-systems.
- Multi-agent orchestration takeaways apply to FOCUS card executor and the autonomous kanban system.
- Tool-use patterns apply to deliver-tools.sh and ArchonOS tool routing.

## TubeOnAI Summary
> - Reliable agents depend less on changing model weights than on the harness around a model. The harness combines memory, tools, perception, and context management to make a model’s variable outputs more predictable and useful. - The agent stack has five layers: application, data, model, infrastructure, and compute. Martinez argues that the data layer offers developers the most control, while the other layers are increasingly commoditized. - A harness needs seven components: storage, memory engineering, a semantic layer, an agent loop, and context engineering, alongside the model and connections to tools and data. Its loop lets a model observe, reason, and act, with limits on retries to prevent endless tool calls. - Files and databases work best together, rather than as competing choices. Files are easy for models and operating systems to use, but lack transactional consistency and built-in backups; databases add consistency, availability, and vector search. The proposed pattern keeps temporary memory in files and promotes durable information, such as user preferences, into a database. - Memory should match what needs to be retained: short-term memory holds current tasks, while episodic memory captures past interactions and procedural memory preserves reusable workflows. A context window alone is not enough because adding more material can dilute attention, a problem Martinez calls context rot. - The semantic layer supplies the organization-specific knowledge that users oft…

## Tags
#archonos-improvement #memory-systems #memory #agents
