---
name: project_android_webview_cleartext
description: "Android WebView blocks plain-HTTP by default (API 28+), independent of the app's own httpx traffic — the fix and its fragility"
metadata: 
  node_type: memory
  type: project
  originSessionId: cb8c5ccd-877c-4b9f-8202-693c30edaf36
---

renar-frontend's register screen loads Cloudflare Turnstile in a `flet_webview.WebView` (`views/auth/turnstile_field.py`). Android blocks cleartext (`http://`) traffic for the system WebView component by default since API 28 — but this does **not** affect the app's own `httpx`-based API calls (Python's own socket stack, a completely different network path from Android's WebView/OkHttp policy enforcement). Symptom: login/register/polling all worked fine over `http://api.renar.breren.com:8882`, but the WebView showed "Webpage not available" for the exact same host — same request, two different cleartext policies.

Fix: hand-added `android:usesCleartextTraffic="true"` to `build/flutter/android/app/src/main/AndroidManifest.xml` after `flet build apk` generates it. `flet_cli` has no build option/pyproject key for this attribute (checked: only permissions/features/meta-data/providers are exposed).

**Why:** the register screen's own Server field explicitly documents self-hosted `http://` LAN servers as a supported use case (hint text: `http://192.168.1.50:8000`), so this isn't just a localhost-dev workaround — cleartext support is a real standing requirement, independent of whether the "real" deployment eventually gets HTTPS.

**How to apply:** this is a manual edit to a *generated* file (`build/flutter/`), not something in `pyproject.toml` — it survives ordinary repeat `uv run build apk` runs (flet's `create_flutter_project()` cookiecutter re-render is hash-gated on template inputs and skips when nothing changed) but **silently disappears** whenever `build/flutter` gets wiped: a flet version bump, `--clear-cache`, or a fresh checkout. If the Turnstile widget ever shows "Webpage not available" again after a rebuild, re-check/re-add this attribute *before* re-diagnosing from scratch. Full writeup: `renar-frontend/docs/design-decisions.md`, "Android APK manifest is hand-patched for usesCleartextTraffic" entry.

**Superseded by (parked, not done):** real HTTPS on `api.renar.breren.com`, which sidesteps the whole policy. Blocked on: port 80 on that host is already owned by an unrelated Kestrel service, so plain Let's Encrypt HTTP-01 can't run there. Options raised: `certbot-dns-cloudflare` (DNS is on Cloudflare) for DNS-01, or simplest — flip the `api` DNS record to Cloudflare-proxied ("orange cloud") for free automatic edge TLS with zero cert management on this host, using SSL mode "Flexible" so the origin keeps serving plain HTTP internally. See [[project_renar_layout]] and [[reference_turnstile_keys]].
