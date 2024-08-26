FROM python:3.12.5-alpine3.20

RUN mkdir -p /home/builder/scripts
RUN mkdir -p /output
WORKDIR /home/builder

COPY ./mypy_boto3_builder ./mypy_boto3_builder
COPY ./LICENSE ./LICENSE
COPY ./pyproject.toml ./pyproject.toml
COPY ./README.md ./README.md

RUN adduser \
    --disabled-password \
    --home /home/builder \
    builder

USER builder

ENV PATH "$PATH:/home/builder/.local/bin"
RUN python -m pip install --no-cache-dir .

COPY ./scripts/docker.sh ./scripts/docker.sh

WORKDIR /output

ENV BOTO3_VERSION ""
ENV BOTOCORE_VERSION ""

ENTRYPOINT ["/builder/scripts/docker.sh"]
