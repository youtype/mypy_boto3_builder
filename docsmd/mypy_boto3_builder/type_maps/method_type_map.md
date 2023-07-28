# Method Type Map

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Type Maps](./index.md#type-maps) /
Method Type Map

> Auto-generated documentation for [mypy_boto3_builder.type_maps.method_type_map](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_maps/method_type_map.py) module.

## get_method_type_stub

[Show source in method_type_map.py:190](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_maps/method_type_map.py#L190)

Get stub type for method argument.

#### Arguments

- `service_name` - Service name.
- `class_name` - Parent class name.
- `method_name` - Method name.
- `argument_name` - Argument name.

#### Returns

Type annotation or None.

#### Signature

```python
def get_method_type_stub(
    service_name: ServiceName, class_name: str, method_name: str, argument_name: str
) -> FakeAnnotation | None:
    ...
```

#### See also

- [ServiceName](../service_name.md#servicename)
