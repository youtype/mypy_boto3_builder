#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
cd $ROOT_PATH

# vulture mypy_boto3_builder --make-whitelist > vulture_whitelist.txt
vulture mypy_boto3_builder vulture_whitelist.txt
# npx pyright mypy_boto3_builder
flake8 mypy_boto3_builder
pytest
black mypy_boto3_builder tests
isort -c mypy_boto3_builder tests
mypy mypy_boto3_builder
# pytest --cov-report html --cov mypy_boto3_builder

./scripts/docs.sh
