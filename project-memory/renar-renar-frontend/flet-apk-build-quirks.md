---
name: flet-apk-build-quirks
description: "How to build the Android APK for renar-frontend on this Windows machine (UTF-8 env vars required, known dependency pitfalls)"
metadata: 
  node_type: memory
  type: project
  originSessionId: d1fef3a8-9fe6-4b52-a42d-482bcbd08fce
  modified: 2026-07-29T21:02:47.408Z
---

Build the APK with: `$env:PYTHONUTF8='1'; $env:PYTHONIOENCODING='utf-8'; .venv\Scripts\flet.exe build apk` — output lands in `build\apk\app-release.apk`. Default build produces one universal `renar-frontend.apk` (~79MB, too big for Telegram's 50MB limit). To get per-ABI splits (arm64-v8a ~35MB etc.) use `--split-per-abi` **alone, without `--arch`** — this produces all three ABI splits (arm64-v8a/armeabi-v7a/x86_64) in `build\apk\`, just pick the arm64-v8a one for the phone. `--arch arm64-v8a` alone is silently ignored (still builds universal).

**Never combine `--split-per-abi` with `--arch arm64`** — confirmed on 2026-07-29 this silently drops `libpythonsitepackages.so` (i.e. ALL third-party deps: httpx, certifi, flet-webview, everything, not just one package) from every split APK, with no warning/error in the build output (exit code 0, "Successfully built" banner shown normally). The app then crashes at launch with `ModuleNotFoundError: No module named 'certifi'` (or whatever import happens first). Verify any split build by unzipping the apk and checking `lib/arm64-v8a/libpythonsitepackages.so` exists (`unzip -l app.apk | grep sitepackages`) before shipping it — don't trust "Successfully built" alone. `--split-per-abi` alone without `--arch` was verified to bundle site-packages correctly.

**Why:** Without `PYTHONUTF8=1`, `flet build` crashes immediately on this machine with `UnicodeEncodeError: 'charmap' codec can't encode '●'` (rich spinner char vs cp1252 console).

**How to apply:** Always set the UTF-8 env vars before any `flet build`/`flet run` invocation on this machine. Other pitfalls already fixed in the repo (July 2026): `path_provider_foundation` pinned to 2.4.1 via `[tool.flet.flutter.pubspec.dependency_overrides]` in pyproject.toml (newer versions pull objective_c >= 9.2 which needs Dart native-assets and breaks the build); avoid Python deps without Android wheels (blake3 was removed for this reason — Rust/C packages need prebuilt Android wheels from pypi.flet.dev). If the build fails oddly after a flet version change, delete `build\flutter` and `build\.hash` to force clean regeneration.

Runtime gotchas on Android: never pass an explicit `port=` to `ft.app()` when packaged — flet then opens a TCP server while the Flutter shell connects via unix socket (`FLET_SERVER_UDS_PATH`), giving a permanently black screen with no error in logcat (main.py guards on that env var now). The Android bundle runs Python 3.12 regardless of `requires-python`, so avoid 3.13+/3.14-only syntax. Install to the Redmi Note 8 Pro (MIUI) via `adb install`: needs "Install via USB" enabled in Developer options and the user tapping the on-phone popup, else `INSTALL_FAILED_USER_RESTRICTED`; phone storage must have headroom or install fails with "not enough space" (`adb shell pm trim-caches 8G` frees cache). Debug a black screen with `adb shell screencap -p /sdcard/screen.png` + `adb pull` (PowerShell `>` corrupts binary adb output).
