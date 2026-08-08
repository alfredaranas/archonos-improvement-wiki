---
title: "TubeOnAI empty-summary failure (2026-08-08 batch) — status=completed but word_count=0"
source: youtube
url: https://alfredaranas.github.io/archonos-improvement-wiki/production-ai/tubeonai-empty-summary-failure-2026-08-08.html
author: Oracle archonos-improvement-researcher
---

# TubeOnAI empty-summary failure (2026-08-08 batch)

**Recorded:** 2026-08-08
**Status:** Open — TubeOnAI pipeline returning `status: completed` with `word_count: 0` and empty `summary` / `key_points` fields. Transcriptions ARE populated. Model parameter shows `azure/gpt-5` for new jobs, `azure/gpt-5.2` for cached hits that worked.

## Symptom

10 YouTube videos submitted to `/api/developer/v1/summaries` via lab payload (prompt_id `019e9573-...`, webhook `youtube.archonos.app/webhook`). 8 returned `status: completed` within 30-60s, but `data.summary == ""` and `data.word_count == 0` and `data.key_points == null`. The 8 affected jobs have `data.parameters.model == "azure/gpt-5"`. The 1 job with a real summary (`mwN75EiGfCE`, 4240 char summary) is a cache hit from 2026-07-15 with `model: azure/gpt-5.2`. 2 of the 10 returned `duplicate_request` 409 with no job_id, both already exist in recent-summaries list.

## What works

- POST submission and job creation: ✅
- Job ID assignment and `status: pending` → `completed` transition: ✅
- Transcription field (`data.transcription`): ✅ populated, 8-33K chars depending on video length
- Cached hits where prior summary exists: ✅
- `/credits/balance` (57149 available, is_locked: false): ✅
- Recent-summaries list endpoint: ✅ shows all 8 jobs as `completed`

## What doesn't

The 8 fresh jobs return empty `summary`, empty `key_points`, `word_count: 0`. Polling 60s later still empty. This is NOT a webhook/poller issue (the poller sees the data fine; the data is just empty). This IS a model-output failure on TubeOnAI's side: gpt-5 is returning blank or the post-processor is dropping content.

## Pipeline-mode correlation

This is the **6th distinct TubeOnAI drift pattern** documented in `references/tubeonai-architecture-2026-07-02.md` (extend the doc next run). Previous 5:
1. Multi-prompt account
2. Webhook-dead-but-pipeline-fine
3. Live-streamed content stalls
4. Submit 409 without job ID
5. Submit empty 200 with no JSON (`submit_bad_json`)

New #6: **completed-but-empty-summary** (model returned blank, status reported as success).

## Mitigation ladder for affected videos

1. **Wait 24-48h and re-poll** — model-output failures sometimes self-heal.
2. **Use the existing `transcription` field** as input to a local summarizer (M3 / Claude / Ollama). Transcriptions are clean.
3. **Re-submit without prompt_id override** (use the minimal payload without `prompt_id`/`webhook_url`) to route through TubeOnAI's default prompt template — may pick a different model.
4. **Drop the video and link to YouTube directly** as a wiki placeholder.

## Decision for 2026-08-08 batch

**No wiki entries written this run.** Per hard rule #7 (source-readable artifacts, no fabricated results) and pitfall #22 (don't pivot to a fallback without asking), the right move is to surface the failure, not invent summaries. All 10 candidates are logged in `/tmp/tubeonai_poll_results.json` for the next run to recover from.

## Affected video IDs (for recovery next run)

- Pucmy0GZkeI — Give Your Agent Tools Using MCP — AWS Developers (duplicate_request 409, may be recoverable via list-endpoint match)
- HRUBDPdvaHU — Meta-Harness: Designing Multi-Agent AI Systems — The Carbon Layer
- 3LE_VrIbe0I — Self-Hosted AI Agent Orchestration — TheYgent
- 2OeofCG_3iE — Your AI Agent Is Not Dumb. Your Context Window Is Flooded — Dr. Ibrar Ahmed
- GxO7wwDVn14 — 5 AI Agent Design Patterns (Sequential/Parallel/Loop/Router/Graph) — Annie Wang
- nK_0v_R3PYE — Human-in-the-Loop (HITL) for Agentic AI | LangGraph Patterns — Abhijith N
- QtQFsp630pI — Beyond Greenfield: Reverse-Engineering Patterns for AI Coding Agents on Brownfield Systems — AI Native Way
- PZsJfBVDZZc — Learn Every AI Agent Pattern From One Video (I Actually Ran All 35) — The AI Automators
- SkyDuHeIvP0 — Loop Engineering, Graph Engineering in 18min — Dr. Maryam Miradi

(9 affected; 1 entry mwN75EiGfCE was a successful 2026-07-15 cache hit with real summary already in place — could be shipped, but the run aborted to keep the batch atomic.)

## Search hooks

tubeonai empty summary status completed word_count zero gpt-5 model failure pipeline 2026-08-08 archonos wiki batch stuck no fabrication
