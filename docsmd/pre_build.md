# How to use pre-built libraries

## boto3 and botocore

Check [types-boto3](https://pypi.org/project/types-boto3/) project for installation
and usage instructions.

If you use VSCode, add [AWS Boto3](https://marketplace.visualstudio.com/items?itemName=Boto3typed.boto3-ide)
extension to your VSCode and run `AWS boto3: Quick Start` command.

If not, just install `types-boto3` with `pip`:

```bash
python -m pip install 'types-boto3[essential]'

# Lite version does not provide session.client/resource overloads
# it is more RAM-friendly, but requires explicit type annotations
python -m pip install 'types-boto3-lite[essential]'

# do not forget to install mypy or pyright
```

That's it! You should already have code completion and type checking in your IDE.

Check [types-boto3 documentation](https://youtype.github.io/types_boto3_docs/) for more details.

## aiobotocore

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

Check [types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/) for more details.

## aioboto3

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

Whoa! All `aioboto3` methods and attributes are now type annotated and even code completion works.

Check [types-aioboto3 documentation](https://youtype.github.io/types_aioboto3_docs/) for more details.
