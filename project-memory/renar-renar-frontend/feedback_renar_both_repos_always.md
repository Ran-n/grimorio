---
name: feedback-renar-both-repos-always
description: "Any task given in renar-frontend (not just push/commit/docs) must be checked against renar-backend too — do the work on whichever repo(s) it actually applies to"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0cc16ecb-b912-47e2-b5d7-9838e8f9706f
  modified: 2026-07-28T10:14:48.503Z
---

When working in renar-frontend and given a task of any kind — not just
push/commit/docs, but bug fixes, feature work, version bumps, audits,
anything — always check whether it also applies to renar-backend
(`d:\Users\{USER}\sw\renar\renar-backend`), and do the work on whichever
repo(s) it actually applies to, in the same pass, rather than stopping at
the frontend.

**Why:** corrected after pushing only the frontend export-screen fix; the
user's actual expectation is that renar-scoped tasks always span both
repos, matching [[feedback_renar_docs_both_repos]] which established this
for documentation specifically. The user then generalized it further:
"when I tell you to do stuff you should look at both be and fe to see if
it applies to both or only one and do work on any that apply" — this is
not limited to push/commit/docs.

**How to apply:** for any renar task, check renar-backend's state too
(`git status`, relevant source/docs) before deciding scope. If the task
applies there too — even if not explicitly mentioned — handle it there in
the same turn. If it only applies to one side, say so explicitly rather
than silently narrowing scope or silently expanding into unrelated backend
work.
