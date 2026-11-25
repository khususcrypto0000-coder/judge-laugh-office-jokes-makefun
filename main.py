#!/usr/bin/env python3
"""Entry generator for "Make the AI Judge Laugh: Office Jokes" (make.fun).

Writes a single one-line office joke to /output/entry.txt (or
$OUTPUT_DIR/entry.txt when OUTPUT_DIR is set), then reads it back and
verifies the written bytes are identical to the source text.

Python standard library only (os, sys).
"""

import os
import sys

# The final entry: one line, under 200 characters, with a twist at the end.
ENTRY = "I booked the conference room to escape meetings, then got invited to a meeting in it."


def _validate(text):
    """Enforce the bounty gate: 1-199 chars, exactly one line, not blank."""
    assert isinstance(text, str), "entry must be a string"
    assert 1 <= len(text) <= 199, "entry must be 1-199 characters, got %d" % len(text)
    assert text.strip(), "entry must not be only whitespace"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be exactly one line"


def main():
    _validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    data = ENTRY.encode("utf-8")  # no trailing newline: exactly one line
    with open(path, "wb") as f:
        f.write(data)
    # Read back and verify byte-identical output.
    with open(path, "rb") as f:
        written = f.read()
    assert written == data, "read-back mismatch: output is not byte-identical"
    assert written.decode("utf-8") == ENTRY, "read-back text mismatch"
    print("wrote %s (%d characters, %d bytes)" % (path, len(ENTRY), len(data)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
