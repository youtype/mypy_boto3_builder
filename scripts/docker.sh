#!/usr/bin/env sh
set -e

if [[ "$BOTO3_VERSION" != "" ]]; then
    python -m pip install boto3==${BOTO3_VERSION}
fi

if [[ "$BOTOCORE_VERSION" != "" ]]; then
    python -m pip install botocore==${BOTOCORE_VERSION}
fi

python -m mypy_boto3_builder /output $@
