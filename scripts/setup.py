#!/usr/bin/env python3
"""Cross-platform setup and validation helper for clown-src-6k-skill."""
from pathlib import Path
import argparse
import py_compile
import shutil
import sys

ROOT = Path(__file__).resolve().parent.parent
REQUIRED_FILES = [
    "AGENTS.md",
    "config.toml",
    "skills/skill/SKILL.md",
    "skills/skill/知识库/README.md",
    "skills/skill/知识库/打穿短表.md",
    "bin/playwright-dual-slot.mjs",
    "mcp-servers/fofa_MCP/fofa.py",
    "mcp-servers/fofa_MCP/.env.example",
]


def validate() -> int:
    errors = []
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            errors.append(f"Missing required file: {rel}")

    fofa_py = ROOT / "mcp-servers/fofa_MCP/fofa.py"
    if fofa_py.is_file():
        try:
            py_compile.compile(str(fofa_py), doraise=True)
        except py_compile.PyCompileError as exc:
            errors.append(f"Syntax error in fofa.py: {exc}")

    rules_count = len(list((ROOT / "rules").glob("*.md"))) if (ROOT / "rules").is_dir() else 0
    kb_count = len(list((ROOT / "skills/skill/知识库").glob("*.md"))) if (ROOT / "skills/skill/知识库").is_dir() else 0

    print(f"Rules count: {rules_count}")
    print(f"Knowledge base docs: {kb_count}")

    if errors:
        print("VALIDATION FAILED:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("VALIDATION PASSED")
    return 0


def init_env() -> None:
    env_example = ROOT / "mcp-servers/fofa_MCP/.env.example"
    env_file = ROOT / "mcp-servers/fofa_MCP/.env"
    if env_example.is_file() and not env_file.is_file():
        shutil.copyfile(env_example, env_file)
        print(f"Created {env_file} from .env.example (please fill in your FOFA keys)")
    else:
        print(f"Skipped .env creation ({env_file} already exists or template missing)")


def main() -> int:
    parser = argparse.ArgumentParser(description="Setup and validate clown-src-6k-skill")
    parser.add_argument("--init-env", action="store_true", help="Create fofa_MCP/.env from .env.example if missing")
    parser.add_argument("--check", action="store_true", help="Run repository integrity and syntax checks")
    args = parser.parse_args()

    if args.init_env:
        init_env()
    if args.check or not args.init_env:
        return validate()
    return 0


if __name__ == "__main__":
    sys.exit(main())
