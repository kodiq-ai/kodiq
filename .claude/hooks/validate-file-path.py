#!/usr/bin/env python3
"""PreToolUse hook: blocks Write/Edit inside submodule directories.

Submodules are separate repositories — changes should be made
inside the submodule repo, not from the monorepo root.
"""
import sys
import json
import os

SUBMODULES = ["academy", "ide", "mobile", "web", "shared"]

data = json.load(sys.stdin)
file_path = data.get("tool_input", {}).get("file_path", "")
cwd = data.get("cwd", "")

if not file_path or not cwd:
    sys.exit(0)

try:
    rel_path = os.path.relpath(file_path, cwd)
except ValueError:
    sys.exit(0)

# Don't block if path goes outside repo (e.g. ../)
if rel_path.startswith(".."):
    sys.exit(0)

for sub in SUBMODULES:
    if rel_path == sub or rel_path.startswith(sub + os.sep):
        print(f"Cannot edit files inside '{sub}/' submodule from the root repo. "
              f"Work inside the submodule repository directly.\n"
              f"Path: {rel_path}", file=sys.stderr)
        sys.exit(2)

sys.exit(0)
