---
name: project_apk_build
description: How to build and deliver the renar-frontend Android APK
metadata: 
  node_type: memory
  type: project
  originSessionId: 206055b2-d397-4b7e-8a82-69edd728e350
---

Build command (current, as of 2026-07-18): `cd renar-frontend && uv run build apk --split-per-abi` (or `--split` shorthand — the wrapper maps it).

**Why:** The project grew its own build wrapper — `src/renar_frontend/launcher.py:build()`, exposed via the `build` script in `pyproject.toml` (`[project.scripts] build = "renar_frontend.launcher:build"`) — that replaces calling `flet build` directly:
- Auto-sets `PYTHONUTF8=1` and re-execs itself in a fresh subprocess with it (fixes the same Windows `UnicodeEncodeError` on the `●` spinner glyph that used to require manually prefixing `PYTHONUTF8=1`; **no longer needed manually**).
- Stamps the app version from `pyproject.toml` into `_version.py` before building (packaged app has no dist metadata/pyproject.toml on-device to read it from otherwise).
- Clears `build/flutter` (the cached Flutter/Gradle bootstrap template) whenever the installed flet version differs from the last stamped one — this fixes a *separate* staleness bug from the split-ABI one below: the template cache doesn't invalidate on a flet version bump, so old/new Gradle templates coexist and can break the build (hit this on the 0.28→0.85 migration).

If ever bypassing the wrapper and calling `flet build` directly, the old manual steps still apply: prefix `PYTHONUTF8=1`, and `--split-per-abi` is not optional — see [[feedback_flet_split_apk_staleness]]. Without it, a plain `flet build apk` only refreshes the universal APK; the arm64/armeabi/x86_64 splits already sitting in `build/apk/` from an earlier `--split-per-abi` run get silently copied forward stale, even though the build reports success. `--clear-cache` alone does not fix this — confirmed by shipping a stale arm64 APK that was missing an entire new source file. If in doubt, `rm -rf build/apk build/flutter` first for a guaranteed-clean rebuild — but if that alone fails with `NotADirectoryError: [WinError 267]` during packaging, it's because `build/.flet_build_version` (the wrapper's own `_clear_stale_flutter_template()` staleness stamp) survived the partial delete and still matches the installed flet version, so the wrapper skips regenerating `build/flutter` — use `rm -rf build` (the whole directory) instead.

Output lands in `renar-frontend/build/apk/`. As of the 2026-07-14 verification, a `--split-per-abi` build only produced the three ABI splits (no universal `renar-frontend.apk` alongside them — worth re-checking if a universal file is needed):
- `renar-frontend-arm64-v8a.apk` — ~28MB, covers virtually all modern Android phones — use this one for Telegram delivery
- `renar-frontend-armeabi-v7a.apk`, `renar-frontend-x86_64.apk` — other ABIs
- (older builds also produced `renar-frontend.apk`, universal, ~72MB, too big for Telegram Bot API's 50MB limit — if it reappears, still skip it for Telegram delivery)

**Before sending, verify freshness:** unzip the target APK's `assets/flutter_assets/app/app.zip` and confirm a recently-changed source file is actually inside, e.g.:
`unzip -p renar-frontend-arm64-v8a.apk assets/flutter_assets/app/app.zip > /tmp/app.zip && unzip -l /tmp/app.zip | grep <recent_file>`
Don't trust the build's success message or file mtimes alone.

**How to apply:** When asked to build and send the APK, use `uv run build apk --split-per-abi`, verify the arm64 APK's contents as above, then send that variant to Telegram (see [[reference_telegram_bot_token]]) rather than the universal build.
