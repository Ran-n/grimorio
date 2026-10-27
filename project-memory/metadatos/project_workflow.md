---
name: project_workflow
description: File headers (metadatos), ruff formatting, and general workflow rules
type: project
originSessionId: 85f4865e-61c5-499c-b6f5-7115e7481c13
---
## File Headers
Use `python C:/Users/{USER}/.claude/memory/metadatos_v0.2.1.py <flag> <file>`.
Source: https://github.com/ran-n/metadatos — update the copy when the version changes.

- On every file edit, run with `-m` to update the `Revised:` timestamp
- If a file has no metadata header, run with `-c` to create one
- If asked to view metadata, run with `-v`
- Supported types: `.py`, `.pyw`, `.sh`, `.bash`, `.rs`, `.md` — for any other type, skip and inform the user

## Python / Ruff
If `pyproject.toml` contains ruff configuration: run `ruff format <file>` on every modified Python file, then run `ruff check <file>` and fix any reported errors manually until it passes clean. Do not use `--fix` — write correct code.

## Workflow
When auto-approve mode is on, execute all commands and edits immediately without asking for confirmation.

## Releases
When editing, resigning, amending, or modifying old commits, tags, or releases in any way, preserve ALL original metadata: author date, committer date, tag date, tagger identity, and message. Use `GIT_AUTHOR_DATE`/`GIT_COMMITTER_DATE` for commits; recreate tag objects with original date/tagger. Goal: history ordering and timestamps look unchanged. When creating a new release, build all dist artifacts and attach to the tag.
