# Parse Collections

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Parsers](./index.md#parsers) /
Parse Collections

> Auto-generated documentation for [mypy_boto3_builder.parsers.parse_collections](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/parse_collections.py) module.

## parse_collections

[Show source in parse_collections.py:17](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/parse_collections.py#L17)

Extract collections from boto3 resource.

#### Arguments

- `resource` - boto3 service resource.

#### Returns

A list of Collection structures.

#### Signature

```python
def parse_collections(
    parent_name: str,
    resource: Boto3ServiceResource,
    service_name: ServiceName,
    shape_parser: ShapeParser,
) -> list[Collection]:
    ...
```

#### See also

- [Collection](../structures/collection.md#collection)
- [ServiceName](../service_name.md#servicename)
- [ShapeParser](./shape_parser.md#shapeparser)



