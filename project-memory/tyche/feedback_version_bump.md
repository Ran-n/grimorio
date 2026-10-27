---
name: version-bump-workflow
description: "User bumps the version in pyproject.toml; only then promote [Unreleased] to that version in CHANGELOG"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2357ec0d-7eb6-4caf-86db-e0049e064f79
---

Never bump `version` in `pyproject.toml` proactively. The user updates the version themselves, then asks to update the changelog. At that point, read the new version from `pyproject.toml` and promote `[Unreleased]` to `[X.Y.Z] - YYYY-MM-DD`.

**Why:** User controls release versioning; Claude touching it jumped ahead of their process.

**How to apply:** When asked to "update the changelog" or "set the versions", read `pyproject.toml` first, use whatever version is there, and only touch `CHANGELOG.md` — never `pyproject.toml`.
