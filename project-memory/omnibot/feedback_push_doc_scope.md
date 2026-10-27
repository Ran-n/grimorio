---
name: ""
metadata: 
  node_type: memory
  originSessionId: f7b3e4d5-dfcd-4cb7-b7f8-cbab37ab05a9
---

When the user says "docpush" or "update doc and docpush," the push applies only to the omnibot remotes (origin, gitlab, codeberg). Do NOT commit or push to the `doc/` git repo at `D:\Users\{USER}\sw\doc\.git`.

**Why:** The doc directory is a separate git repo, but pushing it is not what the user intends when they say "push" in the context of an omnibot task.

**How to apply:** After editing files in `doc/`, run metadatos (`python main.py -m`), then push only the omnibot remotes. Never `git commit` or `git push` inside the doc repo unless explicitly asked.
