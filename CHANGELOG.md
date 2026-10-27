[//]: # ( ---------------------------------------------------------------------- )
[//]: # (+ Authors: 	Ran# <ran.hash@proton.me> )
[//]: # (+ Created: 	2026/10/27 16:48:57.000106 )
[//]: # (+ Revised: 	2026/10/27 19:10:25.363935 )
[//]: # ( ---------------------------------------------------------------------- )

# Changelog

All notable changes to this project are documented here.

---

## [Unreleased]

### Added
- Global `CLAUDE.md` with plain-text `todo` triggers
- `settings.json` with permissions allowlist, hooks and status line, using `python` and `$HOME/.claude/…` paths
- `cladev` and `claresearch` agents
- `/dbp`, `/hk` and `/todo` slash commands
- `git_guard.py` hook: author, bracket commit title, no Co-Authored-By in any `-m`, `-F -` heredoc messages, raw secrets in staged lines, unsealed secret memories; refuses the command instead of ending Claude's turn
- `changelog_check.py` hook: refuses commits without `CHANGELOG.md`, in the repo targeted by `git -C` or a preceding `cd`
- `statusline.ps1` status line spinner
- Global memory store with `MEMORY.md` index
- Per-project memories under plain project names in `project-memory/`, linked from Claude's path-named `projects/…/memory` folders with junctions (`links.json`)
- `grimorio` git filter (`bin/filter.py`): stores the user folder name as a placeholder and encrypts `<!-- private -->` blocks, so files on disk stay readable
- `bin/secrets.py` (`seal`/`open`/`check`) keeping secret memories in git only as GPG-encrypted `.gpg` copies
- `bin/setup.py` for a new machine: registers the filter, decrypts secrets, creates the junctions, adds `bin/` to PATH
- `metadata` header tool in `bin/`, whose `-v`/`-d` only touch the Authors/Created/Revised fields
- `feedback_gpg_sealing` memory on credentials files and private markers
- Whitelist `.gitignore`, README, CONTRIBUTING, CHANGELOG, CONTRIBUTORS and PayBack License (PBL)
