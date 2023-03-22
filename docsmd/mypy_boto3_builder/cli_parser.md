# Cli Parser

[Mypy_boto3_builder Index](../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](./index.md#mypy-boto3-builder) /
Cli Parser

> Auto-generated documentation for [mypy_boto3_builder.cli_parser](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/cli_parser.py) module.

## Namespace

[Show source in cli_parser.py:29](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/cli_parser.py#L29)

CLI arguments namespace.

#### Signature

```python
class Namespace:
    ...
```



## get_absolute_path

[Show source in cli_parser.py:15](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/cli_parser.py#L15)

Get absolute path from a string.

#### Arguments

- `path` - String containing path.

#### Returns

Absolute path.

#### Signature

```python
def get_absolute_path(path: str) -> Path:
    ...
```



## parse_args

[Show source in cli_parser.py:46](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/cli_parser.py#L46)

Parse CLI arguments.

#### Returns

Argument parser.

#### Signature

```python
def parse_args(args: Sequence[str]) -> Namespace:
    ...
```

#### See also

- [Namespace](#namespace)
