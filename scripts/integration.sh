#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))

EXAMPLES=${ROOT_PATH}/examples/*_example.py

${ROOT_PATH}/scripts/install.sh master

for EXAMPLE in $EXAMPLES
do
    FILE_NAME=$(basename ${EXAMPLE})
    SERVICE_NAME=`echo ${FILE_NAME} | sed 's/_example\.py//'`
    DIR_NAME=$(dirname ${EXAMPLE})
    EXPECTED=${DIR_NAME}/e2e_snapshots/${FILE_NAME}.out
    OUTPUT=${DIR_NAME}/e2e_snapshots/current.out

    ${ROOT_PATH}/scripts/install.sh ${SERVICE_NAME}
    mypy_boto3
    echo Running mypy for ${FILE_NAME}
    if [[ ! -f ${EXPECTED} ]]; then
        mypy ${EXAMPLE} | grep -v ' note: ' > ${EXPECTED} || true
        echo "Created ${EXPECTED}"
        continue
    fi
    mypy ${EXAMPLE} | grep -v ' note: ' > ${OUTPUT} || true
    DIFF=`diff ${OUTPUT} ${EXPECTED}` || true
    rm ${OUTPUT}

    if [[ ${DIFF} != "" ]]; then
        echo Output for "mypy ${FILE_NAME}" is different:
        echo $DIFF
        echo
        echo "If it is expected, run: rm ${EXPECTED}"
        exit 1
    fi
done

echo "All tests passed"
