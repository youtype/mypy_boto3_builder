#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
cd ${ROOT_PATH}

VERSION=`python -m mypy_boto3_builder --version | head -1`
echo "Dockerizing mypy_boto3_builder ${VERSION}"
docker build . --tag mypy_boto3_builder
docker tag mypy_boto3_builder docker.pkg.github.com/vemel/mypy_boto3_builder/mypy_boto3_builder_stable:${VERSION}
docker login docker.pkg.github.com --username vemel -p ${GITHUB_TOKEN}
docker push docker.pkg.github.com/vemel/mypy_boto3_builder/mypy_boto3_builder_stable:${VERSION}
