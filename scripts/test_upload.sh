#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))

mypy_boto3 --clean || true
pipenv clean
${ROOT_PATH}/scripts/build.sh -s sqs secretsmanager -b 1.11.0.10

OUTPUT_PATH=${ROOT_PATH}/mypy_boto3_output


cd ${OUTPUT_PATH}/master_package
rm -rf build *.egg-info dist/*
python setup.py build sdist
twine upload --repository-url http://localhost:8080/ --username user --password pass --non-interactive dist/*
cd -

cd ${OUTPUT_PATH}/boto3_stubs_package
rm -rf build *.egg-info dist/*
python setup.py build sdist
twine upload --repository-url http://localhost:8080/ --username user --password pass --non-interactive dist/*
cd -

cd ${OUTPUT_PATH}/mypy_boto3_sqs_package
rm -rf build *.egg-info dist/*
python setup.py build sdist
twine upload --repository-url http://localhost:8080/ --username user --password pass --non-interactive dist/*
cd -

cd ${OUTPUT_PATH}/mypy_boto3_secretsmanager_package
rm -rf build *.egg-info dist/*
python setup.py build sdist
twine upload --repository-url http://localhost:8080/ --username user --password pass --non-interactive dist/*
cd -

pip install --extra-index-url http://localhost:8080/ 'mypy-boto3==1.11.0.10' -v
pip install --extra-index-url http://localhost:8080/ 'boto3-stubs[sqs,secretsmanager]==1.11.0.10' -v