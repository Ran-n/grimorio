# Global Preferences

## Commits
- Never add co-author lines (no `Co-Authored-By`). All commits are solely the user's.
- Commit style: bracket abbreviation as title (do NOT repeat the type word in the title), Conventional Commits in the body.
- Allowed brackets — use only these, never invent others:
  - `[A]` → `feat`
  - `[R]` → `refactor`
  - `[F]` → `fix`
  - `[D]` → `docs`
  - `[T]` → `test`
  - `[C]` → `chore`
  - `[P]` → `perf`
  - `[B]` → `build`
  - `[S]` → `style`
- Breaking changes: use `feat!`/`fix!` in body, or footer `BREAKING CHANGE: <description>`
- Scope is optional: `fix(proxy): ...`
- Body lines are lowercase, imperative mood
- Example:
  ```
  [R] Proxy→ProxyClient, ProxyDTO→Proxy

  refactor: split into proxy.py / proxy_client.py
  fix: refresh_header now guarantees a different value
  ```

## File Headers
Use `python C:/Users/{USER}/.claude/memory/metadatos_v0.2.1.py <flag> <file>`.
- Before editing a file, check whether it already has a metadata header (look for `// ---` or `# ---` at the top)
- If no header exists, run `-c` to create one first, then `-m` to update the revised timestamp
- On every file edit, run with `-m` to update the `Revised:` timestamp
- After `-c`, verify the `Created:` timestamp matches the filesystem creation time; correct it manually if needed
- If asked to view metadata, run with `-v`
- Supported types: `.py`, `.pyw`, `.sh`, `.bash`, `.rs`, `.md` — for any other type, skip and inform the user

## Releases
When editing, resigning, amending, or modifying old commits, tags, or releases in any way, preserve ALL original metadata: author date, committer date, tag date, tagger identity, and message. Use `GIT_AUTHOR_DATE`/`GIT_COMMITTER_DATE` for commits; recreate tag objects with original date/tagger. Goal: history ordering and timestamps look unchanged.

## Workflow
- When auto-approve mode is on, execute all commands and edits immediately without asking for confirmation.

## Author
- Name: Ran#
- Email: ran.hash@proton.me

---

# Project: conexions

## Stack
- Python 3.10+
- Tests: pytest (converted from unittest)
- Build: setuptools, pyproject.toml

## Feedback
- [Keep docs and comments in sync](feedback_docs_sync.md) — always update docstrings, inline comments, and both READMEs (EN + GL) as part of every code change

- [Full sweep trigger](feedback_full_sweep.md) � "full sweep" = autonomous repeating audit-and-fix loop across all levels; don't return control until nothing remains
