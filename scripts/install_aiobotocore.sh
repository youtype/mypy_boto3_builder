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
    cd ${OUTPUT_PATH}/types_aiobotocore_package
    poetry run pip install .
    cd -

    echo Installing types-aioboto3 package
    cd ${OUTPUT_PATH}/types_aioboto3_package
    poetry run pip install .
    cd -

    exit
fi

for package in $PACKAGES
do
    echo Installing $(basename ${package})
    cd ${package}
    poetry run pip install . -v
    cd -
done
