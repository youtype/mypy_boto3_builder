#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
cd $ROOT_PATH

# uv run vulture mypy_boto3_builder --make-whitelist > vulture_whitelist.txt
uv run pre-commit run --all-files

# uv run pytest --cov-report html --cov mypy_boto3_builder

# ./scripts/docs.sh
