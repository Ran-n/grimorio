---
name: renar-dev-prod-domain-split
description: "renar-backend dev traffic uses api.dev.renar.app, prod uses api.renar.app; one SAN cert covers both; certbot is invoked via uvx, not a global install; Turnstile's domain allowlist has no API and must be edited by hand"
metadata: 
  node_type: memory
  type: project
  originSessionId: e8728fb8-3788-4d81-84d6-cd6d27fed7fc
  modified: 2026-08-21T11:59:52.562Z
---

As of 2026-08-21, `renar-backend` dev and prod traffic use separate
hostnames even though (today) they're the same physical server:

- Dev: `api.dev.renar.app` — `renar-frontend/.env`'s `DEV_RENAR_API_URL`
- Prod: `api.renar.app` — `renar-frontend/.env`'s `PROD_RENAR_API_URL`
  (baked into packaged builds by `uv run build`'s `--dev`/`--prod` flag,
  default `--prod`)

Both are separate Cloudflare DNS A records (same Cloudflare API token as
[[reference-cloudflare-token]]), currently pointing at the same origin.
One Let's Encrypt SAN cert covers both hostnames — issued/renewed with
`--cert-name api.renar.app --expand -d api.renar.app -d api.dev.renar.app`,
so a single renewal covers both; no separate cert-per-hostname.

**certbot is invoked via `uvx`, not a global install** — check
`certs/certbot-logs/letsencrypt.log` for `Location of certbot entry
point:` pointing into `uv`'s ephemeral tool cache
(`.cache\uv\archive-v0\...`) if this comes up again. Plain `certbot ...`
on PATH will fail with "not recognized" even in the right elevated shell;
the actual command is
`uvx --with certbot-dns-cloudflare certbot certonly --dns-cloudflare ...`
— still needs an Administrator PowerShell on Windows regardless (certbot's
own unconditional admin-rights check).

Local dev needs `127.0.0.1 api.dev.renar.app` in the Windows hosts file
(`C:\Windows\System32\drivers\etc\hosts`, elevated editor) — separate from
any `api.renar.app` entry added earlier. `https://localhost:8000` or
`https://127.0.0.1:8000` will never work once the backend has a real cert:
TLS hostname validation requires the literal hostname the cert was issued
for, not an IP.

**Turnstile's domain allowlist has no API access** — confirmed by testing
the DNS-edit Cloudflare token against
`/accounts/{id}/challenges/widgets`: `Authentication error`, even though
the same token works fine for DNS record calls. Every hostname that will
ever serve the Turnstile widget page (dev *and* prod) must be added by
hand in the Cloudflare dashboard: Turnstile → widget → Settings →
Domains. Forgetting to add a new hostname there produces a **completely
different symptom** from [[flet-webview-android-js-disabled]] — the page
loads and its script does run, but Cloudflare's own script silently
refuses to render a checkbox for an unrecognized hostname (also fails
silently, easy to conflate with the JS-disabled bug — check
`adb logcat` for any JS/console activity at all first to tell them apart).

**How to apply:** if `uv run app`/`uv run web` can't reach the backend
locally, check the hosts-file entry for the exact dev hostname before
assuming a code/network bug. If a *new* environment (staging, a second
dev machine, a domain rename) needs Turnstile, budget a manual dashboard
step — it can't be scripted with the credentials this project already has.
