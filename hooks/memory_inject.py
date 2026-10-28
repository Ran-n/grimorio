#!/usr/bin/env python3
"""
Authors: Ran# <ran.hash@proton.me>
Created: 2026/10/28 14:25:37.193543
Revised: 2026/10/28 14:26:06.074180

UserPromptSubmit hook: inject the full text of every memory file whose topic the prompt touches.

MEMORY.md only carries one-line summaries, so a matching rule can be skipped when its file is
never opened. This hook removes that step: the bodies land in the context before the reply.
"""

import json
import logging
import re
import sys
from pathlib import Path

MEMORY_DIR = Path.home() / ".claude" / "memory"
LOG_FILE = Path.home() / ".claude" / "hooks" / "memory_inject.log"

logger = logging.getLogger("memory_inject")

# Each pattern is matched case-insensitively against the prompt; every listed file is injected.
TOPICS: list[tuple[str, list[str]]] = [
    (
        r"\btest|coverage|\bcov\b|pytest|cargo test|baseline|snapshot|regression|\bqa\b",
        ["feedback_tests.md", "feedback_regression_safety.md", "feedback_gap_free.md"],
    ),
    (
        r"\b(implement|add|fix|build|change|refactor|feature|bug)",
        [
            "feedback_gap_free.md",
            "feedback_tests.md",
            "feedback_regression_safety.md",
            "feedback_clean_code.md",
        ],
    ),
    (r"\bcommit", ["feedback_commits.md", "feedback_changelog.md", "feedback_push.md"]),
    (
        r"\bpush|\bdbp\b|remote",
        ["feedback_push.md", "feedback_push_all_remotes.md", "reference_ssh_keys.md"],
    ),
    (
        r"\bbump|\brelease|\bversion",
        [
            "feedback_version_bump.md",
            "feedback_releases.md",
            "feedback_versioned_build_filenames.md",
        ],
    ),
    (r"\bhash|blake", ["feedback_hashing.md"]),
    (
        r"i18n|translat|locale|language|galician|spanish",
        ["feedback_i18n_completeness.md"],
    ),
    (r"\blog(s|ging|ger)?\b", ["feedback_logging.md", "feedback_no_silent_failure.md"]),
    (r"\berror|exception|fail", ["feedback_no_silent_failure.md"]),
    (r"schema|database|\bdb\b|table|migration|sql", ["feedback_database_bcnf.md"]),
    (
        r"new repo|scaffold|\binit\b|license|contribut",
        [
            "feedback_new_repo_scaffold.md",
            "reference_license.md",
            "reference_contributing_layout.md",
            "reference_contributors_layout.md",
        ],
    ),
    (
        r"\bui\b|button|dialog|screen|layout|widget|page|window",
        [
            "feedback_ui_disabled_buttons.md",
            "feedback_ui_inline_editing.md",
            "feedback_ui_cta_hierarchy.md",
        ],
    ),
    (r"header|metadata", ["feedback_file_headers.md"]),
    (r"\bruff\b|lint|format", ["feedback_python_projects.md"]),
    (
        r"full sweep|audit",
        ["feedback_full_sweep.md", "feedback_tests.md", "feedback_gap_free.md"],
    ),
    (
        r"\bapk\b|android|flet",
        [
            "feedback_flet_split_apk_staleness.md",
            "reference_flet_cross_target_testing.md",
        ],
    ),
    (
        r"endpoint|\bapi\b",
        ["feedback_stripe_expand_pattern.md", "feedback_bulk_endpoints.md"],
    ),
    (r"folder|structure|organi[sz]", ["feedback_source_organization.md"]),
    (r"\bquit|shutdown|close|exit", ["feedback_universal_behaviours.md"]),
]


def matching_files(prompt: str) -> list[str]:
    files: list[str] = []
    for pattern, names in TOPICS:
        if re.search(pattern, prompt, re.IGNORECASE):
            files.extend(name for name in names if name not in files)
    return files


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    try:
        prompt = json.load(sys.stdin).get("prompt", "")
    except (json.JSONDecodeError, OSError) as error:
        logger.error("could not read hook input: %s", error)
        print(
            f"memory_inject hook: could not read the prompt ({error}); open the matching memory files by hand."
        )
        return 0
    sections = []
    for name in matching_files(prompt):
        path = MEMORY_DIR / name
        try:
            sections.append(f"===== {name} =====\n{path.read_text(encoding='utf-8')}")
        except OSError as error:
            logger.error("could not read %s: %s", path, error)
            sections.append(f"===== {name} ===== (unreadable: {error})")
    if sections:
        logger.info("injected %s", ", ".join(name for name in matching_files(prompt)))
        print(
            "The user's standing rules below match this prompt. They are binding: follow every one that applies, "
            "and when answering about a topic, measure the work against them (e.g. a testing question means the "
            "audit procedure in feedback_tests.md).\n\n" + "\n\n".join(sections)
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
