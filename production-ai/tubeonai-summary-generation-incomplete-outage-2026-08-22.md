# TubeOnAI `summary_generation_incomplete` Outage — 2026-08-22

**Added:** 2026-08-22
**Type:** Operational Incident

## What broke

On 2026-08-22 at 23:55 UTC, the `archonos-improvement-researcher` cron submitted 16 fresh YouTube URLs to TubeOnAI's POST `/summaries` endpoint. All 16 returned `HTTP 200 success:true` with new IDs in the `01a02cf0-*` and `01a02cfa-*` range. Within 60 seconds, every single job reported:

```json
{
  "status": "failed",
  "error": "Summary generation completed without producing content. Please contact support instead of retrying.",
  "error_code": "summary_generation_incomplete"
}
```

A control POST of a known-cached video (Rick Astley) returned a 2024-cached summary — confirming the cache path still works. But 3 independent fresh submissions (all unrelated to the failed batch) also failed identically.

## Endpoint inconsistency

`GET /summaries?limit=50` reports the freshly-submitted jobs as `status: "completed"` (stale/optimistic listing). `GET /summaries/{id}` for the same IDs returns `status: "failed"` with the error message. The list endpoint lies; the by-id endpoint is the source of truth.

## Impact on the wiki pipeline

- **No entries written** — hard rule §6.1 forbids fabricating summaries from failed jobs
- **36 credits consumed** today (down from 50,973 to 50,937)
- **State file updated** with `totalRuns: 9`, `lastBatchTitles: []`, `notes: "Batch FAILED — TubeOnAI backend degraded..."`
- **`totalEntries` unchanged** at 205

## Recovery procedure (verified recipe for next run)

1. **Don't retry immediately.** Server-side URL-cache locks the failure for ~24-48h (pitfall #21).
2. After 24h, re-submit the same 16 URLs once. If the worker has recovered, summaries will complete normally.
3. If still failing after the retry, **switch `prompt_id`** from `019e9573-b9ba-70c3-a61e-2ad835da20cd` (Alfred Lab v1) to `019e499c...` (FinTech Digest v1.1) and submit once more. Different prompt templates use different worker paths.
4. Only consider the `youtube-transcript-api` + M3-summarize fallback if both TubeOnAI prompts fail twice. Get user confirmation per pitfall #22 before pivoting.

## Diagnostic recipe (for future on-calls)

```bash
# 1. Submit one cached-hit control (Rick Astley is reliable)
curl -X POST -H "Authorization: Bearer $TUBEONAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url":"https://www.youtube.com/watch?v=dQw4w9WgXcQ","type":"youtube"}' \
  https://app.tubeonai.com/api/developer/v1/summaries

# 2. Submit one truly-fresh URL
curl -X POST ... # any new URL

# 3. After 60s, check both by-id
for jid in <cached_id> <fresh_id>; do
  curl -s -H "Authorization: Bearer $TUBEONAI_API_KEY" \
    https://app.tubeonai.com/api/developer/v1/summaries/$jid
done

# If cached_id has summary and fresh_id is failed, backend is degraded.
# If both are failed, your account or prompt template is the issue.
```

## Tags

`#tubeonai` `#outage` `#backend-degraded` `#operational`