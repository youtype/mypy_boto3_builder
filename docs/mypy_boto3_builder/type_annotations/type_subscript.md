# TypeSubscript

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.type_subscript](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_subscript.py) module.

Wrapper for subscript type annotations, like `List[str]`.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / TypeSubscript
    - [TypeSubscript](#typesubscript)
        - [TypeSubscript().add_child](#typesubscriptadd_child)
        - [TypeSubscript().copy](#typesubscriptcopy)
        - [TypeSubscript().get_import_record](#typesubscriptget_import_record)
        - [TypeSubscript().get_types](#typesubscriptget_types)
        - [TypeSubscript().is_dict](#typesubscriptis_dict)
        - [TypeSubscript().is_list](#typesubscriptis_list)
        - [TypeSubscript().render](#typesubscriptrender)

## TypeSubscript

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_subscript.py#L11)

```python
class TypeSubscript(FakeAnnotation):
    def __init__(
        parent: TypeAnnotation,
        children: Iterable[FakeAnnotation] = (),
    ) -> None:
```

Wrapper for subscript type annotations, like `List[str]`.

#### Arguments

- `parent` - Parent type annotation.
- `children` - Children type annotations.

#### See also

- [FakeAnnotation](fake_annotation.md#fakeannotation)
- [TypeAnnotation](type_annotation.md#typeannotation)

### TypeSubscript().add_child

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_subscript.py#L56)

```python
def add_child(child: FakeAnnotation) -> None:
```

#### See also

- [FakeAnnotation](fake_annotation.md#fakeannotation)

### TypeSubscript().copy

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_subscript.py#L65)

```python
def copy() -> 'TypeSubscript':
```

Create a copy of type annotation wrapper.

### TypeSubscript().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_subscript.py#L44)

```python
def get_import_record() -> ImportRecord:
```

Get import record required for using type annotation.

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### TypeSubscript().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_subscript.py#L50)

```python
def get_types() -> Set[FakeAnnotation]:
```

### TypeSubscript().is_dict

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_subscript.py#L59)

```python
def is_dict() -> bool:
```

### TypeSubscript().is_list

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_subscript.py#L62)

```python
def is_list() -> bool:
```

### TypeSubscript().render

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_subscript.py#L31)

```python
def render(parent_name: str = '') -> str:
```

Render type annotation to a valid Python code for local usage.

#### Returns

A string with a valid type annotation.
