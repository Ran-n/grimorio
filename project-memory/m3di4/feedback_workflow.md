---
name: workflow
description: Workflow preferences — auto-approve behaviour and git push policy
type: feedback
---

- When auto-approve mode is on, execute all commands and edits immediately without asking for confirmation.
- Do NOT run `git push` unless the user explicitly asks to push/publish. Commit locally as needed, but stop there.

**Why:** User prefers uninterrupted flow when auto-approve is on; pushes are always an explicit decision.
**How to apply:** After committing, stop. Only push when the user says "push" or equivalent.
