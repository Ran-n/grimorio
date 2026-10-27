---
name: reference-page-handoff
description: "Cross-page theme/language hand-off mechanism and stable Pages URLs for Ran#'s properties"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 8ecc114c-207e-4045-93c0-fa380087ccc0
  modified: 2026-08-04T11:32:08.807Z
---

Ran#'s static pages hand off the visitor's current language/theme to each other via `postMessage`, so arriving at one page from another stays in sync instead of resetting.

- Message shape: `{ type: 'rn-preset', lang: '<2-letter code>', theme: 'light'|'dark' }`, applied unconditionally on every load (not just first-seed) — see vitralis commit `acf138a` for why "only seed if unset" was wrong (a manual in-page toggle would stick and never resync).
- Trusted origins allowlist (any of these may send/receive a preset, not just breren.com): `https://breren.com`, `https://ran-n.github.io`, `https://ran-n.gitlab.io`, `https://ran-n.codeberg.page`.
- localStorage keys: newer pages (e.g. `doc`) use generic `rn-lang`/`rn-theme` so preference can be shared across all pages under the same origin (GitHub/Codeberg Pages serve every Ran-n repo under one origin, just different paths). Older `vitralis` page still uses `vitralis-lang`/`vitralis-theme` — not yet migrated to the generic keys, only the origin-message convention.

**GitLab Pages note:** unique-domain mode gives each project a random hostname (e.g. `vitralis-2b19be.gitlab.io`) — unusable for a stable allowlist. Fixed by disabling `pages_unique_domain_enabled` via `glab api projects/<ns>%2F<repo>/pages -X PATCH -f "pages_unique_domain_enabled=false"`, giving the stable `ran-n.gitlab.io/<repo>` scheme that matches GitHub/Codeberg's pattern. Also had to flip `pages_access_level` from `private` to `enabled` via `glab api projects/<ns>%2F<repo> -X PUT -f "pages_access_level=enabled"` — GitLab defaults Pages access separately from repo visibility, so a public repo can still 403 on its Pages site until this is set.

Live pages as of 2026-08-04:
- vitralis: `ran-n.github.io/vitralis`, `ran-n.gitlab.io/vitralis`, `ran-n.codeberg.page/vitralis`
- doc (PBL version history): `ran-n.github.io/doc`, `ran-n.gitlab.io/doc`, `ran-n.codeberg.page/doc`

Codeberg Pages has no CI needed for the page to go live — pushing content directly to a `pages` branch (orphan, docs/ contents at root) is sufficient. The `.woodpecker.yml` in each repo automates that sync on future `docs/` pushes, but needs `codeberg_token` and `mail` secrets set in that repo's Woodpecker CI settings (an account action, not something doable from local tooling) — until set, syncing the `pages` branch after a `docs/` change is manual.
