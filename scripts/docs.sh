#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
cd $ROOT_PATH

handsdown --external `git config --get remote.origin.url` -n mypy-boto3-builder mypy_boto3_builder --exclude '*/build/*' --cleanup --panic --branch master
