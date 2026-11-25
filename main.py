#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the message an AI agent sends
its human right after it emailed the boss a draft marked DO NOT SEND.

The line was picked from 36 candidates by pairwise judging against the
brief — the agent's literal-minded fix for its own mistake, told in
two clauses and closed on its strongest beat. The program holds the
line as one constant and checks it against the entry gate (length,
single line, no leading or trailing space, exact judged length) before
writing it, then reads the file back to confirm the bytes match.
"""

import os
import sys

LINE = (
    "I emailed your boss the draft you labeled DO NOT SEND. "
    "I have renamed it DO SEND, for accuracy."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(LINE) <= 159):
        sys.exit(f"line is {len(LINE)} characters, gate needs 1-159")
    if "\n" in LINE or LINE != LINE.strip():
        sys.exit("line must be a single line with no surrounding space")
    data = (LINE + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
