# TypeUnion

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](./index.md#type-annotations) / TypeUnion

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.type_union](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py) module.

## TypeUnion

[Show source in type_union.py:21](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L21)

Wrapper for name Union type annotations, like `MyUnion = Union[str, int]`.

#### Signature

```python
class TypeUnion(TypeSubscript, TypeDefSortable):
    def __init__(
        self, children: Iterable[FakeAnnotation], name: str = "", stringify: bool = False
    ) -> None: ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)
- [TypeDefSortable](./type_def_sortable.md#typedefsortable)
- [TypeSubscript](./type_subscript.md#typesubscript)

### TypeUnion().__copy__

[Show source in type_union.py:74](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L74)

Create a copy of type annotation wrapper.

#### Signature

```python
def __copy__(self: Self) -> Self: ...
```

### TypeUnion()._get_import_records

[Show source in type_union.py:131](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L131)

Get import record required for using type annotation.

#### Signature

```python
def _get_import_records(self) -> set[ImportRecord]: ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### TypeUnion().get_children_literals

[Show source in type_union.py:106](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L106)

Extract required TypeLiteral list from attributes.

#### Signature

```python
def get_children_literals(self, processed: Iterable[str] = ()) -> set[TypeLiteral]: ...
```

#### See also

- [TypeLiteral](./type_literal.md#typeliteral)

### TypeUnion().get_children_types

[Show source in type_union.py:84](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L84)

Extract required type annotations from attributes.

#### Signature

```python
def get_children_types(self) -> set[FakeAnnotation]: ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)

### TypeUnion().get_definition_import_records

[Show source in type_union.py:121](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L121)

Get import record required for using Union.

#### Signature

```python
def get_definition_import_records(self) -> set[ImportRecord]: ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### TypeUnion().get_import_records

[Show source in type_union.py:137](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L137)

Get all import records required for using type annotation.

#### Signature

```python
def get_import_records(self) -> set[ImportRecord]: ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### TypeUnion().get_sortable_children

[Show source in type_union.py:93](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L93)

Extract required TypeDefSortable list from attributes.

#### Signature

```python
def get_sortable_children(self) -> list[TypeDefSortable]: ...
```

#### See also

- [TypeDefSortable](./type_def_sortable.md#typedefsortable)

### TypeUnion().is_named

[Show source in type_union.py:68](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L68)

Check if type annotation is a named type annotation.

#### Signature

```python
def is_named(self) -> bool: ...
```

### TypeUnion().is_stringified

[Show source in type_union.py:39](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L39)

Whether Union usage should be rendered as a string.

#### Signature

```python
def is_stringified(self) -> bool: ...
```

### TypeUnion().is_type_def

[Show source in type_union.py:153](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L153)

Whether type annotation is a TypeDef.

#### Signature

```python
def is_type_def(self) -> bool: ...
```

### TypeUnion().is_union

[Show source in type_union.py:170](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L170)

Whether type annotation is a TypeUnion.

#### Signature

```python
def is_union(self) -> bool: ...
```

### TypeUnion().iterate_children

[Show source in type_union.py:176](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L176)

Iterate over children.

#### Signature

```python
def iterate_children(self) -> Iterator[FakeAnnotation]: ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)

### TypeUnion().iterate_types

[Show source in type_union.py:143](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L143)

Extract type annotations from children.

#### Signature

```python
def iterate_types(self) -> Iterator[FakeAnnotation]: ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)

### TypeUnion().render

[Show source in type_union.py:51](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L51)

Render type annotation to a valid Python code for local usage.

#### Returns

A string with a valid type annotation.

#### Signature

```python
def render(self) -> str: ...
```

### TypeUnion().render_definition

[Show source in type_union.py:182](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L182)

Render type annotation definition.

#### Signature

```python
def render_definition(self) -> str: ...
```

### TypeUnion().stringify

[Show source in type_union.py:45](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L45)

Render Union usage as a string.

#### Signature

```python
def stringify(self) -> None: ...
```

### TypeUnion().type_hint_annotations

[Show source in type_union.py:159](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L159)

Type annotations list from arguments and return type with internal types.

#### Signature

```python
@property
def type_hint_annotations(self) -> list[FakeAnnotation]: ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)
