---
name: version-bump-workflow
description: "User bumps the version in pyproject.toml; only then update CHANGELOG [Unreleased] to that version"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8d7c8811-3237-44ca-b785-02c23ca6a52f
---

Never bump `version` in `pyproject.toml` proactively. The user updates the version themselves, then asks to update the changelog. At that point, read the new version from `pyproject.toml` and promote `[Unreleased]` to `[X.Y.Z] - YYYY-MM-DD`.

**Why:** User controls release versioning; Claude touching it jumped ahead of their process.

**How to apply:** When asked to "update the changelog" or "set the versions", read `pyproject.toml` first, use whatever version is there, and only touch `CHANGELOG.md` — never `pyproject.toml`.
