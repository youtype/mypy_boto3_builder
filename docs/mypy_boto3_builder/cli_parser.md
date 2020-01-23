# Cli Parser

> Auto-generated documentation for [mypy_boto3_builder.cli_parser](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/cli_parser.py) module.

CLI parser.

- [mypy-boto3-builder](../README.md#mypy_boto3_builder) / [Modules](../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / Cli Parser
    - [get_absolute_path](#get_absolute_path)
    - [get_cli_parser](#get_cli_parser)
    - [get_service_name](#get_service_name)

## get_absolute_path

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/cli_parser.py#L11)

```python
def get_absolute_path(path: str) -> Path:
```

Get absolute path from a string.

#### Arguments

- `path` - String containing path.

#### Returns

Absolute path.

## get_cli_parser

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/cli_parser.py#L40)

```python
def get_cli_parser() -> argparse.ArgumentParser:
```

Main CLI parser for builder.

#### Returns

Argument parser.

## get_service_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/cli_parser.py#L24)

```python
def get_service_name(name: str) -> ServiceName:
```

Convert boto3 service name to ServiceName.

#### Arguments

- `name` - Service name.

#### Raises

- `argparse.ArgumentTypeError` - If service not found.

#### See also

- [ServiceName](service_name.md#servicename)
