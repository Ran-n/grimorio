---
name: timtapper-version-file
description: "timtapper keeps its version in two places; `uv version --bump` only updates pyproject.toml, so core/version.py must be edited in the same bump commit"
metadata:
  node_type: memory
  type: project
  originSessionId: 0741ec54-3556-4502-b3cd-1ccea27bf5ff
  modified: 2026-10-11T23:22:58.088Z
---

timtapper's Settings → About reads `VERSION` from `src/timtapper/core/version.py`, a hand-kept copy of the
`pyproject.toml` version (flet build ships no package metadata). `uv version --bump` does not touch it.

**Why:** the 0.3.0 bump (2026-10-12) updated only pyproject.toml; Settings showed 0.2.0 and
`tests/test_version.py` failed on the pushed main until a follow-up fix commit.

**How to apply:** on every bump in this repo ([[version-bump-workflow]]), set `VERSION` in `core/version.py` to the new
version and run `tests/test_version.py` before the `[R] bump version` commit.
