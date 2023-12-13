#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))

poetry install -n
poetry run pip install -U aioboto3 boto3-stubs types-aiobotocore types-aioboto3
poetry run pip install -r ${ROOT_PATH}/requirements.mkdocs.txt
poetry install -n
