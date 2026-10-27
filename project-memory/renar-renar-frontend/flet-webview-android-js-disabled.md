---
name: flet-webview-android-js-disabled
description: flet_webview leaves JavaScript disabled by default on Android/iOS/macOS; must call set_javascript_mode after mount or embedded pages silently never execute JS
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e8728fb8-3788-4d81-84d6-cd6d27fed7fc
  modified: 2026-08-21T11:59:35.538Z
---

`flet_webview`'s Android/iOS/macOS backend (`webview_mobile_and_mac.dart`)
never calls `WebViewController.setJavaScriptMode` — Flutter's own default
for `webview_flutter`'s Android backend is JavaScript **disabled**. Any
control embedding a page that needs JS to render (Cloudflare Turnstile,
reCAPTCHA, any JS-driven widget) will load the HTML fine (plain GET, no JS
needed for that) but the page's own `<script>` tags never execute — no
errors, no console output, nothing. It looks exactly like a server-side
misconfiguration (wrong domain, blocked CSP, bad cert) because the failure
is completely silent.

**Fix:** after the `WebView` control is created and `page.update()` has
mounted it, call `await webview.set_javascript_mode(JavaScriptMode.UNRESTRICTED)`
(both from `flet_webview`). This is an async invoke-method call requiring
the control to already be in a live page tree — calling it before mounting
raises `RuntimeError: Control must be added to the page first`. Only valid
on Android/iOS/macOS; `webview_web.dart` (Flet's web build) maps the
control to a real browser `<iframe>` which already has JS on and doesn't
even implement this method — guard the call to those platforms only.

**Why:** cost a full debugging pass in [[renar-dev-prod-domain-split]]'s
session chasing Turnstile widget recreation, Cloudflare dashboard domain
edits, and a SAN cert expansion before `adb logcat` showing zero JS/console
activity after a confirmed page load (200 in the backend access log)
pointed at JavaScript being off rather than anything server-side.

**How to apply:** any time a `flet_webview.WebView` embeds a page that
needs to *run* JS (not just serve static/server-rendered content) on
mobile/desktop-app builds — check `set_javascript_mode` was called, first,
before investigating server-side causes for a "loads but does nothing"
symptom.

**Diagnostic technique that found this:** `adb logcat` filtered to the
app's PID (`adb shell pidof <package>`, then
`adb logcat -d --pid=<pid>`) showed WebView engine init but zero
JS/console/network activity after the widget page's confirmed successful
load — normal Android WebView forwards JS `console.*` to logcat via the
`chromium` tag automatically, so total silence after a real page load is a
strong signal JS itself never ran. `adb devices -l` needs the phone's
"Allow USB debugging" popup tapped on-device before it flips from
`unauthorized` to `device`. Chrome's `chrome://inspect#devices` remote
debugging is a dead end unless the app itself called
`WebView.setWebContentsDebuggingEnabled(true)` — checked via
`adb shell cat /proc/net/unix | grep webview_devtools`; absence means no
socket, so don't send the user chasing that path without checking first.
