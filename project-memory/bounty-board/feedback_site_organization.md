---
name: feedback-site-organization
description: static sites/web projects must keep served files grouped in a dedicated folder, separate from repo-meta files, even if it requires a build/deploy step
metadata:
  type: feedback
---

Every site/web project must stay ordered and tidy: files actually served
to visitors (index.html, pages, stylesheets, scripts, icons/assets,
config like links.toml) belong grouped under one dedicated folder (e.g.
`public/`), never scattered loose at the repo root. Repo-meta files
(README, CHANGELOG, LICENSE, CONTRIBUTING, docs/) stay at the top level,
separate from what's served.

**Why:** requested explicitly while reorganizing breren.com — its
dashboard, about/licenses/vitralis pages, and shared assets were flat
at the repo root next to README/CHANGELOG/docs/; the user wanted them
grouped and confirmed this is a general standing rule ("sites always
have to be ordered and be tidy like this"), not a one-off for that repo.

**How to apply:** when starting or reorganizing any static site/web
project, group served files under one folder (ask what to name it if
unclear — industry-standard picks like `public/` are a safe default).
If the hosting platform can't natively serve from that subfolder (e.g.
GitHub Pages' classic branch-deploy only supports `/` or `/docs`), add
a minimal build/deploy step (GitHub Actions publishing the folder as
the Pages artifact, or equivalent) rather than leaving files flat to
dodge the tooling gap. Confirm before flipping any live deploy/hosting
setting, since it affects a real production site.
