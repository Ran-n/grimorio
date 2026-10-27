---
name: feedback_flet_split_apk_staleness
description: flet build apk without --split-per-abi silently ships stale per-ABI split APKs
metadata:
  type: feedback
---

`flet build apk` (no flags) only rebuilds the **universal** APK. If per-ABI split APKs (`*-arm64-v8a.apk`, `*-armeabi-v7a.apk`, `*-x86_64.apk`) already exist in `build/apk/` from an earlier `--split-per-abi` run, they get silently copied forward unchanged on every later plain `flet build apk` run — even though the universal build picks up fresh source. The mtime on the split files looks plausible (build tooling touches them), so nothing visibly signals staleness.

**Why:** Root cause is `build/flutter/build/app/outputs/`: `apk/release/app-release.apk` (universal, gradle's default flavor) rebuilds every run, but `flutter-apk/app-<abi>-release.apk` (the splits) only regenerate when `--split-per-abi` is passed again. A plain run leaves those split files exactly as they were, and `flet build apk`'s "Copying build to build\apk directory" step copies them forward without checking freshness. Caught this because a rebuilt arm64 APK sent to a user was missing an entire new source file that had been added hours earlier — `--clear-cache` alone did *not* fix it, only `rm -rf build/apk build/flutter` + `--split-per-abi` did.

**How to apply:** Whenever building a split/per-ABI APK to hand off (not just the universal one):
1. Pass `--split-per-abi` explicitly on every build, not just the first time.
2. If in doubt, `rm -rf build/apk build/flutter` first for a guaranteed-clean rebuild — `--clear-cache` on its own was insufficient in the one case tested. **Caveat (confirmed 2026-07-18, renar-frontend):** `rm -rf build/apk build/flutter` alone can itself break the build if the project's launcher wrapper stamps a flet-version marker at `build/.flet_build_version` (its own staleness guard, see `_clear_stale_flutter_template()`): with `build/flutter` gone but the stamp file still present and matching the installed flet version, the wrapper sees "no version change" and skips regenerating `build/flutter`, so packaging runs with `cwd=<missing dir>` and Windows raises `NotADirectoryError: [WinError 267]`. Fix is `rm -rf build` (the whole directory, not just `build/apk build/flutter`) so the stamp is cleared too and the wrapper rebuilds the template from scratch.
3. Before sending/shipping, verify freshness directly: unzip the APK's `assets/flutter_assets/app/app.zip` and check that a recently-changed source file is actually inside (e.g. `unzip -l app.zip | grep <recent_file>`), rather than trusting build-step success messages or file mtimes.

See also [[project_apk_build]] (renar-frontend's specific build command) if mirrored into a project's memory.
