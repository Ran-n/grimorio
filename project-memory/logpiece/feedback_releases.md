---
name: release-dist-attachments-and-timestamp-preservation
description: "When creating releases/tags or editing old commits/tags, attach all dist artifacts and preserve original timestamps"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8d6ce87f-ebe4-4c7f-9a7c-dc4de50180fd
---

When doing a release, build all available dist artifacts and attach them to the git release tag (e.g. via `gh release create` or equivalent). Examples: `.exe` (PyInstaller), `.whl`, `.tar.gz`.

**Why:** user wants every release tag to ship all distribution formats.

**How to apply:** on every release request — build all dist targets first, then create the tag and attach all artifacts.

---

When editing, resigning, amending, or in any way modifying old commits, tags, or releases, preserve ALL original metadata as exactly as possible: author date, committer date, tag date, tagger identity, and message. The goal is that the history looks unchanged — no items appear reordered or clustered to today's date.

For commits: capture `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE` before amending, then restore both explicitly.
For tags: record the original tag object date and tagger, then recreate with the same values.
For GitHub releases: preserve the original published/created date when editing via `gh release edit`.

**Why:** retroactive changes must not alter the historical ordering or timestamps of the record. Items re-stamped to today shift position in logs and release lists, making history misleading.

**How to apply:** on any history rewrite — capture all original timestamps and identities first, restore them explicitly in every amended object.
