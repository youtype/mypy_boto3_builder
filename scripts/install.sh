#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
OUTPUT_PATH=${ROOT_PATH}/mypy_boto3_output
PACKAGES=${OUTPUT_PATH}/mypy_boto3_$1_package
if [[ "$1" == "" ]]; then
    PACKAGES=${OUTPUT_PATH}/*_package
fi

if [[ "$1" == "main" ]]; then
    echo Installing boto3-stubs package
    uv pip install ${OUTPUT_PATH}/boto3_stubs_package
    exit
fi

if [[ "$1" == "full" ]]; then
    echo Installing boto3-stubs-full package
    uv pip install ${OUTPUT_PATH}/boto3_stubs_full_package
    exit
fi

for package in $PACKAGES
do
    echo Installing $(basename ${package})
    uv pip install ${package}
done
