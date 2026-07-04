# Agent Evaluation with Gemini Agent Eval API

**URL:** https://www.youtube.com/watch?v=qo8i_0RCieU
**Added:** 2026-07-04
**Relevance:** ⭐⭐⭐⭐ (4/5)

## Key Takeaways
- Agent evaluation was framed around two durable metrics: tool-use correctness and groundedness against trusted data.
- The Gemini Agent Eval API can programmatically score agent behavior using datasets of prompts, expected responses, and references, including intentionally failing cases.
- A custom no-billing evaluation flow can be built by prompting Gemini as a judge to return binary assessments for tool routing and factual consistency.
- Simulated datasets were used instead of historical logs because the demo application did not yet have enough production-style interaction history.
- Groundedness testing was demonstrated by comparing agent answers against live or mocked allergen data and verifying that hallucinated answers reduce the score.
- Security posture in agent systems can be improved by exposing narrowly scoped tools through MCP Toolbox instead of giving agents direct database access.

## Apply to ArchonOS
- Create or select a Google Cloud project, open Cloud Shell, and enable the required APIs listed in the codelab.
- Clone the repository, inspect files such as app.py, appnobill.py, agenteval.py, and agentevalnobill.py, and install dependencies from requirements.txt.
- Populate the .env file with project ID, Google API key, and any required toolbox URL if using the billed evaluation path.
- Run the no-billing app locally with python app_nobill.py and test prompts such as allergen checks and order placement.
- Run the Gemini Agent Eval API example and inspect exact-match and groundedness results for the provided test datasets.

## Subjects
Agent, The Gemini Agent, Gemini, Simulated

## TubeOnAI Summary
> This session continues a multi-part build of a frozen-yogurt store agent on Google Cloud and focuses on evaluating the agent rather than building new data pipelines. The application uses structured data derived from unstructured PDFs in BigQuery, transactional order data in AlloyDB, and an agent layer built with ADK and MCP Toolbox to expose tools such as checking allergens and placing orders. The evaluation walkthrough covers two main dimensions: routing accuracy, meaning whether the agent selected the correct tool or asked for clarification when required, and groundedness, meaning whether its response matched database-backed facts rather than hallucinated content. One path uses the Gemini Agent Eval API from the Gemini Enterprise agent platform to score exact match and groundedness against simulated test cases and live or mocked database context, including intentionally incorrect examples to confirm the evaluator catches failures. A second path shows how to build a no-billing custom evaluator by using Gemini as an LLM judge with structured prompts that assess tool selection and factual consistency from mocked payloads. The session also demonstrates a jailbreak-style prompt against the agent and explains why it fails in this setup: the agent only has access to a narrow tool interface, not arbitrary SQL execution or direct database control. The remainder of the session is operational guidance for setting up a Google Cloud project, Cloud Shell, dependencies, environment variables, API keys, running the application, and submitting a screenshot of evaluation results.

## Tags
`#ai-agents` `#2026` `#productionai` `#archonos-improvement`
