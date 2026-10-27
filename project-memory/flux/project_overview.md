---
name: flux-project-overview
description: what the flux project is — a clipboard QR code GUI tool
metadata: 
  node_type: memory
  type: project
  originSessionId: 9b85014c-78b7-4b1b-84ef-5d9d99e1d30e
---

Single-file Python GUI app (`flux.pyw`) that reads text from the clipboard and displays a QR code using PyQt6 + qrcode + Pillow. Licensed under PayBack License (PBL) v1.0 — free for non-commercial use, revenue-share required for commercial use. Current version: **0.2.3**.

**Runtime deps:** pyperclip, qrcode, Pillow, pywin32 (Windows), PyQt6, flet.

**Features:** clipboard text hidden by default (eye toggle), click label to open full-text popup, right-click QR to copy image to clipboard (Windows win32clipboard / Linux xclip), pin button to keep open on focus loss, dark/light theme toggle (persisted via QSettings), frameless draggable window, auto-close on focus loss when unpinned.

**Architecture:**
- `ClipboardProvider` — reads clipboard via pyperclip
- `QRCodeGenerator` — generates + resizes QR image
- `FullTextDialog` — full-text popup
- `FluxWindow` — main UI
- `copy_image_to_clipboard` — platform-specific (win32clipboard / xclip)
- `_force_foreground` — Windows focus hack
- `build_stylesheet` — generates QSS from color dict (DARK/LIGHT themes)
- Inline SVG icon system (Lucide-style, rendered via QSvgRenderer)

**Repo files:** `flux.pyw`, `build.py` (PyInstaller wrapper, reads version from pyproject.toml, outputs to `build/dist/`), `make_icon.py`, `pyproject.toml`, `media/icon.png`, `media/icon.ico`, `LICENSE`, `README.md`.

**Dev deps:** pyinstaller, ruff. Python >=3.13.

**Why:** quick QR sharing tool for clipboard content.
**How to apply:** single-file, no build system, no tests. Keep it in one file unless the user says otherwise. Build via `python build.py`.
