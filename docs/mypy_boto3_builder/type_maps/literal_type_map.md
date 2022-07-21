# Literal Type Map

[mypy-boto3-builder Index](../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Type Maps](./index.md#type-maps) /
Literal Type Map

> Auto-generated documentation for [mypy_boto3_builder.type_maps.literal_type_map](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_maps/literal_type_map.py) module.

- [Literal Type Map](#literal-type-map)
  - [get_literal_type_stub](#get_literal_type_stub)

## get_literal_type_stub

[Show source in literal_type_map.py:9](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_maps/literal_type_map.py#L9)

Get stub type for botocore literal.

#### Arguments

- `service_name` - Service name.
- `literal_name` - Target Literal name.

#### Returns

Literal children or None.

#### Signature

```python
def get_literal_type_stub(
    service_name: ServiceName, literal_name: str
) -> list[str] | None:
    ...
```

#### See also

- [ServiceName](../service_name.md#servicename)


