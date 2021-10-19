# Service Resource

> Auto-generated documentation for [mypy_boto3_builder.parsers.service_resource](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/service_resource.py) module.

Parser for Boto3 ServiceResource, produces `structires.ServiceResource`.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / Service Resource
    - [get_sub_resources](#get_sub_resources)
    - [parse_service_resource](#parse_service_resource)

## get_sub_resources

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/service_resource.py#L101)

```python
def get_sub_resources(
    session: Session,
    service_name: ServiceName,
    resource: Boto3ServiceResource,
) -> list[Boto3ServiceResource]:
```

Initialize ServiceResource sub-resources with fake data.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.
- `resource` - Parent ServiceResource.

#### Returns

A list of initialized `Boto3ServiceResource`.

#### See also

- [ServiceName](../service_name.md#servicename)

## parse_service_resource

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/service_resource.py#L27)

```python
def parse_service_resource(
    session: Session,
    service_name: ServiceName,
    shape_parser: ShapeParser,
) -> ServiceResource | None:
```

Parse boto3 ServiceResource data.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.

#### Returns

ServiceResource structure or None if service does not have a resource.

#### See also

- [ServiceName](../service_name.md#servicename)
- [ShapeParser](shape_parser.md#shapeparser)
