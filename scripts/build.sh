#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
cd ${ROOT_PATH}

poetry run mypy_boto3_builder mypy_boto3_output $@
