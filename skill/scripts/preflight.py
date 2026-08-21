#!/usr/bin/env python3
"""Validate a generic job-application manifest before delivery."""

import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

REQUIRED = ("company", "role", "url", "verified")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", help="JSON file containing a jobs array")
    args = parser.parse_args()
    data = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    jobs = data.get("jobs", [])
    problems = []
    for index, job in enumerate(jobs, 1):
        missing = [key for key in REQUIRED if not str(job.get(key, "")).strip()]
        if missing:
            problems.append(f"Job {index}: missing {', '.join(missing)}")
        url = str(job.get("url", ""))
        if url and urlparse(url).scheme not in ("http", "https"):
            problems.append(f"Job {index}: url must start with http:// or https://")
    if problems:
        print("DO NOT DELIVER")
        print("\n".join(f"- {problem}" for problem in problems))
        return 1
    print(f"PASS: {len(jobs)} job(s) have the required manifest fields.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
