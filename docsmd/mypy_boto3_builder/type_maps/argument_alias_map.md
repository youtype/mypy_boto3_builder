# Argument Alias Map

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Type Maps](./index.md#type-maps) /
Argument Alias Map

> Auto-generated documentation for [mypy_boto3_builder.type_maps.argument_alias_map](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_maps/argument_alias_map.py) module.

## get_argument_alias

[Show source in argument_alias_map.py:32](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_maps/argument_alias_map.py#L32)

Get argument alias for operation.

#### Arguments

- `service_name` - Service name
- `operation_name` - Resource operation name
- `argument_name` - Argument name

#### Returns

Argument alias name or None if argument has to be deleted.

#### Signature

```python
def get_argument_alias(
    service_name: ServiceName, operation_name: str, argument_name: str
) -> str | None:
    ...
```

#### See also

- [ServiceName](../service_name.md#servicename)
