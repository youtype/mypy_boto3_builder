#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
cd ${ROOT_PATH}

python -m mypy_boto3_builder ../boto3_stubs_docs/docsmd --product boto3-docs $@
