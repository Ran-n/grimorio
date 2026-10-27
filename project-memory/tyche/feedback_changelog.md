---
name: changelog-must-be-up-to-date-before-committing
description: "Before every git commit, verify CHANGELOG.md reflects all unreleased changes; format and wording rules included"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2357ec0d-7eb6-4caf-86db-e0049e064f79
---

Update CHANGELOG.md only when preparing a commit — not during or after editing files.

**Why:** Updating it mid-session (before any commit is requested) is premature and adds noise. The user corrected this explicitly.

**How to apply:** Do not touch CHANGELOG.md unless the user has asked to commit. When a commit is requested, update CHANGELOG.md to reflect all staged changes and include it in the same commit.

## Format rules

- Keep a Changelog style: newest version at top; unreleased changes under `[Unreleased]`; on release, replace with `## [x.y.z] — YYYY-MM-DD`; group bullets under **Added**, **Changed**, **Deprecated**, **Removed**, **Fixed**, or **Security**.
- Write entries in past tense: "Added X", "Fixed Y", "Removed Z".
- One bullet per logical change; no trailing period.
- Be precise: name the specific thing that changed, not the general area. Bad: "Updated documentation." Good: "Added export compliance clause to PBL §7."
- Only record notable changes — skip internal refactors, formatting passes, typo fixes, and housekeeping unless they affect behavior or content.
- No filler. If a change can't fit in one tight line, split into two entries.
