---
name: versioned-build-filenames
description: Every build artifact Claude produces (.apk, .exe, .whl, .zip, …) must carry the app version in its filename
metadata:
  type: feedback
---

Every build output I produce or hand over (APK, EXE, installer, zip, wheel, sdist, any dist file) must include the app's current version in its filename, e.g. `timtapper-0.4.2-arm64-v8a.apk`, `renar-frontend-1.3.0.exe`. Read the version from the project's source of truth (`pyproject.toml` / `uv version --short`), never hardcode it.

If the build tool emits an unversioned name (e.g. `flet build apk` → `app-arm64-v8a.apk`, PyInstaller → `app.exe`), rename/copy it to the versioned name before delivering, attaching to a release, or sending via Telegram. Prefer configuring the tool or the project's build script to emit the versioned name directly so it sticks. In projects with a custom build script (e.g. renar-frontend's `uv run build`), the versioned name belongs in that script.

**Why:** the user has asked for this in several projects (renar among them) and doesn't want to repeat it; unversioned files are indistinguishable once downloaded or shared.

**How to apply:** on every build in every project — check the output filename includes the version before reporting the build as done. Applies alongside [[feedback_releases]] and [[feedback_apk_telegram_delivery]].
