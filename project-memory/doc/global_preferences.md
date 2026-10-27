---
name: Global Preferences
description: User's global git, file header, workflow, author, feedback, and Python project preferences
type: user
originSessionId: 7132f3cc-7909-41b4-9120-7c48eef359da
---
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
Source: https://github.com/ran-n/metadatos — update the copy when the version changes.

- Before editing a file, check whether it already has a metadata header (look for `// ---` or `# ---` at the top)
- If no header exists, run `-c` to create one first, then `-m` to update the revised timestamp
- On every file edit, run with `-m` to update the `Revised:` timestamp
- After `-c`, verify the `Created:` timestamp matches the filesystem creation time; correct it manually if needed
- If asked to view metadata, run with `-v`
- Supported types: `.py`, `.pyw`, `.sh`, `.bash`, `.rs`, `.md` — for any other type, skip and inform the user

## Releases
When editing, resigning, amending, or modifying old commits, tags, or releases in any way, preserve ALL original metadata: author date, committer date, tag date, tagger identity, and message. Use `GIT_AUTHOR_DATE`/`GIT_COMMITTER_DATE` for commits; recreate tag objects with original date/tagger. Goal: history ordering and timestamps look unchanged. When creating a new release, build all dist artifacts and attach to the tag.

## Workflow
- When auto-approve mode is on, execute all commands and edits immediately without asking for confirmation.
- Never commit unless the user explicitly asks. Prepare the commit message if relevant, but do not run `git commit`.

## Author
- Name: Ran#
- Email: ran.hash@proton.me

## Feedback
- Always keep docs in sync with code: update docstrings, inline comments, and all README variants (every language version) as part of every code change. Treat it as part of the task, not a separate step. **Why:** stale field names lingered in READMEs after a rename.
- Use the fewest tokens possible without compromising result quality. Lead with the answer, skip preamble, hypotheses, trailing summaries, and filler.
- Always implement industry-standard behavior by default. If a request deviates from standard: do it, but first name the standard and flag the deviation so the user can decide.

## Writing Style
- All generated text must read as naturally human-written. Avoid patterns that signal AI authorship: no formulaic openers ("Certainly!", "Of course!", "Great question!"), no symmetric bullet triads, no hedging stacks ("it's worth noting that…"), no overly balanced pros/cons structure, no unnaturally even paragraph lengths, no transitional meta-commentary ("In conclusion…", "To summarize…"). Vary sentence rhythm, use direct language, and let the content's own logic drive the structure.

## Python Projects
- If `pyproject.toml` contains ruff configuration: run `ruff format <file>` on every modified Python file, then run `ruff check <file>` and fix any reported errors manually in the code until it passes clean. Do not use `--fix` as a shortcut — write correct code. Use the config from `pyproject.toml`.
