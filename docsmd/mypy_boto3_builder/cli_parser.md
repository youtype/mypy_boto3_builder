# Cli Parser

[Mypy_boto3_builder Index](../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](./index.md#mypy-boto3-builder) / Cli Parser

> Auto-generated documentation for [mypy_boto3_builder.cli_parser](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/cli_parser.py) module.

## CLINamespace

[Show source in cli_parser.py:31](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/cli_parser.py#L31)

CLI arguments namespace.

#### Signature

```python
class CLINamespace: ...
```



## get_absolute_path

[Show source in cli_parser.py:17](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/cli_parser.py#L17)

Get absolute path from a string.

#### Arguments

- `path` - String containing path.

#### Returns

Absolute path.

#### Signature

```python
def get_absolute_path(path: str) -> Path: ...
```



## parse_args

[Show source in cli_parser.py:48](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/cli_parser.py#L48)

Parse CLI arguments.

#### Returns

Argument parser.

#### Signature

```python
def parse_args(args: Sequence[str]) -> CLINamespace: ...
```

#### See also

- [CLINamespace](#clinamespace)
