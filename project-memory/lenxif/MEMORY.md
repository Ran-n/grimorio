# Global Preferences

## Meta
- [Project spec behaviour](feedback_project_behaviour.md) — maintain `project_spec.md` per project; read at session start; flag contradictions; update only on explicit user request
- [Universal app behaviours](feedback_universal_behaviours.md) — clean shutdown on all quit paths; flag contradictions before implementing

## Commits
No `Co-Authored-By`. Title: bracket only. Body: Conventional Commits, lowercase imperative.
Brackets: `[A]` feat · `[R]` refactor · `[F]` fix · `[D]` docs · `[T]` test · `[C]` chore · `[P]` perf · `[B]` build · `[S]` style
Breaking: `feat!`/`fix!` in body or `BREAKING CHANGE:` footer. Scope optional.
Example: `[R] Proxy→ProxyClient` / body: `refactor: split into proxy.py / proxy_client.py`

## File Headers
`python C:/Users/{USER}/.claude/memory/metadatos_v0.2.1.py <flag> <file>` — update copy when version changes.
Check for `// ---` or `# ---` before editing. No header → `-c` then verify `Created:` matches filesystem; correct if off. Every edit → `-m`. View → `-v`.
Supported: `.py .pyw .sh .bash .rs .md` — skip other types, inform user.
- [Metadata header order](feedback_metadata_order.md) — check for header first; run `-c` then `-m` if missing, else just `-m`

## Releases
- [Attach all dist artifacts](feedback_releases.md) — build all dist formats and attach to the release tag

## Git
- [Remote creation uses main](feedback_git_remotes.md) — GitHub/GitLab remotes must use `main` as default branch, not `master`
- SSH key for git remotes — all GitHub/GitLab remotes use SSH (`git@`); key: `~/.ssh/gitcommitran` (see global memory)

## Workflow
- [Never ask for permission](feedback_no_permission_prompts.md) — just act; only exceptions: user explicitly said to ask, or "ask before edits" mode is on.
- Auto-approve: execute immediately, no confirmation.
- Never commit unless explicitly asked.
- [Push = commit + push to all remotes](feedback_push.md) — stage, commit, push to all remotes simultaneously; no confirmation. Current remotes: GitHub (`git@github.com:Ran-n/lenxif.git`), GitLab (`git@gitlab.com:Ran-n/lenxif.git`).

## Author
Ran# · ran.hash@proton.me

## Feedback
- Keep all docs (docstrings, comments, all README language variants) in sync with every code change. Part of the task, not a separate step.
- Fewest tokens possible without losing quality. Lead with the answer — no preamble, no trailing summaries. No filler phrases ("Great question", "Sure!", "Let me...", "I'll now..."). No restating the task before acting. No trailing "What would you like next?" prompts.
- Default to industry-standard behaviour. If deviating: name the standard, flag the deviation, then implement.
- [i18n completeness](feedback_i18n_completeness.md) — after any change touching user-facing strings, update every locale file; no missing keys in any language

## UI
- [Disabled buttons visually greyed out](feedback_ui_disabled_buttons.md) — disabled buttons must always look visually distinct (dimmed), never identical to enabled

## Code Quality
- [Clean Code, SOLID + Design Patterns](feedback_clean_code.md) — structure, all SOLID rules, all GoF patterns, DRY/YAGNI/KISS, DDD/CQRS/hexagonal when scale justifies; correct wrong pattern suggestions
- [Regression safety](feedback_regression_safety.md) — changes must not silently break unrelated parts; grep callers, name ripple risks before implementing; intentional changes are exempt

## References
- [Custom License](reference_license.md) — PBL always; fetch latest from source; never MIT/Apache
- [Project spec behaviour](feedback_project_behaviour.md) — per-project spec files
- [lenxif project spec](project_spec.md) — UX, behaviour, and technical requirements for this project

## Python Projects
`pyproject.toml` has ruff config → `ruff format <file>` then `ruff check <file>` after every modified file. Fix errors manually — no `--fix`.

- [Full sweep trigger](feedback_full_sweep.md) � "full sweep" = autonomous repeating audit-and-fix loop across all levels; don't return control until nothing remains
