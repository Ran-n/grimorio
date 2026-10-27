---
name: feedback-fix-errors-and-continue
description: when a step errors mid-workflow (hook refusal, failed command), fix it and carry on; never stop and hand back
metadata:
  type: feedback
---

When a command or hook fails partway through a task, diagnose it, fix it and continue the workflow to the end. Don't end the turn on the error.

**Why:** during `/dbp` on bounty_board (2026-10-27) a commit was refused (Co-Authored-By line forbidden by [[feedback_commits]]; the changelog hook then fired) and the turn stopped there. The user said: "if you error you shouldnt stop, you should continue and fix it".

**How to apply:** treat errors as one more step: read the message, correct the cause (e.g. drop the attribution line, stage CHANGELOG), retry, and finish. Only stop for decisions that are genuinely the user's. Related: [[feedback_no_permission_prompts]].
