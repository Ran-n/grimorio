---
name: Always push to GitHub, GitLab, and Codeberg
description: Every push must reach GitHub, GitLab, and Codeberg; origin only covers the first two, Codeberg needs its own explicit push
type: feedback
originSessionId: 9a3f4409-64b0-40d3-90f1-4416867daca8
modified: 2026-08-04T18:05:49.946Z
---
Always push to GitHub, GitLab, *and* Codeberg on every push. In the `doc` repo, `origin` is configured with two push URLs (GitHub + GitLab) so a single `git push` covers those two — but Codeberg is a separate remote (`codeberg`) that `git push` does **not** touch. Follow every `git push` with `git push codeberg main` (or check `git remote -v` first if unsure of the remote name/branch).

If any remote is missing, create it via SSH URL: `git@github.com:Ran-n/<repo>.git`, `git@gitlab.com:Ran-n/<repo>.git`, `git@codeberg.org:ran-n/<repo>.git` (note Codeberg's lowercase org).

**Why:** All Ran# projects are mirrored across all three platforms (see site footers). Caught Codeberg silently drifting multiple commits behind because `git push` alone was assumed to cover it, per [[project_doc]].

**How to apply:** After every commit, run `git push` then `git push codeberg main` — never assume one push call reaches all three. SSH URLs only — never HTTPS.
