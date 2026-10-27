---
name: run tests after each change
description: Always run the test suite after every code change in ximrato-app
type: feedback
---

After every code change in ximrato-app, run `uv run pytest tests/ -v` from `d:/Users/{USER}/sw/ximrato-app`.

**Why:** User explicitly asked for this after noticing tests weren't being run post-change.

**How to apply:** Any edit to source files in ximrato-app (screens, app.py, api, etc.) should be followed by a test run before considering the task done.
