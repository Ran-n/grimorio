---
name: always-push-to-all-remotes
description: Every push must go to GitHub, GitLab, and Codeberg remotes via SSH; Bitbucket is not used
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8d6ce87f-ebe4-4c7f-9a7c-dc4de50180fd
---

Always push to `github`, `gitlab`, and `codeberg` remotes on every push. Bitbucket is not used. If any of the three remotes does not exist, create it first using an SSH URL, then push to all three.

- GitHub: `git@github.com:Ran-n/<repo>.git`
- GitLab: `git@gitlab.com:Ran-n/<repo>.git`
- Codeberg: `git@codeberg.org:ran-n/<repo>.git`

**Why:** All Ran# projects are mirrored on GitHub, GitLab, and Codeberg. Bitbucket is not part of the mirror set.

**How to apply:** After every commit, push to all three remotes:
```
git push github main
git push gitlab main
git push codeberg main
```
Use `git remote -v` to inspect existing remotes. Never push only to `origin` if that means a platform is skipped.
SSH URLs only — never HTTPS.
