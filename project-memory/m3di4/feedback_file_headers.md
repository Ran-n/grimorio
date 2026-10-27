---
name: file_header_timestamp
description: Update the Revised timestamp in file headers when modifying files
type: feedback
---

When modifying any file, update the `#+ Editado:` (or `#+ Revised:`) timestamp to the current date and time.

Format: `YYYY/MM/DD HH:MM:SS.ffffff` (microseconds, zero-padded to 6 digits)

**Why:** User tracks modification times in file headers.
**How to apply:** Never use zeroed-out time like `17:15:00.000000` — always use the actual current time including seconds and microseconds.
