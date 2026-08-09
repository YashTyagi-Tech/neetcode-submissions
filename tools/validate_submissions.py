#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ast
import subprocess
import sys
from pathlib import Path
from typing import Iterable, List

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_GLOB_ROOT = REPO_ROOT / "Data Structures & Algorithms"


def _run_git(args: List[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def _tracked_python_files() -> List[Path]:
    if not DEFAULT_GLOB_ROOT.exists():
        return []
    return sorted(p for p in DEFAULT_GLOB_ROOT.rglob("*.py") if p.is_file())


def _changed_python_files(base: str, head: str) -> List[Path]:
    out = _run_git(["diff", "--name-only", f"{base}...{head}"])
    files: List[Path] = []
    for line in out.splitlines():
        rel = Path(line.strip())
        if not rel:
            continue
        if rel.suffix != ".py":
            continue
        if "Data Structures & Algorithms" not in rel.parts:
            continue
        abs_path = REPO_ROOT / rel
        if abs_path.exists():
            files.append(abs_path)
    return sorted(files)


def _validate_syntax(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        source = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        errors.append(f"{path}: not valid UTF-8")
        return errors

    try:
        ast.parse(source, filename=str(path))
    except SyntaxError as exc:
        errors.append(
            f"{path}:{exc.lineno}:{exc.offset}: SyntaxError: {exc.msg}"
        )
    return errors


def _validate_structure(path: Path) -> list[str]:
    """Low-noise structural checks for competitive-programming submissions."""
    errors: list[str] = []
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(path))

    has_solution_class = any(
        isinstance(node, ast.ClassDef) and node.name == "Solution"
        for node in tree.body
    )
    has_top_level_def = any(isinstance(node, ast.FunctionDef) for node in tree.body)
    has_any_class = any(isinstance(node, ast.ClassDef) for node in tree.body)

    # Allow design-style problems that define custom classes without Solution.
    if not has_solution_class and not has_top_level_def and not has_any_class:
        errors.append(
            f"{path}: expected at least one class or top-level function definition"
        )

    return errors


def validate(files: Iterable[Path]) -> int:
    files = list(files)
    if not files:
        print("No Python submission files to validate.")
        return 0

    all_errors: list[str] = []
    for path in files:
        all_errors.extend(_validate_syntax(path))
        if not all_errors or not any(str(path) in e for e in all_errors):
            all_errors.extend(_validate_structure(path))

    if all_errors:
        print("Submission validation failed:\n")
        for err in all_errors:
            print(f"- {err}")
        return 1

    print(f"Validation passed for {len(files)} file(s).")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate NeetCode Python submissions")
    parser.add_argument(
        "--changed-only",
        action="store_true",
        help="Validate only changed Python submission files.",
    )
    parser.add_argument(
        "--base",
        default=None,
        help="Base git ref/SHA for changed-only mode.",
    )
    parser.add_argument(
        "--head",
        default="HEAD",
        help="Head git ref/SHA for changed-only mode.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.changed_only:
        if not args.base:
            print("--base is required when using --changed-only", file=sys.stderr)
            return 2
        files = _changed_python_files(args.base, args.head)
    else:
        files = _tracked_python_files()

    return validate(files)


if __name__ == "__main__":
    raise SystemExit(main())
