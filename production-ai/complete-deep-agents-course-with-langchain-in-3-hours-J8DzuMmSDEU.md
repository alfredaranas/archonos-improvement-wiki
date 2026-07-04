# Complete Deep Agents Course With Langchain In 3 Hours

**URL:** https://www.youtube.com/watch?v=J8DzuMmSDEU
**Added:** 2026-07-04
**Relevance:** ⭐⭐⭐⭐⭐ (5/5)

## Key Takeaways
- Deep agents differ from shallow agents by combining planning, sub-agent delegation, persistent/shared context, and file-system-style memory instead of relying only on simple LLM-tool loops.
- A practical deep agent stack in this course uses LangGraph-based deepagents with tools, system prompts, memory files, skills, and optional sub-agents to support long-running complex tasks.
- Backends determine where agent files and memory are stored, including LangGraph state, local disk via file system backend, and store-based persistence via in-memory or key-value stores.
- Context engineering is treated as a core design discipline: system prompts provide baseline behavior, memory files provide always-loaded project context, and skills provide on-demand specialized knowledge.
- Skills are modular capability packs stored as markdown files such as skill.md, instructions.md, and examples.md, loaded only when the user request matches their domain.
- Sub-agents are specialist agents with their own description, system prompt, tools, and optional response format, enabling cleaner context separation and more focused execution.

## Apply to ArchonOS
- Set up a clean Python project using uv, create a virtual environment, and install deepagents, langchain, langchain-openai, Tavily Python, python-dotenv, and IPython kernel support.
- Create a basic deep agent with createdeepagent, define a Tavily-powered web search tool, connect a model, and test it on a research question such as 'What is deep agents?'
- Compare a normal LangChain create_agent workflow with a deep agent to observe differences in middleware, to-do tracking, summarization, and file handling.
- Experiment with state backend, file system backend, and store backend by asking the agent to create and later read a todo.txt file, then inspect where the data is actually stored.
- Create an AGENT.md file containing project architecture, conventions, and operating guidance, then load it into the agent as persistent memory and test how it changes responses.

## Subjects
Deep, LangGraph, Backends, Context

## TubeOnAI Summary
> This course introduces deep agents as a progression beyond basic and ReAct-style agents, distinguishing them by explicit planning, task decomposition, sub-agents, persistent file-backed context, and stronger state handling for complex multi-step work. It contrasts shallow agents, which mainly route between an LLM and tools, with deep agents that create to-do plans, delegate specialized subtasks, and use shared memory or file systems to retain and organize context across longer workflows. The implementation examples use LangChain, LangGraph, and the deepagents library to build a basic deep agent, attach web search via Tavily, define models, and invoke the agent on research tasks. The course then expands into customization through backends, showing how state backend, file system backend, and store backend change where agent-created files and memory live. A major focus is context engineering, including system prompts, agent.md-style memory files, and skill modules that load specialized instructions only when relevant to a user task. Sub-agents are presented as specialist workers with their own context, tools, and instructions, used to isolate context and parallelize work, including examples with structured outputs using Pydantic models. The final demonstration combines these ideas into a Streamlit chatbot that loads memory, skills, planning, web search, report-writing behavior, and sub-agent delegation to perform deep research-style tasks such as summarizing LLM gateways or answering AWS-related questions.

## Tags
`#ai-agents` `#2026` `#productionai` `#archonos-improvement`
