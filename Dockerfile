FROM python:3.10.0-alpine3.14

RUN apk add --no-cache --virtual .build-deps \
    gcc libc-dev \
    && python -m pip install --no-cache-dir regex==2021.11.2 \
    && apk del --no-cache .build-deps

RUN mkdir -p /builder/scripts
WORKDIR /builder

ADD ./mypy_boto3_builder ./mypy_boto3_builder
ADD ./LICENSE ./LICENSE
ADD ./pyproject.toml ./pyproject.toml
ADD ./setup.cfg ./setup.cfg
ADD ./README.md ./README.md
ADD ./scripts/docker.sh ./scripts/docker.sh

RUN python -m pip install --no-cache-dir .

RUN adduser \
    --disabled-password \
    --home /output \
    builder

USER builder
WORKDIR /output

ENV BOTO3_VERSION ""
ENV BOTOCORE_VERSION ""

ENTRYPOINT ["/builder/scripts/docker.sh"]
