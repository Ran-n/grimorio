---
name: feedback_hashing
description: Always use BLAKE3 as the default hash algorithm; "hash" means blake3 unless specified
metadata:
  type: feedback
---

Always use BLAKE3 as the default hashing algorithm for any file integrity check, deduplication, comparison, or checksumming task. Use whatever tool provides BLAKE3 on the current platform (`b3sum` on Windows, or equivalent on other systems).

**Why:** User preference — faster, modern, and explicitly requested.

**How to apply:** The word "hash" always means BLAKE3 unless the user names a different algorithm explicitly. Never default to SHA-256, MD5, or others unless BLAKE3 is explicitly unavailable on the platform.
