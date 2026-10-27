---
name: feedback-renar-abuse-guard-exempt-ips
description: "renar-backend: any new ban/strike-tracking code path must check site_settings.exempt_ips first, or it can end up banning the exempt IPs it's supposed to protect"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: b7879d2f-deaf-4547-bd64-d1cb7a324509
  modified: 2026-08-20T08:50:37.331Z
---

Any new abuse-tracking logic added in renar-backend (strikes, bans, rate limits — anywhere calling `strike_and_maybe_ban`/`permaban`) must check `site_settings.current().exempt_ips` first and skip tracking entirely for a match, the same way the main `AbuseGuardMiddleware.dispatch` does (`users/security.py`).

**Why:** `127.0.0.1`/`::1` are exempt by default as "monitoring, local tooling". When adding failure-tracking to `/svc/bans`+`/svc/strikes`'s `_require_internal_secret` (routers/svc.py) to close a probe-scanner gap, the first pass banned by raw `client_ip(request)` with no exempt check — since the frontend's anti-abuse calls that route from localhost, a stale/misconfigured secret there would have banned the machine running both frontend and backend. Caught only because the user asked "those were localhost right?" after seeing the fix — not caught by tests, since the existing test suite has no precedent for simulating a specific client IP (TestClient always reports `"testclient"`, distinct from `127.0.0.1`).

**How to apply:** before writing any new call to `strike_and_maybe_ban`/`permaban` outside the existing `AbuseGuardMiddleware.dispatch`, add the exempt-IP check first. See [[feedback-renar-bcnf]] for the sibling "always re-verify this class of invariant on every new touch point" pattern in this repo.
