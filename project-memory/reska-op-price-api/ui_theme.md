---
name: ui-theme
description: "Admin UI uses Gruvbox dark theme — CSS variables, topbar structure, card/button patterns all pages must follow"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 45277f82-b414-4265-a829-56372a28b15f
---

All admin HTML pages must use the **Gruvbox dark** theme defined in `admin.py`'s `_render()` function. Do not invent a new palette or use a different dark theme for a new page.

**Why:** The scrape-manager page (`scrape_manager.html`) originally used a mismatched indigo/slate palette (`#0f1117`, `#6366f1`) that clashed with the rest of the admin UI. User corrected this immediately.

**How to apply:**

CSS variables to use (copy exactly):
```css
--bg: #1d2021;
--surface: #282828;
--surface-hi: #32302f;
--border: #3c3836;
--border-sub: #32302f;
--text: #ebdbb2;
--text-2: #a89984;
--text-3: #7c6f64;
--accent: #d79921;
--violet: #d65d0e;
```

Structural patterns to follow:
- Topbar: `.topbar` with `.topbar-brand-link` (logo + brand-name + brand-sub), `.topbar-fill`, `.admin-pill` back link
- Logo: `width:30px; height:30px; background: linear-gradient(135deg, var(--accent), var(--violet)); border-radius:8px`
- Sections: `.card` > `.card-header` (with `.card-title`) > `.card-body`
- Buttons: `.btn-primary` (gradient accent/violet), `.btn-secondary` (transparent + border), `.btn-success` (green outline), `.btn-danger` (orange outline), all support `.btn-sm` modifier
- Inputs: `background: var(--bg); border: 1px solid var(--border); border-radius:8px; color: var(--text);` with focus ring `box-shadow: 0 0 0 3px rgba(215,153,33,.18)`
- Links/URLs in tables: `color: #fabd2f`
- Status text: `.status` (grey), `.status.ok` (`#b8bb26`), `.status.err` (`#fb4934`)

[[price-api-architecture]]
