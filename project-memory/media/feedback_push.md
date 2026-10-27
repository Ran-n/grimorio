---
name: Push means commit then push
description: When user says "push changes", always commit all pending changes first then push — do not ask for confirmation
type: feedback
---

When the user says "push changes" (or equivalent), always commit all pending/staged changes first and then push in one flow — do not stop to ask if they want to commit first.

**Why:** User explicitly confirmed this is always the intended behavior.

**How to apply:** On any "push" request, stage all relevant changes, create a commit (following commit style rules), then push to remote. No confirmation needed.