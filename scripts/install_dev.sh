#!/usr/bin/env bash
set -e

poetry install -n
poetry run pip install -U --no-dependencies aiobotocore aioboto3 types-aiobotocore types-aioboto3
