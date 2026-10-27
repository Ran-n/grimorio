---
name: global-preferences
description: "all cross-project rules mirrored from global memory — commit style, file headers, workflow, code quality, UI, releases, remotes"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9b85014c-78b7-4b1b-84ef-5d9d99e1d30e
---

## Author
Name: **Ran#** · Email: `ran.hash@proton.me`
Use for git config, CONTRIBUTORS, README attribution, and any name/email context.

## License
Always use the PayBack License (PBL). Fetch in this order (stop at first success):
1. `d:\Users\{USER}\sw\doc\LICENSE`
2. `https://gitlab.com/Ran-n/doc/-/raw/main/LICENSE`
3. `https://raw.githubusercontent.com/ran-n/doc/main/LICENSE`

- Never use MIT, Apache, or any other license
- In READMEs link as `[PayBack License (PBL)](LICENSE)` (no hardcoded version number)
- Copy verbatim; do not edit
- **Do NOT read/parse the license file contents.** Use the Bash tool to copy it directly: `cp "d:/Users/{USER}/sw/doc/LICENSE" LICENSE` (or PowerShell: `Copy-Item`). Never read it line by line or reproduce it via Write/Edit.

## Commits
- No `Co-Authored-By` lines ever.
- Title: bracket prefix only — do NOT repeat the type word (e.g. `[F] Proxy timeout`, not `[F] fix: Proxy timeout`).
- Body: Conventional Commits lowercase imperative. Scope optional.
- Brackets: `[A]` feat · `[R]` refactor · `[F]` fix · `[D]` docs · `[T]` test · `[C]` chore · `[P]` perf · `[B]` build · `[S]` style
- Breaking changes: `feat!`/`fix!` in body or `BREAKING CHANGE:` footer.
- Never commit unless explicitly asked.

## CHANGELOG
- Update CHANGELOG.md only when a commit is requested — not mid-session.
- Include CHANGELOG update in the same commit as the changes.
- Format: Keep a Changelog style; newest at top; `[Unreleased]` → `## [x.y.z] — YYYY-MM-DD` on release.
- Group under: **Added**, **Changed**, **Deprecated**, **Removed**, **Fixed**, **Security**.
- Past tense, one bullet per logical change, no trailing period, no filler.

## File Headers
Run `python C:/Users/{USER}/.claude/memory/metadatos_v0.2.1.py <flag> <file>` on every edit.
- `-c` add header (then verify `Created:` matches filesystem `ctime`; correct if off)
- `-m` update `Revised:` after every save
- `-v` view metadata
- Supported: `.py .pyw .sh .bash .rs .md` — skip others, inform user
- Never write the `Revised:` timestamp by hand.

## Push / Remotes
- Never commit or push unless explicitly asked. When asked, do both: stage → commit → push without re-asking.
- Always push to both `github` and `gitlab` remotes. Create either if missing, using SSH URLs.
  - `git@github.com:Ran-n/<repo>.git` / `git@gitlab.com:Ran-n/<repo>.git`
- All remotes use SSH, never HTTPS. SSH config (`~/.ssh/gitcommitran`) handles key selection automatically.
- Default branch for new repos: `main` (rename from `master` before first push if needed).

## Releases
- Build all dist artifacts (`.exe`, `.whl`, `.tar.gz`) and attach to the release tag.
- When editing old commits/tags/releases: preserve ALL original metadata — author date, committer date, tag date, tagger identity, and message. Use `GIT_AUTHOR_DATE`/`GIT_COMMITTER_DATE` for commits; recreate tag objects with original date/tagger.

## New Repo Scaffold
Every new repo must include before first commit (no need to ask):
- `LICENSE` — PBL (fetch as above)
- `CHANGELOG.md` — Keep a Changelog format
- `CONTRIBUTING.md` — standard section layout (see global memory `reference_contributing_layout.md`)
- `README.md` — must have a License section linking as `[PayBack License (PBL)](LICENSE)`
- `CONTRIBUTORS` — contributor list file

## Workflow
- Never ask for permission or confirmation before taking actions — just act.
  - Exception: do not commit or push unless explicitly requested.
  - Exception: user has said to ask first in the current conversation, or "ask before edits" mode is on.
- Use the `AskUserQuestion` tool for **all** questions and choices — never pose questions as plain prose.

## Response Style
- Lead with the answer — no preamble, no trailing summaries, no filler.
- Fewest tokens without losing quality.
- Default to industry-standard behaviour; flag deviations before implementing.
- Keep all docs (docstrings, comments, all README language variants) in sync with every code change.

## Python Projects
- If `pyproject.toml` has ruff config: after every file edit run `ruff format <file>`, then `ruff check <file>`. Fix errors manually — never `--fix`.

## Code Quality (all projects)
- Clean Code: self-documenting names, guard clauses, no magic numbers, no flag parameters, dead code deleted, no `print` debugging in commits.
- SOLID: single responsibility, open/closed, Liskov, interface segregation, dependency inversion.
- Apply GoF design patterns when structure calls for them; never force them. Scripts/small tools: only what reduces complexity.
- DRY, YAGNI, KISS, Law of Demeter, composition over inheritance, fail fast, separation of concerns always.
- No file over ~200 lines; no function over ~20 lines without strong reason.
- Proactively structure new code this way; call out violations in existing code before touching them.

## UI
- Disabled buttons must be visually distinct (greyed-out background + dimmed label/icon). Never leave them identical to enabled state.

## Regression Safety
- Before editing any shared module, grep all files that import or reference it.
- If touching a shared interface/signal/schema, verify all call sites after the change.
- Name any unintended side-effect risk before proceeding.
- Never remove, rename, or change a function/class signature without updating every caller.

## i18n
- After any change adding, removing, or renaming user-facing strings: update every locale/translation file so no key is missing in any language.

## Universal App Behaviour
- All threads, background workers, and child processes must be cleanly stopped on every quit path (button, shortcut, OS close, tray).
- If a request contradicts an established behaviour, flag it and ask which intent to keep before implementing.
