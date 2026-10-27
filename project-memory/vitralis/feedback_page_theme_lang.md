---
name: feedback-page-theme-lang
description: "Default theming and language pattern for any new Ran# static/landing page"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8ecc114c-207e-4045-93c0-fa380087ccc0
  modified: 2026-08-04T11:31:53.362Z
---

Every new static page across Ran#'s properties (breren.com, vitralis's `docs/index.html`, `doc`'s license page, and any future one) should ship with breren.com's gruvbox light/dark toggle and the same 8-language picker (gl, en, es, pt, fr, de, zh, ja), not a plain single-language page.

**Why:** user explicitly asked to "remember" this after the `doc` repo's PBL version-history page was first built as a deliberately simple, single-language page — that was the wrong default. Confirmed by "retrofit this page now + remember for future" when asked.

**How to apply:**
- Reuse breren.com/vitralis's exact CSS custom-property palette (`--bg`, `--card-bg`, `--accent`, etc. under `:root[data-theme="dark"|"light"]`) and the `lang-picker`/`theme-btn` markup+JS (flag SVGs, `SUPPORTED`/`LANGUAGES`/`STRINGS` dict, `detectLang`/`applyTheme`/`effectiveTheme`) — see [[reference_page_handoff]] for the exact mechanism and current source of truth.
- UI chrome (nav, headings, buttons) gets translated into all 8 languages; long legal/reference text (e.g. license bodies) stays English-only as the source of truth — don't attempt to translate multi-thousand-line legal documents.
- Apply this by default to new pages without being asked again; only skip it if the user explicitly asks for something simpler for a specific page.
