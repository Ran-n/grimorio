---
name: no-coauthor
description: Never add Co-Authored-By trailers to git commits
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 36b54e7a-e54a-42e8-aea7-480524b15f89
---

Never include `Co-Authored-By:` (or any variant) in commit messages. This applies to all commits in this project.

**Why:** User explicitly prohibited this. The `git_guard.py` hook now enforces it at commit time by blocking any message containing `co-authored-by` (case-insensitive).

**How to apply:** When building or proposing a commit message, omit the trailer entirely. No exceptions.
