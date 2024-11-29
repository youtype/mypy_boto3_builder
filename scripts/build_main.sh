#!/usr/bin/env bash
set -e

# types-boto3
uvx --with boto3 mypy_boto3_builder mypy_boto3_output --product types-boto3 types-boto3-lite

# types-aiobotocore
uvx --with aiobotocore mypy_boto3_builder mypy_boto3_output --product aiobotocore aiobotocore-lite

# types-aioboto3
uvx --with aioboto3 mypy_boto3_builder mypy_boto3_output --product aioboto3 aioboto3-lite

# boto3-stubs
uvx --with boto3 mypy_boto3_builder mypy_boto3_output --product boto3 boto3-lite
