#!/usr/bin/env sh
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
cd ${ROOT_PATH}

if [[ "$BOTO3_VERSION" != "" ]]; then
    pip install --user boto3==${BOTO3_VERSION}
fi

if [[ "$BOTOCORE_VERSION" != "" ]]; then
    pip install --user botocore==${BOTOCORE_VERSION}
fi

mypy_boto3_builder . $@
