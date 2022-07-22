# Method Argument Map

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Type Maps](./index.md#type-maps) /
Method Argument Map

> Auto-generated documentation for [mypy_boto3_builder.type_maps.method_argument_map](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_maps/method_argument_map.py) module.

## get_method_arguments_stub

[Show source in method_argument_map.py:31](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_maps/method_argument_map.py#L31)

Get arguments list for method stub.

#### Arguments

- `service_name` - Service name.
- `class_name` - Parent class name.
- `method_name` - Method name.

#### Returns

A list of arguments or None.

#### Signature

```python
def get_method_arguments_stub(
    service_name: ServiceName, class_name: str, method_name: str
) -> list[Argument] | None:
    ...
```

#### See also

- [ServiceName](../service_name.md#servicename)



