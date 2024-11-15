#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
cd ${ROOT_PATH}

python -m mypy_boto3_builder ../boto3_stubs_docs/docsmd --product boto3-docs $@

cd ../boto3_stubs_docs/
uvx --with mkdocs-material mkdocs build
cd -