---
name: Regression safety — no unintended side effects (Vitralis)
description: Every change must be verified not to break other parts of Vitralis; flag risks before implementing
type: feedback
originSessionId: 4c8aca06-9a16-4940-8fb5-db23075a45b1
---
When making a change in Vitralis, ensure it does not silently break unrelated parts of the program. Intentional behaviour changes requested by the user are always correct — this rule is only about unintended ripple effects.

**Why:** The codebase has interconnected components (toolbar, settings window, persistence, i18n, styles, icons). A change in one area can silently break another.

**How to apply:**
- Before editing any shared module (`styles.py`, `icons.py`, `translations.py`, `persistence.py`, `toolbar.py`), grep all files that import or reference it.
- If touching a signal, slot, or Qt property: verify all connect/disconnect sites are still correct after the change.
- If touching translations or styles: confirm all widgets that consume them still render correctly.
- If touching persistence (load/save/snapshot): verify all call sites handle the updated schema or interface.
- If an unintended side effect risk exists, name it before proceeding.
- Never remove, rename, or change a function/class signature without updating every caller in the project.
