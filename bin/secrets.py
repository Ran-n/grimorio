#!/usr/bin/env python3
"""
Authors: Ran# <ran.hash@proton.me>
Created: 2026/10/27 17:57:17.910616
Revised: 2026/10/27 19:06:40.379059
"""

# Keeps secret memories in git as GPG-encrypted copies.
#   seal   encrypt every secret memory into <file>.gpg (only when the plaintext changed)
#   open   decrypt every <file>.gpg back to its plaintext (fresh clone, or a newer .gpg pulled)
#   check  list secret memories whose .gpg is missing or stale; exit 1 if any
# A memory is secret when .gitignore keeps it out (the *token*, *secret*, … patterns), so .gitignore is the only
# list. Only memories (memory/ and project-memory/*/) are handled.

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RECIPIENT = "AA4C66BE276AA0D8D95F003D11705FC643951387"  # Ran# <ran.hash@proton.me>


def memory_files(suffix: str) -> list[Path]:
    dirs = [ROOT / "memory", *ROOT.glob("project-memory/*/")]
    return sorted(f for d in dirs for f in d.glob("*" + suffix) if f.is_file())


def secret_files() -> list[Path]:
    """Plaintext memories that .gitignore keeps out of git."""
    files = memory_files(".md")
    if not files:
        return []
    rel = [f.relative_to(ROOT).as_posix() for f in files]
    # NUL-separated: text-mode newlines become \r\n on Windows and git would match none
    r = subprocess.run(
        ["git", "-C", str(ROOT), "check-ignore", "-z", "--stdin"], input="\0".join(rel), capture_output=True, text=True
    )
    ignored = set(r.stdout.split("\0"))
    return [f for f, p in zip(files, rel) if p in ignored]


def gpg_of(f: Path) -> Path:
    return f.with_name(f.name + ".gpg")


def stale(f: Path) -> bool:
    g = gpg_of(f)
    return not g.exists() or f.stat().st_mtime > g.stat().st_mtime


def seal() -> None:
    for f in secret_files():
        if stale(f):
            subprocess.run(
                ["gpg", "--batch", "--yes", "--quiet", "--encrypt", "--recipient", RECIPIENT,
                 "--output", str(gpg_of(f)), str(f)],
                check=True,
            )
            print("sealed", f.relative_to(ROOT))


def open_() -> None:
    for g in memory_files(".md.gpg"):
        f = g.with_name(g.name[: -len(".gpg")])
        if not f.exists() or g.stat().st_mtime > f.stat().st_mtime:
            subprocess.run(["gpg", "--batch", "--yes", "--quiet", "--decrypt", "--output", str(f), str(g)], check=True)
            t = g.stat().st_mtime
            os.utime(f, (t, t))  # same age as its .gpg, so seal/check don't take it for an edit
            print("opened", f.relative_to(ROOT))


def check() -> None:
    unsealed = [f for f in secret_files() if stale(f)]
    for f in unsealed:
        print("unsealed", f.relative_to(ROOT))
    sys.exit(1 if unsealed else 0)


if __name__ == "__main__":
    actions = {"seal": seal, "open": open_, "check": check}
    if len(sys.argv) != 2 or sys.argv[1] not in actions:
        sys.exit("usage: secrets.py seal|open|check")
    actions[sys.argv[1]]()
