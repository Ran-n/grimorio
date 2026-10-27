---
name: release-dist-attachments-and-timestamp-preservation
description: "When creating releases/tags or editing old commits/tags, attach all dist artifacts and preserve original timestamps"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 53532e8b-f785-4b95-b670-f3695028a191
---

When doing a release, build all available dist artifacts and attach them to the git release tag. Examples: `.exe` (PyInstaller), `.whl`, `.tar.gz`.

**Why:** user wants every release tag to ship all distribution formats.

**How to apply:** on every release request — build all dist targets first, then create the tag and attach all artifacts.

---

When editing, resigning, amending, or in any way modifying old commits, tags, or releases, preserve ALL original metadata: author date, committer date, tag date, tagger identity, and message.

For commits: capture `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE` before amending, then restore both explicitly.
For tags: record the original tag object date and tagger, then recreate with the same values.
For GitHub releases: preserve the original published/created date when editing via `gh release edit`.

**Why:** retroactive changes must not alter the historical ordering or timestamps of the record.
