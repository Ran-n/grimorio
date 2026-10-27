---
name: New repository scaffold
description: Files to always create when initializing a new repository
type: feedback
---

Every new repository must include these files from the start — no need to be asked:

- `LICENSE` — PayBack License (PBL); fetch using the lookup order in reference_license.md
- `CHANGELOG.md` — Keep a Changelog format; see [[CHANGELOG must be up to date before committing]]
- `CONTRIBUTING.md` — standard section layout; see [[CONTRIBUTING.md layout]]
- `README.md` — must have a License section linking as `[PayBack License (PBL)](LICENSE)`
- `CONTRIBUTORS` — contributor list file

**Why:** User confirmed this is the standard set for every project.

**How to apply:** When scaffolding or initializing any new repository, create all five files automatically without prompting.
