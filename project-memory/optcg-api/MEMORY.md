# optcg-api Project Memory

## Project
- [optcg-api project](project_optcg_api.md) — FastAPI One Piece TCG API; FastAPI + uvicorn, src layout, ruff config; clean tree as of 2026-05-20
- [optcg-editor status](project_optcg_editor.md) — Electron+React desktop app; UI fully built, Electron fixed, installer built
- [DB design decisions](project_db_design.md) — Naip/Card/Rarity/NaipSerial/dedup-tables intentional design; all prior bugs resolved

## User
- [Author identity](../../../memory/user_author_identity.md) — Ran# · ran.hash@proton.me; use for git config, CONTRIBUTORS, and attribution

## Session Behaviour
- [Project spec behaviour](../../../memory/feedback_project_behaviour.md) — maintain project_spec.md per project; read at session start; flag contradictions; update only on explicit request
- [Universal app behaviours](../../../memory/feedback_universal_behaviours.md) — clean shutdown on all quit paths; flag contradictions before implementing
- [Response style](../../../memory/feedback_response_style.md) — answer-first, no preamble/filler/trailing prompts; docs always in sync; cite standard deviations

## Git & Version Control
- [Commit style](../../../memory/feedback_commits.md) — bracket title ([A]/[R]/[F]/…), Conventional Commits body, lowercase imperative; no Co-Authored-By
- [Git remote default branch](../../../memory/feedback_git_remotes.md) — always use `main`, not `master`, for new repos on GitHub/GitLab
- [SSH key for git remotes](../../../memory/reference_ssh_keys.md) — all GitHub/GitLab remotes use SSH (`git@`); key: `~/.ssh/gitcommitran`
- [Push semantics](../../../memory/feedback_push.md) — never commit/push unless explicitly asked; when asked, do both: stage → commit → push
- [Push to all remotes](../../../memory/feedback_push_all_remotes.md) — always push to both `github` and `gitlab`; create missing remote if needed; SSH only
- [CHANGELOG before committing](../../../memory/feedback_changelog.md) — update CHANGELOG.md in the same commit as the changes; only when a commit is requested
- [Version bump workflow](feedback_version_bump.md) — user bumps pyproject.toml version; only then promote [Unreleased] to that version in CHANGELOG
- [Release dist attachments](../../../memory/feedback_releases.md) — build all dist formats (.exe, .whl, .tar.gz) and attach to tag; preserve original timestamps on history rewrites

## Repository Setup
- [New repo scaffold](../../../memory/feedback_new_repo_scaffold.md) — LICENSE (PBL), CHANGELOG, CONTRIBUTING, README, CONTRIBUTORS required before first commit
- [Custom License (PBL)](../../../memory/reference_license.md) — always use PayBack License; fetch from d:\Users\{USER}\sw\doc\LICENSE or GitLab/GitHub raw; never MIT/Apache
- [CONTRIBUTING.md layout](../../../memory/reference_contributing_layout.md) — standard section order for all projects; create if missing
- [CONTRIBUTORS file layout](../../../memory/reference_contributors_layout.md) — exact PBL v2.0 clause 18 format: SUMMARY table + DETAILS block with Pseudonym/Name/Role/Email/GPG/Ownership/Revenue fields

## Workflow
- [Apply global memory proactively](../../../memory/feedback_apply_global_memory_proactively.md) — scan MEMORY.md before every task; apply matching rules without waiting to be corrected
- [Never ask for permission](../../../memory/feedback_no_permission_prompts.md) — just act; exceptions: user said to ask, or "ask before edits" mode is on
- [Always use AskUserQuestion](../../../memory/feedback_ask_user_question.md) — use AskUserQuestion tool for all questions and choices, including mid-edit options; never plain-text questions

## Tools
- [Hashing default](../../../memory/feedback_hashing.md) — always use BLAKE3; "hash" means blake3 unless specified; use platform-appropriate tool

## Database
- [updated_ts trigger on new tables](feedback_updated_ts_trigger.md) — every new table needs a `trg_<table>_update` trigger in the same migration; use WHEN NEW.updated_ts IS OLD.updated_ts guard

## Code Quality
- [Clean Code, SOLID + Design Patterns](../../../memory/feedback_clean_code.md) — all SOLID rules, all GoF patterns, DRY/YAGNI/KISS, DDD/CQRS/hexagonal when scale justifies
- [Regression safety](../../../memory/feedback_regression_safety.md) — grep callers before touching shared code; name ripple risks; update all call sites on signature changes
- [i18n completeness](../../../memory/feedback_i18n_completeness.md) — after any user-facing string change, update every locale file; no missing keys in any language
- [File headers (metadata)](../../../memory/feedback_file_headers.md) — `metadata -v` to check, `-c` if empty, `-m` after every edit; never hand-write Revised; supported: .py .pyw .sh .bash .rs .md
- [Python linting (ruff)](../../../memory/feedback_python_projects.md) — ruff format then ruff check on every modified .py file; fix errors manually, never --fix
- [No future imports](../../../memory/feedback_no_future_imports.md) — never add `from __future__` imports; remove existing ones unless removal breaks compilation

## UI
- [Disabled buttons visually greyed out](../../../memory/feedback_ui_disabled_buttons.md) — disabled buttons must appear dimmed, never identical to enabled state
- [Inline editing preference](../../../memory/feedback_ui_inline_editing.md) — always design editable UI with in-place editing; no dialogs/modals unless unavoidable

- [Full sweep trigger](feedback_full_sweep.md) � "full sweep" = autonomous repeating audit-and-fix loop across all levels; don't return control until nothing remains
