# Cli Parser

[Mypy_boto3_builder Index](../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](./index.md#mypy-boto3-builder) / Cli Parser

> Auto-generated documentation for [mypy_boto3_builder.cli_parser](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/cli_parser.py) module.

## CLINamespace

[Show source in cli_parser.py:71](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/cli_parser.py#L71)

CLI arguments namespace.

#### Signature

```python
class CLINamespace: ...
```



## EnumListAction

[Show source in cli_parser.py:32](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/cli_parser.py#L32)

Argparse action for handling Enums.

#### Signature

```python
class EnumListAction(argparse.Action):
    def __init__(self, **kwargs: Any) -> None: ...
```

### EnumListAction().__call__

[Show source in cli_parser.py:51](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/cli_parser.py#L51)

Convert value back into an Enum.

#### Signature

```python
def __call__(
    self,
    parser: argparse.ArgumentParser,
    namespace: argparse.Namespace,
    value: str | Sequence[Any] | None,
    _option_string: str | None = None,
) -> None: ...
```



## get_absolute_path

[Show source in cli_parser.py:19](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/cli_parser.py#L19)

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

[Show source in cli_parser.py:88](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/cli_parser.py#L88)

Parse CLI arguments.

#### Returns

Argument parser.

#### Signature

```python
def parse_args(args: Sequence[str]) -> CLINamespace: ...
```

#### See also

- [CLINamespace](#clinamespace)
