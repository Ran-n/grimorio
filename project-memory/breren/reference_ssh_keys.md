---
name: ssh-keys-for-git-remotes
description: Which SSH key to use for GitHub/GitLab/Bitbucket/Codeberg push; key location and config
metadata: 
  node_type: memory
  type: reference
  originSessionId: c4dba393-f0dd-432c-a851-6d69e4824dee
  modified: 2026-07-30T12:15:48.388Z
---

All git pushes to GitHub, GitLab, Bitbucket, and Codeberg use SSH with the `gitcommitran` key.

- Key: `C:\Users\{USER}\.ssh\gitcommitran` (ed25519, comment: `ran.hash@proton.me`)
- SSH config entries in `C:\Users\{USER}\.ssh\config` map `github.com`, `gitlab.com`, `bitbucket.org`, and `codeberg.org` to this key automatically — no `-i` flag needed.
- Remotes are set up with `git@github.com:...` / `git@gitlab.com:...` / `git@bitbucket.org:...` / `git@codeberg.org:...` URLs, not HTTPS.

**Why:** user uses SSH for consistency and security across all remotes.

**How to apply:** when setting up new git remotes, always use SSH URLs. Never use HTTPS URLs. The SSH config handles key selection automatically.

**Codeberg "Permission denied (publickey)" despite the key being registered:** seen 2026-07-30 on the breren repo — `ssh -T git@codeberg.org` and `git push codeberg` both rejected the key even though `GET /api/v1/user/keys` showed it registered with the matching fingerprint and the repo had `push: true`. The server-side `authorized_keys` had apparently gone stale. Fix: via the Forgejo REST API (see `reference_codeberg_token.md`), `DELETE /api/v1/user/keys/{id}` then `POST /api/v1/user/keys` with the same public key content — this forces Codeberg to regenerate the entry, and the push worked immediately after. No local (client-side) config was wrong.
