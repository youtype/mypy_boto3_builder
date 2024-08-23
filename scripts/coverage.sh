#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))

coverage run mypy_boto3_builder/__main__.py mypy_boto3_output -s ec2 rds s3 lambda sqs cloudformation dynamodb --product boto3 boto3-services aioboto3 aiobotocore aiobotocore-services boto3-docs aioboto3-docs aiobotocore-docs
coverage xml
coverage html
python -m http.server --directory htmlcov 9000
