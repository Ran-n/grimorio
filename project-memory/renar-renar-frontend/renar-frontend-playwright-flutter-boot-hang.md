---
name: renar-frontend-playwright-flutter-boot-hang
description: Root cause of the Flet/Flutter web canvas hanging forever on its loading spinner when driven by Playwright from a Python subprocess-launching script
metadata: 
  node_type: memory
  type: project
  originSessionId: 599264de-9ee4-46a7-8104-fe7e2a63a5b4
  modified: 2026-08-18T14:25:26.962Z
---

When a Python script spawns the Flet web server (`web.exe` / `uv run web`) via `subprocess.Popen(..., stdout=subprocess.PIPE)` and then later launches a Playwright/Chromium browser **in that same process**, the Flutter engine's canvas hangs forever on the loading spinner — `flt.flutterAppLoaded` never resolves, no console error, no failed network request. All resources (canvaskit.wasm, main.dart.js/.mjs) load fine; the hang is silent.

**Root cause:** the `stdout=subprocess.PIPE` handle for the web-server child process is inheritable on Windows. When Chromium is spawned later from the same parent, it inherits that pipe handle too, and this breaks its GPU process's WebGL context recovery (`CONTEXT_LOST_WEBGL` fires but never recovers). Confirmed by isolating every other variable (CDN vs local canvaskit, skwasm vs single-threaded canvaskit, headless vs headed, COOP/COEP headers, Chromium build/version, 90s+ timeouts) — none of those mattered. Only removing the PIPE fixed it, consistently, across 5+ repeated runs.

**Fix:** redirect the web-server subprocess's `stdout`/`stderr` to a real file (`open(path, "w")`) instead of `subprocess.PIPE`, with `close_fds=True`. See `tests/integration/conftest.py`'s `_spawn_logged()` helper in [[renar-frontend-ui-verification-workflow]]'s repo — same fix applies to any script that spawns Flet's web server as a child before driving it with Playwright, not just pytest fixtures.

**Also found along the way (kept, but unconfirmed as necessary once the PIPE fix was in):**
- `FLET_WEB_NO_CDN=1` serves CanvasKit locally instead of fetching from `gstatic.com` — avoids an external network dependency for tests, harmless to keep.
- Added `Cross-Origin-Opener-Policy: same-origin` + `Cross-Origin-Embedder-Policy: credentialless` response headers in `serve_web.py` (real app code, not test-only) for skwasm's SharedArrayBuffer requirement — `credentialless` not `require-corp` so TMDB poster images / the `/tmdb/image` proxy keep working. Real, if unconfirmed-necessary, correctness fix for any real browser that picks the skwasm renderer.
- `playwright` pinned to `1.61.*` in dev deps after 1.62's bundled Chromium looked initially suspicious — turned out to be a red herring (1.61 and 1.62 use the identical chrome.exe/revision once actually compared); the PIPE handle was the real cause. Pin can likely be removed, but wasn't re-verified after the PIPE fix landed.

**Why:** cost ~2 hours of hypothesis-testing (CDN, GPU/WebGL flags, threading, headless vs headed, browser version) across a live debugging session building `tests/integration/` for renar-frontend, before isolating it to the PIPE handle specifically by comparing a script that spawned the web server itself vs. one that connected to an already-running, independently-launched server.

**How to apply:** any future script (test fixture, dev tool, CI helper) that both (a) spawns the Flet web server as a subprocess and (b) drives it with Playwright in the same process — always redirect that subprocess's stdout/stderr to a file, never a pipe.
