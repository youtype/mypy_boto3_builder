# How to build type annotations

## Locally

```bash
# Install preferred version of `boto3`
python -m pip install boto3==1.16.25 botocore==1.19.25

# Install `mypy-boto3-builder`
python -m pip install mypy-boto3-builder

# Build all packages in mypy_boto3_output directory
python -m mypy_boto3_builder mypy_boto3_output

# Or specify required services explicitly
python -m mypy_boto3_builder mypy_boto3_output -s ec2 s3

# Install custom `boto3-stubs` packages
cd mypy_boto3_output
python -m pip install -e ./mypy_boto3_ec2_package
python -m pip install -e ./mypy_boto3_s3_package
python -m pip install -e ./boto3_stubs_package
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
docker run -e BOTO3_VERSION=1.16.25 BOTOCORE_VERSION=1.19.25 -v `pwd`/output:/output -ti mypy_boto3_builder_stable
```

- Install packages from `output` directory as described above
