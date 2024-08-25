#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))

cd $ROOT_PATH/types_boto3
rm -rf dist/* && python setup.py build sdist bdist_wheel
uvx twine upload dist/* || true

cd $ROOT_PATH/types_botocore
rm -rf dist/* && python setup.py build sdist bdist_wheel
uvx twine upload dist/* || true
