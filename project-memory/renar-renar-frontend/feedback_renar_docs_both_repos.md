---
name: renar-docs-both-repos
description: renar-frontend and renar-backend are companion repos — always update documentation for both when asked to update docs
metadata: 
  node_type: memory
  type: feedback
  originSessionId: b8e87e15-7b5b-4376-8fe4-0c8605191ec8
---

When asked to "update documentation" while working in renar-frontend or renar-backend, always check and update docs in **both** repos, not just the one currently open.

**Why:** the two repos ship together and their docs (READMEs, CHANGELOGs, `docs/`) drift out of sync independently; the user confirmed ("yes, always") after being asked whether to also check the backend.

**How to apply:** at the start of any doc-update task in either repo, also run `git status`/`git diff --stat` in the sibling repo (`../renar-backend` or `../renar-frontend`) and reconcile its README/CHANGELOG/docs against its uncommitted diff before considering the task done.
