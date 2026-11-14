# CS329Z Lecture 7: Agent Memory Architectures — Engineering AI Agents (unofficial walkthrough)

**URL:** https://youtube.com/watch?v=2C5O6uguEp4
**Channel:** KatrinaDataING
**Added:** 2026-11-07
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- Start with the simplest baseline, such as long context or plain retrieval, and measure it before adding a dedicated memory system.
- Test whether memory retrieval found the right information separately from whether the agent used it correctly.
- Inspect tool-call logs to check whether the agent searches memory thoroughly instead of giving up early.
- Let users inspect and edit their stored memories, especially when those memories are personal.
- Decide which memories belong in every prompt and which should be retrieved only when relevant.

## Apply to ArchonOS
- Map the memory/retrieval design onto the ArchonOS vault + SupaBrain layer and identify which layer owns each fact.
- Check whether the described decay/compaction behaviour explains any current recall gaps in fleet knowledge queries.
- Prototype on Oracle's node and measure the delta against the existing retrieval path.

## TubeOnAI Summary
> Agent memory lets an agent carry useful facts, skills, and progress across sessions, but it must be designed to avoid stale or irrelevant memories, harmful actions, and privacy failures. Compare systems by what they store, when they read or write it, and how they store it.
> 
> ## Advice
> - Start with the simplest baseline, such as long context or plain retrieval, and measure it before adding a dedicated memory system.
> - Test whether memory retrieval found the right information separately from whether the agent used it correctly.
> - Inspect tool-call logs to check whether the agent searches memory thoroughly instead of giving up early.
> - Let users inspect and edit their stored memories, especially when those memories are personal.
> - Decide which memories belong in every prompt and which should be retrieved only when relevant.
> - Use files for strong agents that already work well in a shell, databases for many small memories and fast lookups, and knowledge graphs when relationships and changes over time matter.
> - Check that stored procedures remain valid when the environment changes, and update or remove stale instructions.…

## Tags
`#agents` `#memory-systems` `#archonos`
