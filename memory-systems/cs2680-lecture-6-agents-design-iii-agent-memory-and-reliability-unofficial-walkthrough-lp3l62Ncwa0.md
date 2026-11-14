# CS2680 Lecture 6: Agents Design III: Agent Memory and Reliability (unofficial walkthrough)

**URL:** https://youtube.com/watch?v=lp3l62Ncwa0
**Channel:** KatrinaDataING
**Added:** 2026-11-07
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- Choose memory formats and storage based on how the agent will use the information; keep raw episodes as a source of truth when useful.
- Use selective memory writes to limit noise, and combine explicit requests, rules, classifiers, or periodic model review as appropriate.
- Filter retrieved memories by user, project, and task; account for importance, validity, and provenance, not just semantic similarity.
- Track when facts became valid and where they came from; supersede outdated facts rather than deleting them when historical accuracy matters.
- Provide ways to invalidate, permanently delete, expire, or archive memories, including for privacy requests and exposed secrets.

## Apply to ArchonOS
- Map the memory/retrieval design onto the ArchonOS vault + SupaBrain layer and identify which layer owns each fact.
- Check whether the described decay/compaction behaviour explains any current recall gaps in fleet knowledge queries.
- Prototype on Oracle's node and measure the delta against the existing retrieval path.

## TubeOnAI Summary
> Agent memory must be designed around deliberate choices about what to save, how to retrieve and update it, and when to forget it. Reliability depends on tracing failures to their source, recording agent trajectories, and checking remembered information against the current world.
> 
> ## Advice
> - Choose memory formats and storage based on how the agent will use the information; keep raw episodes as a source of truth when useful.
> - Use selective memory writes to limit noise, and combine explicit requests, rules, classifiers, or periodic model review as appropriate.
> - Filter retrieved memories by user, project, and task; account for importance, validity, and provenance, not just semantic similarity.
> - Track when facts became valid and where they came from; supersede outdated facts rather than deleting them when historical accuracy matters.
> - Provide ways to invalidate, permanently delete, expire, or archive memories, including for privacy requests and exposed secrets.
> - Evaluate memory retrieval, writes, governance, and system costs separately; check deletion and user-scope isolation.…

## Tags
`#agents` `#memory-systems` `#archonos`
