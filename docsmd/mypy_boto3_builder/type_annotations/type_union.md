# TypeUnion

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Type Annotations](./index.md#type-annotations) /
TypeUnion

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.type_union](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py) module.

## TypeUnion

[Show source in type_union.py:20](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L20)

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

### TypeUnion().copy

[Show source in type_union.py:73](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L73)

Create a copy of type annotation wrapper.

#### Signature

```python
def copy(self: _R) -> _R: ...
```

### TypeUnion().debug_render

[Show source in type_union.py:83](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L83)

Render type annotation for debug purposes.

#### Signature

```python
def debug_render(self) -> str: ...
```

### TypeUnion().get_children_literals

[Show source in type_union.py:111](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L111)

Extract required TypeLiteral list from attributes.

#### Signature

```python
def get_children_literals(self, processed: Iterable[str] = ()) -> set[TypeLiteral]: ...
```

#### See also

- [TypeLiteral](./type_literal.md#typeliteral)

### TypeUnion().get_children_types

[Show source in type_union.py:89](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L89)

Extract required type annotations from attributes.

#### Signature

```python
def get_children_types(self) -> set[FakeAnnotation]: ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)

### TypeUnion().get_definition_import_records

[Show source in type_union.py:126](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L126)

Get import record required for using Union.

#### Signature

```python
def get_definition_import_records(self) -> set[ImportRecord]: ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### TypeUnion().get_import_records

[Show source in type_union.py:142](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L142)

Get all import records required for using type annotation.

#### Signature

```python
def get_import_records(self) -> set[ImportRecord]: ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### TypeUnion().get_sortable_children

[Show source in type_union.py:98](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L98)

Extract required TypeDefSortable list from attributes.

#### Signature

```python
def get_sortable_children(self) -> list[TypeDefSortable]: ...
```

#### See also

- [TypeDefSortable](./type_def_sortable.md#typedefsortable)

### TypeUnion().is_named

[Show source in type_union.py:67](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L67)

Check if type annotation is a named type annotation.

#### Signature

```python
def is_named(self) -> bool: ...
```

### TypeUnion().is_stringified

[Show source in type_union.py:38](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L38)

Whether Union usage should be rendered as a string.

#### Signature

```python
def is_stringified(self) -> bool: ...
```

### TypeUnion().is_type_def

[Show source in type_union.py:158](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L158)

Whether type annotation is a TypeDef.

#### Signature

```python
def is_type_def(self) -> bool: ...
```

### TypeUnion().is_union

[Show source in type_union.py:175](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L175)

Whether type annotation is a TypeUnion.

#### Signature

```python
def is_union(self) -> bool: ...
```

### TypeUnion().iterate_children

[Show source in type_union.py:181](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L181)

Iterate over children.

#### Signature

```python
def iterate_children(self) -> Iterator[FakeAnnotation]: ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)

### TypeUnion().iterate_types

[Show source in type_union.py:148](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L148)

Extract type annotations from children.

#### Signature

```python
def iterate_types(self) -> Iterator[FakeAnnotation]: ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)

### TypeUnion().render

[Show source in type_union.py:50](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L50)

Render type annotation to a valid Python code for local usage.

#### Returns

A string with a valid type annotation.

#### Signature

```python
def render(self, parent_name: str = "") -> str: ...
```

### TypeUnion().stringify

[Show source in type_union.py:44](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L44)

Render Union usage as a string.

#### Signature

```python
def stringify(self) -> None: ...
```

### TypeUnion().type_hint_annotations

[Show source in type_union.py:164](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_union.py#L164)

Type annotations list from arguments and return type with internal types.

#### Signature

```python
@property
def type_hint_annotations(self) -> list[FakeAnnotation]: ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)
