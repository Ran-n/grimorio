---
name: git-remote-creation-use-main-branch
description: "When creating repos on GitHub or GitLab, always use main as the default branch"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 53532e8b-f785-4b95-b670-f3695028a191
---

When creating a new repository and pushing to GitHub, GitLab, Bitbucket, or Codeberg, ensure the default branch is `main`, not `master`.

**Why:** All platforms default to `main`; using `master` causes a mismatch and a past repo was initialized with `master` by mistake.

**How to apply:** Before the first push, rename the branch if needed:
```
git branch -m master main
git push -u github main
git push -u gitlab main
git push -u bitbucket main
git push -u codeberg main
```
Then set the default branch to `main` in each remote's settings. See [[Always push to all remotes]] for remote naming conventions.
