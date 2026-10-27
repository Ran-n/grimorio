---
name: python-linting-ruff
description: "Run ruff format then ruff check on every modified Python file in projects with ruff config; fix errors manually, never --fix"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2357ec0d-7eb6-4caf-86db-e0049e064f79
---

After modifying any Python file in a project whose `pyproject.toml` includes a ruff config:
1. `ruff format <file>`
2. `ruff check <file>`

Fix any errors manually — never use `--fix`.

**Why:** auto-fix can introduce unwanted changes; user wants intentional, reviewed corrections only.

**How to apply:** treat both commands as part of every file edit, before the task is done.
