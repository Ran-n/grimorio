---
name: feedback-verify-after-every-change
description: "After every code change, run the relevant test suite(s) AND actually launch/exercise the app before reporting done — unit tests alone aren't enough"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 75cbd50f-30c1-428d-a315-e669d7f1291c
  modified: 2026-08-13T14:40:10.702Z
---

After making any change, run tests and actually verify the app still works — don't stop at unit tests passing.

**Why:** a share feature change (2026-08-13) passed all 97 frontend unit tests and ruff checks while still shipping two real regressions — Pillow imported eagerly at module scope (slowing every cold start and common-screen visit) and a layout overflow in a tight grid cell — neither of which any unit test could catch, since this frontend has no true integration/E2E suite and unit tests don't render layouts or measure import cost. The user had to notice and report both by feel.

**How to apply:**
1. Run the relevant repo's pytest suite (`uv run pytest -q`) — renar-backend tests hit a real DB per [[feedback_tests]], the closest thing either repo has to integration coverage.
2. Run `uv run ruff format` + `uv run ruff check` on touched files per [[feedback_python_projects]].
3. For renar-frontend UI-visible changes specifically, unit tests are not sufficient — actually launch the app (the `run` skill, or manual relaunch per [[flet-apk-build-quirks]]/[[feedback_frontend_restart_required]] since Flet can silently serve stale code) and exercise the changed feature, not just import/construct it in isolation.
4. For a change touching a hot path (app startup, a commonly-visited screen), sanity-check its cost isn't regressing — e.g. time a fresh import of the touched module(s) — rather than assuming "it imports without error" means "it's cheap."
5. Do this for every change, not just large features — a small edit can still break layout or add import weight.
