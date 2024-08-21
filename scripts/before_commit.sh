#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
cd $ROOT_PATH

# poetry run vulture mypy_boto3_builder --make-whitelist > vulture_whitelist.txt
poetry run pre-commit run --all-files

poetry run ruff check scripts --target-version py38
poetry run pyright scripts --pythonversion 3.8

# poetry run pytest --cov-report html --cov mypy_boto3_builder

# ./scripts/docs.sh
