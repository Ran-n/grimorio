---
name: Python projects — ruff
description: Run ruff format then ruff check on every modified Python file; fix errors manually
type: feedback
originSessionId: 27a28edc-919c-456d-bfa9-7b1db3608dab
---
If `pyproject.toml` contains ruff configuration: run `ruff format <file>` on every modified Python file, then run `ruff check <file>` and fix any reported errors manually in the code until it passes clean. Do not use `--fix` as a shortcut — write correct code. Use the config from `pyproject.toml`.

**Why:** project uses ruff for consistent formatting and linting; --fix can silently change semantics.
**How to apply:** every time a `.py` file is modified and a ruff-configured `pyproject.toml` exists.
