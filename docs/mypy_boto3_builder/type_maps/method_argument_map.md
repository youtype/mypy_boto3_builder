# Method Argument Map

> Auto-generated documentation for [mypy_boto3_builder.type_maps.method_argument_map](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_maps/method_argument_map.py) module.

String to type annotation map that find type annotation by method and argument name.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Maps](index.md#type-maps) / Method Argument Map
    - [get_method_arguments_stub](#get_method_arguments_stub)

## get_method_arguments_stub

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_maps/method_argument_map.py#L31)

```python
def get_method_arguments_stub(
    service_name: ServiceName,
    class_name: str,
    method_name: str,
) -> list[Argument] | None:
```

Get arguments list for method stub.

#### Arguments

- `service_name` - Service name.
- `class_name` - Parent class name.
- `method_name` - Method name.

#### Returns

A list of arguments or None.

#### See also

- [ServiceName](../service_name.md#servicename)
