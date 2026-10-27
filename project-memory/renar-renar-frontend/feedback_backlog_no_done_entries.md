---
name: feedback-backlog-no-done-entries
description: "Never write \"done\"/\"fixed\" entries into docs/backlog.md — remove resolved items entirely instead of annotating them as historical record"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 15497838-85fa-4285-b16c-a79306f48d6b
  modified: 2026-08-01T18:45:13.239Z
---

`docs/backlog.md` (both renar repos) tracks only what's still actionable. When an entry is resolved, remove it from the backlog entirely rather than marking it "done"/"fixed" and leaving the writeup in place.

**Why:** the backlog is loaded into context every time it's touched; a "done" entry is pure token overhead once resolved. The historical record already lives elsewhere: git history/commit messages for what changed, CHANGELOG.md for the user-facing summary, and [[feedback_renar_design_decisions_doc]] (design-decisions.md) for the *why* behind non-obvious choices. Nothing is lost by deleting a resolved backlog entry — the other docs already capture what's worth keeping.

**How to apply:** when closing out backlog work (whether just-shipped or found stale during an audit), delete the entry rather than annotating it. If a resolved entry has genuinely open sub-issues nested inside it (e.g. a fix that closes most of a bug but leaves an edge case), keep only the still-open part, trimmed to a standalone entry — don't keep the "done" framing around it. Also watch for entries in one repo's backlog referencing an entry that gets removed from the other (or the same file) — fix or drop the dangling cross-reference in the same pass.
