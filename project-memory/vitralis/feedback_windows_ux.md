---
name: Window UX conventions
description: All floating windows must be draggable, have a consistent close button, and Esc closes the topmost open window first
type: feedback
originSessionId: d9987a30-23ce-4ae1-88ca-33e015cc7b95
---
All secondary windows (SnapshotWindow, SettingsWindow, any future panels) must follow these conventions:

1. **Draggable** — implement `mousePressEvent` / `mouseMoveEvent` / `mouseReleaseEvent` on the widget itself so the user can drag the window by clicking anywhere on its background.

2. **Close button** — top-right corner, `"✕"` text, `danger_btn()` style, fixed size 22×22. Title row: `[title label, stretch=1] [close_btn]`.

3. **Esc closes topmost** — Esc on the main toolbar closes the snapshot window first, then settings window, then quits. Each secondary window also binds its own `QShortcut(Escape)` → `self.close`.

4. **Grey out unavailable buttons** — buttons must be disabled (`setEnabled(False)`) when their action can't apply. Reconnect `itemSelectionChanged` and any relevant input signals to an `_update_buttons()` method that sets state. Example rules for snapshot panel: Save enabled when name typed or exactly 1 selected; Load enabled when exactly 1 selected; Delete enabled when ≥1 selected. The visual disabled appearance is baked into `base_btn()` via `QPushButton:disabled { background: rgba(255,255,255,5); color: rgba(255,255,255,30); }` — all button helpers inherit this automatically.

**Why:** user feedback — windows felt unmoored without drag, X placement was inconsistent, Esc quitting the whole app while a panel was open was jarring, and clickable-but-noop buttons were confusing.

**How to apply:** apply to every new `QWidget` panel added to Vitralis.
