---
name: no-future-imports
description: Never add from __future__ import annotations (or any __future__ import) to Python files unless strictly required for the code to run
metadata:
  type: feedback
---

Never add any `from __future__` import to a Python file. Only keep or add one if its absence causes a syntax or runtime error that cannot be fixed any other way — this bar is extremely high and will almost never be met on Python 3.10+.

**Why:** modern Python supports all annotation and language features natively; `__future__` imports are unnecessary boilerplate the user explicitly rejects.

**How to apply:** new files — never include. Existing files — strip unless removing breaks compilation (verify with `compile()` or running the file). When in doubt, remove it.