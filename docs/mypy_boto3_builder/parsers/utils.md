# Utils

> Auto-generated documentation for [mypy_boto3_builder.parsers.utils](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/utils.py) module.

Parser utils.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / Utils
    - [get_region_name_literal](#get_region_name_literal)

## get_region_name_literal

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/utils.py#L12)

```python
def get_region_name_literal(
    session: Session,
    service_names: Iterable[ServiceName],
) -> TypeLiteral:
```

Get Literal with all regions.

#### Arguments

- `session` - boto3 session.
- `service_names` - All available service names.

#### Returns

TypeLiteral for region names.

#### See also

- [ServiceName](../service_name.md#servicename)
- [TypeLiteral](../type_annotations/type_literal.md#typeliteral)
