#!/usr/bin/env python3
"""
Authors: Ran# <ran.hash@proton.me>
Created: 2026/10/27 19:06:40.741793
Revised: 2026/10/27 19:10:25.437301
"""

# One-time setup of a grimorio checkout (~/.claude), safe to re-run:
#   1. registers the "grimorio" git filter (bin/filter.py) in this clone's .git/config
#   2. re-checks-out the files through it, if the tree has no local changes, so placeholders and private blocks open
#   3. decrypts the secret memories (bin/secrets.py open)
#   4. links each Claude project-memory folder (projects/<path slug>/memory) to project-memory/<name>/ with a
#      junction, as listed in project-memory/links.json
#   5. adds bin/ to the user PATH (Windows)

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BIN = ROOT / "bin"


def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True, check=True).stdout


def register_filter() -> None:
    git("config", "filter.grimorio.process", f'"{sys.executable}" "{(BIN / "filter.py").as_posix()}"')
    git("config", "filter.grimorio.required", "true")
    if git("status", "--porcelain", "--untracked-files=no").strip():
        print("local changes: skipped re-checkout (run `git checkout-index -f -a` once they're committed)")
        return
    # checkout-index --force skips files git thinks are up to date, so empty the index and check everything out again
    git("read-tree", "--empty")
    git("checkout", "HEAD", "--", ".")
    print("files re-checked-out through the filter")


def link_projects() -> None:
    links = json.loads((ROOT / "project-memory" / "links.json").read_text(encoding="utf-8"))
    for name, slug in links.items():
        target = ROOT / "project-memory" / name
        link = ROOT / "projects" / slug / "memory"
        if link.is_junction() or link.is_symlink():
            continue
        if link.exists():
            print(f"skipped {slug}: a real memory folder is already there")
            continue
        link.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["cmd", "/c", "mklink", "/J", str(link), str(target)], capture_output=True, check=True)
        print("linked", slug, "->", name)


def add_to_path() -> None:
    if sys.platform != "win32":
        print(f"add {BIN} to PATH yourself")
        return
    import winreg

    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_READ | winreg.KEY_WRITE) as key:
        path, kind = winreg.QueryValueEx(key, "Path")
        if str(BIN).lower() not in [p.lower().rstrip("\\") for p in path.split(";")]:
            winreg.SetValueEx(key, "Path", 0, kind, path.rstrip(";") + ";" + str(BIN))
            print("added", BIN, "to the user PATH (new terminals)")


if __name__ == "__main__":
    register_filter()
    subprocess.run([sys.executable, str(BIN / "secrets.py"), "open"], check=True)
    link_projects()
    add_to_path()
