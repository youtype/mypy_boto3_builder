#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
cd ${ROOT_PATH}

if [[ "$GITHUB_ACTOR" == "" ]]; then
    echo "No GITHUB_ACTOR specified"
    exit 1
fi

if [[ "$GITHUB_TOKEN" == "" ]]; then
    echo "No GITHUB_TOKEN specified"
    exit 1
fi

if [[ "$VERSION" == "" ]]; then
    echo "No VERSION specified"
    exit 1
fi

echo "Bumping version to ${VERSION}"
echo '"Source of truth for version."' > mypy_boto3_builder/version.py
echo "__version__ = \"${VERSION}\"" >> mypy_boto3_builder/version.py

if [[ `git diff --stat | grep version` != "" ]]; then
    echo "There are changes: `git diff`"
    git config --global user.email "volshebnyi@gmail.com"
    git config --global user.name ${GITHUB_ACTOR}
    git add mypy_boto3_builder/version.py
    git commit -m "Bump version to ${VERSION}"
    git push https://${GITHUB_ACTOR}:${GITHUB_TOKEN}@github.com/vemel/mypy_boto3_builder.git --tags
    git push https://${GITHUB_ACTOR}:${GITHUB_TOKEN}@github.com/vemel/mypy_boto3_builder.git HEAD:master
fi
