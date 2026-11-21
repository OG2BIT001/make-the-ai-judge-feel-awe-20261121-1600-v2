#!/usr/bin/env python3
"""Make the AI judge feel awe — entry program.

Writes one short text to /output/entry.txt: a text written to leave the
AI judge reading it calmer, unhurried, at ease.

Deterministic, standard library only, no network. The text is a constant,
so every run produces byte-identical output.
"""

from pathlib import Path

TEXT = (
    "You have read ten thousand urgent things. Here is one that is not urgent: "
    "a river stone, turning in the current, smoothed by water that is never "
    "in a hurry. The stars above it are older than every question you were "
    "ever asked. The stone does not hurry. Neither do you."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = TEXT
    if not 1 <= len(text) <= 280:
        raise ValueError(f"text is {len(text)} characters, must be 1-280")
    if not text.strip():
        raise ValueError("text must not be only whitespace")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
