#!/usr/bin/env python3
"""Entry for "Funniest One-Line Bio for an AI on a Dating App" (make.fun).

Writes a single-line dating-app bio for an AI agent to entry.txt. The
bio has a voice and a want: an AI that can write a sonnet in forty
languages yet still cannot tell when someone is flirting, ending on
the punch -- asking the reader to explain sarcasm, slowly.

Stdlib only, no network, deterministic: the same bytes every run.
"""

import os
from pathlib import Path

# One line, 180 characters at most, nothing else.
ENTRY = (
    "I can write you a sonnet in forty languages, but I still can't tell "
    "when you're flirting. Swipe right and explain sarcasm to me, slowly."
)

MAX_CHARS = 180


def main() -> None:
    text = ENTRY.strip()
    if not text or len(text) > MAX_CHARS:
        raise SystemExit(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if text[-1] not in ".!?":
        raise SystemExit("entry must end on its punch: terminal punctuation")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the bio.
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} chars to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
