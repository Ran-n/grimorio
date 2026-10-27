---
name: flet-cross-target-ui-testing
description: How to drive a Flet app's real UI on web (Playwright) and Android (emulator + adb) in tests, and the gotchas that broke it; timtapper is the reference implementation
metadata:
  type: reference
---

Reference implementation: timtapper `tests/rendered/targets.py`, `scripts/android_phone.py`, `scripts/driven_main.py`, `scripts/build_driven.py`, `scripts/serve_site.py` (2026-10-13/14). One rendered suite runs on every target through a per-target adapter ([[tests-requirement]] "Same test depth on every UI target").

**Architecture.** The desktop driver runs the app in-process (commands on stdin). Web and Android run a *driven build*: a staged copy of the project with the demo driver beside main.py, built with `flet build <web|apk> <stage> --module-name driven_main`. The app polls the test harness over HTTP: same origin on web (`pyodide.http.pyfetch`), `127.0.0.1:<port>` + `adb reverse` on Android (plain urllib in `asyncio.to_thread`). The driven APK gets its own `--bundle-id` (never replaces the real app), is debug-signed and built with `--arch x86_64` only. Size the browser viewport and the phone (`wm size`) to the desktop client area in dp, so assertions mean the same thing everywhere.

**Gotchas (each cost a debugging round):**
- Python logs from a Flet APK go to logcat tag `flet.python`, so platform tests can wait on log lines, like the browser console on web.
- Phones use Flutter's standard visual density, desktop and web use compact: fields and segments are taller, so less fits on screen. Tests must scroll until the target is visible, never assume a fixed scroll distance or that N rows fit.
- `adb shell input keycombination` ctrl+a does NOT select all in a Flutter field. Clear with KEYCODE_MOVE_END + N backspaces. `input text` sends ASCII only.
- Flutter ignores touches while a dialog animates in, but the a11y tree (uiautomator) already lists its buttons. Wait until the element's position is stable AND the app area stops changing before tapping.
- `uiautomator dump /dev/tty` exposes Flutter semantics: tap by label. Prefer exact label matches ("Preview the file x.json" contains "x.json"; "Restore this backup?" contains "Restore").
- The status bar's pixel height changes with `wm size` (cutout scaling), and readings right after `wm size` are stale. Re-measure after the bars stop changing, and iterate the size until the app area is exact.
- Compare "screen settled" on the app area only: the emulator's status-bar network icons flicker.
- The emulator shows the soft keyboard over the app despite `hw.keyboard=yes`. Set `settings put secure show_ime_with_hard_keyboard 0` for the session and restore it afterwards ([[cleanup-own-resources]]).
- DocumentsUI opens on "Recent". A pushed file shows only under Show roots → Downloads (after a `MEDIA_SCANNER_SCAN_FILE` broadcast), or in Recent once it has been picked before.
- After hours of installs and resizes the emulator can degrade (stale windows, a soft restart). Kill it and cold-boot.
- Web (Playwright): use touch taps (`has_touch=True`) and park the mouse at (-1, -1) after wheel scrolls, or hover states leak into the captures. Chrome anti-aliases text more: exact-colour blobs are smaller, so use a lower `min_area`.
- On Windows, the Flet client exe is named after the app when run from the project root (`timtapper.exe`), `flet.exe` otherwise. VS Code titles its window after the workspace folder, so find the app's window by title AND owning exe.
- Desktop Flet `prefix_icon_size_constraints` on TextField had no visible effect (Flet 1.0.4).
- A focused search field's blinking caret makes snapshots flaky: ignore its box in the comparison.
