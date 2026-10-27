---
name: python-linting-ruff
description: "Run ruff format then ruff check on every modified Python file in projects with ruff config; fix errors manually, never --fix"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8d6ce87f-ebe4-4c7f-9a7c-dc4de50180fd
---

After modifying any Python file in a project whose `pyproject.toml` includes a ruff config:
1. `ruff format <file>`
2. `ruff check <file>`

Fix any errors manually — never use `--fix`.

**Why:** auto-fix can introduce unwanted changes; user wants intentional, reviewed corrections only.

**How to apply:** treat both commands as part of every file edit, before the task is done.
