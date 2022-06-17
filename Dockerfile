FROM python:3.10.5-alpine3.16

RUN mkdir -p /home/builder/scripts
RUN mkdir -p /output
WORKDIR /builder

ADD ./mypy_boto3_builder ./mypy_boto3_builder
ADD ./LICENSE ./LICENSE
ADD ./pyproject.toml ./pyproject.toml
ADD ./setup.cfg ./setup.cfg
ADD ./README.md ./README.md

RUN adduser \
    --disabled-password \
    --home /home/builder \
    builder

USER builder

ENV PATH "$PATH:/home/builder/.local/bin"
RUN python -m pip install -U pip
RUN python -m pip install --no-cache-dir .

ADD ./scripts/docker.sh ./scripts/docker.sh

WORKDIR /output

ENV BOTO3_VERSION ""
ENV BOTOCORE_VERSION ""

ENTRYPOINT ["/builder/scripts/docker.sh"]
