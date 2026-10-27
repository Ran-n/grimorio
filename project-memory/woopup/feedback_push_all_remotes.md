---
name: always-push-to-all-remotes
description: "Every push must go to GitHub, GitLab, Bitbucket, and Codeberg remotes via SSH; create any missing remote first"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 53532e8b-f785-4b95-b670-f3695028a191
---

Always push to GitHub, GitLab, Bitbucket, and Codeberg remotes on every push. If any remote does not exist, create it first using an SSH URL, then push to all four.

- GitHub: `git@github.com:Ran-n/<repo>.git`
- GitLab: `git@gitlab.com:Ran-n/<repo>.git`
- Bitbucket: `git@bitbucket.org:ran-n/<repo>.git`
- Codeberg: `git@codeberg.org:ran-n/<repo>.git`

**Why:** All Ran# projects are mirrored on all four platforms. Pushing to only some leaves them out of sync.

**How to apply:** Run `git remote -v` first to get the actual remote names, then push to all. Always check with `git remote -v` — never assume the name. SSH URLs only — never HTTPS.
