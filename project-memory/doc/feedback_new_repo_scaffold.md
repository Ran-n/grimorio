---
name: New repository scaffold
description: Files to always create when initializing a new repository for the user
type: feedback
originSessionId: 5ef410f2-fc84-4182-8255-387ba472868b
---
Every new repository must include these files from the start — no need to be asked:

- `LICENSE` — PayBack License (PBL), fetched verbatim from https://github.com/ran-n/doc/blob/main/LICENSE
- `CHANGELOG.md` — date-only headers (`## [YYYY-MM-DD]`), no semver, no `[Unreleased]` block
- `CONTRIBUTING.md` — standard section layout (see reference_contributing_layout.md)
- `README.md` — must have a License section linking as `[PayBack License (PBL)](LICENSE)`
- `CONTRIBUTORS` — contributor list file

**Why:** User confirmed this is the standard set for every project.

**How to apply:** When scaffolding or initializing any new repository, create all five files automatically without prompting.
