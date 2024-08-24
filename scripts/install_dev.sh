#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))

uv sync --dev
uv run pip install -U aioboto3 boto3-stubs types-aiobotocore types-aioboto3
uv run pip install -r ${ROOT_PATH}/requirements.mkdocs.txt
uv sync --dev
