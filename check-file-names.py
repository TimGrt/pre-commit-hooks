#!/usr/bin/env python3
from __future__ import annotations

import re
import pathlib
import subprocess
import argparse

from typing import Any, Sequence


class CalledProcessError(RuntimeError):
    pass


def cmd_output(*cmd: str, retcode: int | None = 0, **kwargs: Any) -> str:
    kwargs.setdefault("stdout", subprocess.PIPE)
    kwargs.setdefault("stderr", subprocess.PIPE)
    proc = subprocess.Popen(cmd, **kwargs)
    stdout, stderr = proc.communicate()
    stdout = stdout.decode()
    if retcode is not None and proc.returncode != retcode:
        raise CalledProcessError(cmd, retcode, proc.returncode, stdout, stderr)
    return stdout


def validate_regex_pattern(pattern: str):
    # pattern is a string containing the regex pattern
    try:
        re.compile(pattern)
    except re.error:
        print("Non valid regex pattern provided, got '%s'" % pattern)
        exit(1)


def check_filenames(files: Sequence[str], pattern: str) -> int:
    staged_files = set(
        cmd_output("git", "diff", "--staged", "--name-only", *files).splitlines()
    )
    invalid_files = []

    validate_regex_pattern(pattern)

    for file in staged_files:
        if not re.search(pattern, pathlib.Path(file).stem):
            invalid_files.append(file)

    if invalid_files:
        for file in sorted(invalid_files):
            print(f"File does not comply to standards: {file}")
        return 1
    else:
        return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*")
    parser.add_argument(
        "--pattern",
        default="^[a-z][a-zA-Z\-]+$",
        help=("regex pattern for file names not allowed to commit"),
    )
    args = parser.parse_args(argv)

    validate_regex_pattern(args.pattern)

    return check_filenames(args.files, args.pattern)


if __name__ == "__main__":
    raise SystemExit(main())
