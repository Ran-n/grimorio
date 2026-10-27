---
name: push-semantics
description: "never commit/push unless explicitly asked; when asked, stage → commit → push in one sequence, no confirmation"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2357ec0d-7eb6-4caf-86db-e0049e064f79
---

Never commit or push unless the user explicitly asks. When asked to commit OR push, do both: stage all relevant changes, commit (following [[commit-style]] rules), then push to remote. No confirmation needed.

**Why:** commit/push are permanent and externally visible; user confirmed this flow — but only on explicit request.

**How to apply:** do not proactively commit or push even in autonomous mode. On any explicit "commit" or "push" request, execute the full stage→commit→push sequence without asking again.
