---
name: feedback_apk_telegram_delivery
description: When to build+deliver the renar-frontend (formerly xoutaim-frontend) APK via Telegram vs. normal file delivery
metadata:
  type: feedback
---

Whenever the user says "send me the apk", build it fresh (`PYTHONUTF8=1 uv run flet build apk` — see project-local memory `project_apk_build`) and deliver it by sending to their Telegram via the bot (see [[reference_telegram_bot_token]]), always — not just via SendUserFile.

**Why:** User wants the APK on their phone via Telegram every time, regardless of whether the session is on Remote Control or at the desktop.

**How to apply:** Always push the built APK to Telegram for "send me the apk" requests. Use the arm64-v8a build (universal is too big for the Telegram Bot API's 50MB limit). SendUserFile can be used in addition, but Telegram delivery is not conditional on Remote Control. This is specific to the renar-frontend project (formerly named xoutaim-frontend — same project, same build wrapper, folder/package renamed; see its project-local memory).
