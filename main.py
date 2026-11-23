#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes — entry program.

Writes one line about office life (under 200 characters) to
/output/entry.txt, or to $MAKEFUN_OUTPUT_DIR/entry.txt when set.
Standard library only; deterministic: the same line every run.
"""

import os
import sys

JOKE = (
    "The meeting could have been an email, the email could have been "
    "a Slack message, and the Slack message could have been silence."
)


def output_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main():
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(JOKE + "\n")
    # Read-back verify: the gate needs 1-199 non-whitespace UTF-8 chars.
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    assert 1 <= len(text.strip()) <= 199, "entry length out of gate range"
    assert text.strip() == JOKE, "read-back mismatch"
    return 0


if __name__ == "__main__":
    sys.exit(main())
