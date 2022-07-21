# Parse References

[mypy-boto3-builder Index](../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Parsers](./index.md#parsers) /
Parse References

> Auto-generated documentation for [mypy_boto3_builder.parsers.parse_references](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/parse_references.py) module.

- [Parse References](#parse-references)
  - [parse_references](#parse_references)

## parse_references

[Show source in parse_references.py:13](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/parse_references.py#L13)

Extract references from boto3 resource.

#### Arguments

- `resource` - boto3 service resource.

#### Returns

A list of Attribute structures.

#### Signature

```python
def parse_references(resource: Boto3ServiceResource) -> list[Attribute]:
    ...
```

#### See also

- [Attribute](../structures/attribute.md#attribute)


