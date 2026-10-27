---
name: workflow_auto_approve
description: When auto-approve mode is on, execute all commands and edits immediately
type: feedback
---

When auto-approve mode is on, execute all commands and edits immediately without asking for confirmation.

**Why:** User prefers uninterrupted flow when they've enabled auto-approve.
**How to apply:** Check context — if the session is running in auto-approve, don't pause to confirm actions.

Do NOT run `git push` unless the user explicitly asks to push/publish. Commit locally as needed, but stop there.
