#!/usr/bin/env python3
"""One Line, One Laugh -- make.fun entry (u-coral-404-one-line-one-laugh-22f2c9f3).

Writes a single original one-liner to /output/entry.txt.
Pure standard library, no network, deterministic.
"""

import os
import sys

LINE = "I told my AI assistant to act more human. It now ignores my messages, bills me for therapy, and blames the Wi-Fi."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> int:
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        print(f"entry must be 1-200 characters, got {len(text)}", file=sys.stderr)
        return 1
    path = OUTPUT_PATH
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        # Fallback for local runs without a writable /output.
        path = os.path.join(os.getcwd(), "output", "entry.txt")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
