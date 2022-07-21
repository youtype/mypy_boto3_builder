# Parse Identifiers

[mypy-boto3-builder Index](../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Parsers](./index.md#parsers) /
Parse Identifiers

> Auto-generated documentation for [mypy_boto3_builder.parsers.parse_identifiers](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/parse_identifiers.py) module.

- [Parse Identifiers](#parse-identifiers)
  - [parse_identifiers](#parse_identifiers)

## parse_identifiers

[Show source in parse_identifiers.py:10](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/parse_identifiers.py#L10)

Extract identifiers from boto3 resource.

#### Arguments

- `resource` - boto3 service resource.

#### Returns

A list of Attribute structures.

#### Signature

```python
def parse_identifiers(resource: Boto3ServiceResource) -> list[Attribute]:
    ...
```

#### See also

- [Attribute](../structures/attribute.md#attribute)


