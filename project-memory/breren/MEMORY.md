# Memory Index

## User
- [Author identity](user_author_identity.md) — Ran# (legal: Anxo Ledo) · ran.hash@proton.me; pseudonym for public/git, legal name for CONTRIBUTORS Name field

## Session Behaviour
- [Project spec behaviour](feedback_project_behaviour.md) — maintain project_spec.md per project; read at session start; flag contradictions; update only on explicit request
- [Universal app behaviours](feedback_universal_behaviours.md) — clean shutdown on all quit paths; flag contradictions before implementing
- [Response style](feedback_response_style.md) — answer-first, no preamble/filler/trailing prompts; docs always in sync; cite standard deviations

## Git & Version Control
- [Commit style](feedback_commits.md) — bracket title ([A]/[R]/[F]/…), Conventional Commits body, lowercase imperative; no Co-Authored-By
- [Git remote default branch](feedback_git_remotes.md) — always use `main`, not `master`, for new repos on GitHub/GitLab/Bitbucket/Codeberg
- [SSH key for git remotes](reference_ssh_keys.md) — all GitHub/GitLab/Bitbucket/Codeberg remotes use SSH (`git@`); key: `~/.ssh/gitcommitran`
- [Push semantics](feedback_push.md) — never commit/push unless explicitly asked; when asked, do both: stage → commit → push
- [Push workflow](feedback_push_all_remotes.md) — "push" = update all doc files → commit → push to `github`, `gitlab`, `codeberg`; Bitbucket dropped 2026-05; create missing remote if needed; SSH only
- [CHANGELOG before committing](feedback_changelog.md) — update CHANGELOG.md in the same commit as the changes; only when a commit is requested
- [Version bump workflow](feedback_version_bump.md) — "bump" = infer level from git diff, run every skipped test group first, write the version with the project's tool (uv, cargo, npm…), promote CHANGELOG [Unreleased]; no manifest → git tag
- [Release dist attachments](feedback_releases.md) — build all dist formats (.exe, .whl, .tar.gz) and attach to tag; preserve original timestamps on history rewrites

## Python Projects
- [pyproject.toml scaffold](reference_pyproject_scaffold.md) — minimum required structure: hatchling build, ruff with lint+format sections, line-length 120, preview=true

## Repository Setup
- [New repo scaffold](feedback_new_repo_scaffold.md) — LICENSE (PBL), CHANGELOG, CONTRIBUTING, README, CONTRIBUTORS required before first commit
- [Custom License (PBL)](reference_license.md) — always use PayBack License; fetch from d:\Users\{USER}\sw\doc\LICENSE or GitLab/GitHub raw; never MIT/Apache
- [CONTRIBUTING.md layout](reference_contributing_layout.md) — standard section order for all projects; create if missing
- [CONTRIBUTORS file layout](reference_contributors_layout.md) — exact PBL v2.0 clause 18 format: SUMMARY table + DETAILS block with Pseudonym/Name/Role/Email/GPG/Ownership/Revenue fields
- [Site organization](feedback_site_organization.md) — served files grouped under one dedicated folder (e.g. `public/`), separate from repo-meta files; add a build/deploy step if the host can't serve that subfolder natively

## Workflow
- [Apply global memory proactively](feedback_apply_global_memory_proactively.md) — scan MEMORY.md before every task; apply matching rules without waiting to be corrected
- [Project memory mirror](feedback_project_memory_mirror.md) — byte-copy global memory into project dir; never modify mirrored files; project-specific files sit alongside but are not indexed in MEMORY.md
- [Never ask for permission](feedback_no_permission_prompts.md) — just act; exceptions: user said to ask, or "ask before edits" mode is on
- [Always use AskUserQuestion](feedback_ask_user_question.md) — use AskUserQuestion tool for all questions and choices, including mid-edit options; never plain-text questions

## Tools
- [Hashing default](feedback_hashing.md) — always use BLAKE3; "hash" means blake3 unless specified; use platform-appropriate tool
- [APK Telegram delivery rule](feedback_apk_telegram_delivery.md) — xoutaim-frontend: build+send APK via Telegram bot only on Remote Control; otherwise normal file delivery
- [Flet split-APK staleness](feedback_flet_split_apk_staleness.md) — `flet build apk` w/o `--split-per-abi` silently ships stale per-ABI splits; always pass the flag, clean-rebuild if unsure, verify by unzipping app.zip before shipping
- [Flet SnackBar quirks](feedback_flet_snackbar_quirks.md) — SnackBar ignores custom ColorScheme tokens + ignores in-place update() after a while (dismiss+recreate instead); also: killing flet.exe ≠ killing the python server, verify process state before trusting a "restart"

## Credentials & Tokens
- [Codeberg API token](reference_codeberg_token.md) — Forgejo REST API token for `Ran-n`; use to create repos via `https://codeberg.org/api/v1/`
- [Telegram bot token](reference_telegram_bot_token.md) — Bot API token for sending messages/files; needs target chat ID first (message the bot once, then `getUpdates`)

## Workflow Triggers
- [Full sweep trigger](feedback_full_sweep.md) — "full sweep" = autonomous repeating audit-and-fix loop across all levels; don't return control until nothing remains

## Code Quality
- [Database BCNF requirement](feedback_database_bcnf.md) — every relational schema must be real BCNF, not just informally "normalized"; check candidate-key dependencies, document exceptions
- [No silent failure](feedback_no_silent_failure.md) — always surface errors explicitly; never swallow exceptions, empty catch blocks, or silent promise rejections
- [Clean Code, SOLID + Design Patterns](feedback_clean_code.md) — all SOLID rules, all GoF patterns, DRY/YAGNI/KISS, DDD/CQRS/hexagonal when scale justifies; DRY is a hard rule — never invoke "no premature abstraction"/YAGNI to skip extracting shared code
- [Logging requirement](feedback_logging.md) — every app needs structured logging: named loggers, INFO/WARNING/ERROR levels, no print(); treat missing logging as a defect
- [Tests requirement](feedback_tests.md) — every change gets tests in every applicable type (checklist: unit, integration, property, regression, golden files, migrations step-by-step, entry points, quit paths, widget, rendered real-app UI + reviewed baselines in the longest locale); real DB; coverage gate via `pytest --cov`; audit procedure
- [Regression safety](feedback_regression_safety.md) — grep callers before touching shared code; name ripple risks; update all call sites on signature changes
- [i18n completeness](feedback_i18n_completeness.md) — after any user-facing string change, update every locale file; no missing keys in any language
- [File headers (metadata)](feedback_file_headers.md) — `metadata -v` to check, `-c` if empty, `-m` after every edit; never hand-write Revised; supported: .py .pyw .sh .bash .rs .md
- [Python linting (ruff)](feedback_python_projects.md) — ruff format then ruff check on every modified .py file; fix errors manually, never --fix
- [No future imports](feedback_no_future_imports.md) — never add `from __future__` imports; remove existing ones unless removal breaks compilation
- [Source tree organization](feedback_source_organization.md) — CCP/CRP/REP + ADP/SDP/SAP, package-by-feature vs by-layer, Screaming Architecture, hexagonal; fills the gap SOLID leaves for file/folder placement

## API Design
- [Stripe-style expand pattern](feedback_stripe_expand_pattern.md) — FK fields are int by default, expanded object with ?expand=field; no *_fk in responses; image_fk+image_path excepted
- [Bulk endpoints over N-call loops](feedback_bulk_endpoints.md) — before looping a per-item API call N times, check for/add a bulk endpoint; batch the write AND the post-write recompute, not just the write

## UI
- [Disabled buttons visually greyed out](feedback_ui_disabled_buttons.md) — disabled buttons must appear dimmed, never identical to enabled state
- [Inline editing preference](feedback_ui_inline_editing.md) — always design editable UI with in-place editing; no dialogs/modals unless unavoidable
- [CTA hierarchy](feedback_ui_cta_hierarchy.md) — primary action big/own row, secondary links (source mirrors etc.) small/below; use each platform's real logo, never a generic placeholder icon

## Project-Specific (breren)
- [Scope: stay breren-focused](feedback_scope.md) — avoid mentioning renar often, keep focus on breren
- [Cloudflare API token](reference_cloudflare_token.md) — DNS-edit token scoped to the breren.com zone only
- [Cert renewal routine](project_cert_renewal_routine.md) — scheduled cloud check 2026-10-15 for breren.com's HTTPS cert renewal
- [Push after each change](feedback_push_after_each_change.md) — push (all remotes) after every individual change here, not batched at the end
