#!/usr/bin/env python3
"""Print the entry line from entry.txt, byte for byte.

Resolves entry.txt relative to this file, so it works from any
working directory, even on a read-only filesystem.
"""
from pathlib import Path

import sys


def main() -> int:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    text = entry_path.read_text(encoding="utf-8")
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
