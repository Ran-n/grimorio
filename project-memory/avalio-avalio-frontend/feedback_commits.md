---
name: Commit Style
description: Bracket-style commit format, no co-author lines
type: feedback
originSessionId: e132952d-97d2-4a9b-a700-0c502415f387
---
Never add `Co-Authored-By` lines. All commits are solely the user's.

Use bracket abbreviation as title, Conventional Commits body:
- `[A]` → `feat`, `[R]` → `refactor`, `[F]` → `fix`, `[D]` → `docs`
- `[T]` → `test`, `[C]` → `chore`, `[P]` → `perf`, `[B]` → `build`, `[S]` → `style`
- Do NOT repeat the type word in the title
- Body lines: lowercase, imperative mood
- Breaking changes: `feat!`/`fix!` in body or `BREAKING CHANGE:` footer
- Scope optional: `fix(proxy): ...`

Example:
```
[R] Proxy→ProxyClient, ProxyDTO→Proxy

refactor: split into proxy.py / proxy_client.py
fix: refresh_header now guarantees a different value
```

**Why:** user's established convention across all projects.
**How to apply:** every commit in this project.
