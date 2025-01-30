#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
cd ${ROOT_PATH}

python -m mypy_boto3_builder --no-smart-version mypy_boto3_output $@
