#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
cd ${ROOT_PATH}
OUTPUT_PATH=${ROOT_PATH}/mypy_boto3_output

scripts/build.sh --product boto3 > /dev/null

echo Installing boto3-stubs-lite package
python -m pip install ${OUTPUT_PATH}/boto3_stubs_lite_package

echo Installing botocore-stubs package
python -m pip install ${OUTPUT_PATH}/botocore_stubs_package

echo Installing types-s3transfer package
python -m pip install ${ROOT_PATH}/types_s3transfer

echo "Checking botocore stubs..."
python -m mypy.stubtest botocore \
    | awk 'BEGIN{RS=ORS="\n\n"}{if ($0 !~ /cannot reconcile @property on stub/) print $0;}' \
    | awk 'BEGIN{RS=ORS="\n\n"}{if ($0 !~ /OrderedDict/) print $0;}' \
    | awk 'BEGIN{RS=ORS="\n\n"}{if ($0 !~ /error: Skipping analyzing "awscrt.auth"/) print $0;}' \
    | awk 'BEGIN{RS=ORS="\n\n"}{if ($0 !~ /error: botocore.__main__ failed to import/) print $0;}' \
    | awk 'BEGIN{RS=ORS="\n\n"}{if ($0 !~ /error: botocore.version failed to import/) print $0;}'

echo "Checking boto3 stubs..."
python -m mypy.stubtest boto3 \
    | awk 'BEGIN{RS=ORS="\n\n"}{if ($0 !~ /error: boto3.resources.base.ServiceResource.meta variable differs from runtime type None/) print $0;}' \
    | awk 'BEGIN{RS=ORS="\n\n"}{if ($0 !~ /error: boto3.setup_default_session is inconsistent/) print $0;}' \
    | awk 'BEGIN{RS=ORS="\n\n"}{if ($0 !~ /error: boto3.__main__ failed to import/) print $0;}' \
    | awk 'BEGIN{RS=ORS="\n\n"}{if ($0 !~ /error: boto3.version failed to import/) print $0;}'

echo "Checking s3transfer stubs..."
python -m mypy.stubtest s3transfer \
    | awk 'BEGIN{RS=ORS="\n\n"}{if ($0 !~ /error: s3transfer.crt failed to import: No module named/) print $0;}' \
    | awk 'BEGIN{RS=ORS="\n\n"}{if ($0 !~ /error: s3transfer.compat.BaseManager.shutdown is not present at runtime/) print $0;}' \
    | awk 'BEGIN{RS=ORS="\n\n"}{if ($0 !~ /error: Skipping analyzing "awscrt.auth"/) print $0;}' \
    | awk 'BEGIN{RS=ORS="\n\n"}{if ($0 !~ /error: Skipping analyzing "awscrt.http"/) print $0;}' \
    | awk 'BEGIN{RS=ORS="\n\n"}{if ($0 !~ /error: Skipping analyzing "awscrt.s3"/) print $0;}' \
    | awk 'BEGIN{RS=ORS="\n\n"}{if ($0 !~ /error: s3transfer.processpool.BaseManager.shutdown is not present at runtime/) print $0;}' \
    | awk 'BEGIN{RS=ORS="\n\n"}{if ($0 !~ /error: s3transfer.processpool.TransferMonitorManager.TransferMonitor is not present in stub/) print $0;}'
