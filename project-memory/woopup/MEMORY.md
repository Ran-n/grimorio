# Memory Index — woopup

> Mirrored from global memory. Source of truth: `C:\Users\{USER}\.claude\memory\MEMORY.md`.

## User
- [Author identity](user_author_identity.md) — Ran# (legal: Anxo Ledo) · ran.hash@proton.me

## Session Behaviour
- [Response style](feedback_response_style.md) — answer-first, no preamble/filler; docs always in sync; cite standard deviations
- [Universal app behaviours](feedback_universal_behaviours.md) — clean shutdown on all quit paths; flag contradictions before implementing
- [Apply global memory proactively](feedback_apply_global_memory_proactively.md) — scan MEMORY.md at session start; apply matching rules without being corrected
- [Never ask for permission](feedback_no_permission_prompts.md) — just act; exceptions: user said to ask, or "ask before edits" mode is on
- [Always use AskUserQuestion](feedback_ask_user_question.md) — use AskUserQuestion tool for all questions, never plain-text questions

## Git & Version Control
- [Commit style](feedback_commits.md) — bracket title ([A]/[R]/[F]/…), Conventional Commits body, lowercase imperative; no Co-Authored-By
- [Git remote / branch](feedback_git_remotes.md) — always `main`; SSH remotes; key `~/.ssh/gitcommitran`
- [Push semantics](feedback_push.md) — never commit/push unless explicitly asked; when asked: stage → commit → push to all remotes
- [Push to all remotes](feedback_push_all_remotes.md) — github, gitlab, codeberg; Bitbucket dropped 2026-05; SSH only
- [CHANGELOG before committing](feedback_changelog.md) — update CHANGELOG.md in same commit
- [Version bump workflow](feedback_version_bump.md) — user bumps pyproject.toml; only then promote [Unreleased] in CHANGELOG
- [Release dist attachments](feedback_releases.md) — build .exe, .whl, .tar.gz; attach to tag

## Repository Setup
- [New repo scaffold](feedback_new_repo_scaffold.md) — LICENSE (PBL), CHANGELOG, CONTRIBUTING, README, CONTRIBUTORS required before first commit
- [Custom License (PBL)](reference_license.md) — PayBack License; fetch from `d:\Users\{USER}\sw\doc\LICENSE`; never MIT/Apache
- [CONTRIBUTING.md layout](reference_contributing_layout.md) — standard section order
- [CONTRIBUTORS file layout](reference_contributors_layout.md) — PBL v2.0 clause 18 format

## Code Quality
- [Clean Code / SOLID / Design Patterns](feedback_clean_code.md) — `src/` layout; one class/module per concern; no file >~200 lines; no function >~20 lines; SOLID; GoF patterns; DRY/YAGNI/KISS
- [Regression safety](feedback_regression_safety.md) — grep callers before touching shared code; update all call sites
- [i18n completeness](feedback_i18n_completeness.md) — update every locale file after any user-facing string change
- [File headers (metadata)](feedback_file_headers.md) — `metadata -v` before edit; `-c` if empty; `-m` after every edit
- [Python linting (ruff)](feedback_python_projects.md) — `ruff format` then `ruff check` on every modified .py; fix manually, never --fix
- [No future imports](feedback_no_future_imports.md) — never add `from __future__` imports

## UI
- [Disabled buttons greyed out](feedback_ui_disabled_buttons.md) — disabled buttons must be visually dimmed, never identical to enabled
- [Inline editing](feedback_ui_inline_editing.md) — in-place editing always; no dialogs/modals unless unavoidable; Enter=confirm, Esc=cancel

- [Full sweep trigger](feedback_full_sweep.md) � "full sweep" = autonomous repeating audit-and-fix loop across all levels; don't return control until nothing remains
