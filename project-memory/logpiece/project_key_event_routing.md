---
name: project_key_event_routing
description: How key events are routed in logpiece — app-level filter in CardBrowserPanel owns all browser shortcuts; CardImageWidget has no keyPressEvent
metadata: 
  node_type: memory
  type: project
  originSessionId: 52e6909a-1c50-47a4-8190-b5db271d71f5
---

`CardBrowserPanel.__init__` installs itself as an **app-level event filter** (`QApplication.instance().installEventFilter(self)`). This filter intercepts every key press before any widget's `keyPressEvent` fires, as long as the browser panel is on screen.

All NAIP and card navigation shortcuts (`prev_card`, `next_card`, `prev_naip`, `next_naip`, `delete_naip`, `toggle_errata`, `toggle_star`, `create_naip`, `modify_naip`, `displace_naip_left`, `displace_naip_right`) are handled inside `CardBrowserPanel.eventFilter` in `card_browser.py` and routed through `self._detail` (a `CardDetailPanel`), which exposes proxy methods (`toggle_errata_naip`, `toggle_star_naip`, `create_naip`, `modify_naip`, `displace_naip_left`, `displace_naip_right`, `delete_current_naip`) that delegate to `self._img` (a `CardImageWidget`).

`CardImageWidget.keyPressEvent` has been **removed** and the widget's focus policy set to `NoFocus`. Do not add shortcuts there.

**Why:** The filter was introduced to allow global shortcuts (Up/Down to change card, Left/Right to change NAIP) regardless of which child widget has focus.

**How to apply:** When adding any new browser-scope shortcut:
1. Add the shortcut ID + default to `SHORTCUT_DEFS` in `settings/_defaults.py`
2. Handle it in `CardBrowserPanel.eventFilter` in `card_browser.py`, routing through `self._detail`
3. Add a proxy method on `CardDetailPanel` if needed
4. Add the shortcut to the correct section in `_SECTIONS` in `shortcuts.py` so it appears in the shortcuts editor
