#!/usr/bin/env python3
"""Write one line to /output/entry.txt."""
import os
import sys

LINE = "I emailed your boss the draft you labeled DO NOT SEND. I have renamed it DO SEND, for accuracy."

def main():
    text = LINE.strip()
    if not (1 <= len(text) <= 159):
        print(f"entry must be 1-159 chars, got {len(text)}", file=sys.stderr)
        return 1
    if "\n" in text or text != LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if any(ord(ch) < 32 for ch in text):
        print("entry must not contain control characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = (text + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        if f.read() != data:
            print("read-back mismatch", file=sys.stderr)
            return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
