#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
OUTPUT_PATH=${ROOT_PATH}/mypy_boto3_output
PACKAGES=${OUTPUT_PATH}/types_aiobotocore_$1_package
if [[ "$1" == "" ]]; then
    PACKAGES=`find ${OUTPUT_PATH} -name 'types_aiobotocore_*_package'`
fi

echo "Packages: " $PACKAGES

for package in $PACKAGES
do
    echo Publishing $(basename ${package})
    cd ${package}
    rm -rf build *.egg-info dist/* > /dev/null
    python setup.py build sdist bdist_wheel 1>/dev/null 2>/dev/null
    twine upload --non-interactive dist/* > /dev/null || true
    rm -rf build *.egg-info dist/* > /dev/null
    cd -
done

echo Publishing types-aiobotocore package
cd ${OUTPUT_PATH}/types_aiobotocore_package
rm -rf build *.egg-info dist/* > /dev/null
python setup.py build sdist bdist_wheel 1>/dev/null 2>/dev/null
twine upload --non-interactive dist/* > /dev/null || true
rm -rf build *.egg-info dist/* > /dev/null
cd -
