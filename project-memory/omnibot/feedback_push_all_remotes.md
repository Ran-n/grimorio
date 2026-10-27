---
name: feedback-push-all-remotes
description: "When user says \"docpush\", run full workflow: update all doc files, commit, push to all 3 remotes"
metadata:
  node_type: memory
  type: feedback
  originSessionId: cbcc531c-f2e0-46ee-a626-71739bbe42e5
---

When the user says **"docpush"** in the omnibot project, run this full workflow:

1. **Update all documentation files** — find every doc file in the project (e.g. files in `doc/`, any `.md` files, etc.) and update them to accurately reflect the current state of the code.
2. **Run metadatos** — after editing any file in `doc/`, run `python main.py -m` from `d:\Users\{USER}\sw\metadatos` to update the Revised timestamp (see [[feedback-use-metadatos-tool]]).
3. **Commit** — commit the documentation changes to the omnibot repo.
4. **Push to all three remotes** — `origin` (git@github.com:Ran-n/omnibot.git), `gitlab` (git@gitlab.com:Ran-n/omnibot.git), `codeberg` (git@codeberg.org:ran-n/omnibot.git).

**Why:** The user wants a single unambiguous word to trigger the full doc-update + commit + mirror workflow without having to break it into steps. "push" was too generic and easy to miss.

**How to apply:** On "docpush", begin immediately. Do NOT push the `doc/` git repo itself — only push the omnibot remotes (see [[feedback-push-doc-scope]]). Push all three remotes every time.
