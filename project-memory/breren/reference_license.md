---
name: custom-license
description: "User's custom license (PBL) — must be used in all projects, always copy the latest version"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 966c3227-c064-44ec-8a4f-fd4a5c3fbfa2
  modified: 2026-08-04T11:52:18.507Z
---

Always use the PayBack License (PBL) for every project. Fetch the latest version in this order (stop at first success):

1. Filesystem: `d:\Users\{USER}\sw\doc\LICENSE` (or equivalent `sw/doc` path on the current machine)
2. GitLab raw: `https://gitlab.com/Ran-n/doc/-/raw/main/LICENSE`
3. GitHub raw: `https://raw.githubusercontent.com/ran-n/doc/main/LICENSE`

- Never use MIT, Apache, or any other license
- In READMEs always link as `[PayBack License (PBL)](LICENSE)` (no hardcoded version number)
- **Do NOT read or parse the license file.** Always copy it directly using the shell: `Copy-Item "d:\Users\{USER}\sw\doc\LICENSE" LICENSE -Force` (or `cp` via Bash). Never reproduce it via Write/Edit tool calls.
- For a human-facing "License" link on a live web page (e.g. a site footer) — as opposed to a repo README link — point to the rendered doc site `https://ran-n.github.io/doc/`, not a raw GitHub file/blob URL. Corrected 2026-08-04 after linking breren's footer to the GitHub blob URL first.
