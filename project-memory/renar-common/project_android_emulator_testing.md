---
name: project-android-emulator-testing
description: "Android emulator is set up locally for adb-driven APK testing (install, launch, logcat, screenshot) without leaving the terminal"
metadata: 
  node_type: memory
  type: project
  originSessionId: 8184d47a-17a1-44fc-874c-c49dd495372a
  modified: 2026-07-27T09:24:09.809Z
---

Android SDK + emulator is fully set up on this machine for testing renar APKs end-to-end via adb, no manual phone or Android Studio UI needed.

**Setup (already done, 2026-07-27):**
- SDK root: `C:\Users\{USER}\Android\sdk` (cmdline-tools, platform-tools, build-tools, platforms already present)
- Installed via `sdkmanager`: `emulator` package + `system-images;android-34;google_apis;x86_64`
- AVD created via `avdmanager`: name `renar_test`, device profile `pixel_6`, Android 14 (API 34), x86_64
- Required Windows feature: **Windows Hypervisor Platform (WHPX)** — separate from Hyper-V, enabled via `dism /online /enable-feature /featurename:HypervisorPlatform /all` + reboot. Without it the emulator refuses to boot x86_64 images at all ("hypervisor driver is not installed").

**How to test an APK:**
1. Boot emulator: `C:\Users\{USER}\Android\sdk\emulator\emulator.exe -avd renar_test` (takes ~30-60s to register in `adb devices`)
2. Build renar APK per [[project_apk_build]] (`uv run build apk --split-per-abi` in renar-frontend)
3. Install the **x86_64** variant (matches this emulator's CPU, not arm64-v8a which is for real device delivery): `adb install -r build\apk\renar-frontend-x86_64.apk`
4. Launch: `adb shell monkey -p com.breren.renar_frontend -c android.intent.category.LAUNCHER 1`
5. Check for crashes: `adb logcat -c` then `adb logcat -d *:E`
6. Screenshot: `adb exec-out screencap -p > out.png`, view with Read tool

Package name: `com.breren.renar_frontend`.

**Why:** supersedes the old limitation in [[feedback_no_flet_browser_tool]] (that one is specifically about the Flet *web* canvas, which still has no browser-automation tool — the Android emulator is a separate, working path for real on-device verification).

**How to apply:** when asked to test/verify a renar-frontend change on Android, to confirm an APK build actually works, or when the user says something like "test this real quick" / "check if it works on the phone" — use this emulator flow instead of just doing a code review / boot-log check. If the emulator isn't already running, boot it first (step 1) before building, so the wait overlaps with the build.
