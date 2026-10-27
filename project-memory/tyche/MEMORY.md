# Memory Index

## User
- [Author identity](user_author_identity.md) — Ran# (legal: Anxo Ledo) · ran.hash@proton.me; pseudonym for public/git, legal name for CONTRIBUTORS Name field

## Session Behaviour
- [Project spec behaviour](feedback_project_behaviour.md) — maintain project_spec.md per project; read at session start; flag contradictions; update only on explicit request
- [Universal app behaviours](feedback_universal_behaviours.md) — clean shutdown on all quit paths; flag contradictions before implementing
- [Response style](feedback_response_style.md) — answer-first, no preamble/filler/trailing prompts; docs always in sync; cite standard deviations

## Git & Version Control
- [Commit style](feedback_commits.md) — bracket title ([A]/[R]/[F]/…), Conventional Commits body, lowercase imperative; no Co-Authored-By
- [Git remote default branch](feedback_git_remotes.md) — always use `main`, not `master`, for new repos on GitHub/GitLab
- [SSH key for git remotes](reference_ssh_keys.md) — all GitHub/GitLab remotes use SSH (`git@`); key: `~/.ssh/gitcommitran`
- [Push semantics](feedback_push.md) — never commit/push unless explicitly asked; when asked, do both: stage → commit → push
- [Push to all remotes](feedback_push_all_remotes.md) — always push to both `github` and `gitlab`; create missing remote if needed; SSH only
- [CHANGELOG before committing](feedback_changelog.md) — update CHANGELOG.md in the same commit as the changes; only when a commit is requested
- [Version bump workflow](feedback_version_bump.md) — user bumps pyproject.toml version; only then promote [Unreleased] to that version in CHANGELOG
- [Release dist attachments](feedback_releases.md) — build all dist formats (.exe, .whl, .tar.gz) and attach to tag; preserve original timestamps on history rewrites

## Repository Setup
- [New repo scaffold](feedback_new_repo_scaffold.md) — LICENSE (PBL), CHANGELOG, CONTRIBUTING, README, CONTRIBUTORS required before first commit
- [Custom License (PBL)](reference_license.md) — always use PayBack License; fetch from d:\Users\{USER}\sw\doc\LICENSE or GitLab/GitHub raw; never MIT/Apache
- [CONTRIBUTING.md layout](reference_contributing_layout.md) — standard section order for all projects; create if missing
- [CONTRIBUTORS file layout](reference_contributors_layout.md) — exact PBL v2.0 clause 18 format: SUMMARY table + DETAILS block with Pseudonym/Name/Role/Email/GPG/Ownership/Revenue fields

## Workflow
- [Apply global memory proactively](feedback_apply_global_memory_proactively.md) — scan MEMORY.md before every task; apply matching rules without waiting to be corrected
- [Never ask for permission](feedback_no_permission_prompts.md) — just act; exceptions: user said to ask, or "ask before edits" mode is on
- [Always use AskUserQuestion](feedback_ask_user_question.md) — use AskUserQuestion tool for all questions and choices, including mid-edit options; never plain-text questions

## Tools
- [Hashing default](feedback_hashing.md) — always use BLAKE3; "hash" means blake3 unless specified; use platform-appropriate tool

## Code Quality
- [Clean Code, SOLID + Design Patterns](feedback_clean_code.md) — all SOLID rules, all GoF patterns, DRY/YAGNI/KISS, DDD/CQRS/hexagonal when scale justifies
- [Regression safety](feedback_regression_safety.md) — grep callers before touching shared code; name ripple risks; update all call sites on signature changes
- [i18n completeness](feedback_i18n_completeness.md) — after any user-facing string change, update every locale file; no missing keys in any language
- [File headers (metadata)](feedback_file_headers.md) — `metadata -v` to check, `-c` if empty, `-m` after every edit; never hand-write Revised; supported: .py .pyw .sh .bash .rs .md
- [Python linting (ruff)](feedback_python_projects.md) — ruff format then ruff check on every modified .py file; fix errors manually, never --fix

## UI
- [Disabled buttons visually greyed out](feedback_ui_disabled_buttons.md) — disabled buttons must appear dimmed, never identical to enabled state
- [Inline editing preference](feedback_ui_inline_editing.md) — always design editable UI with in-place editing; no dialogs/modals unless unavoidable

- [Full sweep trigger](feedback_full_sweep.md) � "full sweep" = autonomous repeating audit-and-fix loop across all levels; don't return control until nothing remains
