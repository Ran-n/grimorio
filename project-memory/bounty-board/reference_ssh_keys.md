---
name: SSH keys for git remotes
description: Which SSH key to use for GitHub/GitLab/Bitbucket/Codeberg push; key location and config
type: reference
---

All git pushes to GitHub, GitLab, Bitbucket, and Codeberg use SSH with the `gitcommitran` key.

- Key: `C:\Users\{USER}\.ssh\gitcommitran` (ed25519, comment: `ran.hash@proton.me`)
- SSH config entries in `C:\Users\{USER}\.ssh\config` map `github.com`, `gitlab.com`, `bitbucket.org`, and `codeberg.org` to this key automatically — no `-i` flag needed.
- Remotes are set up with `git@github.com:...` / `git@gitlab.com:...` / `git@bitbucket.org:...` / `git@codeberg.org:...` URLs, not HTTPS.

**Why:** user uses SSH for consistency and security across all remotes.

**How to apply:** when setting up new git remotes, always use SSH URLs. Never use HTTPS URLs. The SSH config handles key selection automatically.
