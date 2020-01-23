#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
cd ${ROOT_PATH}

python -m mypy_boto3_builder mypy_boto3_output $@
