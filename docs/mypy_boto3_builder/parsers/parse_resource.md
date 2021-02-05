# Parse Resource

> Auto-generated documentation for [mypy_boto3_builder.parsers.parse_resource](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/parse_resource.py) module.

Parser for Boto3 ServiceResource sub-resource, produces `structures.Resource`

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / Parse Resource
    - [get_resource_public_methods](#get_resource_public_methods)
    - [parse_resource](#parse_resource)

## get_resource_public_methods

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/parse_resource.py#L71)

```python
def get_resource_public_methods(
    resource_class: Type[Boto3ServiceResource],
) -> Dict[(str, FunctionType)]:
```

Extract public methods from boto3 sub resource.

#### Arguments

- `resource_class` - boto3 resource meta.

#### Returns

A dictionary of method name and method.

## parse_resource

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/parse_resource.py#L22)

```python
def parse_resource(
    name: str,
    resource: Boto3ServiceResource,
    service_name: ServiceName,
    shape_parser: ShapeParser,
) -> Resource:
```

Parse boto3 sub Resource data.

#### Arguments

- `resource` - Original boto3 resource.

#### Returns

Resource structure.

#### See also

- [Resource](../structures/resource.md#resource)
- [ServiceName](../service_name.md#servicename)
- [ShapeParser](shape_parser.md#shapeparser)
