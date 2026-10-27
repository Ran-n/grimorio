---
name: feedback-backlog-artifact-sync
description: "Whenever renar's backlog.md (frontend or backend) is updated, also update the published Renar Backlog artifact"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7508d177-fbe0-4d6e-893d-515c7917d866
  modified: 2026-08-24T11:36:58.003Z
---

Any time `docs/backlog.md` changes in either renar repo (items added, resolved/removed, edited), also republish the "Renar Backlog" artifact so it stays in sync.

**Why:** user explicitly asked for this to be a standing rule (2026-08-18) — the artifact had drifted from backlog.md (stale entries that had already been resolved and deleted from the source files).

**How to apply:**
- Find the artifact via `Artifact` tool `action: "list"` (title "Renar Backlog") if the URL isn't already known from this session.
- `WebFetch` the artifact URL first (required before any update) to get current content/DATA array.
- Sync the `DATA` array to match both [[renar-backend]]/[[renar-frontend]] `docs/backlog.md` files exactly — add new entries, remove resolved ones, update edited ones.
- The artifact also tracks a `PROGRESS` array (backlog size over time, for its trend chart) — add/update today's data point with the new total and blocking-for-1.0 counts after syncing DATA.
- Republish with the same `url` (don't create a new artifact) and keep the favicon (🗂️) stable — **check this memory for the favicon value before every publish call**, don't guess one; missed once (2026-08-24, published 📋 instead) and had to republish just to fix it.
- This applies automatically going forward — don't wait to be asked to "update the artifact" again after a backlog edit; do both in the same turn per [[feedback_renar_both_repos_always]].
