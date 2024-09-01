#!/usr/bin/env python
"""
Pull static stubs from GitHub to local directories.
"""

import logging
import shutil
import tempfile
from pathlib import Path

from mypy_boto3_builder.constants import StaticStubsPath, StaticStubsPullURL
from mypy_boto3_builder.utils.github import download_and_extract
from mypy_boto3_builder.utils.path import print_path


def setup_logging(level: int) -> logging.Logger:
    """
    Get Logger instance.

    Arguments:
        level -- Log level

    Returns:
        Overriden Logger.
    """
    logger = logging.getLogger(Path(__file__).stem)
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s %(levelname)-7s %(message)s", datefmt="%H:%M:%S")
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(level)
    logger.addHandler(stream_handler)
    logger.setLevel(level)
    return logger


logger = setup_logging(logging.DEBUG)


def pull_static(url: str, output_path: Path, temp_path: Path) -> None:
    """
    Pull static files from URL and copy them to output path.
    """
    logger.debug(f"Pulling static files from {url} to {print_path(output_path)}")
    download_path = download_and_extract(url, temp_path)
    download_path_map = {i.relative_to(download_path): i for i in download_path.glob("**/*.pyi")}
    output_path_map = {i.relative_to(output_path): i for i in output_path.glob("**/*.pyi")}
    for path_key, path in download_path_map.items():
        if path.name == "py.typed":
            continue

        output_file_path = output_path / path_key
        if path_key not in output_path_map:
            shutil.copy(path, output_file_path)
            logger.info(f"Added {print_path(output_file_path)}")

        remote_content = path.read_text()
        local_content = (output_path / path_key).read_text()
        if remote_content != local_content:
            shutil.copy(path, output_file_path)
            logger.info(f"Updated {print_path(output_file_path)}")

    for path_key, path in output_path_map.items():
        if path.is_dir():
            continue

        if path_key not in download_path_map:
            path.unlink()
            logger.info(f"Removed {print_path(path)}")


def main() -> None:
    """
    Run main entrypoint.
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_dir_path = Path(temp_dir)
        pull_static(StaticStubsPullURL.boto3, StaticStubsPath.boto3, temp_dir_path)
        pull_static(StaticStubsPullURL.aiobotocore, StaticStubsPath.aiobotocore, temp_dir_path)
        pull_static(StaticStubsPullURL.aioboto3, StaticStubsPath.aioboto3, temp_dir_path)


if __name__ == "__main__":
    main()
