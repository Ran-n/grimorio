# Memory Index

## User
- [Author identity](user_author_identity.md) — Ran# (legal: Anxo Ledo) · ran.hash@proton.me; pseudonym for public/git, legal name for CONTRIBUTORS Name field

## Session Behaviour
- [Project spec behaviour](feedback_project_behaviour.md) — maintain project_spec.md per project; read at session start; flag contradictions; update only on explicit request
- [Universal app behaviours](feedback_universal_behaviours.md) — clean shutdown on all quit paths; flag contradictions before implementing
- [Response style](feedback_response_style.md) — answer-first, no preamble/filler; docs in sync; cite deviations; hard 100-word cap always

## Git & Version Control
- [Commit style](feedback_commits.md) — bracket title ([A]/[R]/[F]/…), Conventional Commits body, lowercase imperative; no Co-Authored-By
- [Git remote default branch](feedback_git_remotes.md) — always use `main`, not `master`, for new repos on GitHub/GitLab/Bitbucket/Codeberg
- [SSH key for git remotes](reference_ssh_keys.md) — all GitHub/GitLab/Bitbucket/Codeberg remotes use SSH (`git@`); key: `~/.ssh/gitcommitran`
- [Push semantics](feedback_push.md) — never commit/push unless explicitly asked; when asked, do both: stage → commit → push
- [Push workflow](feedback_push_all_remotes.md) — "push" = update all doc files → commit → push to `github`, `gitlab`, `codeberg`; Bitbucket dropped 2026-05; create missing remote if needed; SSH only
- [CHANGELOG before committing](feedback_changelog.md) — update CHANGELOG.md in the same commit as the changes; only when a commit is requested
- [Version bump workflow](feedback_version_bump.md) — "bump" = infer level from git diff, run `uv version --bump <level>` per repo, promote CHANGELOG [Unreleased]; run every deselected pytest marker (live, desktop…) first
- [Auto version-bump hook](feedback_auto_version_bump.md) — Stop hook in both renar repos auto-bumps patch/minor after each turn's changes; major stays manual
- [Release dist attachments](feedback_releases.md) — build all dist formats (.exe, .whl, .tar.gz) and attach to tag; preserve original timestamps on history rewrites

## Python Projects
- [pyproject.toml scaffold](reference_pyproject_scaffold.md) — minimum required structure: hatchling build, ruff with lint+format sections, line-length 120, preview=true

## Repository Setup
- [New repo scaffold](feedback_new_repo_scaffold.md) — LICENSE (PBL), CHANGELOG, CONTRIBUTING, README, CONTRIBUTORS required before first commit
- [Custom License (PBL)](reference_license.md) — always use PayBack License; fetch from d:\Users\{USER}\sw\doc\LICENSE or GitLab/GitHub raw; never MIT/Apache
- [CONTRIBUTING.md layout](reference_contributing_layout.md) — standard section order for all projects; create if missing
- [CONTRIBUTORS file layout](reference_contributors_layout.md) — exact PBL v2.0 clause 18 format: SUMMARY table + DETAILS block with Pseudonym/Name/Role/Email/GPG/Ownership/Revenue fields

## Workflow
- [Apply global memory proactively](feedback_apply_global_memory_proactively.md) — scan MEMORY.md before every task; apply matching rules without waiting to be corrected
- [Project memory mirror](feedback_project_memory_mirror.md) — byte-copy global memory into project dir; never modify mirrored files; project-specific files sit alongside but are not indexed in MEMORY.md
- [Never ask for permission](feedback_no_permission_prompts.md) — just act; exceptions: user said to ask, or "ask before edits" mode is on
- [Don't suggest restart as first fix](feedback_dont_suggest_restart_first.md) — never lead with "restart the backend" when debugging, especially once user says the issue is long-standing; dig into actual code path instead
- [Always use AskUserQuestion](feedback_ask_user_question.md) — use AskUserQuestion tool for all questions and choices, including mid-edit options; never plain-text questions
- [Check global memory before claiming a gap](feedback_check_global_memory_before_claiming_gap.md) — grep global memory, not just project-local, before telling the user a capability is unavailable
- [Verify after every change](feedback_verify_after_every_change.md) — after any change, run tests AND actually launch/exercise the app; unit tests passing isn't enough (missed an import-cost + layout regression)

## Tools
- [Hashing default](feedback_hashing.md) — always use BLAKE3; "hash" means blake3 unless specified; use platform-appropriate tool
- [Flet SnackBar quirks (global)](feedback_flet_snackbar_quirks.md) — SnackBar ignores custom ColorScheme tokens + ignores in-place update() after a while (dismiss+recreate instead); also: killing flet.exe ≠ killing the python server, verify process state before trusting a "restart"

## Credentials & Tokens
- [Codeberg API token](reference_codeberg_token.md) — Forgejo REST API token for `Ran-n`; use to create repos via `https://codeberg.org/api/v1/`
- [Cloudflare API token (renar.app)](reference_cloudflare_token.md) — DNS-edit token scoped to renar.app zone only; use for TXT/DKIM/DMARC/BIMI records

## Workflow Triggers
- [dbp trigger](feedback_dbp_trigger.md) — "dbp" (plain text, like "hk") or `/dbp` = update docs → bump if needed → commit → push all remotes, both renar repos
- [Full sweep trigger](feedback_full_sweep.md) — "full sweep" = autonomous repeating audit-and-fix loop across all levels; don't return control until nothing remains
- [Housekeeping trigger](feedback_housekeeping_trigger.md) — "house keep"/"hk" = docs sync + memory sweep + verify (not redo) file headers/lint/tests + i18n check, run against the session's changes

## Code Quality
- [Database BCNF requirement](feedback_database_bcnf.md) — every relational schema must be real BCNF, not just informally "normalized"; check candidate-key dependencies, document exceptions
- [No silent failure](feedback_no_silent_failure.md) — always surface errors explicitly; never swallow exceptions, empty catch blocks, or silent promise rejections
- [Clean Code, SOLID + Design Patterns](feedback_clean_code.md) — all SOLID rules, all GoF patterns, DRY/YAGNI/KISS, DDD/CQRS/hexagonal when scale justifies; DRY is a hard rule — never invoke "no premature abstraction"/YAGNI to skip extracting shared code
- [Logging requirement](feedback_logging.md) — every app needs structured logging: named loggers, INFO/WARNING/ERROR levels, no print(); treat missing logging as a defect
- [Tests requirement](feedback_tests.md) — every change gets tests in every applicable type (checklist: unit, integration, property, regression, golden files, migrations step-by-step, entry points, quit paths, widget, rendered real-app UI + reviewed baselines in the longest locale); real DB; coverage gate via `pytest --cov`; audit procedure
- [Regression safety](feedback_regression_safety.md) — grep callers before touching shared code; name ripple risks; update all call sites on signature changes
- [i18n completeness](feedback_i18n_completeness.md) — after any user-facing string change, update every locale file; no missing keys in any language
- [File headers (metadata)](feedback_file_headers.md) — `metadata -v` to check, `-c` if empty, `-m` after every edit, one file per call (batching silently skips files); never hand-write Revised; supported: .py .pyw .sh .bash .rs .md
- [Python linting (ruff)](feedback_python_projects.md) — ruff format then ruff check on every modified .py file; fix errors manually, never --fix
- [No future imports](feedback_no_future_imports.md) — never add `from __future__` imports; remove existing ones unless removal breaks compilation
- [Nearest-neighbor zoom artifact](feedback_nearest_neighbor_zoom_artifact.md) — never PIL-zoom a screenshot with NEAREST to judge rendering quality; it fakes pixelation on any image, use LANCZOS or native res
- [Render before showing icons](feedback_render_before_showing_icons.md) — always render hand-coded SVG/icon work to PNG and inspect it (at real deployed size) before sending; never eyeball raw path coordinates

## API Design
- [Stripe-style expand pattern](feedback_stripe_expand_pattern.md) — FK fields are int by default, expanded object with ?expand=field; no *_fk in responses; image_fk+image_path excepted

## UI
- [Distinct icons per control](feedback_distinct_icons.md) — never reuse the same icon for two different settings/actions, even if thematically related
- [Distinct status colors](feedback_distinct_status_colors.md) — every state in a 2+ value status needs its own color; don't let two states share a color or "no color" double as a state once there are 3+ values; red reserved for genuinely bad news
- [Disabled buttons visually greyed out](feedback_ui_disabled_buttons.md) — disabled buttons must appear dimmed, never identical to enabled state
- [Inline editing preference](feedback_ui_inline_editing.md) — always design editable UI with in-place editing; no dialogs/modals unless unavoidable
- [Dialog close pattern](feedback_dialog_close_pattern.md) — dismiss dialogs via X IconButton top-right in the title row; never a bottom "Close" text button or bottom-right X; exception: Cancel/Confirm decision dialogs keep their own actions

## Project-specific (renar-frontend)
- [Don't manage the backend process](feedback_dont_manage_backend_process.md) — user runs be.exe themselves; EXCEPTION: standing permission to start/stop it for UI-verification work (Playwright screenshotting)
- [Flet APK build quirks](flet-apk-build-quirks.md) — set PYTHONUTF8=1 before `flet build`; APK lands in buildpk; known dependency pitfalls
- [Flet SnackBar quirks](flet-snackbar-quirks.md) — SnackBar ignores ColorScheme tokens + ignores in-place update() after a while; dismiss+recreate fix; also: orphaned `uv run app` processes fake "restart didn't help"
- [Telegram bot token](reference_telegram_bot_token.md) — @claudia_touro_bot; chat_id in the file; use for sendDocument/sendMessage
- [APK delivery via Telegram](feedback_apk_telegram_delivery.md) — "send me the apk" always means build fresh + push to Telegram (arm64-v8a, <50MB), not just SendUserFile
- [Custom spinner only](feedback_custom_spinner.md) — always use `loading_row()`/`branding.animated_logo`, never `ft.ProgressRing`, for any loading/busy indicator
- [Docs span both renar repos](feedback_renar_docs_both_repos.md) — "update documentation" means check frontend AND backend, always
- [Repo-wide actions span both repos](feedback_renar_both_repos_always.md) — push/commit/docs in renar-frontend must also check+handle renar-backend, always
- [Design decisions doc](feedback_renar_design_decisions_doc.md) — docs/design-decisions.md in both repos; single doc, grouped by area, decision+Why
- [Backlog: no done/fixed entries](feedback_backlog_no_done_entries.md) — remove resolved backlog items entirely; don't annotate as done, history lives in git/CHANGELOG/design-decisions.md
- [Backlog: blocking/future tags](feedback_backlog_blocking_tags.md) — every item tagged [Blocking for 1.0] or [Future]; ask user when unclear, don't guess
<!-- private -->
-----BEGIN PGP MESSAGE-----

hF4DQ/EuiSPJ5t0SAQdAaL/9ioA1lKKJtYqN8mpn88TXewnE5vKfTIxEOG31gGcw
rHrOJ/yqs6hYoNy1uc7P43AjiH99ZuEO7+OJhyMXzYk5LmQJBF429Vc+3v2Hiz8s
1MAHAQkCEPkuvrBTva5mAWfZ1E4TfvfV0Zrjn1QcAC+d0HMAlpYj+HB8ijcrQqCY
97LKpFFcJ6fvLL3o0w+M6tosDk+0xvQY56Pq+WWc7HritrGEclg0ou+t6qs2ivrG
FblZ1/xzTRCUmSWf8jn6rlnWnC13ko8tjTJVqt/21u0KQH3Va6Y3S7zh7J4ET5yw
DIjxgtuXPtlnzucPNQP4u7G9NTID/kXc2Cr9NQsAkx3TMGcWdcPBBkokTcUKXZ3m
YNGUMVicCjeiBA==
=VTWe
-----END PGP MESSAGE-----
<!-- /private -->
- [renar Postgres migration](renar-postgres-migration.md) — backend fully on Postgres (runtime+tests+alembic); schema normalized 2026-07-10, guarded by tests/test_normalization.py
- [renar-backend must be BCNF](feedback_renar_bcnf.md) — every new column/table: run test_normalization.py + manually check candidate-key dependencies; never silently widen allowlists
- [renar-backend abuse-guard exempt_ips](feedback_renar_abuse_guard_exempt_ips.md) — any new strike/ban code path must check site_settings.exempt_ips first; missed once on /svc auth, would've banned localhost
- [UI verification workflow](renar-frontend-ui-verification-workflow.md) — `uv run web` + Playwright (system Python) to screenshot Flet UI headlessly; pixel-click the canvas, use `/home-progress-style` for hero-card mockups, Windows-path screenshot outputs
- [Manual checks file](renar-manual-checks.md) — sw\renar\common\manual-checks.md, shared frontend+backend; add checks only on explicit request, never pre-populate
- [Frontend restart required](feedback_frontend_restart_required.md) — Flet can silently serve stale code after edits (blank screens, no error); always relaunch fully before verifying/reporting a fix
- [Backlog artifact sync](feedback_backlog_artifact_sync.md) — whenever docs/backlog.md changes in either renar repo, also republish the "Renar Backlog" artifact (DATA + PROGRESS chart point)
- [Playwright/Flutter boot hang](renar-frontend-playwright-flutter-boot-hang.md) — spawning Flet web server with stdout=PIPE then driving it with Playwright in the same process hangs the canvas forever; redirect subprocess output to a file instead
- [Flet GridView.runs_count default](flet-gridview-runs-count-default.md) — defaults to 1, not None; truthiness checks on it misfire for max_extent-only grids; check max_extent first
- [Artifact update from WebFetch copy](feedback_artifact_update_from_webfetch.md) — strip the injected frame-runtime wrapper line + doctype/html/head/body tags before republishing a WebFetch-downloaded artifact copy
- [UI verification account cleanup](feedback_ui_verification_account_cleanup.md) — delete any account created by ad-hoc verification scripts against the real backend before ending the session; use admin delete endpoint
- [flet_webview Android JS disabled by default](flet-webview-android-js-disabled.md) — must call set_javascript_mode after mount or embedded pages (Turnstile etc.) load but silently never run JS; adb logcat is the diagnostic
- [renar dev/prod domain split](renar-dev-prod-domain-split.md) — api.dev.renar.app vs api.renar.app, one SAN cert, certbot via uvx not global install, Turnstile domains are dashboard-only (no API)
- [renar concurrent-editor WIP](renar-backend-uncommitted-wip.md) — 2nd editor active in BOTH renar repos, uncommitted; as of 08-25 it directly iterates on features you just shipped (icon/order/copy changes) — re-read before re-asserting past choices
