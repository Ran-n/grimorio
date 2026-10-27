---
name: reference-breren
description: "breren.com is Anxo's personal brand/site project — used as the style reference for other personal pages like arbore"
metadata: 
  node_type: memory
  type: reference
  originSessionId: ce587a27-9ffc-4ab0-af18-96805e37200d
  modified: 2026-08-24T11:49:26.291Z
---

`D:\Users\{USER}\sw\breren` is Anxo's personal-brand site (breren.com), a link dashboard in the style of Heimdall/Homer, published via GitHub Pages from `public/`. Shared look lives in `public/common.css` and `public/common.js`: Gruvbox palette with light/dark toggle (`prefers-color-scheme` + `data-theme` override, remembered via `localStorage`), and a language picker (flag+name trigger button opening a dropdown listbox, SVG flags defined inline since emoji flags don't render everywhere) supporting ~24 languages with Galego pinned first.

When Anxo asks to match "the style" of another personal project without naming it, check `d:\Users\{USER}\sw\breren\public\common.css`/`common.js` first — see [[feedback_arbore_design]] for an example of adapting it (arbore project copied the toolbar/picker pattern but swapped out the actual gruvbox colors).
