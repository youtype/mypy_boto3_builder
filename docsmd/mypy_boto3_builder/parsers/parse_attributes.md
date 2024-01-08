# Parse Attributes

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](./index.md#parsers) / Parse Attributes

> Auto-generated documentation for [mypy_boto3_builder.parsers.parse_attributes](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/parse_attributes.py) module.

## parse_attributes

[Show source in parse_attributes.py:13](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/parse_attributes.py#L13)

Extract attributes from boto3 resource.

#### Arguments

- `resource` - boto3 service resource.

#### Returns

A list of Attribute structures.

#### Signature

```python
def parse_attributes(
    service_name: ServiceName,
    resource_name: str,
    resource: Boto3ServiceResource,
    shape_parser: ShapeParser,
) -> list[Attribute]: ...
```

#### See also

- [Attribute](../structures/attribute.md#attribute)
- [ServiceName](../service_name.md#servicename)
- [ShapeParser](./shape_parser.md#shapeparser)
