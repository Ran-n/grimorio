---
name: Vitralis project spec
description: How Vitralis should work — UX, behaviour, and technical requirements
type: project
originSessionId: 308b5082-acb2-4e7b-8d2c-964b03e52afc
---
Always-on-top transparent overlay for drawing over the desktop. Floating toolbar controls all drawing. Overlay is click-through when not in an active mode.

## Shortcuts
- `F8` — global focus toggle: shows toolbar + steals OS focus, saves previous window; second press hides and restores previous window.
- All other shortcuts are local (fire only when Vitralis has focus).
- When focused: bare keys, no Ctrl prefix where unnecessary.
- Local: `D` draw, `Z` undo, `Del` clear, `H` visibility, `P/E/L/A/R/O` tools, `Esc` contextual, `Ctrl+Q` quit.

## Escape
- In draw/pan/delete mode: exits that mode, does NOT quit.
- When idle: quits.

## Focus
- `SetForegroundWindow` used to steal OS focus. Saves and restores the previously focused window.

## Draw mode
- `DrawCapture` overlay intercepts mouse for drawing.
- Right-click or `Esc` exits draw mode.
- Toolbar stays visible and interactive while drawing.
