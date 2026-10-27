---
name: commit_style
description: Commit message format and bracket convention for this user
type: feedback
---

Use bracket abbreviation as the title, Conventional Commits keywords in the body. Never add `Co-Authored-By` lines.

Allowed brackets (never invent others):
- `[A]` → `feat`
- `[R]` → `refactor`
- `[F]` → `fix`
- `[D]` → `docs`
- `[T]` → `test`
- `[C]` → `chore`
- `[P]` → `perf`
- `[B]` → `build`
- `[S]` → `style`

Breaking changes: use `feat!`/`fix!` in body, or footer `BREAKING CHANGE: <description>`.
Scope is optional: `fix(proxy): ...`
Body lines: lowercase, imperative mood.

Example:
```
[R] Proxy→ProxyClient, ProxyDTO→Proxy

refactor: split into proxy.py / proxy_client.py
fix: refresh_header now guarantees a different value
```

**Why:** User's personal convention, do NOT repeat the bracket type word in the title.
**How to apply:** Every commit in this repo must follow this format exactly.
