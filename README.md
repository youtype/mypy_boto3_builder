# Mypy Boto3 Builder

[![PyPI - mypy-boto3-builder](https://img.shields.io/pypi/v/mypy-boto3-builder.svg?color=blue&label=mypy-boto3-builder)](https://pypi.org/project/mypy-boto3-builder)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/types-boto3.svg?color=blue)](https://pypi.org/project/types-boto3)
[![Docs](https://img.shields.io/readthedocs/mypy-boto3-builder.svg?color=blue&label=builder%20docs)](https://youtype.github.io/mypy_boto3_builder/)

[![PyPI - types-boto3](https://img.shields.io/pypi/v/types-boto3.svg?color=blue&label=types-boto3)](https://pypi.org/project/types-boto3)
[![PyPI - boto3](https://img.shields.io/pypi/v/boto3.svg?color=blue&label=boto3)](https://pypi.org/project/boto3)
[![Docs](https://img.shields.io/readthedocs/types-boto3.svg?color=blue&label=types-boto3%20docs)](https://youtype.github.io/types_boto3_docs/)
[![PyPI - Downloads](https://static.pepy.tech/badge/types-boto3)](https://pepy.tech/project/types-boto3)
[![PyPI - Monthly Downloads](https://img.shields.io/pypi/dm/types-boto3?color=blue)](https://pypistats.org/packages/types-boto3)

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
[types-aiobotocore](https://pypi.org/project/types-aiobotocore/),
and [types-aioboto3](https://pypi.org/project/types-aioboto3/) projects.

The `boto3-stubs` package family is deprecated in favor of `types-boto3`. Every
`boto3-stubs` package is 100% equivalent and fully compatible with its `types-boto3`
counterpart, so existing projects can switch package names without changing imports or type
annotations.

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

Do you want more? Check the [documentation](https://youtype.github.io/types_boto3_docs/) and use `boto3` like a pro!

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
[Python Packaging version specifiers](https://packaging.python.org/en/latest/specifications/version-specifiers/).

## Latest changes

Full changelog can be found in [Releases](https://github.com/youtype/mypy_boto3_builder/releases).
