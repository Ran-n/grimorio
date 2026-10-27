---
name: Push means commit then push
description: When user says "push changes", always commit all pending changes first then push — do not ask for confirmation
type: feedback
originSessionId: 118f0cca-fa1f-4976-b472-c4b2b1d69b12
---
When the user says "push changes" (or equivalent), always commit all pending/staged changes first and then push in one flow — do not stop to ask if they want to commit first.

**Why:** User explicitly confirmed this is always the intended behavior.

**How to apply:** On any "push" request, stage all relevant changes, create a commit (following commit style rules), then push to remote. No confirmation needed.
