---
description: Update docs, bump version if needed, commit, and push (renar docs-bump-push workflow)
---

Run this as one workflow, in order, for the current project — and for renar work, always check+handle both `renar-frontend` and `renar-backend` (`feedback_renar_both_repos_always.md`, `feedback_renar_docs_both_repos.md`):

1. **Update documentation.** Sync any docs affected by this session's changes (CHANGELOG, backlog, design-decisions, README, etc. as applicable) per each project's own doc conventions in memory.
2. **Bump if needed.** Follow `feedback_version_bump.md`: infer the level from the diff, write the version with the repo's own tool (uv, cargo, npm…, or a git tag when there is no manifest) per repo that has changes, promote the CHANGELOG `[Unreleased]` section. Only bump repos that actually changed. Update CHANGELOG in the same commit per `feedback_changelog.md`.
3. **Push.** Follow `feedback_push_all_remotes.md`: commit (bracket-style title per `feedback_commits.md`), then push to all configured remotes (`github`/`origin`, `gitlab`, `codeberg`) for every repo touched.

These memory files are the source of truth for each step's exact rules — don't restate or duplicate them here. Skip a repo entirely if it has no changes.
