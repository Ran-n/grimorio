---
name: version-bump-workflow
description: User bumps the version in pyproject.toml; only then promote [Unreleased] to that version in CHANGELOG
metadata:
  type: feedback
---

Never bump `version` in `pyproject.toml` proactively. The user updates the version themselves, then asks to update the changelog. At that point, read the new version from `pyproject.toml` and promote `[Unreleased]` to `[X.Y.Z] - YYYY-MM-DD`.

**Why:** User controls release versioning; Claude touching it jumped ahead of their process.

**How to apply:** When asked to "update the changelog" or "set the versions", read `pyproject.toml` first, use whatever version is there, and only touch `CHANGELOG.md` — never `pyproject.toml`.

**Incident (2026-07-28, both renar repos):** A prior session bumped `pyproject.toml` *and* promoted the CHANGELOG together, but folded the bump into an `[A]` feature commit's body (e.g. "...promote CHANGELOG [Unreleased] to [0.7.1]") instead of giving it its own dedicated `[R] bump version` commit ([[feedback_commits]]). Follow-up `[F]` fix commits then added new `[Unreleased]` content without ever bumping again, so `pyproject.toml` silently fell one version behind the real unreleased state in both repos — surfaced only when the user noticed the reported version looked stale. Even when a version bump is bundled with real feature work, it must still be its own commit; never combine "bump version" into a commit whose primary bracket tag is `[A]`/`[F]`/etc.
