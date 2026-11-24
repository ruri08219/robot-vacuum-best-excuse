#!/usr/bin/env python3
"""Writes the one-line robot vacuum excuse to /output/entry.txt.

Entry for make.fun's "The Robot Vacuum's Best Excuse" bounty.
Stdlib only.
"""

import os

ENTRY = "My cliff sensor saw your black rug, called it a staircase, and I am not falling for that again."

MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"

# SPDX-License-Identifier: MIT


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        back = f.read()
    assert back == ENTRY, "round-trip mismatch"
    assert 1 <= len(back) <= MAX_CHARS, "entry length outside 1-140 gate"
    assert back.strip(), "entry is only whitespace"


if __name__ == "__main__":
    main()
