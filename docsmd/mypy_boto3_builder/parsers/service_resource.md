# Service Resource

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Parsers](./index.md#parsers) /
Service Resource

> Auto-generated documentation for [mypy_boto3_builder.parsers.service_resource](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/service_resource.py) module.

## get_sub_resources

[Show source in service_resource.py:99](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/service_resource.py#L99)

Initialize ServiceResource sub-resources with fake data.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.
- `resource` - Parent ServiceResource.

#### Returns

A list of initialized `Boto3ServiceResource`.

#### Signature

```python
def get_sub_resources(
    session: Session, service_name: ServiceName, resource: Boto3ServiceResource
) -> list[Boto3ServiceResource]:
    ...
```

#### See also

- [ServiceName](../service_name.md#servicename)



## parse_service_resource

[Show source in service_resource.py:28](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/service_resource.py#L28)

Parse boto3 ServiceResource data.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.

#### Returns

ServiceResource structure or None if service does not have a resource.

#### Signature

```python
def parse_service_resource(
    session: Session, service_name: ServiceName, shape_parser: ShapeParser
) -> ServiceResource | None:
    ...
```

#### See also

- [ServiceName](../service_name.md#servicename)
- [ShapeParser](./shape_parser.md#shapeparser)
