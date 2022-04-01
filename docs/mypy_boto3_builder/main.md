# Main

> Auto-generated documentation for [mypy_boto3_builder.main](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/main.py) module.

Main entrypoint for builder.

- [mypy-boto3-builder](../README.md#mypy_boto3_builder) / [Modules](../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / Main
    - [generate_product](#generate_product)
    - [get_available_service_names](#get_available_service_names)
    - [get_selected_service_names](#get_selected_service_names)
    - [main](#main)

## generate_product

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/main.py#L85)

```python
def generate_product(
    product: Product,
    args: Namespace,
    session: Session,
    service_names: Sequence[ServiceName],
    master_service_names: Sequence[ServiceName],
) -> None:
```

Generate a selected product.

#### Arguments

- `product` - Product to generate
- `args` - CLI namespace
- `session` - Boto3 session
- `service_names` - Selected service names
- `master_service_names` - Service names included in master

#### See also

- [Namespace](cli_parser.md#namespace)
- [Product](constants.md#product)
- [ServiceName](service_name.md#servicename)

## get_available_service_names

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/main.py#L63)

```python
def get_available_service_names(session: Session) -> list[ServiceName]:
```

Get a list of boto3 supported service names.

#### Arguments

- `session` - Boto3 session

#### Returns

A list of supported services.

#### See also

- [ServiceName](service_name.md#servicename)

## get_selected_service_names

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/main.py#L23)

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

#### See also

- [ServiceName](service_name.md#servicename)

## main

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/main.py#L119)

```python
def main() -> None:
```

Main entrypoint for builder.
