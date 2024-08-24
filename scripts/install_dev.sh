#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))

uv sync --dev
uv pip install -U aioboto3
uv pip install -r ${ROOT_PATH}/requirements.mkdocs.txt
