---
name: feedback-frontend-restart-required
description: "renar-frontend: a running Flet instance can silently serve stale code after edits (blank screens, no error) — always restart fully before calling a fix done"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 48092c58-515f-4f6d-9fb3-407706f55120
  modified: 2026-08-10T09:48:24.129Z
---

Editing renar-frontend source files while a Flet instance is already
running does not reliably hot-reload. The stale process can keep serving
old code with no visible error — e.g. the Home view went completely blank
(not even the loading spinner) after several view files were edited while
the app stayed open; the fix was simply relaunching, no code change needed.

**Why:** the user hit this directly ("fixed on relaunch but i dont want it
to happen ever again"). Silent staleness is worse than a crash — it looks
like a real bug, burns debugging time chasing code that's already correct,
and risks reporting "fixed" when only the stale instance was ever tested.
Same root cause as the process-hygiene lesson in
[[flet-snackbar-quirks]] (orphaned `flet.exe`/`python.exe` serving old
code) and the port-bind conflict this session hit trying to launch a
second instance for debugging (`OSError 10048` on `localhost:8080` —
proof an old instance was still alive).

**How to apply:** after making renar-frontend code changes, before
verifying a fix or telling the user it's done:
1. Check for an already-running instance (`flet.exe` process, or a
   listener on the app's port) rather than assuming a clean slate.
2. If one exists, don't silently kill it — the user runs/owns this
   process too (weaker version of [[feedback_dont_manage_backend_process]]:
   unlike the backend, I can relaunch the frontend myself, but say so
   first if a window is visibly open, since closing it loses their
   window/session state).
3. Once relaunched, confirm exactly one `flet.exe` exists before treating
   a test as valid — same instance-count check as the SnackBar lesson.
4. Never diagnose a frontend rendering bug (blank screen, stale UI,
   "changes aren't showing up") purely by reading code — reproduce it
   against a freshly relaunched instance first, since the running one may
   simply be stale.
