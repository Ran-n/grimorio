---
name: version-bump-workflow
description: "When told to \"bump\" (with no level given), determine major/minor/patch from git diff, write the version with the project's own tool (uv, cargo, npm…; never hand-edit a manifest a tool can write), then promote [Unreleased] in CHANGELOG; repos without a manifest get a git tag"
metadata:
  type: feedback
---

When told to bump the version (e.g. "bump", "bump rn", step 2 of `/dbp`),
in any project:

1. Determine bump level from `git diff`/`git status` (the real uncommitted
   changes — CHANGELOG.md can lag behind, see [[feedback_changelog]]):
   breaking → major, new backward-compatible feature → minor, fix-only →
   patch.
2. **Release test gate — before the bump, run the whole suite, including
   everything the default run skips.** Read the project's test config and
   development docs for deselected groups and run each on its own, on top of
   the default run: pytest markers in `addopts` / `markers` (`uv run pytest
   -m live`, `-m desktop`, `-m e2e`, …), Rust `#[ignore]` tests (`cargo test
   -- --include-ignored`) and feature-gated tests (`--all-features`), npm
   scripts beyond `test` (`test:e2e`, …). A plain default run is not enough
   for a release. Suites that take over the mouse/keyboard or the screen
   (e.g. bounty_board's `desktop`) still run: ask with AskUserQuestion when
   to run them (now / when I'm away), never skip them silently. Anything that
   fails blocks the bump. In the hand-over, list which groups ran and their
   counts; if a run was really impossible (no network), say so as an open
   item and don't call the release verified. A repo with no tests skips this
   step.
3. Write the new version with the project's own tool — never hand-edit a
   version field a tool can write:

   | Manifest | Command |
   |----------|---------|
   | `pyproject.toml` (uv) | `uv version --bump <level>` |
   | `Cargo.toml` | `cargo set-version --bump <level>` (from `cargo-edit`; install it with `cargo install cargo-edit` if missing) |
   | `package.json` | `npm version <level> --no-git-tag-version` |
   | other manifest | the ecosystem's version command; if it has none, edit the one version field |
   | none (e.g. grimorio) | no file to write: the version lives only in CHANGELOG.md and the git tag (step 6) |

   In a Cargo workspace with `[workspace.package] version`, bump that once
   (`cargo set-version --workspace --bump <level>`); otherwise bump only the
   crates whose code changed (`-p <crate>`). Afterwards also update any
   hand-kept copy of the version the project's own memory names (e.g.
   timtapper's `core/version.py`) and refresh the lockfile (`Cargo.lock`,
   `uv.lock`, `package-lock.json`) if the tool didn't.
4. Read the new version back from the manifest (or, with no manifest, take
   the last released CHANGELOG version and apply the level), then promote
   `[Unreleased]` in `CHANGELOG.md` to `[X.Y.Z] - YYYY-MM-DD`.
5. Give the version bump its own dedicated `[R] bump version` commit if a
   commit is requested — never fold it into an `[A]`/`[F]` commit body
   ([[feedback_commits]]).
6. **No-manifest repos only:** tag that commit `vX.Y.Z` (annotated:
   `git tag -a vX.Y.Z -m "vX.Y.Z"`) and push the tag to every remote along
   with the branch ([[feedback_push_all_remotes]]). The tag is the version.

For multi-repo projects (e.g. renar's frontend+backend split), check every
related repo for unreleased changes and bump each independently — see the
project-specific mirror rule if one exists for the project at hand.

**Why:** originally the user did the pyproject.toml edit themselves and
only asked Claude to promote the CHANGELOG afterward. The user then asked
to be able to say "bump" and have Claude do the whole thing, and clarified
the actual mechanism is `uv version --bump <level>`, not a hand-edit of
`pyproject.toml` — "you do the uv version command as needed, that is what
modifies the pyproject." On 2026-10-28 `/dbp` skipped the bump in grimorio
because the rule only knew `pyproject.toml`; the user asked to "make it
work for all projects", which is why the tool table and the tag rule exist.

**How to apply:** on "bump" (with no level specified), infer the level from
the diff and run the bump command yourself; don't ask the user to pick a
number first unless the diff is genuinely ambiguous. Still never *commit or
push* without being asked separately ([[feedback_push]]).

**Incident (2026-10-10, bounty_board 0.6.0):** `/dbp` ran only the default
`uv run pytest`, which deselects `live` and `desktop` through `addopts`, then
bumped and pushed. `docs/development.md` says to run `-m live` before every
release. The user asked "why were those skipped?" and then "make sure it
doesnt happen again", which is why step 2 exists.

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
