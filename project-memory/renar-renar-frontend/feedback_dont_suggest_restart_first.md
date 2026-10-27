---
name: feedback-dont-suggest-restart-first
description: "don't suggest \"restart the backend\" as a troubleshooting step when the user says the issue is persistent/long-standing"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 685179bf-da49-4084-982b-709d17d4fbed
  modified: 2026-08-19T13:59:22.134Z
---

Don't default to "have you tried restarting be.exe" when diagnosing a bug, especially once the user has said the problem has been happening for a long time (i.e. survives restarts already).

**Why:** User was told to restart as the likely fix for a 404 on `/svc/bans`; the issue had actually been present for a long time (so restarts don't matter) and the suggestion just wasted a round-trip. This compounds [[feedback_dont_manage_backend_process]] — since I never restart be.exe myself, proposing a restart as the fix is a low-value guess unless there's concrete evidence (e.g. a `.env` value was just edited in this session) that a stale in-memory config is the actual cause.

**How to apply:** When debugging renar backend/frontend issues, only suggest a restart if there's direct evidence config/code changed since the process last started. Otherwise keep digging into the actual code path (config loading, env file resolution, request headers, etc.) instead of reaching for "restart it" as a first-line answer.

**svc/bans 404 specifically:** user confirmed (2026-08-19) that neither the renar-backend nor renar-frontend process predates the `INTERNAL_SERVICE_SECRET`/`RENAR_INTERNAL_SECRET` pairing being set correctly in both `.env` files. Process staleness is ruled out for this issue — do not raise it again here. `.env` values were verified byte-identical, URL/port match, no OS-level env var shadowing found. The 404 cause is still unresolved; keep looking elsewhere (e.g. actual live request/response inspection, middleware ordering, whether the running process's in-memory settings actually reflect the file — e.g. via logging the loaded secret's length/hash at startup — rather than re-deriving the same static checks already done).
