---
name: always-push-to-github-and-gitlab
description: Every push must go to both GitHub and GitLab remotes via SSH; create either remote if missing
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2357ec0d-7eb6-4caf-86db-e0049e064f79
---

Always push to both `github` and `gitlab` remotes on every push. If either remote does not exist, create it first using an SSH URL (`git@github.com:Ran-n/<repo>.git` / `git@gitlab.com:Ran-n/<repo>.git`), then push to both.

**Why:** All Ran# projects are mirrored on both platforms. Pushing to only one leaves them out of sync.

**How to apply:** After every commit, push to all remotes:
```
git push github main
git push gitlab main
```
Or if the repo only has one remote named `origin`, check whether the second platform has a repo and add it. Use `git remote -v` to inspect. Never push only to `origin` if that means one platform is skipped.
SSH URLs only — never HTTPS.
