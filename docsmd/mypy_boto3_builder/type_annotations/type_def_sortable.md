# TypeDefSortable

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Type Annotations](./index.md#type-annotations) /
TypeDefSortable

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.type_def_sortable](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py) module.

## TypeDefSortable

[Show source in type_def_sortable.py:15](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L15)

Sortable protocol for TypeDefSorter.

#### Signature

```python
class TypeDefSortable(Protocol):
    ...
```

### TypeDefSortable().debug_render

[Show source in type_def_sortable.py:53](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L53)

Render type annotation for debug purposes.

#### Signature

```python
def debug_render(self) -> str:
    ...
```

### TypeDefSortable().get_children_literals

[Show source in type_def_sortable.py:59](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L59)

Extract required TypeLiteral list from attributes.

#### Signature

```python
def get_children_literals(self, processed: Iterable[str] = ()) -> set[TypeLiteral]:
    ...
```

#### See also

- [TypeLiteral](./type_literal.md#typeliteral)

### TypeDefSortable().get_children_types

[Show source in type_def_sortable.py:47](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L47)

Extract required type annotations from attributes.

#### Signature

```python
def get_children_types(self) -> set[FakeAnnotation]:
    ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)

### TypeDefSortable().get_sortable_children

[Show source in type_def_sortable.py:29](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L29)

Extract required sortable TypeDef list from attributes.

#### Signature

```python
def get_sortable_children(self) -> list["TypeDefSortable"]:
    ...
```

### TypeDefSortable().get_typing_import_records

[Show source in type_def_sortable.py:78](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L78)

Get import record required for using TypeAnnotation.

#### Signature

```python
def get_typing_import_records(self) -> set[ImportRecord]:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### TypeDefSortable().is_stringified

[Show source in type_def_sortable.py:35](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L35)

Whether TypeDef usage should be rendered as a string.

#### Signature

```python
def is_stringified(self) -> bool:
    ...
```

### TypeDefSortable().is_type_def

[Show source in type_def_sortable.py:65](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L65)

Whether type annotation is a TypeDef.

#### Signature

```python
def is_type_def(self) -> bool:
    ...
```

### TypeDefSortable().is_typed_dict

[Show source in type_def_sortable.py:84](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L84)

Whether type annotation is a TypedDict.

#### Signature

```python
def is_typed_dict(self) -> bool:
    ...
```

### TypeDefSortable().is_union

[Show source in type_def_sortable.py:90](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L90)

Whether type annotation is a TypeUnion.

#### Signature

```python
def is_union(self) -> bool:
    ...
```

### TypeDefSortable().iterate_children

[Show source in type_def_sortable.py:102](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L102)

Iterate over children.

#### Signature

```python
def iterate_children(self) -> Iterator[Any]:
    ...
```

### TypeDefSortable().replace_self_references

[Show source in type_def_sortable.py:96](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L96)

Replace self references with `Dict[str, Any]` to avoid circular dependencies.

#### Signature

```python
def replace_self_references(self) -> None:
    ...
```

### TypeDefSortable().stringify

[Show source in type_def_sortable.py:41](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L41)

Render TypeDef usage as a string.

#### Signature

```python
def stringify(self) -> None:
    ...
```

### TypeDefSortable().type_hint_annotations

[Show source in type_def_sortable.py:71](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L71)

Type annotations list from arguments and return type with internal types.

#### Signature

```python
@property
def type_hint_annotations(self) -> list[FakeAnnotation]:
    ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)
