# Agents Without Code: Skills, YAML, and Filesystems Replaced Python — Philipp Schmid, Google DeepMind

**URL:** https://www.youtube.com/watch?v=fjF8EKnxKCU
**Added:** 2026-09-19
**Relevance:** ⭐⭐⭐⭐ (4/5)

## Key Takeaways
- The speaker argues that agent systems can replace custom Python orchestration with instructions, skills, general tools, and files, allowing developers to remove code as models improve.…
- Advice
- Stop micromanaging execution paths; give agents general-purpose tools and let the model explore, reason, and choose how to complete tasks.
- Define domain instructions, workflows, and rules in agent files such as AGENTS.
- Mentioned
- People: Simon
- Companies: Google DeepMind, Cursor, Manus, LangChain, Vercel
- Products: Gemini, Antigravity, Gemini API, Google AI Studio
- Tools: GitHub CLI, Google Search, GitHub API
- Software: Interactions API, Agents API, ADK framework
- Sour
- Numbers to remember
- Three implementations show the same GitHub pull-request review agent, with less Python and more files in each version.
- 12,000 lines of TypeScript were replaced by about 200 lines of agent files in Cursor’s example.
- Manus refactored it

## Apply to ArchonOS
- The speaker argues that agent systems can replace custom Python orchestration with instructions, skills, general tools, and files, allowing developers to remove code as models improve.
- Advice
- Stop micromanaging execution paths; give agents general-purpose tools and let the model explore, reason, and choose how to complete tasks.
- - Define domain instructions, workflows, and rules in agent files such as AGENTS.md.

## TubeOnAI Summary
> The speaker argues that agent systems can replace custom Python orchestration with instructions, skills, general tools, and files, allowing developers to remove code as models improve.

Advice
- Stop micromanaging execution paths; give agents general-purpose tools and let the model explore, reason, and choose how to complete tasks.
- Define domain instructions, workflows, and rules in agent files such as AGENTS.md.
- Add capabilities through skills files and available command-line tools instead of writing new Python functions and schemas.
- Keep tools clean and verify the outcomes with evaluations.
- Secure sandbox access by injecting credentials through a network proxy and limiting allowed domains when needed.
- Start experimenting with the Antigravity harness in AI Studio, create an API key if necessary, and begin building files and skills.

Mentioned
- People: Simon
- Companies: Google DeepMind, Cursor, Manus, LangChain, Vercel
- Products: Gemini, Antigravity, Gemini API, Google AI Studio
- Tools: GitHub CLI, Google Search, GitHub API
- Software: Interactions API, Agents API, ADK framework
- Sources: AGENTS.md, SKILL.md

Numbers to remember
- Three implementations show the same GitHub pull-request review agent, with less Python and more files in each version.
- 12,000 lines of TypeScript were replaced by about 200 lines of agent files in Cursor’s example.
- Manus refactored its agent harness five times in six months.
- LangChain rearchitected Open Deep Research three times

## Tags
`#agents` `#orchestration` `#frameworks` `#langchain`
