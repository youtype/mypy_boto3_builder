#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
cd ${ROOT_PATH}

PACKAGES=`find mypy_boto3_output -name 'type_defs.pyi' | grep "${1}" | sort`

for f in $PACKAGES; do
    DIRNAME="$(dirname "$f")"
    echo "Checking $DIRNAME"
    flake8 $DIRNAME
    # mypy $DIRNAME
    [ -f $DIRNAME/waiters.py ] && pyright $DIRNAME/waiter.py
    [ -f $DIRNAME/paginator.py ] && pyright $DIRNAME/paginator.py
    [ -f $DIRNAME/service_resource.py ] && pyright $DIRNAME/service_resource.py
    [ -f $DIRNAME/literals.py ] && pyright $DIRNAME/literals.py
    [ -f $DIRNAME/type_defs.py ] && pyright $DIRNAME/type_defs.py
done
