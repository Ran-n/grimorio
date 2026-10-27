---
name: project-cert-renewal-routine
description: "Scheduled cloud routine watching breren.com's GitHub Pages cert renewal"
metadata: 
  node_type: memory
  type: project
  originSessionId: b75f4d14-b866-4ede-8e56-54bc3f7850d6
  modified: 2026-07-21T17:43:42.080Z
---

<!-- private -->
-----BEGIN PGP MESSAGE-----

hF4DQ/EuiSPJ5t0SAQdAV6lnw4QlaPK7dTGzQFWjn19rcfeMXrGUE0osZNhBUUUw
k98tuGGPptV83sP6o/RYsGO7iecVp6zFIB6Mr6znTrSqxsGHFOI4brq8KqPXan7L
1LABCQIQmBTGrPCQkM4+h/srDIswPBgNO3RJkGdxbJzARV5/A0aPDfweyXhf6F3b
jJVn455lSv+Ww3EGHetqOrDL8hErrT3oz7PB7D1iPgl+d73VmkLteaYw7ktJ0m50
BPGJL+XslXc04KTZY9DgiOFx+oQZJLtlzqoWj9Pv8Yi+cL2HsEYWPR5iCzAElAuk
57J3fVTBiYc0wzZOT8FOlzIL5OTRzTcrPtBvM+gpym83ew==
=km4E
-----END PGP MESSAGE-----
<!-- /private -->
for 2026-10-15T07:00:00Z. It checks whether breren.com's GitHub Pages
HTTPS certificate (issued 2026-07-21, expires 2026-10-19) has auto-renewed.

**Why:** the 8 apex DNS records for breren.com (4 A + 4 AAAA, Cloudflare
<!-- private -->
-----BEGIN PGP MESSAGE-----

hF4DQ/EuiSPJ5t0SAQdADCqN1xo2BzDDuSmoC32fGQopVW8t/+n8bSXRKUbQkEQw
bHqZ3u1d05mLJdhs0JD19aggQDP50QtCpTTjy2NsD4O+Z5RwKEuRZ0SoqnzT1hh3
1IwBCQIQc9JmQbNmktY3X8vAz9cjbcbI4kroM81emhLFFQ4Ka+ew5+L97qQ1aGFY
FWhq3gTp8VbtguWISvHUIDH56iJj+Ti9Noa86MkU4CcQwn7Yaq3s5StlW3TqdJ8s
K5euMaqDM/VJT6wapWh2Uh1Gni72FyewaTHNZ4FdiDBYUFCWlOqewA6/znFfKQ==
=uA1O
-----END PGP MESSAGE-----
<!-- /private -->
(matching the existing `tyche.breren.com` setup), which *may* interfere
with Let's Encrypt's renewal validation the same way it could have
blocked initial issuance.

The routine is intentionally read-only: it only checks
`https_certificate.expires_at`/`state` via GitHub's public API and
messages the result — it holds no Cloudflare credentials and cannot
modify DNS itself (user chose this over a fully autonomous fix-it
version, specifically to avoid the token living in two places). If it
reports the cert hasn't renewed, the actual DNS unproxy/reproxy fix is
manual — done by hand or in a live session using
[[reference-cloudflare-token]] from local memory.

**How to apply:** if asked about breren.com's HTTPS/cert status, check
whether this routine already fired and what it reported before
re-investigating from scratch. If the cert renews cleanly on GitHub's
own and this routine turns out unnecessary, it's safe to ignore/let it
report a no-op.
