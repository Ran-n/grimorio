---
name: uv cheatsheet
description: uv essentials — setup, deps, run, build, publish, version bumping
type: reference
---

# uv essentials

**Setup**
```bash
uv init          # init project in current dir (creates pyproject.toml, .venv, uv.lock)
uv sync          # install all deps from lockfile (creates .venv if missing)
```

**Dependencies**
```bash
uv add requests              # add runtime dep
uv add pytest --dev          # add to [dependency-groups] dev
uv remove requests           # remove dep
uv lock --upgrade-package requests   # upgrade one package
uv lock --upgrade            # upgrade all
```

**Run things**
```bash
uv run pytest                # run inside venv (no manual activation)
uv run python script.py
uv run python -c "import conexions"
```

**One-off tools (no install)**
```bash
uvx ruff check .
uvx black .
```

**Build & publish**
```bash
uv build         # builds wheel + sdist → dist/
uv publish       # uploads to PyPI (prompts for API token)
```

**Info**
```bash
uv pip list      # list installed packages
uv python list   # list available Python versions
uv self update   # update uv itself
```

**Dev extras**
```bash
uv add --editable . --dev
uv run ipython
```

**Version bumping**
```bash
uv version                          # show current version
uv version --bump patch             # 0.1.0 → 0.1.1
uv version --bump minor             # 0.1.0 → 0.2.0
uv version --bump major             # 0.1.0 → 1.0.0
uv version 1.2.3                    # set exact version
uv version --bump patch --dry-run   # preview without writing
uv version --bump patch --bump alpha  # 0.1.1a1
uv version --bump patch --bump beta   # 0.1.1b1
uv version --bump patch --bump rc     # 0.1.1rc1
uv version --bump stable              # strips pre-release suffix
```
