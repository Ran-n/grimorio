---
name: CHANGELOG must be up to date before committing
description: Before every git commit, verify CHANGELOG.md reflects all unreleased changes; format and wording rules included
type: feedback
originSessionId: 7b4f139b-dfa0-4e46-9ff1-d42787d816fe
---
Update CHANGELOG.md only when preparing a commit — not after every edit session.

**Why:** User corrected premature CHANGELOG updates that happened mid-session before any commit was requested.

**How to apply:** Do not touch CHANGELOG.md during or after editing files unless the user has explicitly asked to commit. When a commit is requested, update CHANGELOG.md to reflect all staged changes and include it in the same commit.

## Format rules

- Keep a Changelog style: newest version at top; unreleased changes under `[Unreleased]`; on release, replace with `## [x.y.z] — YYYY-MM-DD`; group bullets under **Added**, **Changed**, **Deprecated**, **Removed**, **Fixed**, or **Security**.
- Write entries in past tense: "Added X", "Fixed Y", "Removed Z".
- One bullet per logical change; no trailing period.
- Be precise and concise: name the specific thing that changed, not the general area. Bad: "Updated documentation." Good: "Added export compliance clause to PBL §7."
- Only record changes that are notable to a reader — skip internal refactors, formatting passes, typo fixes, and housekeeping unless they affect behavior or content.
- No filler, no padding. If a change can't be summarized in one tight line, it probably needs two separate entries.
