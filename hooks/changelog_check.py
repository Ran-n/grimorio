#!/usr/bin/env python3
"""
Authors: Ran# <ran.hash@proton.me>
Created: 2026/10/27 17:21:16.345106
Revised: 2026/10/27 17:21:16.345106
"""

"""
Pre-commit hook: refuses a git commit if CHANGELOG.md is not staged.
Allows it if CHANGELOG.md is among the staged files or if nothing worth
documenting is staged. Checks the repo the commit is for: the directory of a
`cd <dir>` before the commit, or `git -C <dir>`, else the hook's own cwd.
A refusal is a PreToolUse "deny" with the reason: the commit doesn't run
until CHANGELOG.md is staged, but Claude's turn goes on, so it can fix that
and retry ("continue": false would end the whole turn instead).
"""
import json
import re
import subprocess
import sys


def deny(reason: str) -> None:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }))
    sys.exit(0)


def repo_dir(cmd: str) -> str | None:
    """Where the commit runs: `git -C <dir> commit`, else the last `cd <dir>` before `git commit`."""
    m = re.search(r"git\s+-C\s+['\"]?([^'\" ;&|]+)['\"]?\s+commit", cmd)
    if m:
        return m.group(1)
    before = cmd[: cmd.find("git commit")] if "git commit" in cmd else cmd
    dirs = re.findall(r"(?:^|[;&|]\s*)cd\s+(?:/d\s+)?['\"]?([^'\";&|]+?)['\"]?\s*(?=$|[;&|])", before)
    return dirs[-1].strip() if dirs else None


def to_windows(path: str) -> str:
    """Git Bash paths like /d/Users/x -> D:/Users/x, so git.exe finds them."""
    m = re.match(r"^/([a-zA-Z])/(.*)$", path)
    return f"{m.group(1).upper()}:/{m.group(2)}" if m else path


def staged_files(where: str | None) -> list[str]:
    base = ["git", "-C", to_windows(where)] if where else ["git"]
    result = subprocess.run(base + ["diff", "--staged", "--name-only"], capture_output=True, text=True)
    return [f.strip() for f in result.stdout.splitlines() if f.strip()]


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except ValueError:
        data = {}
    cmd = data.get("tool_input", {}).get("command", "")
    if cmd and not re.search(r"\bgit\s+(-C\s+\S+\s+)?commit\b", cmd):
        sys.exit(0)

    where = repo_dir(cmd)
    files = staged_files(where)
    if not files or "CHANGELOG.md" in files:
        sys.exit(0)

    # Only refuse if there are staged changes worth documenting
    ignorable = {".gitignore", "TODO.md"}
    meaningful = [f for f in files if f not in ignorable and not f.startswith(".")]
    if not meaningful:
        sys.exit(0)

    deny(
        "CHANGELOG.md has not been updated to reflect the staged changes"
        f"{' in ' + where if where else ''}.\n"
        f"Staged files: {', '.join(files)}\n"
        "Update CHANGELOG.md, stage it, and run the commit again."
    )


if __name__ == "__main__":
    main()
