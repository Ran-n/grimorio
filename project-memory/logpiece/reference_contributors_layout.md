---
name: contributors-layout
description: Exact CONTRIBUTORS file format mandated by PBL v2.0 clause 18; use for all projects under this license
metadata: 
  node_type: memory
  type: reference
  originSessionId: 0e22badb-5e0f-43e1-96b9-5c7c935ed5e5
---

Format mandated by PBL v2.0, clause 18. Must be followed exactly.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 CONTRIBUTORS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

 Authoritative record of ownership and revenue shares for this project.
 Governed by the PayBack License (PBL) v2.0.

──────────────────────────────────────────────────────────────────────────
 LEGEND
──────────────────────────────────────────────────────────────────────────

 ⁕     founder
 [x%]  undiluted floor

──────────────────────────────────────────────────────────────────────────
 SUMMARY                                    OWNERSHIP    REVENUE
──────────────────────────────────────────────────────────────────────────

 ⁕ <Pseudonym>                              100% [30%]   100% [30%]

──────────────────────────────────────────────────────────────────────────
 DETAILS
──────────────────────────────────────────────────────────────────────────

 ⁕ <Pseudonym>
   Pseudonym            <Pseudonym>
   Name                 <Legal Name>
   Role                 Founder
   Email                <email>
   GPG                  <full 40-char fingerprint, space-separated pairs>
   Ownership            100% [30%]
   Revenue              100% [30%]
   Commercial-Agent     (optional)
   Successor-Ownership  (optional)
   Successor-Revenue    (optional)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Field rules:**
- `⁕` marks the Founder entry
- `[x%]` = undiluted floor; cannot be diluted by new contributors
- SUMMARY is a quick-reference table; DETAILS has full entries
- `Pseudonym` = public identity; `Name` = legal name (private, for legal proceedings)
- `GPG` = full fingerprint used for signing ballots
- `Ownership` total across all entries must equal 100%
- `Revenue` values are resolved percentages (no dynamic placeholders)
- `Commercial-Agent`, `Successor-Ownership`, `Successor-Revenue` are optional; omit line or leave blank
- For contributors (non-Founder): no `Commercial-Agent` field; `Successor-Ownership` only if ownership > 0%

**User's values:** [[author-identity]]
- Pseudonym: `Ran#`
- Email: `ran.hash@proton.me`
- GPG: (retrieve with `gpg --list-keys ran.hash@proton.me`)
