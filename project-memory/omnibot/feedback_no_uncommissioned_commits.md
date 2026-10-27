---
name: feedback_no_uncommissioned_commits
description: "Never commit or push unless the user explicitly asks — \"everything yes\" is not commit authorization"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 85147169-047c-498f-a1d1-2634df84c925
---

Do not create git commits or push unless the user explicitly says to commit or push. Ambiguous affirmations like "everything yes", "yes", "looks good", or "do it" are not sufficient authorization for a commit or push.

**Why:** User had to undo a commit I created without being asked after misreading "everything yes" as commit approval.

**How to apply:** Only run `git commit` or `git push` when the user's message contains an unambiguous instruction to do so (e.g. "commit", "push", "ship it", "create a commit"). When in doubt, ask.
