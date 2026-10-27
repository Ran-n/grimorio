---
name: feedback-ui-verification-account-cleanup
description: "Delete any account created by ad-hoc UI verification scripts against the real backend, at end of session"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 41f1bb2f-458b-4916-bcdd-37da38522c1f
  modified: 2026-08-20T15:54:15.792Z
---

Ad-hoc Playwright/manual verification scripts (see [[renar-frontend-ui-verification-workflow]]) run against the real backend at `http://127.0.0.1:8000` — the Flet web server's `RENAR_API_URL` defaults there unless overridden. Unlike the pytest suite ([[renar-frontend-ui-verification-workflow]]'s isolated-schema fixtures, and `tests/integration/conftest.py` in renar-frontend), these accounts land in the real dev DB and are never auto-cleaned.

On 2026-08-20, 22 leftover test accounts (`tmdblogo*`, `verifybot*`, `clautest_*`, `e2etest*`, `herotest*`, `pgtest_*`, `qatestA/B`, `dbgtest_*`, `sharetest01`, `screenshottest`) had accumulated in the live User Manager and had to be manually identified and deleted via the admin panel.

**Why:** scratchpad verification scripts (`D:\tmp\*.py`) register throwaway accounts to exercise UI flows but have no teardown step; nothing else cleans them up.

<!-- private -->
-----BEGIN PGP MESSAGE-----

hF4DQ/EuiSPJ5t0SAQdAZEzRU48cDV3eOo2/UueScjfZ66mRIQkQIm7JLXgoFF0w
EdF6Y1CoP9ai+OiKO/yTakGfEEdy2u46fa/OGYbyBTjQi7e+V9X7Tz+8aq+euTVg
1MEKAQkCEEcIwslLHjvdaj+aZiLgXlh6BGh/CX7Xfq7LD1Ba4HJKcUHwMpWymXWI
XyKOajygN7AfbFRzpFMQz9BHYbRFHWjiniNR0flj2ejEDFPXK/bjd2pjKbyTOLlR
s/jRYqyhZ5lbWhWd61p38SIWtQN4DDI8Jqmgnzv4cRUGzJBcwDHm3kwe7uWyHuy9
9A47drfG6AHE+VvNDrgQU0eCmLfSkfQozdA22f5ego9lVvTrbbWygz9xzLPJ1Zpd
7nySnFuCYxxJ9kZvWTPxIQ3P997RDqbaoOssA+eZsQOs4EB0c9QTKAy9Bo+6vJ1r
AE/d5x2Sk4lkzwAAH1VJ4913/PPclDleekiA+vXgoV6dJBKAaPbjvLo7/stof+hK
9Up2vdARfnu/dk8E3LxnxH9NPTsvedWeQ+RKo1dz/VulfKGckMjW+QmLGcJvjj4r
Ytaz3l2xD7LHRQUMlC+jPvqeQ7OAKQjFrcpEzS/z/pA9xJ8+FAPeV9jGi0OiJPOn
+o3+x/Gs9Eb7rz69V3oZ+SHpUtzkxE17HHWdsW5fwSmsJXYqBn8QXxNxXWt9RNo/
/IZI/vCZulrmXZLgooUZvXCo4cRNwMITU2Z7jW0=
=w0o5
-----END PGP MESSAGE-----
<!-- /private -->
