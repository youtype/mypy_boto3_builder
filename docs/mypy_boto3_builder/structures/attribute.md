# Attribute

> Auto-generated documentation for [mypy_boto3_builder.structures.attribute](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/attribute.py) module.

Class or module attribute.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / Attribute
    - [Attribute](#attribute)
        - [Attribute().iterate_types](#attributeiterate_types)
        - [Attribute().render](#attributerender)

## Attribute

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/attribute.py#L10)

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

### Attribute().iterate_types

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/attribute.py#L33)

```python
def iterate_types() -> Iterator[FakeAnnotation]:
```

Iterate over all type annotations used.

#### Yields

Type annotation.

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### Attribute().render

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/attribute.py#L42)

```python
def render() -> str:
```

Render to a string.
