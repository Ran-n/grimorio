---
name: Never commit or push without explicit user instruction
description: Do not run git commit or git push unless the user explicitly asks for it
type: feedback
originSessionId: a9faf96a-074c-4209-a524-30e5f7027481
---
Never commit or push unless the user explicitly says to commit or push. Finishing a task (edits, fixes, CHANGELOG update) does not imply permission to commit.

**Why:** User corrected this after a commit+push was made automatically at the end of a task without being asked.

**How to apply:** After completing file edits, stop. Do not invoke the commit skill, run `git commit`, or `git push` unless the user's message clearly requests it (e.g., "commit this", "push it", "/commit"). The commit-commands:commit skill must not be triggered speculatively.

When the user does ask to commit OR push, always do both: stage, commit, then push. Either word implies the full sequence.
