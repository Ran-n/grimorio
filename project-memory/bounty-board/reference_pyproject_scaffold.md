---
name: reference-pyproject-scaffold
description: Minimum required pyproject.toml structure for all Python projects (uv + hatchling + ruff)
metadata:
  type: reference
---

# Minimum pyproject.toml Scaffold

All Python projects must include these sections. Fill in project-specific values; the ruff config is fixed.

```toml
[project]
name = "project-name"
version = "0.1.0"
description = "..."
readme = "README.md"
authors = [{ name = "Ran#" }]
license-files = ["LICENSE"]
requires-python = ">=3.14"
dependencies = []

[project.scripts]
entrypoint = "package.__main__:run"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/package_name"]

[tool.ruff]
src = ["src"]
target-version = "py314"
line-length = 120
preview = true

[tool.ruff.lint]
select = ["E", "F", "I", "B", "UP", "SIM"]
ignore = []

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
line-ending = "auto"
```

**Notes:**
- `readme`, `authors`, `license-files` are required in `[project]` — currently missing from reska repos (add on next scaffold pass)
- `src =` in `[tool.ruff]` is project-specific; keep it when using `src/` layout
- `preview = true` enables ruff's preview lint rules — always on
- See [[feedback-new-repo-scaffold]] for the full file set required before first commit