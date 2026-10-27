---
name: git-remote-creation-use-main-branch
description: "When creating repos on GitHub or GitLab, always use main as the default branch"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2357ec0d-7eb6-4caf-86db-e0049e064f79
---

When creating a new repository and pushing to GitHub or GitLab, ensure the default branch is `main`, not `master`.

**Why:** GitHub and GitLab both default to `main`; using `master` causes a mismatch and a past repo was initialized with `master` by mistake.

**How to apply:** Before the first push, rename the branch if needed:
```
git branch -m master main
git push -u github main
git push -u gitlab main
```
Then set the default branch to `main` in the remote's settings (GitHub: Settings → Branches; GitLab: Settings → Repository → Default branch). See [[Always push to GitHub and GitLab]] for remote naming conventions.
