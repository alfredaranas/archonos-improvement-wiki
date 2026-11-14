# Build an Agentic AI Research Assistant from Scratch | Multi-Agent Project (LangGraph, FastAPI, Groq)

**URL:** https://youtube.com/watch?v=qeyi7mIjdMc
**Channel:** AmanAI Lab
**Added:** 2026-11-14
**Relevance:** ⭐⭐⭐⭐ (4/5)

## Key Takeaways
- Use a virtual environment with Python 3.12 rather than the newest Python version, to reduce compatibility problems and keep dependencies isolated.
- Keep API keys and the virtual environment out of GitHub by adding them to `.gitignore`; configure required secrets separately on deployment platforms.
- Test each agent before connecting it to the workflow, then test the API endpoints and frontend communication before deployment.
- Give the research agent web search results as evidence, and instruct it to distinguish facts from uncertainty and retain source URLs.
- Define structured request and response models in FastAPI so inputs and outputs follow the formats the application expects.

## Apply to ArchonOS
- Map the orchestration pattern onto ArchonOS archon delegation boundaries and the demiurge/archon split.
- Check the pattern against the fleet's 26-archon topology — does it assume a single coordinator that ArchonOS does not have?
- Add the pattern to the ArchonOS architecture reference notes.

## TubeOnAI Summary
> The project builds and deploys a web-based research assistant that routes questions through research, analysis, and writing agents. It uses LangGraph to run the workflow, FastAPI for the backend, Streamlit for the interface, and LangSmith to trace runs.
> 
> ## Advice
> - Use a virtual environment with Python 3.12 rather than the newest Python version, to reduce compatibility problems and keep dependencies isolated.
> - Keep API keys and the virtual environment out of GitHub by adding them to `.gitignore`; configure required secrets separately on deployment platforms.
> - Test each agent before connecting it to the workflow, then test the API endpoints and frontend communication before deployment.
> - Give the research agent web search results as evidence, and instruct it to distinguish facts from uncertainty and retain source URLs.
> - Define structured request and response models in FastAPI so inputs and outputs follow the formats the application expects.
> - Add LangSmith tracing to inspect inputs, outputs, errors, token usage, and costs.
> - Deploy the backend and frontend separately, then configure the frontend with the deployed backend’s base URL.

## Tags
`#agents` `#agent-architectures` `#archonos`
