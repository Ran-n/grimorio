---
name: version-bump-workflow
description: "When told to \"bump\" (e.g. \"bump rn\"), determine major/minor/patch from git diff per repo, run `uv version --bump <level>` (never hand-edit pyproject.toml), then promote [Unreleased] to that version in CHANGELOG — for FE and/or BE per [[feedback_renar_both_repos_always]]"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f6264f50-66a9-4b1d-8e4a-c5523244a0ce
  modified: 2026-07-28T10:18:03.722Z
---

When told to bump the version (e.g. "bump rn"), for each of renar-frontend
and renar-backend that has unreleased changes (check both, per
[[feedback_renar_both_repos_always]]):

1. Determine bump level from `git diff`/`git status` (the real uncommitted
   changes — CHANGELOG.md can lag behind, see [[feedback_changelog]]):
   breaking → major, new backward-compatible feature → minor, fix-only →
   patch.
2. Run `uv version --bump {major|minor|patch}` in that repo's directory —
   this is the correct way to write the new version into `pyproject.toml`.
   Never hand-edit the version field directly.
3. Read the new version back from `pyproject.toml`, then promote
   `[Unreleased]` in `CHANGELOG.md` to `[X.Y.Z] - YYYY-MM-DD`.
4. Give the version bump its own dedicated `[R] bump version` commit if a
   commit is requested — never fold it into an `[A]`/`[F]` commit body
   ([[feedback_commits]]).

**Why:** originally the user did the pyproject.toml edit themselves and
only asked Claude to promote the CHANGELOG afterward. The user then asked
to be able to say "bump" and have Claude do the whole thing, and clarified
the actual mechanism is `uv version --bump <level>`, not a hand-edit of
`pyproject.toml` — "you do the uv version command as needed, that is what
modifies the pyproject."

**How to apply:** on "bump" (with no level specified), infer the level per
repo from the diff and run the `uv version --bump` command yourself; don't
ask the user to pick a number first unless the diff is ambiguous. Still
never *commit or push* without being asked separately
([[feedback_push]]).

**Incident (2026-07-28, both renar repos):** A prior session bumped `pyproject.toml` *and* promoted the CHANGELOG together, but folded the bump into an `[A]` feature commit's body (e.g. "...promote CHANGELOG [Unreleased] to [0.7.1]") instead of giving it its own dedicated `[R] bump version` commit ([[feedback_commits]]). Follow-up `[F]` fix commits then added new `[Unreleased]` content without ever bumping again, so `pyproject.toml` silently fell one version behind the real unreleased state in both repos — surfaced only when the user noticed the reported version looked stale. Even when a version bump is bundled with real feature work, it must still be its own commit; never combine "bump version" into a commit whose primary bracket tag is `[A]`/`[F]`/etc.
