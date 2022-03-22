# Parse Collections

> Auto-generated documentation for [mypy_boto3_builder.parsers.parse_collections](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/parse_collections.py) module.

Boto3 ServiceResource collections parser, produces `structures.Collection`.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / Parse Collections
    - [parse_collections](#parse_collections)

## parse_collections

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/parse_collections.py#L17)

```python
def parse_collections(
    parent_name: str,
    resource: Boto3ServiceResource,
    service_name: ServiceName,
    shape_parser: ShapeParser,
) -> list[Collection]:
```

Extract collections from boto3 resource.

#### Arguments

- `resource` - boto3 service resource.

#### Returns

A list of Collection structures.

#### See also

- [Collection](../structures/collection.md#collection)
- [ServiceName](../service_name.md#servicename)
- [ShapeParser](shape_parser.md#shapeparser)
