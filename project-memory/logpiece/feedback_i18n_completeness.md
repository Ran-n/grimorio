---
name: i18n-completeness-after-changes
description: "after any change adding or modifying user-facing strings, update all translation files so no key is missing from any locale"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8d6ce87f-ebe4-4c7f-9a7c-dc4de50180fd
---

After any change that adds, removes, or renames user-facing strings: update every translation/locale file so all keys are present and up to date in every supported language.

**Why:** missing keys in non-primary locales can surface as crashes or raw key strings at runtime, and are easy to overlook when only testing one language.

**How to apply:** treat translation file updates as part of the task, not a follow-up. If a key is added in code, it must appear in every locale file before the task is done.
