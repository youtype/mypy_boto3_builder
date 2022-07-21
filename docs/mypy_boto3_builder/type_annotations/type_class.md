# TypeClass

[mypy-boto3-builder Index](../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Type Annotations](./index.md#type-annotations) /
TypeClass

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.type_class](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_class.py) module.

- [TypeClass](#typeclass)
  - [TypeClass](#typeclass-1)
    - [TypeClass().copy](#typeclass()copy)
    - [TypeClass().get_import_name](#typeclass()get_import_name)
    - [TypeClass().get_import_record](#typeclass()get_import_record)
    - [TypeClass().render](#typeclass()render)

## TypeClass

[Show source in type_class.py:11](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_class.py#L11)

Wrapper for classes like `Paginator`.

#### Arguments

- `value` - Any Class.
- `alias` - Local name.

#### Signature

```python
class TypeClass(FakeAnnotation):
    def __init__(self, value: type, alias: str = "") -> None:
        ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)

### TypeClass().copy

[Show source in type_class.py:57](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_class.py#L57)

Create a copy of type annotation wrapper.

#### Signature

```python
def copy(self) -> "TypeClass":
    ...
```

### TypeClass().get_import_name

[Show source in type_class.py:36](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_class.py#L36)

Get name for import string.

#### Signature

```python
def get_import_name(self) -> str:
    ...
```

### TypeClass().get_import_record

[Show source in type_class.py:42](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_class.py#L42)

Create an impoort record to insert where TypeClass is used.

#### Signature

```python
def get_import_record(self) -> ImportRecord:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### TypeClass().render

[Show source in type_class.py:24](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_class.py#L24)

Render type annotation to a valid Python code for local usage.

#### Returns

A string with a valid type annotation.

#### Signature

```python
def render(self, parent_name: str = "") -> str:
    ...
```


