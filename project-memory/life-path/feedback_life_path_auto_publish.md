---
name: life-path-auto-publish
description: "in the life-path project only, auto-commit+push (dbp workflow) when a task is done, no explicit ask needed"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 527169c3-9d02-4b10-8124-8c2e9fe80183
  modified: 2026-08-27T08:37:11.228Z
---

In the **life-path** project specifically, run the full docs-bump-push workflow (update CHANGELOG, commit with [[commit-style]] bracket title, push to `github`/`gitlab`/`codeberg` per [[git-remote-default-branch]]) automatically whenever a task finishes leaving the working tree dirty — no need to wait for an explicit "push"/"commit"/"dbp" request first.

**Why:** user said "automatically publish when done" — GitHub/GitLab/Codeberg Pages all auto-build `src/` on push to `main`, so pushing *is* publishing for this static site; the user wants that to happen without asking each time.

**How to apply:** this overrides [[push-semantics]] (global "never commit/push unless explicitly asked" default) but only inside the life-path repo. Still skip commits containing nothing meaningful, and still follow normal safety checks (git status before destructive ops, no secrets staged). Other projects keep the global ask-first behavior unless similarly overridden.
