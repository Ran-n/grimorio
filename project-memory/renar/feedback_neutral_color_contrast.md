---
name: feedback-neutral-color-contrast
description: "whenever adding a user-customizable color (premium palette pickers, accents, badges), verify it stays visible against every background it can land on"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 99459b1b-01ba-4529-bf9f-9992dff9fb1c
---

Any UI element whose color is user-chosen from an open palette (especially one including true black/white/grey) must stay visually distinct regardless of what's behind or around it — never assume a saturated-color assumption holds for neutrals.

**Why:** Caught after shipping premium per-status accent colors on Library cards ([project-renar-images-webgl](project-renar-images-webgl.md) is a different bug, this is separate) — the accent bar and its settings-page preview were built without checking whether a black/white/grey pick would blend into the black gradient scrim or the page background. The app already had the right fix pattern (`needs_halo()` in `branding/__init__.py` — flags low-saturation/near-neutral colors) used for ring badges, capsule bars, and chips, but it wasn't carried over to the new feature. The user had to explicitly ask "did you keep in mind users may pick any color, and it stays visible against any background?" — this should be caught proactively, not on request.

**How to apply:** Before shipping any new control that renders a stored/user-picked color as a fill, bar, dot, or swatch, ask: (1) what's directly behind/around this element, and (2) does the palette allow near-black/near-white/near-grey values? If yes to both, either reuse `needs_halo()` (or an equivalent saturation check) to add a thin contrasting rim/border when the color is neutral, or use an always-present border regardless of color (like the palette swatch circles already do). Check every render site of the new color, not just the primary one — a settings-page preview needs the same treatment as the real in-app usage.
