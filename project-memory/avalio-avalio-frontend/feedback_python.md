---
name: Python Projects - ruff
description: Run ruff format and check on every modified Python file
type: feedback
originSessionId: e132952d-97d2-4a9b-a700-0c502415f387
---
If `pyproject.toml` contains ruff configuration: run `ruff format <file>` on every modified Python file, then run `ruff check <file>` and fix any reported errors manually until it passes clean.

Do NOT use `--fix` as a shortcut — write correct code. Use config from `pyproject.toml`.

**Why:** user enforces ruff formatting and linting on all Python projects.
**How to apply:** after every Python file edit, if ruff is configured.
