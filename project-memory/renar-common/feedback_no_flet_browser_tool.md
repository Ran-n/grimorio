---
name: no-flet-browser-tool
description: How to actually screenshot the renar-frontend Flet app for visual verification (corrects an earlier wrong assumption that this was impossible)
metadata: 
  node_type: memory
  type: feedback
  originSessionId: b1484943-80f8-4a47-b702-8f86266677e2
  modified: 2026-07-27T13:16:19.277Z
---

Flet UI changes in renar-frontend CAN be visually screenshotted end-to-end in this environment — a prior memory claimed otherwise and was wrong; the user corrected this directly ("you can screenshot flet directly").

**Why:** `uv run web` (or a custom harness) serves a Flutter/canvaskit canvas, which needs a real browser to render, not raw HTTP/HTML parsing. The fix isn't a missing tool, it's the right one: Playwright is installed under the system Python 3.11 (`C:\Users\{USER}\AppData\Local\Programs\Python\Python311\python.exe`, NOT the project's `uv` venv or the `python`/`python3` on PATH — check with `pip show playwright`, which resolves against 3.11 in this environment). `chromium-cli` (the tool the generic `run` skill assumes) is not installed here; use `playwright.sync_api` directly instead.

**How to apply:**
1. For isolated view review (no login/backend needed), write a small standalone harness script that imports the view function directly with a stub `ApiClient` and mounts it via `ft.run(main, export_asgi_app=True)` + `uvicorn.run(app, ...)` on a scratch port (mirrors `serve_web.py`'s own pattern) — avoids needing a running backend or a real login flow. Put `src/renar_frontend` on `sys.path` since the app uses flat imports (`from api_client import ...`).
2. Kill any stale process on that port first (`netstat -ano | grep :PORT`, `taskkill //F //PID <pid>`) before relaunching — same stale-process issue as [[feedback_stale_web_exe_cleanup]].
3. Wait for the port with `curl -sf` polling, not a fixed sleep.
4. Screenshot with the Python 3.11 Playwright install: `sync_playwright()`, `page.goto(url, wait_until='networkidle')`, then `page.wait_for_timeout(3000-4000)` before `page.screenshot(...)` — the Flutter/CanvasKit boot needs real wall-clock time after `networkidle`; a bare headless-Chromium `--screenshot` CLI call (msedge/chrome) fires before CanvasKit paints and only captures the static splash logo. `--virtual-time-budget` does NOT fix this — it breaks the real-time websocket handshake Flet needs, so the page never boots past the splash under it either.
5. Actually read the resulting PNG with the Read tool before claiming something renders correctly — don't infer from code review alone once a screenshot is possible.
