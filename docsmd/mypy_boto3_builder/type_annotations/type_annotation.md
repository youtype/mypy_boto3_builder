# TypeAnnotation

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Type Annotations](./index.md#type-annotations) /
TypeAnnotation

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.type_annotation](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_annotation.py) module.

## TypeAnnotation

[Show source in type_annotation.py:13](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_annotation.py#L13)

Wrapper for `typing` type annotation.

#### Arguments

- `wrapped_type` - Original type annotation as a string.

#### Signature

```python
class TypeAnnotation(FakeAnnotation):
    def __init__(self, wrapped_type: str) -> None:
        ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)

### TypeAnnotation().copy

[Show source in type_annotation.py:112](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_annotation.py#L112)

Create a copy of type annotation wrapper.

#### Signature

```python
def copy(self: _R) -> _R:
    ...
```

### TypeAnnotation().get_import_name

[Show source in type_annotation.py:70](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_annotation.py#L70)

Create a safe name for imported annotation.

#### Signature

```python
def get_import_name(self) -> str:
    ...
```

### TypeAnnotation().get_import_record

[Show source in type_annotation.py:76](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_annotation.py#L76)

Create a safe Import Record for annotation.

#### Signature

```python
def get_import_record(self) -> ImportRecord:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### TypeAnnotation().is_dict

[Show source in type_annotation.py:94](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_annotation.py#L94)

Whether annotation is a plain Dict.

#### Signature

```python
def is_dict(self) -> bool:
    ...
```

### TypeAnnotation().is_list

[Show source in type_annotation.py:100](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_annotation.py#L100)

Whether annotation is a plain List.

#### Signature

```python
def is_list(self) -> bool:
    ...
```

### TypeAnnotation().is_union

[Show source in type_annotation.py:106](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_annotation.py#L106)

Whether annotation is a Union.

#### Signature

```python
def is_union(self) -> bool:
    ...
```

### TypeAnnotation().render

[Show source in type_annotation.py:61](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_annotation.py#L61)

Render type annotation to a valid Python code for local usage.

#### Returns

A string with a valid type annotation.

#### Signature

```python
def render(self, parent_name: str = "") -> str:
    ...
```
