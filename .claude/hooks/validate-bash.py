#!/usr/bin/env python3
"""PreToolUse hook: validates Bash commands in kodiq monorepo.

Blocks:
- git add -A / git add . / git add --all (parallel agents may have uncommitted changes)
- git push --force to main/master
- git commit inside submodule directories
"""
import sys
import json
import re

SUBMODULES = ["academy", "ide", "mobile", "web", "shared"]

data = json.load(sys.stdin)
command = data.get("tool_input", {}).get("command", "")
cwd = data.get("cwd", "")

# --- Block dangerous git add patterns ---
if re.search(r"\bgit\s+add\s+(-A|--all)\b", command):
    print("Use 'git add <specific_files>' instead of 'git add -A/--all'. "
          "Parallel agents may have uncommitted changes!", file=sys.stderr)
    sys.exit(2)

if re.search(r"\bgit\s+add\s+\.\s*($|[;&|])", command):
    print("Use 'git add <specific_files>' instead of 'git add .'. "
          "Parallel agents may have uncommitted changes!", file=sys.stderr)
    sys.exit(2)

# --- Block force push to main/master ---
if re.search(r"\bgit\s+push\b", command) and re.search(r"(--force\b|-f\b)", command):
    if re.search(r"\b(main|master)\b", command):
        print("Force push to main/master is prohibited.", file=sys.stderr)
        sys.exit(2)

# --- Block git commit inside submodule directories ---
if re.search(r"\bgit\s+commit\b", command):
    for sub in SUBMODULES:
        if re.search(rf"\bcd\s+{sub}\b", command) or re.search(rf"\b{sub}/", command):
            print(f"Do not commit inside '{sub}/' submodule from the root repo. "
                  f"Work inside the submodule repository directly.", file=sys.stderr)
            sys.exit(2)

sys.exit(0)
