#!/usr/bin/env bash
set -e

poetry install -n
poetry run pip install -U aioboto3 boto3-stubs types-aiobotocore types-aioboto3
poetry install -n
