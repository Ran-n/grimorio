[//]: # ( ---------------------------------------------------------------------- )
[//]: # (+ Authors: 	Ran# <ran.hash@proton.me> )
[//]: # (+ Created: 	2026/10/27 16:48:56.833706 )
[//]: # (+ Revised: 	2026/10/27 19:10:25.289798 )
[//]: # ( ---------------------------------------------------------------------- )

# grimorio

> *Grimorio* (Galician): a grimoire, a book of spells.

The spellbook behind every [Claude Code](https://claude.com/claude-code) session I run: global instructions, custom agents, slash commands, guard-rail hooks and a persistent memory of how I like things done.

This repository **is** `~/.claude`. Clone it and a new machine's Claude starts out knowing the commit style, the license, the stack, the test bar and the rest.

## Contents

- [What's inside](#whats-inside)
- [Install](#install)
- [Commands](#commands)
- [Agents](#agents)
- [Hooks](#hooks)
- [Memory](#memory)
- [What is never tracked](#what-is-never-tracked)
- [Day-to-day](#day-to-day)
- [Contributing](#contributing)
- [License](#license)

---

## What's inside

```
~/.claude
├── CLAUDE.md          global instructions, loaded in every project
├── settings.json      permissions allowlist, hooks, status line
├── agents/            custom subagents
├── commands/          slash commands
├── bin/               setup, git filter, secrets and the metadata header tool (on PATH)
├── hooks/             scripts wired into settings.json
├── skills/            locally authored skills (skills/synced/ is not tracked)
├── memory/            global one-fact-per-file memory + MEMORY.md index
└── project-memory/    per-project memories, one folder per project + links.json
```

Claude Code keeps each project's memory in `projects/<project path as a slug>/memory`. Those folder names hold your drive, user folder and project path, so the repo stores the memories under plain project names in `project-memory/` instead, and each `projects/…/memory` is a junction to its folder there.

Everything else Claude Code writes here (sessions, history, caches, project transcripts, plugins) is ignored by a whitelist [`.gitignore`](.gitignore). Ignoring everything is the default, and a path is tracked only when it is listed explicitly.

---

## Install

### Fresh machine

```sh
git clone git@github.com:Ran-n/grimorio.git ~/.claude
```

### `~/.claude` already exists

```sh
cd ~/.claude
git init -b main
git remote add github git@github.com:Ran-n/grimorio.git
git fetch github
git checkout -f -t github/main   # overwrites tracked files only
```

### After cloning

1. **Install the tools the hooks and memories use:** Python 3.12+ on PATH as `python`, `gpg`, `uv`, `ruff`, `gh`, `glab`, and the `gitcommitran` SSH key with its `~/.ssh/config` entries. Log in to `gh` and `glab`.
2. **Import the GPG key** `Ran# <ran.hash@proton.me>` (`11705FC643951387`).
3. **Run `python ~/.claude/bin/setup.py`.** It registers the git filter and re-checks-out the files through it, decrypts the secret memories, links every `projects/…/memory` folder to `project-memory/`, and adds `bin/` to the user PATH.
4. **Keep the same code layout,** or edit [`project-memory/links.json`](project-memory/links.json) (project name → Claude's path slug) to match where the code lives now, then run `setup.py` again.
5. **Optional:** in `settings.json`, `additionalDirectories` and the Discord plugin's `bun.exe` path name this machine's folders. Fix them if you use them.

---

## Commands

| Trigger | What it does |
|---------|--------------|
| `/todo <idea>` or `todo: …` | Adds a self-contained item to the project's `TODO.md` |
| `/todo do <N\|next>`, `show`, `refine`, `move`, `drop` | Works through and maintains the backlog |
| `/dbp` | Docs → bump → push: syncs docs, bumps the version from the diff, commits and pushes to every remote |
| `/hk` | Housekeeping wrap-up: docs sync, memory sweep, headers, lint, tests, i18n |

The plain-text `todo` triggers are declared in [`CLAUDE.md`](CLAUDE.md), so they work in every project without the slash.

---

## Agents

| Agent | Tools | Use for |
|-------|-------|---------|
| [`cladev`](agents/cladev.agent.md) | Read, Edit, Write, Grep, Glob, Bash | Hands-on engineering: edit, run, debug |
| [`claresearch`](agents/claresearch.agent.md) | Read, Grep, Glob, Bash, WebFetch, WebSearch | Read-only investigation, with no changes |

---

## Hooks

| Script | Fires on | Effect |
|--------|----------|--------|
| [`git_guard.py`](hooks/git_guard.py) | `git commit`, `git push` | Rejects the wrong author (must be `Ran#` / `ran.hash@proton.me`), commit titles without a `[A]`/`[F]`/`[R]`… bracket, a `Co-Authored-By` trailer in any `-m`, staged lines that look like raw secrets, and (here) unsealed secret memories |
| [`changelog_check.py`](hooks/changelog_check.py) | `git commit` | Blocks the commit when documentable changes are staged without `CHANGELOG.md`, in the repo the commit targets (`git -C <dir>` or a preceding `cd <dir>`) |
| [`statusline.ps1`](hooks/statusline.ps1) | Status line | Braille spinner showing the tool Claude is running right now |

Both guards refuse the command rather than ending Claude's turn: the commit doesn't run until the problem is fixed, and Claude gets the reason back, fixes it and retries.

---

## Memory

[`memory/`](memory) is Claude's long-term memory. There is one fact per file, with frontmatter:

```markdown
---
name: commit-style
description: Bracketed title, Conventional Commits body, lowercase imperative
metadata:
  type: feedback
---

The rule itself, then **Why:** and **How to apply:**.
```

| Type | Holds |
|------|-------|
| `user` | Who I am: identity, authorship |
| `feedback` | How to work, and why. These are rules learned from corrections |
| `project` | Ongoing work and constraints |
| `reference` | Pointers: license source, SSH keys, scaffolds, layouts |

[`MEMORY.md`](memory/MEMORY.md) is the index. It has one line per memory, grouped by topic (git, Python, repo setup, code quality, API design, UI…), and it is loaded into context at the start of every session. Memories link to each other with `[[name]]`.

---

## What is never tracked

- Session transcripts, `history.jsonl`, `projects/`, caches, debug logs
- `settings.json.bak`, `backups/`, plugin installs
- `skills/synced/`, which is pulled from claude.ai and not written here
- Secrets in plain text. Memories named `*token*`, `*secret*`, `*credential*`, `*password*`, `*_keys*` or `*private*`, and a few listed by name, stay local; only their GPG-encrypted `.gpg` copies are committed
- Your user folder name. Every text file passes through the `grimorio` git filter ([`bin/filter.py`](bin/filter.py)), which stores it as a placeholder and puts it back on checkout

### Secrets

Three layers, all encrypted to the GPG key above:

- **Whole files.** `python bin/secrets.py seal` encrypts every secret memory, and `open` decrypts them. After adding or editing one, run `seal` before committing.
- **Parts of a file.** Lines between a line `<!-- private -->` and a line `<!-- /private -->` are encrypted by the git filter on commit and decrypted on checkout, so the file on disk stays readable. The markers must sit on their own lines.
- **Commit guard.** `git_guard.py` refuses commits while a secret memory is unsealed. In every repo, it also refuses staged lines that look like a raw token or key.

Before adding a new top-level path, whitelist it in `.gitignore`. Then check `git status` to confirm it is the only new path.

---

## Day-to-day

Claude edits these files as it learns, so the repo drifts. To sync:

```sh
cd ~/.claude
git pull            # pick up changes from another machine
git status          # review what Claude learned or changed
```

Then say **push** in a Claude session. The memory-driven workflow updates the docs and `CHANGELOG.md`, commits in the bracket style and pushes to GitHub, GitLab and Codeberg.

---

## Contributing

This is a personal setup, but ideas and fixes are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for the process, the commit style and the AI-disclosure requirement.

---

## License

Released under the [PayBack License (PBL)](LICENSE). Free for personal and non-commercial use. Commercial use requires a revenue-share agreement; contact [ran.hash@proton.me](mailto:ran.hash@proton.me).
