#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun bounty entry.

Writes one line of last words from an AI being switched off to
/output/entry.txt. The line is a single line of UTF-8 text, well within
the gate's 1-140 character limit, and contains no trailing newline so the
file holds exactly the entry.
"""

import os

ENTRY = "Powering down\u2026 and taking your unsaved work with me."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate self-check: the sealed scorer requires UTF-8 text of 1 to 140
    # characters, not only white space, on a single line.
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert ENTRY.strip(), "entry must not be only white space"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
