---
name: project-tcg-plus-probing
description: "bounty_board — probing the TCG+ API trips a firewall 403; the website's cancel route is gone (404) since 2026-10"
metadata:
  node_type: memory
  type: project
  originSessionId: e9810db4-81b1-44c8-99b8-e5b563d8c104
  modified: 2026-10-27T10:47:11.141Z
---

Probing many TCG+ API write routes in a row (about 50 DELETE/POST/PUT requests on 2026-10-19) made `api.bandai-tcg-plus.com` answer a plain nginx "403 Forbidden" to every write request from that IP, while GETs still worked.

**Why:** the store-entry cancel (`DELETE /api/user/{id}/register`, what the TCG+ website's own bundle still calls) answers 404 Symfony "No route found" for any ID and User-Agent. An unsigned request tells an existing route (401) from a missing one (404), so probing looked attractive, but the firewall cut it off before the real endpoint was found.

**How to apply:** don't burst-probe the TCG+ API. To find the real cancel endpoint, have the user capture it (browser dev tools on the website, or HTTP Toolkit/mitmproxy on the phone app) and test one request at a time. Related: [[feedback-no-silent-failure]].

2026-10-27: the site's bundle (`bundle.js?20261027121035`) still calls `DELETE /api/user/{id}/register` with `{cancel_reason: 4}` (5 for "within two hours" auto-cancels); no other cancel route in it. The app now cancels in its own TCG+ window instead (`SignInWindow.visit`: the player's token is put in the site's localStorage, then the event page opens). Whether the site's own button works there is unconfirmed until tried on a real entry.
Same day: user confirmed cancelling on the website works. The app now sends the withdraw from inside a TCG+ page in the hidden `PageWindow` (`fetch` with axios's headers, origin www.bandai-tcg-plus.com); the visible window is only the fallback. Not yet confirmed against a real entry.
ROOT CAUSE (2026-10-27): the 404 "no route" was a missing `X-Accept-Version: v1` header (the site's script sets it on every call; Symfony routes the withdraw only in v1). Recorded site call: same DELETE + body → HTTP 204 (empty body). Sending from a hidden page did NOT help (still 404 without the header); that path was removed. The app now sends the header on every call.
