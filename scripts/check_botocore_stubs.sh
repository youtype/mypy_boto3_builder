#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
cd ${ROOT_PATH}

scripts/build.sh --skip-service > /dev/null
scripts/install.sh master > /dev/null


cd mypy_boto3_output/botocore_stubs_package
# rm -rf .mypy_cache
python -m mypy.stubtest botocore \
    | awk 'BEGIN{RS=ORS="\n\n"}{if ($0 !~ /cannot reconcile @property on stub/) print$0;}' \
    | awk 'BEGIN{RS=ORS="\n\n"}{if ($0 !~ /OrderedDict/) print$0;}' \
    | awk 'BEGIN{RS=ORS="\n\n"}{if ($0 !~ /error: botocore.__main__ failed to import/) print$0;}' \
    | awk 'BEGIN{RS=ORS="\n\n"}{if ($0 !~ /error: botocore.version failed to import/) print$0;}'
cd ../..
