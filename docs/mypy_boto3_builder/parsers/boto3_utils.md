# Boto3 Utils

> Auto-generated documentation for [mypy_boto3_builder.parsers.boto3_utils](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/boto3_utils.py) module.

Getters for boto3 client and resource from session.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / Boto3 Utils
    - [get_boto3_client](#get_boto3_client)
    - [get_boto3_resource](#get_boto3_resource)

## get_boto3_client

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/boto3_utils.py#L12)

```python
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

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/boto3_utils.py#L26)

```python
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
