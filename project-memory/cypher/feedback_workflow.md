---
name: Workflow — auto-approve and commits
description: Auto-approve mode behavior and commit gating rule
type: feedback
originSessionId: 27a28edc-919c-456d-bfa9-7b1db3608dab
---
- When auto-approve mode is on, execute all commands and edits immediately without asking for confirmation.
- Never commit unless the user explicitly asks. When asked to push, always commit first then push.

**Why:** user controls commit cadence; "push" implies "commit then push" in this workflow.
**How to apply:** every session — gate commits on explicit user instruction; when "push" is requested, stage all changes, commit, then push without asking.
