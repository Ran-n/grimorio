---
name: seal-secret-memories
description: ~/.claude is a public repo; credentials go in *token*/*secret*/… files sealed with secrets.py, sensitive lines in other memories go between <!-- private --> marker lines
metadata:
  type: feedback
---

`~/.claude` is the public `grimorio` repo, and every memory (global, and per project through the `projects/…/memory` junctions into `project-memory/`) is published unless protected:

- **Credentials:** a memory named `*token*`, `*secret*`, `*credential*`, `*password*`, `*_keys*` or `*private*` is ignored in plain text; only `<file>.gpg`, encrypted to the user's GPG key, is tracked.
- **Sensitive lines in any other memory** (other people's names or IDs, contact details, passwords, admin paths, anti-abuse and security internals, account/zone IDs): wrap them in a line `<!-- private -->` before and a line `<!-- /private -->` after. The git filter encrypts that block on commit; the file on disk stays readable.
- The user folder name is replaced with a placeholder by the same filter, so paths are fine to write.

**Why:** the user wants every memory portable to a new machine without publishing tokens or personal data; a privacy review on 2026-10-27 found other people's real names and Discord IDs, a database password and security internals in project memories.

**How to apply:** when saving a credential, name the file to match a pattern (e.g. `reference_<service>_token.md`) and run `python ~/.claude/bin/secrets.py seal` before committing. When a memory needs a sensitive detail, put it inside private markers instead. `git_guard.py` refuses the commit if a secret is unsealed or a raw token is staged. See [[file-headers-metadata]].
