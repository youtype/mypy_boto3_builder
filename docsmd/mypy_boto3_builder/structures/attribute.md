# Attribute

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](./index.md#structures) / Attribute

> Auto-generated documentation for [mypy_boto3_builder.structures.attribute](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/attribute.py) module.

## Attribute

[Show source in attribute.py:11](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/attribute.py#L11)

Class or module attribute.

#### Attributes

- `name` - Attribute name.
- `type` - Attribute type annotation.
- `value` - Attribute value.
- `type_ignore` - Add type: ignore comment.
- `is_reference` - Whether the attribute parsed from references.
- `is_identifier` - Whether the attribute parsed from identifiers.
- `is_collection` - Whether the attribute parsed from collections.

#### Signature

```python
class Attribute:
    def __init__(
        self,
        name: str,
        type_annotation: FakeAnnotation,
        value: TypeConstant | None = None,
        type_ignore: bool = False,
        is_reference: bool = False,
        is_identifier: bool = False,
        is_collection: bool = False,
    ) -> None: ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### Attribute().is_autoload_property

[Show source in attribute.py:61](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/attribute.py#L61)

Whether the attribute is an autoload property.

#### Signature

```python
def is_autoload_property(self) -> bool: ...
```

### Attribute().iterate_types

[Show source in attribute.py:43](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/attribute.py#L43)

Iterate over all type annotations used.

#### Yields

Type annotation.

#### Signature

```python
def iterate_types(self) -> Iterator[FakeAnnotation]: ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### Attribute().render

[Show source in attribute.py:52](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/attribute.py#L52)

Render to a string.

#### Signature

```python
def render(self) -> str: ...
```
