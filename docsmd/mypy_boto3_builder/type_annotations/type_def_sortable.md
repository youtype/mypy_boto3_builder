# TypeDefSortable

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Type Annotations](./index.md#type-annotations) /
TypeDefSortable

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.type_def_sortable](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py) module.

## TypeDefSortable

[Show source in type_def_sortable.py:14](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L14)

Sortable protocol for TypeDefSorter.

#### Signature

```python
class TypeDefSortable(Protocol): ...
```

### TypeDefSortable().debug_render

[Show source in type_def_sortable.py:50](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L50)

Render type annotation for debug purposes.

#### Signature

```python
def debug_render(self) -> str: ...
```

### TypeDefSortable().get_children_literals

[Show source in type_def_sortable.py:56](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L56)

Extract required TypeLiteral list from attributes.

#### Signature

```python
def get_children_literals(self, processed: Iterable[str] = ()) -> set[TypeLiteral]: ...
```

#### See also

- [TypeLiteral](./type_literal.md#typeliteral)

### TypeDefSortable().get_children_types

[Show source in type_def_sortable.py:44](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L44)

Extract required type annotations from attributes.

#### Signature

```python
def get_children_types(self) -> set[FakeAnnotation]: ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)

### TypeDefSortable().get_definition_import_records

[Show source in type_def_sortable.py:75](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L75)

Get import record required for using TypeAnnotation.

#### Signature

```python
def get_definition_import_records(self) -> set[ImportRecord]: ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### TypeDefSortable().get_sortable_children

[Show source in type_def_sortable.py:26](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L26)

Extract required sortable TypeDef list from attributes.

#### Signature

```python
def get_sortable_children(self) -> list["TypeDefSortable"]: ...
```

### TypeDefSortable().is_stringified

[Show source in type_def_sortable.py:32](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L32)

Whether TypeDef usage should be rendered as a string.

#### Signature

```python
def is_stringified(self) -> bool: ...
```

### TypeDefSortable().is_type_def

[Show source in type_def_sortable.py:62](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L62)

Whether type annotation is a TypeDef.

#### Signature

```python
def is_type_def(self) -> bool: ...
```

### TypeDefSortable().is_typed_dict

[Show source in type_def_sortable.py:81](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L81)

Whether type annotation is a TypedDict.

#### Signature

```python
def is_typed_dict(self) -> bool: ...
```

### TypeDefSortable().is_union

[Show source in type_def_sortable.py:87](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L87)

Whether type annotation is a TypeUnion.

#### Signature

```python
def is_union(self) -> bool: ...
```

### TypeDefSortable().iterate_children

[Show source in type_def_sortable.py:93](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L93)

Iterate over children.

#### Signature

```python
def iterate_children(self) -> Iterator[Any]: ...
```

### TypeDefSortable().stringify

[Show source in type_def_sortable.py:38](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L38)

Render TypeDef usage as a string.

#### Signature

```python
def stringify(self) -> None: ...
```

### TypeDefSortable().type_hint_annotations

[Show source in type_def_sortable.py:68](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L68)

Type annotations list from arguments and return type with internal types.

#### Signature

```python
@property
def type_hint_annotations(self) -> list[FakeAnnotation]: ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)
