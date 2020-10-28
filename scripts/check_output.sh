#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
cd ${ROOT_PATH}

PACKAGES=`find mypy_boto3_output -name 'type_defs.pyi' | grep "${1}" | sort`

for f in $PACKAGES; do
    DIRNAME="$(dirname "$f")"
    echo "Checking $DIRNAME"
    pylint $DIRNAME
    mypy $DIRNAME
done
