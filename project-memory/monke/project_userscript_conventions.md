---
name: userscript_conventions
description: Conventions for userscripts in this repo (header format, metadata block, etc.)
type: project
---

The comment block goes at the very top of the file, BEFORE `// ==UserScript==`. Userscript managers (Tampermonkey, Violentmonkey) scan for `==UserScript==` anywhere in the file, so preceding comments are safe.

```js
// -*- coding: utf-8 -*-
// ------------------------------------------------------------------------
//+ Authors: 	Ran#
//+ Created:	YYYY/MM/DD HH:MM:SS.ffffff
//+ Revised:	YYYY/MM/DD HH:MM:SS.ffffff
// ------------------------------------------------------------------------

// ==UserScript==
// ...
// ==/UserScript==
```

- `Created` = original authoring date, never changes after first commit.
- `Revised` = update to actual current timestamp every time the file is modified.
- Timestamp format: `YYYY/MM/DD HH:MM:SS.ffffff` (microseconds, never zeroed-out).
- Do NOT use a `@description` date line — use this block instead.

**Why:** User's explicit preference; block goes on top like all other authored files.
**How to apply:** Always add/update this block when creating or editing any userscript.
