---
description: Manage the project's TODO.md backlog - add a self-contained item (default), or do, show, refine, move or drop one
argument-hint: <idea> | do <N|next> | show | refine <N>: <change> | move <N> <top|before M> | drop <N>
---

Backlog request: $ARGUMENTS

Pick the action from the first word of the request (plain-text messages like "todo: …" or "do todo 2" map the same way):

| Request | Action |
|---|---|
| anything else, or nothing (then use the user's latest message and screenshots) | **Add** |
| `do <N>`, `do next` | **Implement** that item |
| `show`, `list` | **Show**: one line per item in file order (number, title, first line of Goal) |
| `refine <N>: <change>` | **Refine**: rewrite that item with the change, following the writing rules |
| `move <N> top`, `move <N> before <M>` | **Move**: reorder the items |
| `drop <N>` | **Drop**: delete the item (and its screenshots) without implementing it |

The order of items in the file is the priority: "next" is the first item in the file, not the lowest number. Numbers are IDs and never change. After any edit to `TODO.md` run `metadata -m TODO.md`. Only Implement touches code; no action commits or pushes unless asked.

## Adding an item

Several ideas in one request (separated by "also", ";" or a list) become one item each.

1. **Find or create `TODO.md`** at the repo root. If it doesn't exist, create it from the skeleton at the end of this file, add the file header per `feedback_file_headers.md` (`metadata -c`), and add a short "Backlog" section pointing at it in the project's developer docs (`docs/development.md`, or `CONTRIBUTING.md` if there is no such doc). If it exists but its header block (how to use, writing rules, implementing steps, template) is older than this file's skeleton, bring it up to date.
2. **Check for duplicates.** If an existing item already covers the idea, refine that item instead and say so.
3. **Research before writing.** Read the code, tests, locale files and docs the request touches, so every file, function, constant, key and test named in the item is real. Grep callers of anything the item changes and name the ripple effects.
4. **Keep the screenshots.** Copy each screenshot the user attached to `docs/todo/<n>-<slug>.png` and link it from the item's Why, so the implementer sees what the user saw. Describe it in words too.
5. **Size it.** If the idea is more than one sitting of work or mixes unrelated changes, split it into several items, each shippable alone, and note the order in their Why lines ("after item 4").
6. **Write the item** following the writing rules below, numbered with the header's "Next item number", then increase that number. Put it at the end of the file unless the user says it's urgent (then first). Use AskUserQuestion only for a choice that really is the user's to make and can't be inferred.
7. **Reply** with the item number and title, plus a few lines on the decisions you made.

## Writing rules for an item

- Write for someone who has never seen this conversation or the screenshot. Describe the current behaviour concretely (what is on screen, what goes wrong), then the wanted result as the user will see it.
- Give the reason for every decision that isn't obvious, right next to it.
- Be concrete: real paths, names, sizes, colours, keys, numbers. Leave no "maybe" or open "e.g.". If the implementer must choose (for example, whichever renders best), say exactly how to choose and how to check.
- Sections, in this order: **Why**, **Goal**, **Behaviour** (one bullet per case, edge cases included), **Out of scope**, **Implementation** (a numbered list of steps in the order to do them, one action per step, each naming the file and what changes in it and why), **Tests** (each test case named with what it proves; every applicable type, happy and error paths), **Docs** (every file and the line or section to change, plus the changelog line), **Done when** (a `- [ ]` checklist the implementer can tick with evidence).
- Put the user's rules from memory that apply (clean code, tests, i18n in every locale, logging, no silent failure, UI preferences, file headers, lint) into the steps, so the implementer doesn't need to look them up.

## Implementing an item ("do todo N" / "do the next todo")

"next" is the first item in the file. Then:

1. **Read** the whole item and every file it names. Check `git status` so uncommitted work isn't overwritten.
2. **Check the item still matches the code.** If names or files have drifted, adapt to the current code and note it. If the item contradicts the project spec, memory or a newer decision, raise it with AskUserQuestion before building.
3. **Implement the steps in order**, following the user's memory rules (grep callers before changing shared code, logging, no silent failure, every locale file).
4. **Write the tests** the item lists, plus any others the change needs.
5. **Verify:** `ruff format` then `ruff check` on edited Python files, `metadata -m` on every edited file (`-c` on new ones), and the full test suite. Fix until everything is clean.
6. **See it working.** For anything visible, run the app and check it (screenshots at the states the item names, in light and dark themes when relevant).
7. **Update the docs** the item lists. Write the changelog line when a commit is requested, per `feedback_changelog.md`.
8. **Walk the "Done when" checklist**, with evidence for each line.
9. **Delete the item** from `TODO.md`, and its screenshots in `docs/todo/`. Don't renumber the others. Add any follow-up work found along the way as new items, using the writing rules.
10. **Don't commit or push** unless asked. Reply with what changed, any departures from the item and why, the test results, and any new follow-up items.

## Skeleton for a new `TODO.md`

````markdown
# TODO

The backlog. Each item is self-contained: reading it alone is enough to
implement it fully, without asking anything. Work top to bottom unless an item
says otherwise.

Next item number: 1

## Adding an item

- Write for someone who has never seen the conversation: what happens today,
  what should happen instead, and why each non-obvious decision was made.
- Be concrete: real file paths, names, sizes, colours, keys. No open "maybe";
  if the implementer must choose, say how to choose and how to check.
- Use the template below. Implementation is a numbered list of steps in the
  order to do them; Done when is a checklist.
- Number it with "Next item number" above, then increase that number. Numbers
  are IDs: never reused or renumbered.
- File order is priority: the first item is the next one to do.
- Screenshots go in `docs/todo/<n>-<slug>.png`, linked from the item.
- Split anything bigger than one sitting into items that ship alone.

## Implementing an item

1. Read the whole item and every file it names; check `git status` first.
2. If the code has drifted from the item, adapt and note it; if the item
   contradicts a newer decision, ask before building.
3. Do the Implementation steps in order.
4. Write the listed tests, plus any others the change needs.
5. Lint, format, update file headers and run the full test suite until clean.
6. For visible changes, run the app and check it in the states the item names.
7. Update the listed docs; write the changelog line when committing.
8. Tick every Done when line, with evidence.
9. Delete the item and its screenshots; add follow-up work as new items.

## Template

```markdown
## <n>. <short imperative title>

**Why:** what happens today and what is wrong with it.
**Goal:** the result, as the user will see it.

### Behaviour
- One bullet per case, edge cases included.

### Out of scope
- What this item deliberately doesn't change.

### Implementation
1. `<path>`: what changes and why.

### Tests
- `<test file>`: each case and what it proves.

### Docs
- `<doc file>`: what to change. Changelog: "<line>".

### Done when
- [ ] Checkable result.
```

---
````
