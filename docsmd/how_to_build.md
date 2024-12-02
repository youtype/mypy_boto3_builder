# How to build type annotations

- [How to build type annotations](#how-to-build-type-annotations)
  - [With your personal assistant (recommended)](#with-your-personal-assistant-recommended)
  - [With CLI](#with-cli)
  - [With Docker image](#with-docker-image)


## With your personal assistant (recommended)

- Install [uv](https://docs.astral.sh/uv/getting-started/installation/)

```bash
# run builder and chat with him :)
uvx mypy-boto3-builder

# set library version explicitly for better results
uvx --with 'boto3==1.35.71' mypy-boto3-builder
```

## With CLI

```bash
# Install preferred version of `boto3`
python -m pip install boto3==1.35.71 botocore==1.35.71

# Install `mypy-boto3-builder`
python -m pip install mypy-boto3-builder

# Build all packages in typings directory
python -m mypy_boto3_builder ./typings --product types-boto3 types-boto3-services --output-type wheel

# Or specify required services explicitly
python -m mypy_boto3_builder ./typings --product types-boto3 types-boto3-services --output-type wheel -s ec2 s3

# Install custom `types-boto3` packages
python -m pip install ./typings/*.whl
```

## With Docker image

- Install [Docker](https://docs.docker.com/install/)
- Pull latest `mypy_boto3_builder` version and tag it

```bash
docker pull docker.pkg.github.com/youtype/mypy_boto3_builder/mypy_boto3_builder_stable:latest
docker tag docker.pkg.github.com/youtype/mypy_boto3_builder/mypy_boto3_builder_stable:latest mypy_boto3_builder
```

- Generate stubs in `output` directory

```bash
mkdir output

# generate stubs for all services
docker run -v `pwd`/output:/output -ti mypy_boto3_builder_stable

# generate stubs for s3 service
docker run -v `pwd`/output:/output -ti mypy_boto3_builder_stable -s s3

# generate stubs for a specific boto3 version
docker run -e BOTO3_VERSION=1.35.71 BOTOCORE_VERSION=1.35.71 -v `pwd`/output:/output -ti mypy_boto3_builder_stable
```

- Install packages from `output` directory as described above
