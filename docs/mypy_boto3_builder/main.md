# Main

> Auto-generated documentation for [mypy_boto3_builder.main](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/main.py) module.

Main entrypoint for builder.

- [mypy-boto3-builder](../README.md#mypy_boto3_builder) / [Modules](../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / Main
    - [get_available_service_names](#get_available_service_names)
    - [get_selected_service_names](#get_selected_service_names)
    - [main](#main)

## get_available_service_names

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/main.py#L63)

```python
def get_available_service_names(session: Session) -> list[ServiceName]:
```

Get a list of boto3 supported service names.

#### Arguments

- `session` - Boto3 session

#### Returns

A list of supported services.

## get_selected_service_names

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/main.py#L25)

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

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/main.py#L85)

```python
def main() -> None:
```

Main entrypoint for builder.
