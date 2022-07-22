# Attribute

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Structures](./index.md#structures) /
Attribute

> Auto-generated documentation for [mypy_boto3_builder.structures.attribute](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/attribute.py) module.

## Attribute

[Show source in attribute.py:10](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/attribute.py#L10)

Class or module attribute.

#### Attributes

- `name` - Attribute name.
- `type` - Attribute type annotation.
- `value` - Attribute value.
- `type_ignore` - Add type: ignore comment.

#### Signature

```python
class Attribute:
    def __init__(
        self,
        name: str,
        type_annotation: FakeAnnotation,
        value: TypeConstant | None = None,
        type_ignore: bool = False,
    ):
        ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### Attribute().iterate_types

[Show source in attribute.py:33](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/attribute.py#L33)

Iterate over all type annotations used.

#### Yields

Type annotation.

#### Signature

```python
def iterate_types(self) -> Iterator[FakeAnnotation]:
    ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### Attribute().render

[Show source in attribute.py:42](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/attribute.py#L42)

Render to a string.

#### Signature

```python
def render(self) -> str:
    ...
```



