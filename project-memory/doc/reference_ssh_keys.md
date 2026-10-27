---
name: SSH keys for git remotes
description: Which SSH key to use for GitHub/GitLab push; key location and config
type: reference
originSessionId: 9a3f4409-64b0-40d3-90f1-4416867daca8
---
All git pushes to GitHub and GitLab use SSH with the `gitcommitran` key.

- Key: `C:\Users\{USER}\.ssh\gitcommitran` (ed25519, comment: `ran.hash@proton.me`)
- SSH config entries in `C:\Users\{USER}\.ssh\config` map both `github.com` and `gitlab.com` to this key automatically — no `-i` flag needed.
- Remotes are set up with `git@github.com:...` / `git@gitlab.com:...` URLs, not HTTPS.
- `signing_key` is registered for commit signing only, not authentication.

**Why:** user switched all git remotes to SSH for consistency and security; HTTPS was only used initially before the key was set up.

**How to apply:** when setting up new git remotes, always use SSH URLs (`git@github.com:Ran-n/...`). Never use HTTPS URLs for GitHub or GitLab. The SSH config handles key selection automatically.
