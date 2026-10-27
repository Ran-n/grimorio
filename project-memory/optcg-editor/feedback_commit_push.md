---
name: feedback-commit-push
description: "When user says \"push\" or \"commit\", always commit all relevant changes then push — don't ask, just do it"
metadata: 
  node_type: memory
  type: feedback
---

When the user says "push", treat it as commit + push. When the user says "commit", also push after committing.

**Why:** User explicitly stated this is their expected workflow — asking for clarification each time is friction.

**How to apply:** On "push" or "commit", stage relevant changes, create a commit, then push to the remote branch without asking for confirmation.
