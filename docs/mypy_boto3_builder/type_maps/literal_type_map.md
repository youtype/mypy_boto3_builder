# Literal Type Map

> Auto-generated documentation for [mypy_boto3_builder.type_maps.literal_type_map](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_maps/literal_type_map.py) module.

String to type annotation map to replace overriden botocore literals.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Maps](index.md#type-maps) / Literal Type Map
    - [get_literal_type_stub](#get_literal_type_stub)

## get_literal_type_stub

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_maps/literal_type_map.py#L48)

```python
def get_literal_type_stub(
    service_name: ServiceName,
    literal_name: str,
) -> Optional[FakeAnnotation]:
```

Get stub type for botocore literal.

#### Arguments

- `service_name` - Service name.
- `literal_name` - Target Literal name.

#### Returns

Type annotation or None.

#### See also

- [ServiceName](../service_name.md#servicename)
