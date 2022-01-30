# Parse Attributes

> Auto-generated documentation for [mypy_boto3_builder.parsers.parse_attributes](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/parse_attributes.py) module.

Parser for Boto3 ServiceResource attributes, produces `structures.Attribute`.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / Parse Attributes
    - [parse_attributes](#parse_attributes)

## parse_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/parse_attributes.py#L12)

```python
def parse_attributes(
    service_name: ServiceName,
    resource_name: str,
    resource: Boto3ServiceResource,
    shape_parser: ShapeParser,
) -> list[Attribute]:
```

Extract attributes from boto3 resource.

#### Arguments

- `resource` - boto3 service resource.

#### Returns

A list of Attribute structures.

#### See also

- [ServiceName](../service_name.md#servicename)
- [ShapeParser](shape_parser.md#shapeparser)
