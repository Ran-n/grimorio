---
name: feedback_apk_telegram_delivery
description: When to build+deliver the renar-frontend APK via Telegram vs. normal file delivery
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 82a0006a-2f96-43d9-9723-daa27d0fd22c
---

Only build and send the APK when the user explicitly asks (e.g. "send me the apk") in that specific turn — never proactively, even right after a round of UI/feature changes to renar-frontend that would obviously affect the app. Building the APK as part of finishing unrelated work and sending it unprompted is NOT wanted.

When the user does ask, build it fresh (`PYTHONUTF8=1 uv run flet build apk` — see project-local memory `project_apk_build`) and deliver it by sending to their Telegram via the bot (see [[reference_telegram_bot_token]]), always — not just via SendUserFile.

**Why:** User corrected this directly ("dont send me anything unless i tell you to") after several proactive sends during a multi-round session of UI changes. Wanting the APK on Telegram (not just SendUserFile) when asked is still correct — the mistake was sending without being asked at all.

**How to apply:** Never build/send an APK as a side-effect of finishing other renar-frontend work. Wait for an explicit request each time. Once asked, always push the built APK to Telegram (arm64-v8a build — universal is too big for the Bot API's 50MB limit); SendUserFile can be used in addition, but Telegram delivery is not conditional on Remote Control. This is specific to the renar-frontend project (see its project-local memory).
