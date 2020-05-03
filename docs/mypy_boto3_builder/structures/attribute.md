# Attribute

> Auto-generated documentation for [mypy_boto3_builder.structures.attribute](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/attribute.py) module.

Class or module attribute.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / Attribute
    - [Attribute](#attribute)
        - [Attribute().get_types](#attributeget_types)

## Attribute

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/attribute.py#L12)

```python
dataclass
class Attribute():
```

Class or module attribute.

#### Attributes

- `name` - Attribute name.
- `type` - Attribute type annotation.
- `value` - Attribute value.

### Attribute().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/attribute.py#L26)

```python
def get_types() -> Set[FakeAnnotation]:
```

Return all type annotations used.

#### Returns

A set of type annotations.
