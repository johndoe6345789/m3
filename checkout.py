#!/usr/bin/env python3
"""Check out the m3 family of split repos into sibling directories for local dev."""

import argparse
import subprocess
from pathlib import Path

REPOS = [
    "components",
    "icons",
    "scss",
    "hooks",
    "types",
    "redux",
    "interfaces",
    "schemas",
    "translations",
]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--owner", default="johndoe6345789", help="GitHub owner/org")
    parser.add_argument("--dest", default=".", help="Directory to clone into (default: current directory)")
    parser.add_argument(
        "--repo",
        action="append",
        dest="repos",
        help="Only check out this repo (repeatable). Default: all m3-family repos.",
    )
    args = parser.parse_args()

    repos = args.repos or REPOS
    dest = Path(args.dest)
    dest.mkdir(parents=True, exist_ok=True)

    for name in repos:
        target = dest / name
        if target.exists():
            print(f"skip {name}: {target} already exists")
            continue
        url = f"https://github.com/{args.owner}/{name}.git"
        print(f"cloning {url} -> {target}")
        subprocess.run(["git", "clone", url, str(target)], check=True)


if __name__ == "__main__":
    main()
