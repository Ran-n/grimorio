---
name: Releases and timestamp preservation
description: Preserve all original metadata when editing commits/tags/releases; attach all dist artifacts on new releases
type: feedback
---

When editing, resigning, amending, or modifying old commits, tags, or releases in any way, preserve ALL original metadata: author date, committer date, tag date, tagger identity, and message. Use `GIT_AUTHOR_DATE`/`GIT_COMMITTER_DATE` for commits; recreate tag objects with original date/tagger. Goal: history ordering and timestamps look unchanged.

When creating a new release, build all available dist artifacts and attach them to the tag (e.g. via `gh release create`). Examples: `.exe`, `.whl`, `.tar.gz`.

**Why:** retroactive changes must not alter historical ordering; every release tag should ship all distribution formats.

**How to apply:** on any history rewrite — capture all original timestamps and identities first, restore them explicitly. On new releases — build all dist targets first.
