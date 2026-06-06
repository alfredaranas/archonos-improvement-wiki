# TubeOnAI API Playground

Source: [https://web.tubeonai.com/api-playground](https://web.tubeonai.com/api-playground)

## What it is
TubeOnAI's developer API is a REST API for summarizing and transcribing content at scale.

## Auth
- Header: `Authorization: Bearer toai_sk_your_key`

## Rate limits
- `60 requests/minute` per API key
- Concurrent processing limits depend on plan
- Every response includes `X-Request-ID` and `request_id`

## Supported sources
- YouTube
- Article / web pages / blog posts / news / Twitter/X posts
- Podcast RSS / Spotify / Apple
- Document: PDF, DOCX, TXT, Google Drive, Google Sheets
- Audio: MP3, WAV, M4A, SoundCloud
- Rumble
- Video: TikTok, Instagram, Vimeo, Facebook, Dailymotion, Twitch, direct URLs
- PowerPoint

## Core endpoints
### Summaries
- `POST /api/developer/v1/summaries`
- `GET /api/developer/v1/summaries`
- `GET /api/developer/v1/summaries/{id}`
- `DEL /api/developer/v1/summaries/{id}`
- `GET /api/developer/v1/summaries/{id}/progress`

### Transcriptions
- `POST /api/developer/v1/transcriptions`
- `GET /api/developer/v1/transcriptions`
- `GET /api/developer/v1/transcriptions/{id}`
- `GET /api/developer/v1/transcriptions/{id}/progress`

### Prompts
- `GET /api/developer/v1/prompts`
- `POST /api/developer/v1/prompts`
- `GET /api/developer/v1/prompts/{id}`
- `PUT /api/developer/v1/prompts/{id}`
- `DEL /api/developer/v1/prompts/{id}`

### Repurpose
- `GET /api/developer/v1/repurpose`
- `POST /api/developer/v1/repurpose`
- `GET /api/developer/v1/repurpose/{id}`

### Credits & usage
- `GET /api/developer/v1/usage`
- `GET /api/developer/v1/credits/balance`
- `GET /api/developer/v1/credits/history`

### Webhooks
- `POST /api/developer/v1/webhooks/test`

## Response envelope
Successful responses follow this shape:

```json
{
  "success": true,
  "message": "...",
  "data": {},
  "request_id": "req_...",
  "usage": {
    "credits_reserved": 10,
    "credits_used": 0,
    "remaining_credits": 99996
  },
  "_links": {}
}
```

## Notes for ArchonOS
- Use summaries for YouTube discovery before writing into the wiki
- Use credits/balance when deciding whether to batch ingest
- Use progress endpoints for long-running jobs
- The API already exposes the exact credit and usage endpoints Alfred asked about
