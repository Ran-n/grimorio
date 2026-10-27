---
name: auto-version-bump-hook
description: "renar-frontend and renar-backend have a Stop hook that auto-bumps version+CHANGELOG after each turn's implementation work, patch/minor only, never major"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 1e50c662-7063-433c-a6fa-9c33a698530c
  modified: 2026-08-01T17:14:26.208Z
---

Both renar repos (`renar-frontend/.claude/settings.json` and
`renar-backend/.claude/settings.json`) have a `Stop`-event `agent` hook that
runs automatically after each turn: it checks for uncommitted changes, and
if real work was done (not just pyproject.toml/CHANGELOG churn), bumps the
version via `uv version --bump patch|minor` and promotes CHANGELOG
`[Unreleased]` — same mechanism as [[feedback_version_bump]], just fired
automatically instead of on the "bump" keyword.

**Why:** the user wants version bumps to happen automatically "after
implementing some stuff" — normally patch, minor when the diff adds a real
new capability — without having to say "bump" every time. They explicitly
chose an agent (not a fixed script) to judge patch vs. minor from the diff,
and explicitly excluded major/release bumps from automation — those stay
manual only ([[feedback_version_bump]], [[feedback_releases]]).

**How to apply:** don't manually bump versions after every change in these
two repos anymore during a live session — the Stop hook already does it.
Manual "bump" requests ([[feedback_version_bump]]) still work the same way
and remain the tool for explicit major bumps. The hook never commits/pushes
([[feedback_push]]) — it only edits pyproject.toml and CHANGELOG.md, so
those files may show as modified-but-uncommitted after a session even
without you asking for a bump.
