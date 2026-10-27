---
name: Push means commit then push
description: "push changes" = stage all pending + commit + push, no confirmation
type: feedback
originSessionId: b1919612-18b3-42e2-826b-d27f7852ca1c
---
On any "push" request: stage all relevant changes, commit (following commit style rules), push to all remotes simultaneously. No confirmation needed.

**Why:** user confirmed this is always the intended flow; repos are mirrored across all platforms.

**How to apply:** Push to all remotes in one step. Current remotes for this repo are both configured under `origin` (multi-push-URL):
- GitHub: `git@github.com:Ran-n/lenxif.git`
- GitLab: `git@gitlab.com:Ran-n/lenxif.git`

```
git push origin main
```
(pushes to both URLs since origin has two push URLs configured)
