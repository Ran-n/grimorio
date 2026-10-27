---
name: Always push to all remotes
description: "push" = full workflow — update all doc files → commit → push to GitHub, GitLab, and Codeberg; create missing remote first; SSH only
metadata:
  type: feedback
---

When the user says **"push"**, run this full workflow:

1. **Update all documentation files** — find every doc file in the project (files in `doc/`, any `.md` files, etc.) and update them to accurately reflect the current state of the code.
2. **Run file header tool** — after editing any doc file, update its Revised timestamp per the file headers rule (`metadata -m`; see [[feedback-file-headers]]).
3. **Commit** — commit all documentation changes.
4. **Push to all three remotes** — GitHub, GitLab, and Codeberg via SSH. If any remote does not exist, create it first.

Remote URL patterns:
- GitHub: `git@github.com:Ran-n/<repo>.git`
- GitLab: `git@gitlab.com:Ran-n/<repo>.git`
- Codeberg: `git@codeberg.org:ran-n/<repo>.git`

**Why:** Bitbucket dropped 2026-05. All Ran# projects mirror to three platforms. "push" is a single word to trigger the full doc-update + commit + mirror workflow.

**How to apply:** Run `git remote -v` first to get actual remote names — never assume names. SSH URLs only, never HTTPS. Never push the `doc/` git repo itself — only push the project's own remotes.