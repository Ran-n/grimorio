---
name: feedback-apk-stale-pycache
description: flet build zips __pycache__ verbatim into app.zip; a stale .pyc can silently override a bumped .py source on-device
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 10543cbe-17c1-4f2c-a6ed-3f72acbb0e53
---

`flet build apk` zips `tool.flet.app.path` verbatim into `app.zip`, including any leftover `__pycache__` directories. A `.pyc` compiled before a source edit still has old constants folded into its bytecode, and the packaged runtime's mtime-based staleness check doesn't reliably invalidate it after zip extraction on-device — so a stale compiled `.pyc` can silently ship instead of the edited `.py`.

Concretely: `src/renar_frontend/__pycache__/_version.cpython-314.pyc` had `"0.1.0"` baked in from before a version bump to `0.2.0`. The `.py` source was correctly `0.2.0`, but the installed APK still showed `0.1.0` — even on a build made *after* the bump — because the stale `.pyc` won.

**Why:** Android's extracted-app runtime doesn't recompile `.pyc` on mtime mismatch the way a normal filesystem does, so `__pycache__` acts as a silent staleness trap similar to [[feedback_flet_split_apk_staleness]].

**How to apply:** `renar_frontend/launcher.py`'s `build()` now calls `_clear_app_pycache()` first, which `rglob`s and deletes every `__pycache__` under the app source before each build. If APK-displayed version (or any other baked-in constant) ever looks stale again despite correct source and a build timestamp after the edit, suspect a leftover `.pyc` shipped in `app.zip` — inspect via `zipfile` on `assets/flutter_assets/app/app.zip` inside the APK, not just the source tree.
