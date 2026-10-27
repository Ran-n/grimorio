---
name: feedback_ui_icon_buttons
description: "Close buttons (and all action buttons) must use SVG icons, never text labels or Unicode glyphs"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 913b0ea9-01b9-46f4-95f8-346950a65d77
---

All buttons must use SVG icons via `svg_icon()` — never text labels, Unicode characters (e.g. `"✕"`, `"×"`), or emoji. This applies globally to every dialog, widget, and panel in the project.

**Why:** User explicitly stated this as a global directive. Text-based buttons are inconsistent with the app's icon-driven UI language.

**How to apply:** When creating any button — close, confirm, cancel, or action — always call `svg_icon(name, color, size)` and `setIcon()`/`setIconSize()`. Use `x.svg` for close/dismiss, `check.svg` for confirm, `trash.svg` for delete, etc. Never write `QPushButton("✕")` or similar.
