#!/usr/bin/env python3
"""
Authors: Ran# <ran.hash@proton.me>
Created: 2026/10/27 17:05:42.639618
Revised: 2026/10/27 18:00:36.420839
"""

import sys
import json
import re
import subprocess
from pathlib import Path

data = json.load(sys.stdin)
cmd = data.get("tool_input", {}).get("command", "")

if not re.match(r"^git\s+(commit|push)", cmd):
    sys.exit(0)

errors = []

# extract -C <dir> if present, otherwise use cwd
git_dir_match = re.search(r"git\s+-C\s+['\"]?([^'\" ]+)['\"]?", cmd)
git_cwd = git_dir_match.group(1) if git_dir_match else None
git_base = ["git", "-C", git_cwd] if git_cwd else ["git"]

r = subprocess.run(git_base + ["config", "user.name"], capture_output=True, text=True)
name = r.stdout.strip()
r = subprocess.run(git_base + ["config", "user.email"], capture_output=True, text=True)
email = r.stdout.strip()

if name != "Ran#" or email != "ran.hash@proton.me":
    errors.append(
        f"Wrong author: name='{name}' email='{email}' (expected Ran# / ran.hash@proton.me)"
    )

if re.match(r"^git\s+commit", cmd):
    # -m "$(cat <<'EOF' ... EOF)" heredoc idiom (used for multi-line messages)
    heredoc_m = re.search(
        r"-m\s+\"\$\(cat\s+<<-?(['\"]?)(\w+)\1\s*\n(.*?)\n\s*\2\s*\n?\)\"",
        cmd,
        re.DOTALL,
    )
    m = None if heredoc_m else (
        re.search(r'-m\s+"((?:[^"\\]|\\.)+)"', cmd) or re.search(r"-m\s+'([^']+)'", cmd)
    )
    if heredoc_m:
        msg = heredoc_m.group(3)
    elif m:
        msg = m.group(1)
    else:
        # -F <file> (also accepted as a way to pass a commit message)
        f = (
            re.search(r'-F\s+"([^"]+)"', cmd)
            or re.search(r"-F\s+'([^']+)'", cmd)
            or re.search(r"-F\s+(\S+)", cmd)
        )
        if f and f.group(1) == "-":
            # -F - reads stdin: take the message from the heredoc fed to it
            h = re.search(r"<<-?(['\"]?)(\w+)\1[^\n]*\n(.*?)\n\s*\2\s*(?:\n|$)", cmd, re.DOTALL)
            msg = h.group(3) if h else None
            if not h:
                errors.append("Could not find the heredoc message for -F -")
        elif f:
            try:
                with open(f.group(1), "r", encoding="utf-8") as fh:
                    msg = fh.read()
            except OSError as e:
                msg = None
                errors.append(f"Could not read -F commit message file '{f.group(1)}': {e}")
        else:
            msg = ""
    if msg is not None and not re.match(r"^\[([ARFDTCPBS])\]", msg):
        errors.append(
            f"Invalid bracket in commit message: '{msg}' — allowed: [A][R][F][D][T][C][P][B][S]"
        )

    if re.search(r"co-authored-by", (msg or "") + "\n" + cmd, re.IGNORECASE):  # any -m, not just the first
        errors.append("Co-Authored-By trailer is not allowed in commit messages")

    # CONTRIBUTING.md must exist in the repo
    r = subprocess.run(
        git_base + ["ls-files", "CONTRIBUTING.md"],
        capture_output=True, text=True
    )
    if not r.stdout.strip():
        errors.append("CONTRIBUTING.md is missing from the repository — create it before committing")

    # no raw secrets in the staged lines (tokens, API keys, private keys)
    r = subprocess.run(git_base + ["diff", "--cached", "-U0", "--no-color"], capture_output=True, text=True)
    secret_re = re.compile(
        r"gh[pousr]_[A-Za-z0-9]{30,}|github_pat_\w{30,}|glpat-[\w-]{20,}|sk-[\w-]{30,}|sk_live_\w{20,}|whsec_\w{20,}"
        r"|xox[abp]-[\w-]{20,}|AKIA[0-9A-Z]{16}|AIza[\w-]{35}|\b\d{8,10}:AA[\w-]{30,}|cfut_\w{20,}"
        r"|BEGIN [A-Z ]*PRIVATE KEY|`[0-9a-f]{40}`"
    )
    leaked = sorted({ln[1:].strip()[:24] + "…" for ln in r.stdout.splitlines()
                     if ln.startswith("+") and not ln.startswith("+++") and secret_re.search(ln)})
    if leaked:
        errors.append("Staged lines look like raw secrets (encrypt them instead): " + "; ".join(leaked))

    # in grimorio, every secret memory must be sealed (bin/secrets.py) before committing
    r = subprocess.run(git_base + ["rev-parse", "--show-toplevel"], capture_output=True, text=True)
    sealer = Path(r.stdout.strip()) / "bin" / "secrets.py"
    if r.stdout.strip() and sealer.is_file():
        r = subprocess.run([sys.executable, str(sealer), "check"], capture_output=True, text=True)
        if r.returncode:
            errors.append("Secret memories changed but not re-sealed: run `python bin/secrets.py seal`\n"
                          + r.stdout.strip())

    # never let .claude/ enter history
    r = subprocess.run(
        git_base + ["diff", "--cached", "--name-only"],
        capture_output=True, text=True
    )
    staged_claude = [f for f in r.stdout.splitlines() if re.search(r"(^|/)\.claude/", f)]
    if staged_claude:
        errors.append(
            "Staged files under .claude/ are not allowed in commits: " + ", ".join(staged_claude)
        )

if errors:
    # Refuse the command (it doesn't run until the errors are fixed) but keep Claude's turn going: the reasons go
    # back to Claude, which fixes them and retries. "continue": false would end the whole turn instead.
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": "Blocked:\n- " + "\n- ".join(errors) + "\nFix these and run the command again.",
        }
    }))
    sys.exit(0)
