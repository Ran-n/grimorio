# Project Memory — doc

- [Global Preferences](global_preferences.md) — git commit style, file headers, workflow, author info, feedback rules, Python ruff config
- [License files — no metadata headers](feedback_licenses.md) — skip metadatos for anything under licenses/
- [doc — project overview](project_doc.md) — repo structure, PBL license policy, donation addresses

## File Headers
- [Always run metadatos -m after file edits](feedback_metadatos_on_edit.md) — never set Revised timestamp manually; always use the script

## Workflow
- [Never ask for permission](feedback_no_permission_prompts.md) — just act; only exceptions: user explicitly said to ask, or "ask before edits" mode is on
- [Never commit or push without explicit instruction](feedback_no_commit_without_approval.md) — only commit/push when user explicitly asks; finishing edits does not imply permission
- [CHANGELOG before committing](feedback_changelog.md) — CHANGELOG.md must be updated before every git commit; include in the same commit
- [Push to GitHub and GitLab always](feedback_push_all_remotes.md) — origin has two push URLs; single `git push` covers both; SSH only
- [Project spec behaviour](feedback_project_behaviour.md) — maintain `project_spec.md` per project; read at session start; flag contradictions; update only on explicit user request
- [Universal app behaviours](feedback_universal_behaviours.md) — clean shutdown on all quit paths; flag contradictions before implementing

## Git
- [SSH key for git remotes](reference_ssh_keys.md) — GitHub/GitLab use `~/.ssh/gitcommitran`; signing_key is for signing only
- [Remote creation uses main](feedback_git_remotes.md) — default branch must be `main`, not `master`

## Releases
- [Attach all dist artifacts](feedback_releases.md) — build all dist formats and attach to release tag; preserve all timestamps on history rewrites

## Code Quality
- [Clean Code, SOLID + Design Patterns](feedback_clean_code.md) — structure, all SOLID rules, all GoF patterns, DRY/YAGNI/KISS, DDD/CQRS/hexagonal when scale justifies
- [Regression safety](feedback_regression_safety.md) — changes must not silently break unrelated parts; grep callers, name ripple risks before implementing

## Writing Style
- [Human-sounding text](global_preferences.md) — all generated text must be indistinguishable from human writing; no AI-signature patterns

## Interaction Style
- [Always use AskUserQuestion](feedback_ask_user_question.md) — use AskUserQuestion for all questions to the user, never plain-text questions
- [Use AskUserQuestion during text editing](feedback_text_editing_ui.md) — when editing text and user gives directives, surface options via AskUserQuestion, not text blocks

## UI
- [Disabled buttons visually greyed out](feedback_ui_disabled_buttons.md) — disabled buttons must always look visually distinct (dimmed), never identical to enabled

## i18n
- [i18n completeness](feedback_i18n_completeness.md) — after any change touching user-facing strings, update every locale file; no missing keys in any language

## New Repositories
- [New repo scaffold](feedback_new_repo_scaffold.md) — LICENSE (PBL), CHANGELOG, CONTRIBUTING, README, CONTRIBUTORS always included

## References
- [Custom License](reference_license.md) — PBL always; fetch latest from source; never MIT/Apache
- [CONTRIBUTING.md layout](reference_contributing_layout.md) — standard section order; create if missing

- [Full sweep trigger](feedback_full_sweep.md) � "full sweep" = autonomous repeating audit-and-fix loop across all levels; don't return control until nothing remains
