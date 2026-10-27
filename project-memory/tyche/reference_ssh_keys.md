---
name: ssh-keys-for-git-remotes
description: Which SSH key to use for GitHub/GitLab push; key location and config
metadata: 
  node_type: memory
  type: reference
  originSessionId: 2357ec0d-7eb6-4caf-86db-e0049e064f79
---

All git pushes to GitHub and GitLab use SSH with the `gitcommitran` key.

- Key: `C:\Users\{USER}\.ssh\gitcommitran` (ed25519, comment: `ran.hash@proton.me`)
- SSH config entries in `C:\Users\{USER}\.ssh\config` map both `github.com` and `gitlab.com` to this key automatically — no `-i` flag needed.
- Remotes are set up with `git@github.com:...` / `git@gitlab.com:...` URLs, not HTTPS.

**Why:** user switched all git remotes to SSH for consistency and security; HTTPS was only used initially before the key was set up.

**How to apply:** when setting up new git remotes, always use SSH URLs (`git@github.com:Ran-n/...`). Never use HTTPS URLs for GitHub or GitLab. The SSH config handles key selection automatically.
