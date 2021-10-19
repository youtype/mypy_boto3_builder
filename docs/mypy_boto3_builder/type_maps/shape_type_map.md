# Shape Type Map

> Auto-generated documentation for [mypy_boto3_builder.type_maps.shape_type_map](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_maps/shape_type_map.py) module.

String to type annotation map to replace overriden botocore shapes.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Maps](index.md#type-maps) / Shape Type Map
    - [get_shape_type_stub](#get_shape_type_stub)

## get_shape_type_stub

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_maps/shape_type_map.py#L104)

```python
def get_shape_type_stub(
    service_name: ServiceName,
    typed_dict_name: str,
) -> FakeAnnotation | None:
```

Get stub type for botocore shape.

#### Arguments

- `service_name` - Service name.
- `typed_dict_name` - Target TypedDict name.

#### Returns

Type annotation or None.

#### See also

- [ServiceName](../service_name.md#servicename)
