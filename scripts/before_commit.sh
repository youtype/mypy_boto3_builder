#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
cd $ROOT_PATH

# poetry run vulture mypy_boto3_builder --make-whitelist > vulture_whitelist.txt
poetry run vulture mypy_boto3_builder vulture_whitelist.txt
poetry run npx pyright mypy_boto3_builder
poetry run flake8 mypy_boto3_builder
poetry run pytest
poetry run black mypy_boto3_builder tests
poetry run isort mypy_boto3_builder tests
poetry run mypy mypy_boto3_builder
# poetry run pytest --cov-report html --cov mypy_boto3_builder

# ./scripts/docs.sh
