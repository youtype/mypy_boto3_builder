# Mypy Boto3 Builder

[![PyPI - mypy-boto3-builder](https://img.shields.io/pypi/v/mypy-boto3-builder.svg?color=blue&label=mypy-boto3-builder)](https://pypi.org/project/mypy-boto3-builder)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/boto3-stubs.svg?color=blue)](https://pypi.org/project/boto3-stubs)
[![Docs](https://img.shields.io/readthedocs/mypy-boto3-builder.svg?color=blue&label=builder%20docs)](https://youtype.github.io/mypy_boto3_builder/)

[![PyPI - boto3-stubs](https://img.shields.io/pypi/v/boto3-stubs.svg?color=blue&label=boto3-stubs)](https://pypi.org/project/boto3-stubs)
[![PyPI - boto3](https://img.shields.io/pypi/v/boto3.svg?color=blue&label=boto3)](https://pypi.org/project/boto3)
[![Docs](https://img.shields.io/readthedocs/boto3-stubs.svg?color=blue&label=boto3-stubs%20docs)](https://youtype.github.io/boto3_stubs_docs/)
[![PyPI - Downloads](https://static.pepy.tech/badge/boto3-stubs)](https://pepy.tech/project/boto3-stubs)
[![PyPI - Monthly Downloads](https://img.shields.io/pypi/dm/boto3-stubs?color=blue)](https://pypistats.org/packages/boto3-stubs)

[![PyPI - types-aiobotocore](https://img.shields.io/pypi/v/types-aiobotocore.svg?color=blue&label=types-aiobotocore)](https://pypi.org/project/types-aiobotocore)
[![PyPI - aiobotocore](https://img.shields.io/pypi/v/aiobotocore.svg?color=blue&label=aiobotocore)](https://pypi.org/project/aiobotocore)
[![Docs](https://img.shields.io/readthedocs/types-aiobotocore.svg?color=blue&label=types-aiobotocore%20docs)](https://youtype.github.io/types_aiobotocore_docs/)
[![PyPI - Downloads](https://static.pepy.tech/badge/types-aiobotocore)](https://pepy.tech/project/types-aiobotocore)
[![PyPI - Monthly Downloads](https://img.shields.io/pypi/dm/types-aiobotocore?color=blue)](https://pypistats.org/packages/types-aiobotocore)

[![PyPI - types-aioboto3](https://img.shields.io/pypi/v/types-aioboto3.svg?color=blue&label=types-aioboto3)](https://pypi.org/project/types-aioboto3)
[![PyPI - aioboto3](https://img.shields.io/pypi/v/aioboto3.svg?color=blue&label=aioboto3)](https://pypi.org/project/aioboto3)
[![Docs](https://img.shields.io/readthedocs/types-aioboto3.svg?color=blue&label=types-aioboto3%20docs)](https://youtype.github.io/types_aioboto3_docs/)
[![PyPI - Downloads](https://static.pepy.tech/badge/types-aioboto3)](https://pepy.tech/project/types-aioboto3)
[![PyPI - Monthly Downloads](https://img.shields.io/pypi/dm/types-aioboto3?color=blue)](https://pypistats.org/packages/types-aioboto3)

![boto3.typed](https://github.com/youtype/mypy_boto3_builder/raw/main/logo.png)

Type annotations generator for [types-boto3](https://pypi.org/project/types-boto3/),
[boto3-stubs](https://pypi.org/project/boto3-stubs/),
[types-aiobotocore](https://pypi.org/project/types-aiobotocore/),
and [types-aioboto3](https://pypi.org/project/types-aioboto3/) projects.
Compatible with
[VSCode](https://code.visualstudio.com/),
[PyCharm](https://www.jetbrains.com/pycharm/),
[Emacs](https://www.gnu.org/software/emacs/),
[Sublime Text](https://www.sublimetext.com/),
[mypy](https://github.com/python/mypy),
[pyright](https://github.com/microsoft/pyright)
and other tools.

See how it helps to find and fix potential bugs:

![types-boto3 demo](https://raw.githubusercontent.com/youtype/mypy_boto3_builder/main/demo.gif)

Do you want more? Check the [documentation](https://youtype.github.io/boto3_stubs_docs/) and use `boto3` like a pro!

- [Mypy Boto3 Builder](#mypy-boto3-builder)
  - [Quickstart](#quickstart)
  - [Type annotations documentation](#type-annotations-documentation)
  - [Builder documentation](#builder-documentation)
  - [Versioning](#versioning)
  - [Latest changes](#latest-changes)

## Quickstart

- Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Run `uvx mypy_boto3_builder`
- Answer some questions, get your custom package
- Install a generated package

## Type annotations documentation

- If you use `boto3` or `botocore`, follow [types-boto3 documentation](https://youtype.github.io/types_boto3_docs/)
- For `aiobotocore` follow [types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/)
- For `aioboto3` follow [types-aioboto3 documentation](https://youtype.github.io/types_aioboto3_docs/)

## Builder documentation

- [How to use pre-built libraries](./docsmd/pre_build.md)
- [How builder works](./docsmd/how_it_works.md)
- [How to build type annotations](./docsmd/how_to_build.md)
- [Development](./docsmd/development.md)
- [Contributors](./docsmd/thank_you.md)

## Versioning

`mypy_boto3_builder` version is not related to `boto3` version and follows
[PEP 440](https://www.python.org/dev/peps/pep-0440/).

## Latest changes

Full changelog can be found in [Releases](https://github.com/youtype/mypy_boto3_builder/releases).
