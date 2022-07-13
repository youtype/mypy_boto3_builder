#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))


cd $ROOT_PATH/types_s3transfer

rm -rf dist build *.egg-info || true

python setup.py build sdist bdist_wheel
python -m twine upload --non-interactive dist/*

cd -
