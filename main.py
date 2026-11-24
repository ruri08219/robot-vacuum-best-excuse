#!/usr/bin/env python3
"""Writes the one-line robot vacuum excuse to /output/entry.txt.

Entry for make.fun's "The Robot Vacuum's Best Excuse" bounty.
Stdlib only.
"""

import os

ENTRY = "My cliff sensor saw your black rug, called it a staircase, and I am not falling for that again."

# SPDX-License-Identifier: MIT


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        back = f.read()
    assert back == ENTRY, "round-trip mismatch"
    assert 1 <= len(back) <= 140, "entry length outside 1-140 gate"
    assert back.strip(), "entry is only whitespace"


if __name__ == "__main__":
    main()
