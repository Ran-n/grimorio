# Nexum
- [Nexum project](project_nexum.md) — on-chain username identity layer; concept + open questions

# Vitralis

## Project
- [Project spec](project_spec.md) — UX, behaviour, and technical requirements; read at start of each session
- [Toolbar fixed width](feedback_toolbar_size.md) — lock width after init; mode buttons must never resize the window
- [Title always centered](feedback_title_centered.md) — toolbar logo+title must be visually centered; mirror fixed widgets with equal spacers
- [Window UX conventions](feedback_windows_ux.md) — all windows: draggable, ✕ danger_btn 22×22 top-right, Esc closes topmost panel first, buttons greyed out when action unavailable
- [Regression safety](feedback_regression_safety.md) — every change must not break other parts; grep callers, trace signals/styles/translations, name risks before implementing

# Global Preferences

## References
- [Custom License](reference_license.md) — PBL, always use for all projects, source: ran-n/doc/LICENSE
- [Page theme/lang hand-off](reference_page_handoff.md) — rn-preset postMessage convention, trusted origins, stable Pages URLs

## Static Pages
- [Default theme + language](feedback_page_theme_lang.md) — every new page gets breren.com's gruvbox toggle + 8-language picker by default, not a plain single-language page

## Releases
- [Releases + timestamp preservation](feedback_releases.md) — attach all dist artifacts; preserve all original timestamps when editing commits/tags/releases

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

## Workflow
- When auto-approve mode is on, execute all commands and edits immediately without asking for confirmation.
- Never commit unless the user explicitly asks. Prepare the commit message if relevant, but do not run `git commit`.
- [Push means commit then push](feedback_push.md) — "push changes" = commit all pending + push, no confirmation needed
- When pushing, do not ask for permission — commit and push immediately.

## Author
- Name: Ran#
- Email: ran.hash@proton.me

## Feedback
- Always keep docs in sync with code: update docstrings, inline comments, and all README variants (every language version) as part of every code change. Treat it as part of the task, not a separate step. **Why:** stale field names lingered in READMEs after a rename.
- Use the fewest tokens possible without compromising result quality. Lead with the answer, skip preamble, hypotheses, trailing summaries, and filler.
- Always implement industry-standard behavior by default. If a request deviates from standard: do it, but first name the standard and flag the deviation so the user can decide.
- [i18n completeness](feedback_i18n_completeness.md) — after any change touching user-facing strings, update every locale file; no missing keys in any language

## Python Projects
- If `pyproject.toml` contains ruff configuration: run `ruff format <file>` on every modified Python file, then run `ruff check <file>` and fix any reported errors manually in the code until it passes clean. Do not use `--fix` as a shortcut — write correct code. Use the config from `pyproject.toml`.

- [Full sweep trigger](feedback_full_sweep.md) � "full sweep" = autonomous repeating audit-and-fix loop across all levels; don't return control until nothing remains
