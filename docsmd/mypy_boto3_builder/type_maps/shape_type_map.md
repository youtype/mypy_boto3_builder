# Shape Type Map

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Type Maps](./index.md#type-maps) /
Shape Type Map

> Auto-generated documentation for [mypy_boto3_builder.type_maps.shape_type_map](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_maps/shape_type_map.py) module.

## get_shape_type_stub

[Show source in shape_type_map.py:84](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_maps/shape_type_map.py#L84)

Get stub type for input botocore shape.

#### Arguments

- `shape_type_map` - Map to lookup
- `service_name` - Service name
- `shape_name` - Target TypedDict name

#### Returns

Type annotation or None.

#### Signature

```python
def get_shape_type_stub(
    shape_type_maps: Iterable[ShapeTypeMap], service_name: ServiceName, shape_name: str
) -> FakeAnnotation | None:
    ...
```

#### See also

- [ServiceName](../service_name.md#servicename)
- [ShapeTypeMap](#shapetypemap)



