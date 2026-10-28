[//]: # ( ---------------------------------------------------------------------- )
[//]: # (+ Authors: 	Ran# <ran.hash@proton.me> )
[//]: # (+ Created: 	2026/10/27 16:48:56.833706 )
[//]: # (+ Revised: 	2026/10/28 15:07:03.680748 )
[//]: # ( ---------------------------------------------------------------------- )

# grimorio

> *Grimorio* (Galician): a grimoire, a book of spells.

My [Claude Code](https://claude.com/claude-code) configuration: global instructions, agents, slash commands, hooks and a persistent memory of how I like things done.

This repository **is** `~/.claude`. Clone it on a new machine and Claude already knows my commit style, stack, test bar and the rest.

---

## Layout

```
~/.claude
├── CLAUDE.md          global instructions, loaded in every project
├── settings.json      permissions, hooks, status line
├── agents/            custom subagents
├── commands/          slash commands
├── hooks/             scripts run by settings.json
├── bin/               setup, secrets and file-header tools (added to PATH)
├── skills/            my own skills
├── memory/            global memory, one fact per file
└── project-memory/    per-project memory, one folder per project
```

Everything else Claude Code writes here (sessions, history, caches, plugins) is ignored: [`.gitignore`](.gitignore) ignores everything and lists only the paths to track. A new top-level path must be added there first.

---

## Install

```sh
git clone git@github.com:Ran-n/grimorio.git ~/.claude
```

If `~/.claude` already exists, fetch into it instead:

```sh
cd ~/.claude
git init -b main
git remote add github git@github.com:Ran-n/grimorio.git
git fetch github
git checkout -f -t github/main   # overwrites tracked files only
```

Then:

1. Install `python` (3.12+), `gpg`, `uv`, `ruff`, `gh` and `glab`, and log in to `gh` and `glab`.
2. Import the GPG key `Ran# <ran.hash@proton.me>` (`11705FC643951387`) and the `gitcommitran` SSH key.
3. Run `python ~/.claude/bin/setup.py`.
4. If your code lives somewhere else than on the old machine, edit [`project-memory/links.json`](project-memory/links.json) and run `setup.py` again.
5. Check the machine-specific paths in `settings.json` (`additionalDirectories`, the Discord plugin's `bun.exe`).

---

## Commands

| Trigger | What it does |
|---------|--------------|
| `/todo <idea>` or `todo: …` | Adds an item to the project's `TODO.md` |
| `/todo do <N\|next>`, `show`, `refine`, `move`, `drop` | Works through the backlog |
| `/dbp` | Updates docs, bumps the version, commits and pushes to every remote |
| `/hk` | Wrap-up checklist: docs, memory, headers, lint, tests, i18n |

The plain-text `todo` triggers work in any project without the slash.

## Agents

| Agent | Use for |
|-------|---------|
| [`cladev`](agents/cladev.agent.md) | Engineering: edit, run, debug |
| [`claresearch`](agents/claresearch.agent.md) | Read-only research |

## Hooks

| Script | When | What it does |
|--------|------|--------------|
| [`git_guard.py`](hooks/git_guard.py) | `git commit`, `git push` | Blocks the wrong author, unbracketed titles (`[A]`, `[F]`, …), `Co-Authored-By` trailers, raw secrets and unsealed secret memories |
| [`changelog_check.py`](hooks/changelog_check.py) | `git commit` | Blocks commits that change documentable files without `CHANGELOG.md` |
| [`memory_inject.py`](hooks/memory_inject.py) | Each prompt | Adds the full memory files whose topic the prompt mentions |
| [`statusline.ps1`](hooks/statusline.ps1) | Status line | Shows the tool Claude is running |

A blocked command doesn't end Claude's turn: Claude gets the reason, fixes it and retries.

---

## Memory

[`memory/`](memory) holds one fact per file. [`MEMORY.md`](memory/MEMORY.md) indexes them and is loaded at the start of every session.

```markdown
---
name: commit-style
description: Bracketed title, Conventional Commits body, lowercase imperative
metadata:
  type: feedback        # user | feedback | project | reference
---

The rule, then **Why:** and **How to apply:**.
```

Per-project memories live in [`project-memory/`](project-memory) under plain project names. `setup.py` links each one to the folder Claude Code actually reads (`projects/<path slug>/memory`), so the repo never stores your local paths.

---

## Secrets

Secrets are committed only encrypted to the GPG key above:

- **Secret memory files** (names containing `token`, `secret`, `credential`, `password`, `_keys` or `private`) are committed only as `.gpg` copies. After editing one, run `python bin/secrets.py seal`; `open` decrypts them.
- **Private sections** of any file go between `<!-- private -->` and `<!-- /private -->`, each on its own line. They are encrypted on commit and readable on disk.
- **Your user folder name** is replaced by a placeholder on commit and restored on checkout.

`git_guard.py` blocks commits while a secret memory is unsealed, or when a staged line looks like a raw key.

---

## Syncing

Claude edits these files as it learns. To sync:

```sh
cd ~/.claude
git pull      # changes from other machines
git status    # what Claude changed here
```

Then say **push** in a Claude session: it updates the docs and `CHANGELOG.md`, commits and pushes to GitHub, GitLab and Codeberg.

---

## Contributing

This is a personal setup, but ideas and fixes are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[PayBack License (PBL)](LICENSE): free for personal and non-commercial use. Commercial use needs a revenue-share agreement; contact [ran.hash@proton.me](mailto:ran.hash@proton.me).
