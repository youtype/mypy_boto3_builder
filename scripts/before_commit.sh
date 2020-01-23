#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
cd $ROOT_PATH

vulture mypy_boto3_builder vulture_whitelist.txt
mypy mypy_boto3_builder
pylint mypy_boto3_builder
pytest

./scripts/docs.sh
