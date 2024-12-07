#!/usr/bin/env bash
set -e

# types-boto3
uv run --no-project --with ruff --with boto3 mypy_boto3_builder mypy_boto3_output --product types-boto3 types-boto3-lite

# types-aiobotocore
uv run --no-project --with ruff --with aiobotocore mypy_boto3_builder mypy_boto3_output --product aiobotocore aiobotocore-lite

# types-aioboto3
uv run --no-project --with ruff --with aioboto3 mypy_boto3_builder mypy_boto3_output --product aioboto3 aioboto3-lite

# boto3-stubs
uv run --no-project --with ruff --with boto3 mypy_boto3_builder mypy_boto3_output --product boto3 boto3-lite
