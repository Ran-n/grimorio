---
name: feedback-todo-trigger
description: "todo: …" in plain text or /todo … adds a self-contained item to the project's TODO.md backlog (creates it if missing); "do todo N" implements one and deletes it
metadata:
  type: feedback
---

There is a global slash command `/todo` (`C:\Users\{USER}\.claude\commands\todo.md`). When the user types **`/todo <idea>`**, or in plain text **"todo: <idea>"**, **"todo <idea>"** or **"add to the todo/backlog …"**, run that command file as written for the current project. It creates `TODO.md` if missing, researches the code, and appends a numbered item that can be implemented from the item alone. It never implements, commits or pushes.

**"do todo N"** / **"do the next todo"** = implement that item end to end, then delete it from TODO.md.

**Why:** the user wants a backlog where reading one item is enough to fully implement it, and a short trigger that works both typed plainly and as a slash command, like [[feedback-dbp-trigger]] and "hk".
**How to apply:** treat the plain-text forms as an explicit request; the command file is the source of truth for the steps, so don't restate them here.
