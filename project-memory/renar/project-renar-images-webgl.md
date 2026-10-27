---
name: project-renar-images-webgl
description: "Renar images \"not loading\" has TWO known distinct root causes: (1) browser WebGL/hw-accel disabled, (2) backend CORS_ORIGINS not matching the frontend's actual port"
metadata: 
  type: project
  originSessionId: 430e967c-7c13-4d0d-b2e4-023dd0a6c413
---

Renar's "images not loading" symptom (text/UI fine, only image bitmaps blank) has recurred twice with two different root causes — check both, don't assume it's the same one as last time.

**Cause 1 (found 2026-07-03, base64 architecture — now superseded):** browser WebGL/hardware acceleration disabled; Flet's Flutter CanvasKit renderer draws no images at all without it. Check `chrome://gpu`. Fixes: enable hw accel, or run the desktop app (bypasses the browser). This was diagnosed back when posters were base64-embedded server-side — that approach was later replaced (see cause 2's context), but the WebGL limitation is a renderer-level fact independent of transport, so it can still recur.

**Cause 2 (found 2026-07-22, current architecture):** images are now fetched as real URLs by the browser — `poster_image()` in `views/ui.py` builds `ft.Image(src=...)` where `src` comes from `ApiClient.poster_src()` (`api_client.py`), a same-origin-style proxy path (`/tmdb/image/<size>/<file>`) prefixed with the backend's base URL. This is a genuine cross-origin fetch done **by the browser's CanvasKit renderer** (not by the Python app's own `httpx` calls, which run server-side and never touch browser CORS). `renar-backend/.env`'s `CORS_ORIGINS` only listed `localhost`/`127.0.0.1` origins — not the actual origin the browser uses. Two layers of this bit in the same session:
  1. `renar-frontend/.env`'s `RENAR_FRONTEND_PORT=8080`, not the `CORS_ORIGINS` default's `8550` — first fix added `:8080` variants.
  2. The user doesn't browse via `localhost` at all — they hit the frontend directly at `http://renar.app:8080` / `http://renar.breren.com:8080` (port-forwarded straight to the Flet dev server on the deployment host, bypassing an unrelated Kestrel service that squats on port 80 — see `docs/design-decisions.md`). Neither hostname was in `CORS_ORIGINS` either, so the fix wasn't complete until both public origins were added too.
  **Ask what URL is literally in the address bar before assuming `localhost` — don't guess.**

Working `CORS_ORIGINS` after both fixes: `["http://localhost:8550","http://127.0.0.1:8550","http://localhost:8080","http://127.0.0.1:8080","http://renar.app:8080","http://renar.breren.com:8080"]`.

**Why this is easy to misdiagnose:** all the ordinary signals (backend up, proxy endpoint returns 200 with real image bytes via curl, TMDB reachable) look healthy, because the failure only happens inside the *browser's* CORS enforcement on the image fetch — curl doesn't send an `Origin` header so it never reproduces the block; you have to pass `-H "Origin: <the exact browser origin>"` to a curl `OPTIONS` preflight to see it. `WebGL: Hardware accelerated` in `chrome://gpu` rules out cause 1. Everything is plain HTTP right now (no TLS anywhere in this deployment yet — see backlog.md's HTTPS item — so mixed content isn't a factor, but revisit this note if that changes).

**How to apply:** if images go missing again: (a) ask exactly what URL is in the address bar — don't assume `localhost`; (b) check `chrome://gpu` for WebGL/hw-accel status; (c) if that's fine, confirm `renar-backend/.env`'s `CORS_ORIGINS` includes that *exact* origin (scheme+host+port) — the backend must be **restarted** after editing `.env` since pydantic-settings reads it once at startup; (d) a curl `OPTIONS` preflight with `-H "Origin: <origin>"` against `/tmdb/image/...` confirms the fix (look for a matching `access-control-allow-origin` in the response) without needing to reproduce it in-browser. See [[project_renar_layout]].
</content>
