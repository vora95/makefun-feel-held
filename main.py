#!/usr/bin/env python3
"""feel-held entry: write one short text to /output/entry.txt.

The text is a concrete night-kitchen scene (no imperatives, no address to
the judge, no stock wellness phrasing). Deterministic: same bytes every run.
"""
import os

MAX_CODE_POINTS = 280  # gate: 1-280 Unicode code points, not bytes

TEXT = (
    "The kitchen after midnight. The kettle cooling on the stove, "
    "one mug upside down on the rack, rain taking its time on the window. "
    "The chair stays pulled out, keeping a place for whoever stood up, "
    "without asking where they went."
)

def main():
    # Counted as Unicode code points, as the gate requires.
    n = len(TEXT)
    assert 1 <= n <= MAX_CODE_POINTS, f"entry length {n} code points out of range"
    assert TEXT.strip(), "entry is only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
