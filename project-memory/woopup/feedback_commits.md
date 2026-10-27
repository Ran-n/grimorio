---
name: commit-style
description: "Bracketed title, Conventional Commits body, lowercase imperative; no Co-Authored-By ever"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 53532e8b-f785-4b95-b670-f3695028a191
---

**Title format:** bracket prefix only. No `Co-Authored-By` line ever.

Bracket table:
- `[A]` feat · `[R]` refactor · `[F]` fix · `[D]` docs · `[T]` test · `[C]` chore · `[P]` perf · `[B]` build · `[S]` style

**Body format:** Conventional Commits, lowercase imperative verb.
- Breaking changes: `feat!`/`fix!` in body or `BREAKING CHANGE:` footer.
- Scope is optional.

**Example:**
```
[R] Proxy→ProxyClient
refactor: split into proxy.py / proxy_client.py
```

**Why:** user has a custom commit format used across all repos. No AI attribution in commits.

**How to apply:** on every commit — bracket prefix in title, Conventional Commits in body, never add `Co-Authored-By`.
