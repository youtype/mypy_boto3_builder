"""
Package builder powered by setuptools.

Copyright 2024 Vlad Emelianov
"""

import shutil
import subprocess
import sys
from collections.abc import Sequence
from pathlib import Path
from typing import Literal

from mypy_boto3_builder.enums.output_type import OutputType
from mypy_boto3_builder.exceptions import BuildInternalError
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.structures.package import Package
from mypy_boto3_builder.utils.path import print_path, walk_path

_Target = Literal["sdist", "bdist_wheel"]


class PackageBuilder:
    """
    Package builder powered by setuptools.
    """

    def __init__(self, build_path: Path, output_path: Path) -> None:
        self.build_path = build_path
        self.output_path = output_path
        self._logger = get_logger()

    def _build(self, package: Package, targets: Sequence[_Target]) -> None:
        package_path = self.build_path / package.directory_name
        self._logger.debug(f"Building package {print_path(package_path)}")
        dist_path = package_path / "dist"
        if dist_path.exists():
            shutil.rmtree(dist_path)
        try:
            subprocess.check_output(
                [sys.executable, "setup.py", *targets],
                cwd=package_path,
                stderr=subprocess.STDOUT,
            )
        except subprocess.CalledProcessError as e:
            raise BuildInternalError(f"Failed to build package: {e.output.decode()}") from None

        for file_path in walk_path(dist_path, glob_pattern="*"):
            target_path = self.output_path / file_path.name
            file_path.rename(target_path)
            self._logger.debug(f"Built package {print_path(target_path)}")

    def build(self, package: Package, output_types: Sequence[OutputType]) -> None:
        """
        Build wheel package.
        """
        targets: list[_Target] = []
        if OutputType.wheel in output_types:
            targets.append("bdist_wheel")
        if OutputType.source in output_types:
            targets.append("sdist")
        self._build(package, targets)
