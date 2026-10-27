---
name: Release dist attachments and timestamp preservation
description: When creating releases/tags or editing old commits/tags, attach all dist artifacts and preserve original timestamps
type: feedback
---

When doing a release, unless the user says otherwise, ship it in every way the project's stack can produce, and attach every artifact to the release on every forge the repo is on (GitHub, GitLab, Codeberg). Examples: `.whl` + `.tar.gz` always; `.exe`/Windows zip; for Flet apps every platform Flet builds from this machine — Android per-ABI split APKs **and** one universal APK, Windows zip, the web build (zip attached + published to the Pages sites); iOS/macOS/Linux only when a host for them is available (say so when skipped).

If a forge refuses a file (e.g. GitLab's 100 MB release-attachment cap on a universal APK), use that forge's documented route for large files (GitLab generic package registry, linked from the release) rather than dropping it.

**Why:** user wants every release to reach users on every platform and in every format, without having to ask for each one (confirmed 2026-10-13: "the release unless said otherwise should be in all possible ways… every platform and the apks split and global").

**How to apply:** on every release request — list the targets the stack supports, build all of them first (versioned filenames, see [[feedback_versioned_build_filenames]]), then tag and attach everything on all forges; report any target that couldn't be built and why.

---

When editing, resigning, amending, or in any way modifying old commits, tags, or releases, preserve ALL original metadata as exactly as possible: author date, committer date, tag date, tagger identity, and message. The goal is that the history looks unchanged — no items appear reordered or clustered to today's date.

For commits: capture `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE` before amending, then restore both explicitly.
For tags: record the original tag object date and tagger, then recreate with the same values.
For GitHub releases: preserve the original published/created date when editing via `gh release edit`.

**Why:** retroactive changes must not alter the historical ordering or timestamps of the record. Items re-stamped to today shift position in logs and release lists, making history misleading.

**How to apply:** on any history rewrite — capture all original timestamps and identities first, restore them explicitly in every amended object.
