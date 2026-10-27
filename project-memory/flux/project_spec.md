---
name: flux-project-spec
description: "UX, behaviour, and technical requirements for flux — source of truth; read at session start; update only on explicit user confirmation"
metadata: 
  node_type: memory
  type: project
  originSessionId: 9b85014c-78b7-4b1b-84ef-5d9d99e1d30e
---

## Overview
flux is a single-file PyQt6 desktop tool that reads the system clipboard and displays the text as a QR code. Goal: frictionless clipboard→QR in one motion, no account, no sync service.

## UX Requirements

### Window
- Frameless, always-on-top, fixed width (380 px), draggable by any non-interactive surface.
- Positions itself at the cursor's screen on launch.
- Auto-closes on focus loss when **unpinned**.
- On launch, attempts to force foreground focus (Windows: `_force_foreground` via win32 API; retries up to 5× via QTimer at 50 ms intervals).

### Title Bar
- App icon (16×16) + "flux" label.
- Right-side icon buttons: theme toggle, pin, close.
- No window chrome; all three buttons are custom SVG icon buttons.

### Clipboard Row
- Clipboard text is **hidden by default** — shown as bullet dots (`•` × min(len, 16)).
- Eye button toggles visibility. When visible: truncated preview (42 chars + `…`).
- Clicking the label (when visible) opens `FullTextDialog`.
- When text is hidden, clicking the label does nothing.

### QR Area
- QR code rendered in a white-background framed panel, centered.
- Right-click on QR image → copies image to clipboard.
  - Windows: `win32clipboard` (CF_DIB).
  - Linux: `xclip` via subprocess.
- Left-click on QR image → initiates window drag.
- On copy: animated status label fades in/out (opacity animation, `OutCubic` easing).
- If clipboard is empty or text exceeds QR capacity (version 40, ECL M): show error label instead of QR.

### FullTextDialog
- Frameless, draggable, 520×340.
- Read-only QTextEdit with monospace font.
- Closes on: X button, Escape, Q, or focus loss when parent is unpinned.
- Positioned at parent's center on open.

### Pin Behaviour
- Unpinned (default): window and any open FullTextDialog close on focus loss.
- Pinned: window stays open. Pin button changes to `icon_btn_active` style (accent background, white lock icon).
- Unpinning closes any open FullTextDialog.

### Theme
- Dark (default) / Light toggle. Persisted via QSettings (`"flux"/"flux"`).
- Full QSS rebuild on toggle via `build_stylesheet(c: dict)`.
- Theme icon: sun (in dark mode) / moon (in light mode).

### Persistent Settings (QSettings)
- `dark_mode` (bool, default `True`)
- `text_visible` (bool, default `False`)
- `pinned` (bool, default `False`)

## Technical Requirements

### Stack
- Python ≥ 3.13
- PyQt6 ≥ 6.11.0
- qrcode ≥ 8.0 + Pillow ≥ 11.0.0
- pyperclip ≥ 1.9.0 (clipboard read)
- pywin32 ≥ 308 (Windows clipboard image write)
- flet ≥ 0.25.0 (listed as dependency; not used in current UI)

### Structure
- Single file: `flux.pyw`. Do not split into multiple files unless user explicitly asks.
- No build system, no tests.
- `build.py` — PyInstaller wrapper; reads version from `pyproject.toml`; outputs to `build/dist/flux-<version>.exe`.
- `make_icon.py` — generates `media/icon.ico` manually with struct (multiple sizes).
- `media/icon.png` and `media/icon.ico` bundled.

### Icon Resolution
- `_BASE = Path(getattr(sys, "_MEIPASS", Path(__file__).parent))` — resolves correctly when frozen by PyInstaller.

### QR Generation
- `QRCodeGenerator(box_size=8, border=3, max_size=320)` — generates PIL Image, resizes if over 320 px.
- Error correction level: default (M).

### SVG Icons
- Inline Lucide-style SVG bodies in `_SVG_BODIES` dict; rendered to `QPixmap` via `QSvgRenderer`.
- Icons: `sun`, `moon`, `eye`, `eye_off`, `x`, `lock`, `lock_open`.

### Shutdown
- No background threads. QApplication event loop only. Clean shutdown on window close is automatic.

## Constraints
- Windows-primary. Linux supported for clipboard image copy (xclip). macOS not explicitly targeted.
- No network access, no file I/O beyond QSettings and icon load.
- No i18n — UI strings are English only, no translation layer.
