---
name: project-breren-pages-restructure
description: "breren.com's served files live under public/, deployed via a GitHub Actions workflow instead of GitHub Pages' classic branch-deploy"
metadata: 
  node_type: memory
  type: project
  originSessionId: e4718233-675a-4cf1-99eb-e58fa9fd8d8c
  modified: 2026-08-05T07:38:40.873Z
---

As of 2026-08-05, everything actually served at breren.com (index.html,
about/, licenses/, vitralis/, common.css/common.js, icons/, links.toml,
translations.toml, CNAME, .nojekyll) lives under `public/` in the
`breren` repo. Repo-meta files (README, CHANGELOG, docs/, the license
text) stay at the top level.

**Why:** GitHub Pages' classic "deploy from a branch" source only
supports publishing from `/` or `/docs`, not an arbitrary folder name
like `public/`. `.github/workflows/deploy-pages.yml` publishes
`public/` via `actions/upload-pages-artifact` + `actions/deploy-pages`
on every push to `main`. The repo's Pages source setting was switched
from "deploy from a branch" to "GitHub Actions" (`build_type: workflow`
via the API) to match — this is a real, live setting on a
custom-domain (breren.com) site, not just a repo file.

**How to apply:** any further reorganization of what's under `public/`
doesn't need a settings change — the workflow already publishes
whatever's there. Only touch the Pages source setting again if the
deploy mechanism itself changes (e.g. reverting to branch-deploy).
See [[feedback-site-organization]] for the general rule this came from.
