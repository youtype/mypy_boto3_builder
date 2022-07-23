# mypy_boto3_builder

[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/youtype/mypy_boto3_builder)

[![PyPI - mypy-boto3-builder](https://img.shields.io/pypi/v/mypy-boto3-builder.svg?color=blue&label=mypy-boto3-builder)](https://pypi.org/project/mypy-boto3-builder)
[![PyPI - boto3-stubs](https://img.shields.io/pypi/v/boto3-stubs.svg?color=blue&label=boto3-stubs)](https://pypi.org/project/boto3-stubs)
[![PyPI - boto3](https://img.shields.io/pypi/v/boto3.svg?color=blue&label=boto3)](https://pypi.org/project/boto3)

[![Docs](https://img.shields.io/readthedocs/mypy-boto3-builder.svg?color=blue&label=boto3-stubs-docs)](https://youtype.github.io/boto3_stubs_docs/)
[![Docs](https://img.shields.io/readthedocs/mypy-boto3-builder.svg?color=blue&label=builder%20docs)](https://youtype.github.io/mypy_boto3_builder/)

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/boto3-stubs.svg?color=blue)](https://pypi.org/project/boto3-stubs)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/boto3-stubs?color=blue)](https://pypistats.org/packages/boto3-stubs)

![boto3.typed](https://github.com/youtype/mypy_boto3_builder/raw/main/logo.png)

Type annotations builder for [boto3-stubs](https://pypi.org/project/boto3-stubs/) project. Compatible with
[VSCode](https://code.visualstudio.com/),
[PyCharm](https://www.jetbrains.com/pycharm/),
[Emacs](https://www.gnu.org/software/emacs/),
[Sublime Text](https://www.sublimetext.com/),
[mypy](https://github.com/python/mypy),
[pyright](https://github.com/microsoft/pyright)
and other tools.

See how it helps to find and fix potential bugs:

![boto3-stubs demo](https://raw.githubusercontent.com/youtype/mypy_boto3_builder/main/demo.gif)

Do you want more? Check the [documentation](https://youtype.github.io/boto3_stubs_docs/) and use `boto3` like a pro!

- [mypy_boto3_builder](#mypy_boto3_builder)
  - [Using built libraries](#using-built-libraries)
    - [boto3](#boto3)
    - [aiobotocore](#aiobotocore)
    - [aioboto3](#aioboto3)
  - [How to build type annotations](#how-to-build-type-annotations)
    - [Locally](#locally)
    - [With Docker image](#with-docker-image)
  - [Development](#development)
  - [Versioning](#versioning)
  - [Latest changes](#latest-changes)
  - [Thank you](#thank-you)
    - [Toolset](#toolset)
    - [Contributors](#contributors)

## Using built libraries

### boto3

Check [boto3-stubs](https://pypi.org/project/boto3-stubs/) project for installation
and usage instructions.

If you use VSCode, add [AWS Boto3](https://marketplace.visualstudio.com/items?itemName=Boto3typed.boto3-ide)
extension to your VSCode and run `AWS boto3: Quick Start` command.

If not, just install `boto3-stubs` with `pip`:

```bash
python -m pip install 'boto3-stubs[essential]'

# Lite version does not provide session.client/resource overloads
# it is more RAM-friendly, but requires explicit type annotations
python -m pip install 'boto3-stubs-lite[essential]'

# do not forget to install mypy or pyright
```

That's it! You should already have code completion and type checking in your IDE.

### aiobotocore

Check [types-aiobotocore](https://pypi.org/project/types-aiobotocore/) project for installation
and usage instructions.

Or just install `types-aiobotocore` with `pip`:

```bash
python -m pip install 'types-aiobotocore[essential]'

# Lite version does not provide session.create_client overloads
# it is more RAM-friendly, but requires explicit type annotations
python -m pip install 'types-aiobotocore-lite[essential]'

# do not forget to install mypy or pyright
```

Ready to go! Enjoy code completion and type checking in your `aiobotocore` project.

### aioboto3

Check [types-aioboto3](https://pypi.org/project/types-aioboto3/) project for installation
and usage instructions.

Or just install `types-aioboto3` with `pip`:

```bash
python -m pip install 'types-aioboto3[essential]'

# Lite version does not provide session.client/resource overloads
# it is more RAM-friendly, but requires explicit type annotations
python -m pip install 'types-aioboto3-lite[essential]'

# do not forget to install mypy or pyright
```

Whoa! All `aioboto3` methods and attributes are now type-annotated and even code completion works.

## How to build type annotations

### Locally

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

### With Docker image

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

## Development

- Install Python 3.10+, ideally with [pyenv](https://github.com/pyenv/pyenv)
- Install [poetry](https://python-poetry.org/): `pip install poetry`
- Install dependencies: `poetry install`
- Use scripts for repo to check if everything works: `./scripts/build.sh`
- Run manual pre-commit: `./scripts/before_commit.sh`

## Versioning

`mypy_boto3_builder` version is not related to `boto3` version and follows
[PEP 440](https://www.python.org/dev/peps/pep-0440/).

## Latest changes

Full changelog can be found in [Releases](https://github.com/youtype/mypy_boto3_builder/releases).

## Thank you

### Toolset

- [black](https://github.com/psf/black) developers for an awesome formatting tool
- [Timothy Edmund Crosley](https://github.com/timothycrosley) for
  [isort](https://github.com/PyCQA/isort) and how flexible it is
- [mypy](https://github.com/python/mypy) developers for doing all dirty work for us
- [pyright](https://github.com/microsoft/pyright) team for the new era of typed Python

### Contributors

- [Allie Fitter](https://github.com/alliefitter), author of original
  [boto3-type-annotations](https://pypi.org/project/boto3-type-annotations/)
- [jbpratt](https://github.com/jbpratt)
- [Chris Hollinworth](https://github.com/chrishollinworth)
- [Yoan Blanc](https://github.com/greut)
- [Kostya Leschenko](https://github.com/kleschenko)
- [pyto86](https://github.com/pyto86pri)
- [Ashton Honnecke](https://github.com/ahonnecke)
- [Mike Carey](https://github.com/mike-carey)
- [Ole-Martin Bratteng](https://github.com/omBratteng)
- [Nikhil Benesch](https://github.com/benesch)
