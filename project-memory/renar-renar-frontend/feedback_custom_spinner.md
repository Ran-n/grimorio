---
name: feedback-custom-spinner
description: "Always use the app's own animated logo mark as the loading spinner, never a generic ft.ProgressRing"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 72c12944-5741-4f48-853a-0f0336c3d354
  modified: 2026-07-28T10:56:59.840Z
---

Any loading/busy indicator in renar-frontend must use the brand mark, not a generic `ft.ProgressRing`. The existing helper is `loading_row(page)` in `views/ui.py` (wraps `branding.animated_logo`, picks the light/dark variant automatically) — reuse it, or `branding.pulsing_logo`/`animated_logo` directly for a different size/layout, instead of reaching for `ft.ProgressRing`.

**Why:** user corrected a busy-state spinner I added to the poster/backdrop alternates picker (`open_alternate_image_picker` in `views/ui.py`) that used `ft.ProgressRing` — "the loader spinner is not the correct one, I ALWAYS want my custom one."

**How to apply:** whenever adding a new loading/busy overlay anywhere in this app, default to `loading_row()`/the animated logo mark. Treat a bare `ft.ProgressRing` (or `ft.CircularProgressIndicator`) appearing in new code as a mistake to fix, not a stylistic choice. See [[flet-apk-build-quirks]] for other renar-frontend UI conventions.
