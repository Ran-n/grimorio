---
name: Git remote creation — use main branch
description: When creating repos on GitHub or GitLab, always use main as the default branch
type: feedback
originSessionId: 9a3f4409-64b0-40d3-90f1-4416867daca8
---
When creating a new repository and pushing to GitHub or GitLab, ensure the default branch is `main`, not `master`.

**Why:** GitHub and GitLab both default to `main`; using `master` causes a mismatch and a past repo was initialized with `master` by mistake.

**How to apply:** Before the first push, rename the branch if needed:
```
git branch -m master main
git push -u origin main
```
Then set the default branch to `main` in the remote's settings (GitHub: Settings → Branches; GitLab: Settings → Repository → Default branch).
