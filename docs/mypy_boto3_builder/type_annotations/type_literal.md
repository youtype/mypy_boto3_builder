# TypeLiteral

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.type_literal](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_literal.py) module.

Wrapper for `typing/typing_extensions.Literal` type annotations like `Literal['a', 'b']`.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / TypeLiteral
    - [TypeLiteral](#typeliteral)
        - [TypeLiteral().add_child](#typeliteraladd_child)
        - [TypeLiteral().copy](#typeliteralcopy)
        - [TypeLiteral().get_import_record](#typeliteralget_import_record)
        - [TypeLiteral().get_sort_key](#typeliteralget_sort_key)
        - [TypeLiteral.get_typing_import_record](#typeliteralget_typing_import_record)
        - [TypeLiteral().inline](#typeliteralinline)
        - [TypeLiteral().is_literal](#typeliteralis_literal)
        - [TypeLiteral().is_same](#typeliteralis_same)
        - [TypeLiteral().render](#typeliteralrender)
        - [TypeLiteral().render_children](#typeliteralrender_children)

## TypeLiteral

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_literal.py#L14)

```python
class TypeLiteral(FakeAnnotation):
    def __init__(name: str, children: Iterable[Any]) -> None:
```

Wrapper for `typing/typing_extensions.Literal` type annotations like `Literal['a', 'b']`.

#### Arguments

- `name` - Literal name for non-inline.
- `children` - Literal values.
- `inline` - Render literal inline.

#### See also

- [FakeAnnotation](fake_annotation.md#fakeannotation)

### TypeLiteral().add_child

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_literal.py#L110)

```python
def add_child(child: FakeAnnotation) -> None:
```

Disabled method to avoid confusion.

#### See also

- [FakeAnnotation](fake_annotation.md#fakeannotation)

### TypeLiteral().copy

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_literal.py#L98)

```python
def copy() -> 'TypeLiteral':
```

Create a copy of type annotation wrapper.

### TypeLiteral().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_literal.py#L89)

```python
def get_import_record() -> ImportRecord:
```

Get import record required for using type annotation.

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### TypeLiteral().get_sort_key

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_literal.py#L30)

```python
def get_sort_key() -> str:
```

Sort literals by name.

### TypeLiteral.get_typing_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_literal.py#L75)

```python
@staticmethod
def get_typing_import_record() -> ImportRecord:
```

Get import record required for using Literal.

Fallback to typing_extensions for py38-.

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### TypeLiteral().inline

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_literal.py#L36)

```python
@property
def inline() -> bool:
```

Whether Litereal should be rendered inline.

1-value literals are rendered inline.

### TypeLiteral().is_literal

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_literal.py#L104)

```python
def is_literal() -> bool:
```

Whether type annotation is `Literal`.

### TypeLiteral().is_same

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_literal.py#L116)

```python
def is_same(other: 'TypeLiteral') -> bool:
```

Check if literals have the same children.

### TypeLiteral().render

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_literal.py#L56)

```python
def render(parent_name: str = '') -> str:
```

Render type annotation to a valid Python code for local usage.

#### Returns

A string with a valid type annotation.

### TypeLiteral().render_children

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_literal.py#L69)

```python
def render_children() -> str:
```

Render literal children to representation.
