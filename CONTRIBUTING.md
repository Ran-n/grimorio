[//]: # ( ---------------------------------------------------------------------- )
[//]: # (+ Authors: 	Ran# <ran.hash@proton.me> )
[//]: # (+ Created: 	2026/10/27 16:48:57.156421 )
[//]: # (+ Revised: 	2026/10/27 16:48:57.156421 )
[//]: # ( ---------------------------------------------------------------------- )


# Contributing

Thank you for your interest in contributing.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)
- [Submitting Changes](#submitting-changes)
- [Review Process](#review-process)
- [Commit Style](#commit-style)
- [License](#license)
  - [AI Disclosure](#ai-disclosure)

---

## Code of Conduct

Be respectful and constructive. Harassment, discrimination, or bad-faith behaviour will not be tolerated.

---

## Reporting Bugs

Open an issue and include:

- A clear, descriptive title
- Steps to reproduce the problem
- Expected vs actual behaviour
- Environment details (OS, version, etc.) if relevant

---

## Suggesting Features

Open an issue and describe:

- The problem you are trying to solve
- Your proposed solution
- Any alternatives you considered

---

## Submitting Changes

1. Fork the repository
2. Create a branch from `main`: `git checkout -b my-change`
3. Make your changes
4. Commit following the [Commit Style](#commit-style) below
5. Push your branch and open a pull request against `main`
6. Describe what you changed and why in the PR body
7. Include an [AI disclosure](#ai-disclosure) in the PR description — this is required

Keep each pull request focused on a single concern. Unrelated changes belong in separate PRs.

---

## Review Process

Pull requests are reviewed by the maintainer. Expect feedback within a reasonable time; there is no guaranteed SLA. A PR may be:

- **Merged** as-is
- **Merged after changes** — address the requested changes and push to the same branch
- **Closed** — if it is out of scope, duplicates existing work, or cannot be reconciled with the project direction

Do not open a new PR to replace a closed one without first discussing the closure in the original thread.

---

## Commit Style

Use a bracketed abbreviation as the title and a Conventional Commits body:

```
[A] short description of what was added

feat: add X
fix: correct Y
```

Allowed brackets:

| Bracket | Type       |
|---------|------------|
| `[A]`   | `feat`     |
| `[R]`   | `refactor` |
| `[F]`   | `fix`      |
| `[D]`   | `docs`     |
| `[T]`   | `test`     |
| `[C]`   | `chore`    |
| `[P]`   | `perf`     |
| `[B]`   | `build`    |
| `[S]`   | `style`    |

Rules:

- Title: bracket + short phrase — do not repeat the type word
- Body lines: lowercase, imperative mood
- Breaking changes: `feat!`/`fix!` in the body, or a `BREAKING CHANGE:` footer
- Scope is optional: `fix(module): ...`

---

## License

By contributing, you agree that your work will be released under the [PayBack License (PBL)](LICENSE). Free for personal and non-commercial use. Commercial use requires a revenue-share agreement — contact [ran.hash@proton.me](mailto:ran.hash@proton.me).

**What qualifies as a meaningful contribution:** new features, bug fixes, and substantive code changes. Documentation, formatting, and comment-only changes do not qualify.

Meaningful contributions may entitle you to a revenue share, subject to a resolution vote among existing owners. You must be listed in the [CONTRIBUTORS](CONTRIBUTORS) file before any entitlement applies. Until listed, you hold no ownership or revenue rights regardless of the work merged.

### AI Disclosure

Every pull request must include an AI disclosure in the PR description. This is a binding requirement under clause 43 of the license — omitting it constitutes misrepresentation of authorship.

If you used an AI tool (code generation, completion, or transformation):

```
AI-Disclosure: yes
Tool: <name of the AI tool, e.g. GitHub Copilot, ChatGPT>
Scope: <which files, functions, or sections were produced by the AI tool>
```

If you did not use any AI tool:

```
AI-Disclosure: none
```

Any AI-generated portion of a contribution is not considered your original work and does not entitle you to ownership or revenue share on that portion — it is treated as the Founder's contribution.
