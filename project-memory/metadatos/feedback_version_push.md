---
name: feedback_version_push
description: When a new version is pushed, update the metadatos script copy in global memory
type: feedback
---

When a new version of metadatos is pushed to remote, update the script copy in global memory:
1. Copy `main.py` to `C:/Users/{USER}/.claude/memory/metadatos_v<new_version>.py`
2. Delete the old versioned file
3. Update the path reference in `project_workflow.md` (this project's memory) to point to the new filename
4. Update the path reference in `C:/Users/{USER}/.claude/memory/MEMORY.md` (global memory) to point to the new filename

**Why:** Both global and project memory hold the path to the local script copy; both must stay in sync with the latest pushed version.

**How to apply:** After every `git push` that includes a version bump in this project.
