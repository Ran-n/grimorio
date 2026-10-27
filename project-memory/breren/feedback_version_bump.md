---
name: version-bump-workflow
description: "When told to \"bump\" (with no level given), determine major/minor/patch from git diff, run `uv version --bump <level>` (never hand-edit pyproject.toml), then promote [Unreleased] to that version in CHANGELOG"
metadata:
  type: feedback
---

When told to bump the version (e.g. "bump", "bump rn") for a uv-managed
Python project:

1. Determine bump level from `git diff`/`git status` (the real uncommitted
   changes — CHANGELOG.md can lag behind, see [[feedback_changelog]]):
   breaking → major, new backward-compatible feature → minor, fix-only →
   patch.
2. Run `uv version --bump {major|minor|patch}` in the repo's directory —
   this is the correct way to write the new version into `pyproject.toml`.
   Never hand-edit the version field directly.
2a. **Release test gate — before the bump, run the whole suite, including
   every marker the default run deselects.** Read `addopts` / `markers` in
   `pyproject.toml` (and the project's development docs) and run each
   deselected marker on its own (`uv run pytest -m live`, `-m desktop`,
   `-m e2e`, …), on top of the default run. A plain `uv run pytest` is not
   enough for a release. Markers that take over the mouse/keyboard or the
   screen (e.g. bounty_board's `desktop`) still run: ask with
   AskUserQuestion when to run them (now / when I'm away), never skip them
   silently. Anything that fails blocks the bump. In the hand-over, list
   which markers ran and their counts; if a run was really impossible (no
   network), say so as an open item and don't call the release verified.
3. Read the new version back from `pyproject.toml`, then promote
   `[Unreleased]` in `CHANGELOG.md` to `[X.Y.Z] - YYYY-MM-DD`.
4. Give the version bump its own dedicated `[R] bump version` commit if a
   commit is requested — never fold it into an `[A]`/`[F]` commit body
   ([[feedback_commits]]).

For multi-repo projects (e.g. renar's frontend+backend split), check every
related repo for unreleased changes and bump each independently — see the
project-specific mirror rule if one exists for the project at hand.

**Why:** originally the user did the pyproject.toml edit themselves and
only asked Claude to promote the CHANGELOG afterward. The user then asked
to be able to say "bump" and have Claude do the whole thing, and clarified
the actual mechanism is `uv version --bump <level>`, not a hand-edit of
`pyproject.toml` — "you do the uv version command as needed, that is what
modifies the pyproject."

**How to apply:** on "bump" (with no level specified), infer the level from
the diff and run the `uv version --bump` command yourself; don't ask the
user to pick a number first unless the diff is genuinely ambiguous. Still
never *commit or push* without being asked separately
([[feedback_push]]).

**Incident (2026-10-10, bounty_board 0.6.0):** `/dbp` ran only the default
`uv run pytest`, which deselects `live` and `desktop` through `addopts`, then
bumped and pushed. `docs/development.md` says to run `-m live` before every
release. The user asked "why were those skipped?" and then "make sure it
doesnt happen again", which is why step 2a exists.

**Incident (2026-07-28, both renar repos):** A prior session bumped
`pyproject.toml` *and* promoted the CHANGELOG together, but folded the
bump into an `[A]` feature commit's body (e.g. "...promote CHANGELOG
[Unreleased] to [0.7.1]") instead of giving it its own dedicated `[R] bump
version` commit ([[feedback_commits]]). Follow-up `[F]` fix commits then
added new `[Unreleased]` content without ever bumping again, so
`pyproject.toml` silently fell one version behind the real unreleased
state in both repos — surfaced only when the user noticed the reported
version looked stale. Even when a version bump is bundled with real
feature work, it must still be its own commit; never combine "bump
version" into a commit whose primary bracket tag is `[A]`/`[F]`/etc.
