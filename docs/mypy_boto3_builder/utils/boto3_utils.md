# Boto3 Utils

> Auto-generated documentation for [mypy_boto3_builder.utils.boto3_utils](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/utils/boto3_utils.py) module.

Getters for boto3 client and resource from session.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Utils](index.md#utils) / Boto3 Utils
    - [get_boto3_client](#get_boto3_client)
    - [get_boto3_resource](#get_boto3_resource)
    - [get_region_name_literal](#get_region_name_literal)

## get_boto3_client

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/utils/boto3_utils.py#L16)

```python
@cache
def get_boto3_client(
    session: Session,
    service_name: ServiceName,
) -> BaseClient:
```

Get boto3 client from `session`.

#### Arguments

- `session` - boto3 session.
- `service_name` - ServiceName instance.

#### Returns

Boto3 client.

#### See also

- [ServiceName](../service_name.md#servicename)

## get_boto3_resource

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/utils/boto3_utils.py#L31)

```python
@cache
def get_boto3_resource(
    session: Session,
    service_name: ServiceName,
) -> Boto3ServiceResource | None:
```

Get boto3 resource from `session`.

#### Arguments

- `session` - boto3 session.
- `service_name` - ServiceName instance.

#### Returns

Boto3 resource or None.

#### See also

- [ServiceName](../service_name.md#servicename)

## get_region_name_literal

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/utils/boto3_utils.py#L49)

```python
def get_region_name_literal(
    session: Session,
    service_names: Iterable[ServiceName],
) -> TypeLiteral | None:
```

Get Literal with all regions.

#### Arguments

- `session` - boto3 session.
- `service_names` - All available service names.

#### Returns

TypeLiteral for region names.

#### See also

- [ServiceName](../service_name.md#servicename)
