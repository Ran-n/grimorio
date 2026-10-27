---
name: Git remote creation — use main branch
description: When creating repos on GitHub or GitLab, always use main as the default branch
type: feedback
originSessionId: fdcb977d-f6a9-4b05-88b3-55b062f97029
---
When creating a new repository and pushing to GitHub or GitLab, ensure the default branch is `main`, not `master`.

**Why:** This repo was initialized with `master` by mistake; GitHub and GitLab both default to `main`.

**How to apply:** Before the first push, rename the branch if needed:
```
git branch -m master main
git push -u origin main
```
Then set the default branch to `main` in the remote's settings (GitHub: Settings → Branches; GitLab: Settings → Repository → Default branch).
