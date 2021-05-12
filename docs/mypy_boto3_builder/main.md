# Main

> Auto-generated documentation for [mypy_boto3_builder.main](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/main.py) module.

Main entrypoint for builder.

- [mypy-boto3-builder](../README.md#mypy_boto3_builder) / [Modules](../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / Main
    - [generate_docs](#generate_docs)
    - [generate_stubs](#generate_stubs)
    - [main](#main)

## generate_docs

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/main.py#L123)

```python
def generate_docs(
    args: Namespace,
    service_names: List[ServiceName],
    session: Session,
) -> None:
```

Generate service and master docs.

#### Arguments

- `args` - Config namespace
- `service_names` - Enabled service names
- `session` - Botocore session

#### See also

- [Namespace](cli_parser.md#namespace)

## generate_stubs

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/main.py#L82)

```python
def generate_stubs(
    args: Namespace,
    service_names: List[ServiceName],
    session: Session,
) -> None:
```

Generate service and master stubs.

#### Arguments

- `args` - Config namespace
- `service_names` - Enabled service names
- `session` - Botocore session

#### See also

- [Namespace](cli_parser.md#namespace)

## main

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/main.py#L25)

```python
def main() -> None:
```

Main entrypoint for builder.
