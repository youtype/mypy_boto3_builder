# Main

> Auto-generated documentation for [mypy_boto3_builder.main](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/main.py) module.

Main entrypoint for builder.

- [mypy-boto3-builder](../README.md#mypy_boto3_builder) / [Modules](../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / Main
    - [generate_docs](#generate_docs)
    - [generate_stubs](#generate_stubs)
    - [get_available_service_names](#get_available_service_names)
    - [main](#main)

## generate_docs

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/main.py#L176)

```python
def generate_docs(
    args: Namespace,
    service_names: Sequence[ServiceName],
    available_service_names: Iterable[ServiceName],
    session: Session,
) -> None:
```

Generate service and master docs.

#### Arguments

- `args` - Config namespace
- `service_names` - Enabled service names
- `available_service_names` - All service names
- `session` - Botocore session

#### See also

- [Namespace](cli_parser.md#namespace)

## generate_stubs

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/main.py#L120)

```python
def generate_stubs(
    args: Namespace,
    service_names: Sequence[ServiceName],
    available_service_names: Iterable[ServiceName],
    session: Session,
) -> None:
```

Generate service and master stubs.

#### Arguments

- `args` - Config namespace
- `service_names` - Enabled service names
- `available_service_names` - All service names
- `session` - Botocore session

#### See also

- [Namespace](cli_parser.md#namespace)

## get_available_service_names

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/main.py#L37)

```python
def get_available_service_names(session: Session) -> list[ServiceName]:
```

Get a list of boto3 supported service names.

#### Arguments

- `session` - Boto3 session

#### Returns

A list of supported services.

## main

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/main.py#L59)

```python
def main() -> None:
```

Main entrypoint for builder.
