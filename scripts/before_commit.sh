#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
cd $ROOT_PATH

# uvx vulture mypy_boto3_builder --make-whitelist > vulture_whitelist.txt
uvx pre-commit run --all-files

# uvx pytest --cov-report html --cov mypy_boto3_builder

# ./scripts/docs.sh
