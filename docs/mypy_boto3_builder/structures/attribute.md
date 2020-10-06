# Attribute

> Auto-generated documentation for [mypy_boto3_builder.structures.attribute](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/attribute.py) module.

Class or module attribute.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / Attribute
    - [Attribute](#attribute)
        - [Attribute().get_types](#attributeget_types)

## Attribute

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/attribute.py#L10)

```python
class Attribute():
    def __init__(
        name: str,
        type_annotation: FakeAnnotation,
        value: Optional[TypeConstant] = None,
    ):
```

Class or module attribute.

#### Attributes

- `name` - Attribute name.
- `type` - Attribute type annotation.
- `value` - Attribute value.

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### Attribute().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/attribute.py#L30)

```python
def get_types() -> Set[FakeAnnotation]:
```

Return all type annotations used.

#### Returns

A set of type annotations.
