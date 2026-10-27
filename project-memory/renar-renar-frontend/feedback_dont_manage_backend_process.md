---
name: feedback-dont-manage-backend-process
description: "Don't start/stop/restart the renar-backend process during normal dev work; exception granted for UI-verification workflows"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c1fe6874-d2f0-43fa-ba0c-887330a1dc3a
  modified: 2026-08-20T11:18:41.379Z
---

Don't kill, start, or restart the renar-backend `be.exe` process during
normal day-to-day dev work on your own initiative — that's still the
user's own terminal/workflow to manage.

**Exception (2026-08-20):** for UI-verification work specifically — using
[[renar-frontend-ui-verification-workflow]] to launch the frontend web
server + Playwright and screenshot a real change — the user explicitly
authorized starting/stopping the backend as needed, without asking each
time: "u start the backend, dont stop again for this kind of stuff you can
stop or start the backend when ur doing work." Applies to this verification
flow going forward; still don't touch the backend the user is running
themselves for anything else without asking.

**Why:** originally added because the user kept finding the backend
restarted out from under them mid-session during the Brevo/email-template
work ("kill the be, i run the be not you"). But UI verification needs a
live backend to log in against, and asking every time was friction the user
didn't want for that specific workflow — they'd rather grant standing
permission than be asked each time.

**How to apply:** for [[feedback-verify-after-every-change]]-style live app
checks in renar-frontend, start the backend yourself if it's not already
running, screenshot/verify, and leave it running afterward (don't stop it).
For any other renar-backend code/`.env` change, still just flag that a
restart is needed and let the user handle it themselves.
