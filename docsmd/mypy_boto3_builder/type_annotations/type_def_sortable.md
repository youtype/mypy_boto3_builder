# TypeDefSortable

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](./index.md#type-annotations) / TypeDefSortable

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.type_def_sortable](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py) module.

## TypeDefSortable

[Show source in type_def_sortable.py:14](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L14)

Sortable protocol for TypeDefSorter.

#### Signature

```python
class TypeDefSortable(Protocol): ...
```

### TypeDefSortable().__gt__

[Show source in type_def_sortable.py:22](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L22)

Compare with another TypeDefSortable. Has to be implemented.

#### Signature

```python
def __gt__(self, other: FakeAnnotation) -> bool: ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)

### TypeDefSortable().__lt__

[Show source in type_def_sortable.py:28](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L28)

Compare with another TypeDefSortable. Has to be implemented.

#### Signature

```python
def __lt__(self, other: FakeAnnotation) -> bool: ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)

### TypeDefSortable().get_children_literals

[Show source in type_def_sortable.py:64](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L64)

Extract required TypeLiteral list from attributes.

#### Signature

```python
def get_children_literals(self, processed: Iterable[str] = ()) -> set[TypeLiteral]: ...
```

#### See also

- [TypeLiteral](./type_literal.md#typeliteral)

### TypeDefSortable().get_children_types

[Show source in type_def_sortable.py:52](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L52)

Extract required type annotations from attributes.

#### Signature

```python
def get_children_types(self) -> set[FakeAnnotation]: ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)

### TypeDefSortable().get_definition_import_records

[Show source in type_def_sortable.py:83](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L83)

Get import record required for using TypeAnnotation.

#### Signature

```python
def get_definition_import_records(self) -> set[ImportRecord]: ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### TypeDefSortable().get_sortable_children

[Show source in type_def_sortable.py:34](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L34)

Extract required sortable TypeDef list from attributes.

#### Signature

```python
def get_sortable_children(self) -> list["TypeDefSortable"]: ...
```

### TypeDefSortable().is_stringified

[Show source in type_def_sortable.py:40](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L40)

Whether TypeDef usage should be rendered as a string.

#### Signature

```python
def is_stringified(self) -> bool: ...
```

### TypeDefSortable().is_type_def

[Show source in type_def_sortable.py:70](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L70)

Whether type annotation is a TypeDef.

#### Signature

```python
def is_type_def(self) -> bool: ...
```

### TypeDefSortable().is_typed_dict

[Show source in type_def_sortable.py:89](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L89)

Whether type annotation is a TypedDict.

#### Signature

```python
def is_typed_dict(self) -> bool: ...
```

### TypeDefSortable().is_union

[Show source in type_def_sortable.py:95](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L95)

Whether type annotation is a TypeUnion.

#### Signature

```python
def is_union(self) -> bool: ...
```

### TypeDefSortable().iterate_children

[Show source in type_def_sortable.py:101](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L101)

Iterate over children.

#### Signature

```python
def iterate_children(self) -> Iterator[Any]: ...
```

### TypeDefSortable().render_definition

[Show source in type_def_sortable.py:58](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L58)

Render type annotation for debug purposes.

#### Signature

```python
def render_definition(self) -> str: ...
```

### TypeDefSortable().stringify

[Show source in type_def_sortable.py:46](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L46)

Render TypeDef usage as a string.

#### Signature

```python
def stringify(self) -> None: ...
```

### TypeDefSortable().type_hint_annotations

[Show source in type_def_sortable.py:76](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_def_sortable.py#L76)

Type annotations list from arguments and return type with internal types.

#### Signature

```python
@property
def type_hint_annotations(self) -> list[FakeAnnotation]: ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)
