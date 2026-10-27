---
name: i18n completeness after changes
description: after any change adding or modifying user-facing strings, update all translation files so no key is missing from any locale
type: feedback
originSessionId: 6dbf84ee-87f0-495f-80d5-37db4a8e5a19
---
After any change that adds, removes, or renames user-facing strings: update every translation/locale file so all keys are present and up to date in every supported language. Also audit all locales for missing keys whenever reading translations.py for any reason — gaps should be fixed immediately, not noted and left.

**Why:** missing keys in non-primary locales surface as raw key strings at runtime and are easy to overlook when only testing one language. User explicitly flagged this as a rule.

**How to apply:** treat translation file updates as part of the task, not a follow-up. If a key is added in code, it must appear in every locale file before the task is done. If an existing locale is found missing keys, fix them in the same edit.
