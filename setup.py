#!/usr/bin/env python
from pathlib import Path

import setuptools

if __name__ == "__main__":
    setuptools.setup(
        install_requires=[
            line
            for line in (Path(__file__).parent / "requirements.txt").read_text().split("\n")
            if line.strip() and not line.startswith("-")
        ]
    )
