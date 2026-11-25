#!/usr/bin/env python3
"""One-Line Laugh-Off entry: writes exactly one funny line to entry.txt.

Pure stdlib. Deterministic: the same bytes on every run.
"""
import os

LINE = "My grandmother answers the phone on the second ring. She says the first ring is for people with nothing to hide."

# Gate (RULES.txt): entry.txt must be UTF-8 text of 1 to 200 characters.
assert 1 <= len(LINE) <= 200, "keeper outside the 1-200 char gate"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Self-check: what we wrote is exactly the keeper, nothing else.
    with open(path, "r", encoding="utf-8", newline="") as f:
        assert f.read() == LINE


if __name__ == "__main__":
    main()
