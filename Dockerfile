FROM python:3.9.1-alpine3.12

RUN apk add --no-cache gcc libc-dev

RUN mkdir -p /builder/scripts
WORKDIR /builder

ADD ./mypy_boto3_builder ./mypy_boto3_builder
ADD ./LICENSE ./LICENSE
ADD ./pyproject.toml ./pyproject.toml
ADD ./setup.cfg ./setup.cfg
ADD ./setup.py ./setup.py
ADD ./README.md ./README.md
ADD ./scripts/docker.sh ./scripts/docker.sh

RUN pip install .

RUN adduser \
    --disabled-password \
    --home /output \
    builder

USER builder
WORKDIR /output

ENV BOTO3_VERSION ""
ENV BOTOCORE_VERSION ""

ENTRYPOINT ["/builder/scripts/docker.sh"]
