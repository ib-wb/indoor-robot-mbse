#!/usr/bin/env python3
"""Reject files outside the reviewed publication list before pushing."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    entries = [line.strip() for line in (ROOT / ".publication-files.txt").read_text(
        encoding="utf-8").splitlines() if line.strip() and not line.startswith("#")]
    allowed = set(entries)
    if len(entries) != len(allowed):
        raise RuntimeError("Duplicate publication entry")
    for path in allowed:
        if "\\" in path or path.startswith("/") or any(
                part in {"", ".", "..", ".git"} for part in path.split("/")):
            raise RuntimeError(f"Invalid publication path: {path}")
    result = subprocess.run(["git", "ls-files", "--stage", "-z"], cwd=ROOT,
                            capture_output=True, check=True)
    tracked = set()
    for entry in result.stdout.decode("utf-8").split("\0"):
        if not entry:
            continue
        meta, path = entry.split("\t", 1)
        mode, _, stage = meta.split()
        if mode not in {"100644", "100755"} or stage != "0":
            raise RuntimeError(f"Unsupported Git entry: {path}")
        tracked.add(path)
    local = set()
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if relative.parts[0] == ".git":
            continue
        if path.is_symlink():
            raise RuntimeError(f"Symbolic link: {relative.as_posix()}")
        if path.is_file():
            local.add(relative.as_posix())
    problems = []
    for label, files in (("Git index", tracked), ("working tree", local)):
        if files != allowed:
            problems.append(f"{label}: unexpected={sorted(files - allowed)}, "
                            f"missing={sorted(allowed - files)}")
    if problems:
        raise RuntimeError("\n".join(problems))
    print(f"PUBLICATION files={len(allowed)} tracked_and_local_match=true")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, subprocess.SubprocessError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)
