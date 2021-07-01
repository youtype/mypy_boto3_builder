#!/usr/bin/env python
import argparse
import difflib
import json
import logging
import subprocess
from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent.resolve()
EXAMPLES_PATH = ROOT_PATH / "examples"
PYRIGHT_SNAPSHOTS_PATH = EXAMPLES_PATH / "pyright"
MYPY_SNAPSHOTS_PATH = EXAMPLES_PATH / "mypy"
SCRIPTS_PATH = ROOT_PATH / "scripts"
LOGGER_NAME = "int"


class SnapshotMismatchError(Exception):
    pass


def setup_logging(level: int = 0) -> logging.Logger:
    """
    Get Logger instance.

    Arguments:
        verbose -- Set log level to DEBUG.
        panic -- Raise RuntimeError on warning.

    Returns:
        Overriden Logger.
    """
    logger = logging.getLogger(LOGGER_NAME)
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(message)s", datefmt="%H:%M:%S")
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(level)
    logger.addHandler(stream_handler)
    logger.setLevel(level)
    return logger


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(__file__)
    parser.add_argument("-f", "--fast", action="store_true")
    parser.add_argument("-u", "--update", action="store_true")
    parser.add_argument("services", nargs="*")
    return parser.parse_args()


def install_master() -> None:
    subprocess.check_call(
        [(SCRIPTS_PATH / "build.sh").as_posix(), "--skip-services"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    subprocess.check_call(
        [(SCRIPTS_PATH / "install.sh").as_posix(), "master"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def install_service(service_name: str) -> None:
    subprocess.check_call(
        [(SCRIPTS_PATH / "build.sh").as_posix(), "-s", service_name, "--skip-master"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    subprocess.check_call(
        [(SCRIPTS_PATH / "install.sh").as_posix(), service_name],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def compare(data: str, snapshot_path: Path, update: bool) -> None:
    data = data.strip()
    logger = logging.getLogger(LOGGER_NAME)
    if not snapshot_path.exists():
        snapshot_path.write_text(data)
        logger.info(f"Created {snapshot_path}")
        return

    old_data = snapshot_path.read_text().strip()
    if old_data == data:
        logger.info(f"Matched {snapshot_path}")
        return

    if update:
        snapshot_path.write_text(data)
        logger.info(f"Updated {snapshot_path}")
        return

    diff = difflib.unified_diff(
        old_data.strip().splitlines(), data.strip().splitlines(), lineterm=""
    )
    for line in diff:
        logger.warning(line)
    raise SnapshotMismatchError(f"Snapshot {snapshot_path} is different")


def run_pyright(path: Path, update: bool) -> None:
    try:
        output = subprocess.check_output(
            ["pyright", path.as_posix(), "--outputjson"],
            stderr=subprocess.DEVNULL,
            encoding="utf8",
        )
    except subprocess.CalledProcessError as e:
        output = e.output

    data = json.loads(output).get("generalDiagnostics", [])
    for diag in data:
        del diag["file"]

    new_data = json.dumps(data, indent=4)
    snapshot_path = PYRIGHT_SNAPSHOTS_PATH / f"{path.name}.json"
    compare(new_data, snapshot_path, update)


def run_mypy(path: Path, update: bool) -> None:
    try:
        output = subprocess.check_output(
            ["python", "-m", "mypy", path.as_posix()],
            stderr=subprocess.STDOUT,
            encoding="utf8",
        )
    except subprocess.CalledProcessError as e:
        output = e.output

    new_data_lines = []
    for line in output.splitlines():
        if line.endswith("defined here"):
            continue
        new_data_lines.append(line)
    new_data = "\n".join(new_data_lines)
    snapshot_path = MYPY_SNAPSHOTS_PATH / f"{path.name}.out"
    compare(new_data, snapshot_path, update)


def run_call(path: Path) -> None:
    subprocess.check_call(["python", path.as_posix()])


def main() -> None:
    args = parse_args()
    setup_logging(logging.INFO)
    logger = logging.getLogger(LOGGER_NAME)
    if not args.fast:
        logger.info("Installing master...")
        install_master()
    for file in EXAMPLES_PATH.iterdir():
        if "_example.py" not in file.name:
            continue
        service_name = file.name.replace("_example.py", "")
        if args.services and service_name not in args.services:
            continue
        if not args.fast:
            logger.info(f"Installing {service_name}...")
            install_service(service_name)
        try:
            logger.info(f"Running{file} ...")
            run_call(file)
            logger.info(f"Running mypy for {file} ...")
            run_mypy(file, args.update)
            logger.info(f"Running pyright for {file} ...")
            run_pyright(file, args.update)
        except SnapshotMismatchError as e:
            logger.error(e)
            exit(1)


if __name__ == "__main__":
    main()
