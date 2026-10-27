---
name: feedback-apply-global-memory-proactively
description: "Always scan global MEMORY.md before acting on any repo/file task — don't wait to be corrected"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2357ec0d-7eb6-4caf-86db-e0049e064f79
---

Before starting any task (scaffold, new file, commit, etc.), actively check the global MEMORY.md index for relevant rules and apply them without being asked.

**Why:** On logpiece init, the new-repo scaffold rules (LICENSE, CHANGELOG, CONTRIBUTING, CONTRIBUTORS, README License section) were in global memory the whole time but were missed because global memory was treated as passive context rather than an active checklist.

**How to apply:** When starting a task, mentally scan the MEMORY.md sections (Repository Setup, Workflow, Code Quality, etc.) for anything that applies. If a rule matches the task, execute it — don't wait for the user to point it out.

When initializing a new project (new repo, new claude projects directory), also replicate global memory into the project's memory directory automatically — copy `feedback_commit_push.md` and any other globally-applicable feedback/reference files, and seed `MEMORY.md` with the same workflow/releases boilerplate. No need to be asked.
