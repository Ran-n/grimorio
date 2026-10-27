# Memory Index

## User
- [Author identity](user_author_identity.md) â€” Ran# (legal: Anxo Ledo) Â· ran.hash@proton.me; pseudonym for public/git, legal name for CONTRIBUTORS Name field

## Session Behaviour
- [Project spec behaviour](feedback_project_behaviour.md) â€” maintain project_spec.md per project; read at session start; flag contradictions; update only on explicit request
- [Universal app behaviours](feedback_universal_behaviours.md) â€” clean shutdown on all quit paths; flag contradictions before implementing
- [Persist all settings](feedback_persist_all_settings.md) — every setting, filter, choice and UI state is remembered between runs; defaults only until the user picks
- [Response style](feedback_response_style.md) â€” answer-first, no preamble/filler/trailing prompts; docs always in sync; cite standard deviations

## Git & Version Control
- [Commit style](feedback_commits.md) â€” bracket title ([A]/[R]/[F]/â€¦), Conventional Commits body, lowercase imperative; no Co-Authored-By
- [Git remote default branch](feedback_git_remotes.md) â€” always use `main`, not `master`, for new repos on GitHub/GitLab/Bitbucket/Codeberg
- [SSH key for git remotes](reference_ssh_keys.md) â€” all GitHub/GitLab/Bitbucket/Codeberg remotes use SSH (`git@`); key: `~/.ssh/gitcommitran`
- [Push semantics](feedback_push.md) â€” never commit/push unless explicitly asked; when asked, do both: stage â†’ commit â†’ push
- [Push workflow](feedback_push_all_remotes.md) â€” "push" = update all doc files â†’ commit â†’ push to `github`, `gitlab`, `codeberg`; Bitbucket dropped 2026-05; create missing remote if needed; SSH only
- [CHANGELOG before committing](feedback_changelog.md) â€” update CHANGELOG.md in the same commit as the changes; only when a commit is requested
- [Version bump workflow](feedback_version_bump.md) â€” "bump" = infer level from git diff, run `uv version --bump <level>`, promote CHANGELOG [Unreleased]; run every deselected pytest marker (live, desktop…) first
- [Release dist attachments](feedback_releases.md) â€” build all dist formats (.exe, .whl, .tar.gz) and attach to tag; preserve original timestamps on history rewrites

## Python Projects
- [Preferred stack](reference_preferred_stack.md) â€” default for new apps: uv, FastAPI + SQLAlchemy/Alembic (SQLiteâ†’Postgres), Flet frontend, pytest; backend/frontend as separate repos
- [pyproject.toml scaffold](reference_pyproject_scaffold.md) â€” minimum required structure: hatchling build, ruff with lint+format sections, line-length 120, preview=true

## Repository Setup
- [New repo scaffold](feedback_new_repo_scaffold.md) â€” LICENSE (PBL), CHANGELOG, CONTRIBUTING, README, CONTRIBUTORS required before first commit
- [Custom License (PBL)](reference_license.md) â€” always use PayBack License; fetch from d:\Users\{USER}\sw\doc\LICENSE or GitLab/GitHub raw; never MIT/Apache
- [CONTRIBUTING.md layout](reference_contributing_layout.md) â€” standard section order for all projects; create if missing
- [CONTRIBUTORS file layout](reference_contributors_layout.md) â€” exact PBL v2.0 clause 18 format: SUMMARY table + DETAILS block with Pseudonym/Name/Role/Email/GPG/Ownership/Revenue fields
- [Site organization](feedback_site_organization.md) â€” served files grouped under one dedicated folder (e.g. `public/`), separate from repo-meta files; add a build/deploy step if the host can't serve that subfolder natively

## Workflow
- [Apply global memory proactively](feedback_apply_global_memory_proactively.md) â€” scan MEMORY.md before every task; apply matching rules without waiting to be corrected
- [Project memory mirror](feedback_project_memory_mirror.md) â€” byte-copy global memory into project dir; never modify mirrored files; project-specific files sit alongside but are not indexed in MEMORY.md
- [Never ask for permission](feedback_no_permission_prompts.md) â€” just act; exceptions: user said to ask, or "ask before edits" mode is on
- [Fix errors and continue](feedback_fix_errors_and_continue.md) — on a failed step or hook refusal, fix it and finish the workflow; never stop at the error
- [Always use AskUserQuestion](feedback_ask_user_question.md) â€” use AskUserQuestion tool for all questions and choices, including mid-edit options; never plain-text questions

## Tools
- [Hashing default](feedback_hashing.md) â€” always use BLAKE3; "hash" means blake3 unless specified; use platform-appropriate tool
- [APK Telegram delivery rule](feedback_apk_telegram_delivery.md) â€” xoutaim-frontend: build+send APK via Telegram bot only on Remote Control; otherwise normal file delivery
- [Flet split-APK staleness](feedback_flet_split_apk_staleness.md) â€” `flet build apk` w/o `--split-per-abi` silently ships stale per-ABI splits; always pass the flag, clean-rebuild if unsure, verify by unzipping app.zip before shipping
- [Flet SnackBar quirks](feedback_flet_snackbar_quirks.md) â€” SnackBar ignores custom ColorScheme tokens + ignores in-place update() after a while (dismiss+recreate instead); also: killing flet.exe â‰  killing the python server, verify process state before trusting a "restart"
- [Flet wrap + expand grey box](feedback_flet_wrap_expand.md) — `Row(wrap=True)` with an `expand` child renders a silent grey box in the real window (widget tests pass); use `tight` children or drop `wrap`

## Credentials & Tokens
- [Codeberg API token](reference_codeberg_token.md) â€” Forgejo REST API token for `Ran-n`; use to create repos via `https://codeberg.org/api/v1/`
- [Telegram bot token](reference_telegram_bot_token.md) â€” Bot API token for sending messages/files; needs target chat ID first (message the bot once, then `getUpdates`)

## Workflow Triggers
- [Full sweep trigger](feedback_full_sweep.md) â€” "full sweep" = autonomous repeating audit-and-fix loop across all levels; don't return control until nothing remains
- [TODO backlog trigger](feedback_todo_trigger.md) — "todo: …" or /todo … = add a self-contained item to TODO.md (creates it if missing); "do todo N" = implement it, then delete it

## Code Quality
- [Database BCNF requirement](feedback_database_bcnf.md) â€” every relational schema must be real BCNF, not just informally "normalized"; check candidate-key dependencies, document exceptions
- [No silent failure](feedback_no_silent_failure.md) â€” always surface errors explicitly; never swallow exceptions, empty catch blocks, or silent promise rejections
- [Clean Code, SOLID + Design Patterns](feedback_clean_code.md) â€” all SOLID rules, all GoF patterns, DRY/YAGNI/KISS, DDD/CQRS/hexagonal when scale justifies; DRY is a hard rule â€” never invoke "no premature abstraction"/YAGNI to skip extracting shared code
- [Logging requirement](feedback_logging.md) â€” every app needs structured logging: named loggers, INFO/WARNING/ERROR levels, no print(); treat missing logging as a defect
- [Tests requirement](feedback_tests.md) — every change gets tests in every applicable type (checklist: unit, integration, property, regression, golden files, migrations step-by-step, entry points, quit paths, widget, rendered real-app UI + reviewed baselines in the longest locale); real DB; coverage gate via `pytest --cov`; audit procedure
- [Regression safety](feedback_regression_safety.md) â€” grep callers before touching shared code; name ripple risks; update all call sites on signature changes
- [i18n completeness](feedback_i18n_completeness.md) â€” after any user-facing string change, update every locale file; no missing keys in any language
- [File headers (metadata)](feedback_file_headers.md) â€” `metadata -v` to check, `-c` if empty, `-m` after every edit; never hand-write Revised; supported: .py .pyw .sh .bash .rs .md
- [Python linting (ruff)](feedback_python_projects.md) â€” ruff format then ruff check on every modified .py file; fix errors manually, never --fix
- [No future imports](feedback_no_future_imports.md) â€” never add `from __future__` imports; remove existing ones unless removal breaks compilation
- [Source tree organization](feedback_source_organization.md) â€” CCP/CRP/REP + ADP/SDP/SAP, package-by-feature vs by-layer, Screaming Architecture, hexagonal; fills the gap SOLID leaves for file/folder placement

## API Design
- [Stripe-style expand pattern](feedback_stripe_expand_pattern.md) â€” FK fields are int by default, expanded object with ?expand=field; no *_fk in responses; image_fk+image_path excepted
- [Bulk endpoints over N-call loops](feedback_bulk_endpoints.md) â€” before looping a per-item API call N times, check for/add a bulk endpoint; batch the write AND the post-write recompute, not just the write

## UI
- [Disabled buttons visually greyed out](feedback_ui_disabled_buttons.md) â€” disabled buttons must appear dimmed, never identical to enabled state
- [Inline editing preference](feedback_ui_inline_editing.md) â€” always design editable UI with in-place editing; no dialogs/modals unless unavoidable
- [CTA hierarchy](feedback_ui_cta_hierarchy.md) â€” primary action big/own row, secondary links (source mirrors etc.) small/below; use each platform's real logo, never a generic placeholder icon

## Project-specific
- [UI tests never hijack input](feedback_ui_tests_no_input_hijack.md) — drive the window with posted messages + PrintWindow; never move the real mouse/keyboard
- [Map buttons open the in-app map](feedback_map_buttons_in_app.md) â€” bounty_board: every Map button focuses the app's Map tab; Google Maps only as no-coordinates fallback
- [TCG+ API probing](project_tcg_plus_probing.md) — bursts of write probes trip a 403 firewall; website's cancel route is a 404 since 2026-10; capture the real call instead
- [Telegram token location](project_telegram_token_location.md) — app's bot token is in Windows Credential Manager (`bounty_board`/`telegram_token`), never settings.json
- [Desktop tests vs parallel sessions](project_desktop_tests_parallel.md) — one shared harness window title: concurrent `-m desktop` runs close each other's windows; rerun when no test window is open, don't "fix" the tests
