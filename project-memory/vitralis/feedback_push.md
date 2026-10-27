---
name: push-means-commit-then-push
description: "When user says \"push changes\", always commit all pending changes first then push — do not ask for confirmation. Also, push after every change by default, not just when asked once."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8ecc114c-207e-4045-93c0-fa380087ccc0
  modified: 2026-08-04T17:52:01.602Z
---

When the user says "push changes" (or equivalent), always commit all pending/staged changes first and then push in one flow — do not stop to ask if they want to commit first.

**Why:** User explicitly confirmed this is always the intended behavior.

**How to apply:** On any "push" request, stage all relevant changes, create a commit (following commit style rules), then push to remote. No confirmation needed.

Push after each change, as a standing default — not just when the user explicitly says "push" once. Each logically-complete change (a bug fix, a feature, a content update) gets its own commit + push immediately, rather than batching multiple changes into one push at the end of a session.

**Why:** User explicitly asked to "push after each change" and to remember it as an ongoing rule, not a one-off request.

**How to apply:** After finishing any discrete change across any repo in this project (vitralis, doc, etc.), commit and push it to all configured remotes before moving to the next task — don't wait to be asked again. If a repo has a Pages `pages` branch that isn't wired to auto-sync via CI (see [[reference_page_handoff]] — Codeberg's Woodpecker secrets aren't set up yet), also manually re-sync that branch as part of the same push, since that's the only thing currently keeping Codeberg's live site in sync with `docs/`.

For vitralis specifically, `main` tracks `codeberg` as its upstream, so a bare `git push` only reaches Codeberg — it silently skips GitHub and GitLab. **Always push explicitly to all three remotes** (`git push origin main && git push gitlab main && git push codeberg main`, or equivalent), never rely on the tracked-branch default. GitHub (`origin`) is the primary/canonical remote of the three, even though it isn't the tracking upstream.

**Why:** User caught a push that only reached Codeberg because of the tracking-branch default, and clarified GitHub is the main remote despite not being upstream.