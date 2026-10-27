---
name: feedback-housekeeping-trigger
description: "Trigger phrase \"house keep\"/\"hk\" — run the doc-sync + code-quality wrap-up checklist for the session's changes"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 58fe1840-0e9b-445d-a9d0-86b8def5ea1b
  modified: 2026-08-17T10:30:33.591Z
---

When the user says **"house keep"** or **"hk"**, run this wrap-up checklist against everything changed in the session (or, if nothing obvious changed this session, against the current uncommitted diff), without waiting for a more specific request:

1. **Docs sync** — for each affected repo (see [[feedback-renar-docs-both-repos]]/[[feedback-renar-both-repos-always]] when in a renar repo):
   - `CHANGELOG.md`: add/update the `[Unreleased]` entry for what changed.
   - `docs/design-decisions.md`: add an entry for any non-obvious decision made (see [[feedback-renar-design-decisions-doc]]).
   - `docs/backlog.md`: remove any item the session's work resolved (see [[feedback-backlog-no-done-entries]]); add new items surfaced but not done, tagged `[Blocking for 1.0]`/`[Future]` — ask if unclear.
2. **File headers** — `metadata -m` is supposed to run right after every edit already (see [[feedback-file-headers]]), so this is a verification sweep, not the primary mechanism: for every file touched this session, actually check (`metadata -v`) that Revised was updated, and run `metadata -m` on any that were missed.
3. **Lint/format** — same verification pattern for ruff (see [[feedback-python-projects]]): for every modified `.py` file, actually run `ruff format` + `ruff check` and confirm both pass; fix anything that wasn't already clean, don't just assume the per-edit rule fired.
4. **Tests** — same verification pattern: tests should already have been run and passing after the session's changes (see [[feedback-tests]]/[[feedback-verify-after-every-change]]). Only re-run if there's no confirmed clean run since the last code change (e.g. edits made after the last run, or none was run at all); don't re-run a suite that already just passed against the current code for no reason.
5. **i18n** — if any user-facing string changed, update every locale file (see [[feedback-i18n-completeness]]).
6. **Memory sweep** — separate from docs sync: check whether anything from the session should be saved as a memory entry (feedback/project/reference) that wasn't captured live — a correction or confirmed approach, a non-obvious gotcha, new project context (deadlines, ownership, motivation). Docs sync covers the four repo files; this covers the persistent memory system itself.
7. **Loose ends** — scan for anything else needed before the session closes: stray/incomplete edits, TODOs left mid-work, uncommitted files that look like scratch/debug output.

Report a short summary of what the checklist found/fixed, not a step-by-step narration.

**Why:** user wants one short phrase to trigger the same wrap-up pass every time, instead of having to ask for docs/lint/tests separately at the end of each session (established after asking for exactly this bundle via "update documentation" following a bug fix).

**How to apply:** Treat "house keep"/"hk" as its own explicit request — it overrides the normal "only touch CHANGELOG when a commit is requested" default (see [[feedback-changelog]]) for this one pass, since the user is explicitly asking for docs sync here. Does not commit or push on its own — that's still a separate explicit request (see [[feedback-push]]).
