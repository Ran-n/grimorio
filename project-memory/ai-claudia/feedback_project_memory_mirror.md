---
name: project-memory-mirror
description: Project memory directory must be a byte-for-byte copy of global memory; never modify mirrored files
metadata:
  type: feedback
---

When mirroring global memory into a project memory directory, use `Copy-Item` (or equivalent) for a byte-for-byte copy. Do not read/ingest and recreate the files, and do not edit any of the copied files afterward (including MEMORY.md).

Project-specific files (e.g. `project_spec.md`) live in the project memory directory alongside the copies. Exception (confirmed 2026-07-03): project-specific *memory* entries may be appended as index lines at the end of the project MEMORY.md so they load each session; the rest of MEMORY.md must remain identical to the global copy.

**Why:** User wants the mirror to be an exact copy, not a processed/modified version.

**How to apply:** On every `mirror global memory` task — copy with a shell command, then stop; never edit the copied MEMORY.md.
