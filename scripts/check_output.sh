#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
cd ${ROOT_PATH}
START="$1"

PACKAGES=`find mypy_boto3_output -name 'type_defs.pyi' | sort`

for f in $PACKAGES; do
    DIRNAME="$(dirname "$f")"
    if [[ ! "$f" == *"$START"* ]]; then
        continue
    fi
    echo "Checking $DIRNAME"
    # pylint $DIRNAME
    mypy $DIRNAME
done
