---
name: feedback-dbp-trigger
description: "Trigger phrase \"dbp\" (typed plainly, like \"hk\") or /dbp — runs the docs-update + version-bump + push workflow"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0aa21bce-1f9a-43b9-89ad-65f89cba350a
  modified: 2026-08-25T13:00:44.221Z
---

Created a global slash command `/dbp` (`C:\Users\{USER}\.claude\commands\dbp.md`) that runs, in order: update documentation → bump version if needed → commit → push to all remotes.

**Why:** user had to repeat "update documentation, bump if needed, push changes" every time as a plain-text request; wanted a reusable command instead. Same pattern as [[feedback_housekeeping_trigger]]'s "house keep"/"hk" — a short plain-text phrase, not just a slash command.

**How to apply:** when the user types **"dbp"** as a plain message (no slash) or `/dbp`, treat it as an explicit request and run the `dbp.md` command file as written — it delegates to [[feedback_renar_both_repos_always]], [[feedback_version_bump]], [[feedback_changelog]], and [[feedback_push_all_remotes]] as the source of truth for each step, checking both renar-frontend and renar-backend. This overrides the normal "only touch CHANGELOG when a commit is requested" default for this one pass, same as "hk" does — the user is explicitly asking for the full pass including push. If the user asks in plain English for this same combo spelled out again, mention that "dbp" exists instead of re-deriving the steps from scratch.
