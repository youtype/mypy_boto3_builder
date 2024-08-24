#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
OUTPUT_PATH=${ROOT_PATH}/mypy_boto3_output
PACKAGES=${OUTPUT_PATH}/types_aiobotocore_$1_package
if [[ "$1" == "" ]]; then
    PACKAGES=${OUTPUT_PATH}/*_package
fi

if [[ "$1" == "master" ]]; then
    echo Installing types-aiobotocore package
    uv pip install ${OUTPUT_PATH}/types_aiobotocore_package

    echo Installing types-aioboto3 package
    uv pip install ${OUTPUT_PATH}/types_aioboto3_package

    exit
fi

if [[ "$1" == "full" ]]; then
    echo Installing types-aiobotocore-full package
    uv pip install ${OUTPUT_PATH}/types_aiobotocore_full_package

    exit
fi

for package in $PACKAGES
do
    echo Installing $(basename ${package})
    uv pip install ${package}
done
