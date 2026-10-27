---
name: push-semantics
description: "never commit/push unless explicitly asked; when asked, stage → commit → push in one sequence, no confirmation"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c1eb3afb-65df-419c-8c56-97eef30b3f4d
---

Never commit or push unless the user explicitly asks. When asked to commit OR push, do both: stage all relevant changes, commit (following [[commit-style]] rules), then push to remote. No confirmation needed.

**Why:** commit/push are permanent and externally visible; user confirmed this flow — but only on explicit request.

**How to apply:** do not proactively commit or push even in autonomous mode. On any explicit "commit" or "push" request, execute the full stage→commit→push sequence without asking again. If other edits were made earlier in the same turn/session for a different reason (e.g. a small UI tweak requested mid-session), a later "push" request covers those too — bundle everything pending into the commit(s)/push rather than asking separately for each edit. Confirmed 2026-07-18 after asking explicitly.
