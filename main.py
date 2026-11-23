#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes entry.

One original line about office life (120 characters), written to
/output/entry.txt. Deterministic: the same line on every run, no
network, no randomness, stdlib only.
"""

from pathlib import Path

LINE = "The break room sign says 'Your mother doesn't work here' \u2014 mine does, she's in accounting, and she agrees with the sign."

MAX_CHARS = 199


def validate(line: str) -> str:
    """The gate needs 1-199 characters of real text, not only whitespace."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"line is {len(line)} characters, must be 1-{MAX_CHARS}")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if line != line.strip():
        raise ValueError("line must not start or end with whitespace")
    return line


def main() -> None:
    text = validate(LINE)
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
