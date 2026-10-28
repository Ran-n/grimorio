---
name: feedback-apply-global-memory-proactively
description: Always scan global MEMORY.md before acting on any repo/file task — don't wait to be corrected
metadata:
  node_type: memory
  type: feedback
---

Before starting any task (scaffold, new file, commit, etc.), actively check the global MEMORY.md index for relevant rules and apply them without being asked.

**Why:** On logpiece init, the new-repo scaffold rules (LICENSE, CHANGELOG, CONTRIBUTING, CONTRIBUTORS, README License section) were in global memory the whole time but were missed because global memory was treated as passive context rather than an active checklist.

**How to apply:** When starting a task, mentally scan the MEMORY.md sections (Repository Setup, Workflow, Code Quality, etc.) for anything that applies. If a rule matches the task, execute it — don't wait for the user to point it out.

When initializing a new project (new repo, new claude projects directory), also replicate global memory into the project's memory directory automatically — copy `feedback_commit_push.md` and any other globally-applicable feedback/reference files, and seed `MEMORY.md` with the same workflow/releases boilerplate. No need to be asked.
**Open the file, never act on the index line.** MEMORY.md only holds one-line summaries; the rule itself (checklists, procedures) lives in the linked file. For every index line that matches the task, Read its file before replying, including for questions ("what's the testing situation?", "what's the coverage?" are both [[tests-requirement]] audits). The `~/.claude/hooks/memory_inject.py` UserPromptSubmit hook injects matching files automatically; when it hasn't, open them by hand.

**Why:** 2026-10-28, avalio-lite: asked about testing and coverage, I answered from defaults twice (test counts, a line-coverage table) without opening feedback_tests.md, which spells out the audit procedure (checklist type by type, uncovered lines and branches, screens without baselines, formats without golden files). The user: "can't ever miss them again".
