---
name: License files — no metadata headers
description: Do not add metadatos headers to files inside the licenses/ folder
type: feedback
originSessionId: 7132f3cc-7909-41b4-9120-7c48eef359da
---
Do not run metadatos (`-c` or `-m`) on files inside `licenses/`.

**Why:** License files are canonical text — metadata timestamps are noise and clutter the content.

**How to apply:** Skip the metadatos step entirely for any file under `licenses/`, regardless of extension.

When editing `LICENSE`, always sync the corresponding versioned archive under `licenses/` by copying the file directly (e.g. `cp LICENSE licenses/pbl_v2.0.md`, or `licenses/pbl_v4.0.md` for v4.0, etc.) rather than applying the same edits twice. The versioned filename always matches the version declared in `LICENSE`.

**Why:** The two files are identical in content; copying is guaranteed to keep them in sync and avoids double-editing errors.

When reviewing the LICENSE file (on a loop or otherwise), fix all of the following:
- Errors (typos, broken sentences, wrong cross-references)
- Inconsistencies (conflicting clauses, duplicate definitions, mismatched terminology)
- Gaps (missing edge cases, unaddressed scenarios, loopholes)
- Improvements (clarity, precision, legal robustness)

**Why:** User explicitly asked for gap-fixing to be part of the review loop.
