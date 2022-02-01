# Main

> Auto-generated documentation for [mypy_boto3_builder.main](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/main.py) module.

Main entrypoint for builder.

- [mypy-boto3-builder](../README.md#mypy_boto3_builder) / [Modules](../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / Main
    - [generate_boto3_stubs](#generate_boto3_stubs)
    - [generate_botocore_stubs](#generate_botocore_stubs)
    - [generate_docs](#generate_docs)
    - [generate_master](#generate_master)
    - [generate_stubs](#generate_stubs)
    - [get_available_service_names](#get_available_service_names)
    - [get_selected_service_names](#get_selected_service_names)
    - [main](#main)

## generate_boto3_stubs

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/main.py#L245)

```python
def generate_boto3_stubs(
    args: Namespace,
    session: Session,
    service_names: Iterable[ServiceName],
) -> None:
```

Generate `boto3-stubs` package.

#### See also

- [Namespace](cli_parser.md#namespace)

## generate_botocore_stubs

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/main.py#L273)

```python
def generate_botocore_stubs(args: Namespace) -> None:
```

Generate `botocore-stubs` package.

#### See also

- [Namespace](cli_parser.md#namespace)

## generate_docs

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/main.py#L302)

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

## generate_master

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/main.py#L217)

```python
def generate_master(
    args: Namespace,
    session: Session,
    service_names: Iterable[ServiceName],
) -> None:
```

Generate `mypy-boto3` package.

#### See also

- [Namespace](cli_parser.md#namespace)

## generate_stubs

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/main.py#L159)

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
- `build_version` - Package build version

#### See also

- [Namespace](cli_parser.md#namespace)

## get_available_service_names

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/main.py#L78)

```python
def get_available_service_names(session: Session) -> list[ServiceName]:
```

Get a list of boto3 supported service names.

#### Arguments

- `session` - Boto3 session

#### Returns

A list of supported services.

## get_selected_service_names

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/main.py#L40)

```python
def get_selected_service_names(
    selected: Iterable[str],
    available: Iterable[ServiceName],
) -> list[ServiceName]:
```

Get a list of selected service names.

Supports `updated` to select only services updated in currect `boto3` release.
Supports `all` to select all available service names.

#### Arguments

- `selected` - Selected service names as strings.
- `available` - All ServiceNames available in current boto3 release.

#### Returns

A list of selected ServiceNames.

## main

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/main.py#L100)

```python
def main() -> None:
```

Main entrypoint for builder.
