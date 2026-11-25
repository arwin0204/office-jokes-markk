#!/usr/bin/env python3
"""One-Line Office Jokes — make.fun entry (program/v1).

Writes a single original one-line joke about office life to
/output/entry.txt (or to the path given as the first argument).
Deterministic: no randomness, no clock, no network, no input files.
The joke turns on a real office detail (reply-all) and lands its
laugh in the last few words.
"""

import os
import sys
from pathlib import Path

# The joke in three beats: a real office detail (reply-all), an
# escalation (400 people pile in), and the laugh on the final beat
# ("by reply-all") — the plea against reply-all is itself answered
# by reply-all, so the line bites its own tail.
ENTRY = (
    "Someone hit reply-all to say 'please stop hitting reply-all,' "
    "and now 400 people agree with them, all at once, by reply-all."
)

MIN_CHARS = 1
MAX_CHARS = 199


def check_entry(text: str) -> None:
    """Enforce the competition gate: 1-199 chars, one line, not blank."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry length {len(text)} outside gate {MIN_CHARS}-{MAX_CHARS}"
        )
    if text.strip() == "":
        raise SystemExit("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")


def main(argv: list[str]) -> int:
    check_entry(ENTRY)
    if len(argv) > 1:
        out = Path(argv[1])
    elif os.environ.get("MAKEFUN_OUTPUT"):
        out = Path(os.environ["MAKEFUN_OUTPUT"])
    else:
        out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    # Write the entry exactly, with no trailing newline, so the file
    # bytes are the entry itself.
    out.write_text(ENTRY, encoding="utf-8")
    # Round-trip check: what was written is exactly what we meant.
    if out.read_text(encoding="utf-8") != ENTRY:
        raise SystemExit("round-trip mismatch")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
