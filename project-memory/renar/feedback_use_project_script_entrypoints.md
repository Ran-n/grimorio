---
name: feedback_use_project_script_entrypoints
description: "always invoke a Python project's own script entry points via `uv run <script>` instead of calling the underlying CLI tool directly"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e6702396-7cad-4643-a6ff-d6b6577d35ee
  modified: 2026-07-23T08:20:56.711Z
---

When a `pyproject.toml` defines `[project.scripts]` wrappers (e.g. `app`, `web`, `build`), always run them via `uv run <script-name>` — never shell out to the underlying tool directly (e.g. `flet build apk`, `flet run`, raw `python -m ...`).

**Why:** on renar-frontend, `uv run build` wraps `flet build` and does critical work the raw command skips — clearing `build/.hash/package` (a stale-cache bug that silently drops pinned deps like `certifi` from the shipped APK, `flet-dev/flet#5376`), stamping the app version and API URL into packaged sources, clearing stale `__pycache__`, and wiping incompatible cached Flutter templates. Calling `flet build apk` directly bypassed all of this and reproduced a `ModuleNotFoundError: No module named 'certifi'` crash on-device that had already been fixed once at the wrapper level. See [[project_renar_layout]].

**How to apply:** before running any build/serve/run command in a Python project, check `pyproject.toml` for `[project.scripts]` entries first. If one exists for the task at hand, use `uv run <name> [args]` and pass through any extra flags the wrapper forwards (check the wrapper source for arg-translation, e.g. `--split` → `--split-per-abi`). Only fall back to the raw tool if no project wrapper covers the task.
