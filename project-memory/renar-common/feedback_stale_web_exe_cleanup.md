---
name: feedback-stale-web-exe-cleanup
description: "Kill background web.exe/flet app processes when done, and check for stale ones before starting a new run, instead of leaving them running and locking the venv"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2ebd941a-d8e7-4a99-997f-e27f42d3aa36
---

When running the renar-frontend app (`uv run app`, `uv run web`, etc.) in the background, always stop the process once done with it, and check for leftover `web.exe`/`python.exe` instances from prior sessions before starting a new run.

**Why:** Leftover background app processes hold a file lock on `.venv\Lib\site-packages\...\web.exe`, causing `uv run app` to fail with `os error 32` ("process cannot access the file"). This happened because a previous run was left running in the background and never killed.

**How to apply:** Before starting `uv run app`/`uv run web` for renar-frontend, run `tasklist | grep -i web.exe` and kill any stale instances first. After finishing a background dev-server session, proactively kill the process rather than leaving it dangling for the next run.
