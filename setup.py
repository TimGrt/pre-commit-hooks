#!/usr/bin/env python

from distutils.core import setup

setup(
    name="check-file-names",
    version="0.1.1",
    description="Pre-commit hook the check file names for compliance",
    author="Tim Gruetzmacher",
    url="https://github.com/TimGrt/pre-commit-hooks/",
    py_modules=["pre_commit_hooks.check-file-names"],
)
