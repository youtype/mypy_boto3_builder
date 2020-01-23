# Identifiers

> Auto-generated documentation for [mypy_boto3_builder.parsers.identifiers](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/identifiers.py) module.

Parser for Boto3 ServiceResource identifiers, produces `structures.Attribute`.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / Identifiers
    - [parse_identifiers](#parse_identifiers)

## parse_identifiers

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/identifiers.py#L12)

```python
def parse_identifiers(resource: Boto3ServiceResource) -> List[Attribute]:
```

Extract identifiers from boto3 resource.

#### Arguments

- `resource` - boto3 service resource.

#### Returns

A list of Attribute structures.
