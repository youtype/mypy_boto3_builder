#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
OUTPUT_PATH=${ROOT_PATH}/mypy_boto3_output
PACKAGES=${OUTPUT_PATH}/mypy_boto3_$1_package
if [[ "$1" == "" ]]; then
    PACKAGES=${OUTPUT_PATH}/mypy_boto3_*
fi

if [[ `pip freeze | grep black` == "" ]]; then
    echo "black not found, installing it now"
    pip install --user black==19.10b0
fi

for package in $PACKAGES
do
    echo Publishing $(basename ${package})
    cd ${package}
    rm -rf build *.egg-info dist/* > /dev/null
    python setup.py build sdist 1>/dev/null 2>/dev/null
    twine upload --non-interactive dist/* > /dev/null || true
    rm -rf build *.egg-info dist/* > /dev/null
done

echo Publishing master package
cd ${OUTPUT_PATH}/master_package
rm -rf build *.egg-info dist/* > /dev/null
python setup.py build sdist 1>/dev/null 2>/dev/null
twine upload --non-interactive dist/* > /dev/null || true
rm -rf build *.egg-info dist/* > /dev/null

echo Publishing boto3-stubs package
cd ${OUTPUT_PATH}/boto3_stubs_package
rm -rf build *.egg-info dist/* > /dev/null
python setup.py build sdist 1>/dev/null 2>/dev/null
twine upload --non-interactive dist/* > /dev/null || true
rm -rf build *.egg-info dist/* > /dev/null
