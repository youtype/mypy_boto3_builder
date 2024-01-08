# Parse Resource

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](./index.md#parsers) / Parse Resource

> Auto-generated documentation for [mypy_boto3_builder.parsers.parse_resource](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/parse_resource.py) module.

## get_resource_public_methods

[Show source in parse_resource.py:86](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/parse_resource.py#L86)

Extract public methods from boto3 sub resource.

#### Arguments

- `resource_class` - boto3 resource meta.

#### Returns

A dictionary of method name and method.

#### Signature

```python
def get_resource_public_methods(
    resource_class: type[Boto3ServiceResource],
) -> dict[str, MethodType]: ...
```



## parse_resource

[Show source in parse_resource.py:26](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/parse_resource.py#L26)

Parse boto3 sub Resource data.

#### Arguments

- `resource` - Original boto3 resource.

#### Returns

Resource structure.

#### Signature

```python
def parse_resource(
    name: str,
    resource: Boto3ServiceResource,
    service_name: ServiceName,
    shape_parser: ShapeParser,
) -> Resource: ...
```

#### See also

- [Resource](../structures/resource.md#resource)
- [ServiceName](../service_name.md#servicename)
- [ShapeParser](./shape_parser.md#shapeparser)
