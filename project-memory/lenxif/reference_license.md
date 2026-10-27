---
name: Custom License
description: User's custom license (PBL) — must be used in all projects, always copy the latest version
type: reference
originSessionId: b1919612-18b3-42e2-826b-d27f7852ca1c
---
Always use the PayBack License (PBL) for every project. Fetch the latest version in this order (stop at first success):

1. Filesystem: `d:\Users\{USER}\sw\doc\LICENSE` (or equivalent `sw/doc` path on the current machine)
2. GitLab raw: `https://gitlab.com/Ran-n/doc/-/raw/main/LICENSE`
3. GitHub raw: `https://raw.githubusercontent.com/ran-n/doc/main/LICENSE`

- Never use MIT, Apache, or any other license
- In READMEs always link as `[PayBack License (PBL)](LICENSE)` (no hardcoded version number)
- Copy the fetched file verbatim; do not edit it
