---
name: commit_style
description: Commit format rules — bracket title, Conventional Commits body, no co-author lines
type: feedback
---

Commit format:
- Title: bracket abbreviation only, no co-author lines
- Body: Conventional Commits style, lowercase imperative mood
- Allowed brackets: `[A]`=feat, `[R]`=refactor, `[F]`=fix, `[D]`=docs, `[T]`=test, `[C]`=chore, `[P]`=perf, `[B]`=build, `[S]`=style
- Breaking changes: `feat!`/`fix!` in body or footer `BREAKING CHANGE: <description>`
- Scope optional: `fix(proxy): ...`
- Never invent new bracket types
- NEVER add `Co-Authored-By` lines

**Why:** user's personal commit style convention.

**How to apply:** Use on every commit in this project.

Example:
```
[R] Proxy→ProxyClient, ProxyDTO→Proxy

refactor: split into proxy.py / proxy_client.py
fix: refresh_header now guarantees a different value
```
