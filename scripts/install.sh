#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
OUTPUT_PATH=${ROOT_PATH}/mypy_boto3_output
PACKAGES=${OUTPUT_PATH}/mypy_boto3_$1_package
if [[ "$1" == "" ]]; then
    PACKAGES=${OUTPUT_PATH}/*_package
fi

if [[ "$1" == "master" ]]; then
    echo Installing boto3-stubs package
    cd ${OUTPUT_PATH}/boto3_stubs_package
    uv run pip install .
    cd -

    exit
fi

if [[ "$1" == "full" ]]; then
    echo Installing boto3-stubs-full package
    cd ${OUTPUT_PATH}/boto3_stubs_full_package
    uv run pip install .
    cd -

    exit
fi

for package in $PACKAGES
do
    echo Installing $(basename ${package})
    cd ${package}
    uv run pip install . -v
    cd -
done
