# Attribute

> Auto-generated documentation for [mypy_boto3_builder.structures.attribute](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/attribute.py) module.

Class or module attribute.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / Attribute
    - [Attribute](#attribute)
        - [Attribute().get_types](#attributeget_types)
        - [Attribute().render](#attributerender)

## Attribute

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/attribute.py#L8)

```python
class Attribute():
    def __init__(
        name: str,
        type_annotation: FakeAnnotation,
        value: TypeConstant | None = None,
        type_ignore: bool = False,
    ):
```

Class or module attribute.

#### Attributes

- `name` - Attribute name.
- `type` - Attribute type annotation.
- `value` - Attribute value.
- `type_ignore` - Add type: ignore comment.

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### Attribute().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/attribute.py#L31)

```python
def get_types() -> set[FakeAnnotation]:
```

Return all type annotations used.

#### Returns

A set of type annotations.

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### Attribute().render

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/attribute.py#L40)

```python
def render() -> str:
```

Render to a string.
