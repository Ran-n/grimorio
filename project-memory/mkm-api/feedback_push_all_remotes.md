---
name: Always push to all remotes
description: Every push must go to GitHub, GitLab, and Codeberg remotes via SSH; create any missing remote first
metadata:
  type: feedback
---

Always push to GitHub, GitLab, and Codeberg remotes on every push. If any remote does not exist, create it first using an SSH URL, then push to all three.

- GitHub: `git@github.com:Ran-n/<repo>.git`
- GitLab: `git@gitlab.com:Ran-n/<repo>.git`
- Codeberg: `git@codeberg.org:ran-n/<repo>.git`

**Why:** Bitbucket dropped in 2026-05 — its repo creation API does not support API tokens (only App Passwords, which are unavailable). All Ran# projects are now mirrored on three platforms.

**How to apply:** Run `git remote -v` first to get the actual remote names, then push to all three. Always check with `git remote -v` — never assume the name. SSH URLs only — never HTTPS.
