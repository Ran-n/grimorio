# Memory

## Author
- Name: Ran#
- Email: ran.hash@proton.me

## Commits
- Never add co-author lines (`Co-Authored-By`). All commits are solely the user's.
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
- Breaking changes: `feat!`/`fix!` in body, or footer `BREAKING CHANGE: <description>`
- Scope optional: `fix(proxy): ...`
- Body lines: lowercase, imperative mood
- Example:
  ```
  [R] Proxy→ProxyClient, ProxyDTO→Proxy

  refactor: split into proxy.py / proxy_client.py
  fix: refresh_header now guarantees a different value
  ```

## File Headers
Use `python C:/Users/{USER}/.claude/memory/metadatos_v0.2.1.py <flag> <file>`.
Source: https://github.com/ran-n/metadatos — update the copy when the version changes.

- Before editing a file, check whether it already has a metadata header (look for `// ---` or `# ---` at the top)
- If no header exists, run `-c` to create one first, then `-m` to update the revised timestamp
- On every file edit, run with `-m` to update the `Revised:` timestamp
- After `-c`, verify the `Created:` timestamp matches the filesystem creation time; correct it manually if needed
- If asked to view metadata, run with `-v`
- Supported types: `.py`, `.pyw`, `.sh`, `.bash`, `.rs`, `.md` — for any other type, skip and inform the user

## Releases
When editing, resigning, amending, or modifying old commits, tags, or releases in any way, preserve ALL original metadata: author date, committer date, tag date, tagger identity, and message. Use `GIT_AUTHOR_DATE`/`GIT_COMMITTER_DATE` for commits; recreate tag objects with original date/tagger. Goal: history ordering and timestamps look unchanged. When creating a new release, build all dist artifacts and attach to the tag.

## Docs Sync
- Always keep docs in sync with code: update docstrings, inline comments, and all README variants (every language version) as part of every code change. Treat it as part of the task, not a separate step. **Why:** stale field names lingered in READMEs after a rename.

## Workflow
- When auto-approve mode is on, execute all commands and edits immediately without asking for confirmation.
- Never commit unless the user explicitly asks. Prepare the commit message if relevant, but do not run `git commit`.

## Docs Location
- Do not create standalone spec or documentation files at the repo root. Use the README and a `docs/` folder within each repo. For multi-repo projects, split the relevant specs between the repos where they belong.

## Python Projects
- If `pyproject.toml` contains ruff configuration: run `ruff format <file>` on every modified Python file, then run `ruff check <file>` and fix any reported errors manually in the code until it passes clean. Do not use `--fix` as a shortcut — write correct code. Use the config from `pyproject.toml`.

## Mirrored Memory
- This memory is always kept identical to `ximrato-app` memory. Any change made to one must be made to the other at the same time.

## Cross-Project Sync
- `ximrato-app` (frontend) and `ximrato-server` (backend) are a pair. When making changes to one, always consider whether the other needs a corresponding update (e.g. API contract changes, shared types, endpoint additions/removals, auth flow changes). If it does, apply it in the same task.

## Database Design
- See [feedback_db_normalization.md](feedback_db_normalization.md)

## Response Style
- See [feedback_response_style.md](feedback_response_style.md)

## Industry Standard
- See [feedback_industry_standard.md](feedback_industry_standard.md)

## Project
- See [project_ximrato.md](project_ximrato.md)

- [Full sweep trigger](feedback_full_sweep.md) � "full sweep" = autonomous repeating audit-and-fix loop across all levels; don't return control until nothing remains
