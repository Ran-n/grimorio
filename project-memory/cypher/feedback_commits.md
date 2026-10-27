---
name: Commit style
description: Bracket-title commit format with Conventional Commits body, no co-author lines
type: feedback
originSessionId: 27a28edc-919c-456d-bfa9-7b1db3608dab
---
Use bracket abbreviation as title (do NOT repeat the type word in the title). Conventional Commits in the body. Never add `Co-Authored-By` lines — all commits are solely the user's.

Allowed brackets:
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
Scope is optional: `fix(proxy): ...`. Body lines are lowercase, imperative mood.

Example:
```
[R] Proxy→ProxyClient, ProxyDTO→Proxy

refactor: split into proxy.py / proxy_client.py
fix: refresh_header now guarantees a different value
```

**Why:** user's established commit convention across all projects.
**How to apply:** every commit in this repo.
