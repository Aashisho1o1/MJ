#!/usr/bin/env python3
"""Check a document for em-dashes and en-dashes."""

import argparse
import re
import sys

DASH = re.compile(r"[\u2013\u2014]|\\\\textemdash|\\\\textendash")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    text = sys.stdin.read() if args.path == "-" else open(args.path, encoding="utf-8", errors="replace").read()
    hits = [(number, line) for number, line in enumerate(text.splitlines(), 1) if DASH.search(line)]
    if hits:
        print(f"Found prohibited dash characters on {len(hits)} line(s):")
        for number, line in hits[:10]:
            print(f"  {number}: {line}")
        return 1
    print("No em-dashes or en-dashes found.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
