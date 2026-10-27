---
name: feedback_ui_action_buttons
description: "Always build action buttons the standard way — objectName actionBtn, DIMS sizes, svg_icon with p(\"ACCENT\"), no custom fills or overrides"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2f11e97a-7788-40d5-9e54-ec39d3c7ca67
---

For any icon-only action button, always use the exact standard pattern:

```python
btn = QPushButton()
btn.setObjectName("actionBtn")
btn.setFixedSize(DIMS["ACTION_BTN"], DIMS["ACTION_BTN"])
btn.setIconSize(QSize(DIMS["ACTION_ICON"], DIMS["ACTION_ICON"]))
btn.setIcon(_svg("icon-name", p("ACCENT"), DIMS["ACTION_ICON"]))
btn.setToolTip("...")
```

Never hand-roll sizes, colors, or stylesheet overrides for these buttons. The global `#actionBtn` stylesheet handles background, border, hover, pressed, and disabled states automatically.

SVG files must use `fill="currentColor"` (not hardcoded hex) so tinting works.

**Why:** Repeatedly diverged from this pattern — set wrong colors (`TEXT_SEC` instead of `ACCENT`), added unnecessary local `#actionBtn` stylesheet overrides, used non-standard sizes — causing multiple rounds of broken visuals.

**How to apply:** Every time a new action button is needed, copy this pattern verbatim. Do not invent variations. Check any new SVG icon for hardcoded `fill="#..."` before using it.
