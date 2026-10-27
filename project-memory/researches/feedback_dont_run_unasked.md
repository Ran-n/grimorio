---
name: Don't run project code without being asked
description: Don't run the project's own scripts/code unless asked, but do run supporting commands as needed to complete tasks
type: feedback
---

Do not run the project's own scripts (e.g. op_scrapper.py, main.py) unless the user explicitly asks to run them.

**Why:** User wants control over when their own code executes.

**How to apply:** After making code changes, stop there — don't execute the script. However, running supporting commands (installs, file ops, shell utilities, etc.) to fulfill a task is fine.
