# TypeAnnotation

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](./index.md#type-annotations) / TypeAnnotation

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.type_annotation](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_annotation.py) module.

## TypeAnnotation

[Show source in type_annotation.py:14](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_annotation.py#L14)

#### Attributes

- `SUPPORTED_TYPES`: `dict[str, ImportString]` - Set of supported type annotations. value is default import module: {'Union': _typing, 'Any': _typing, 'Dict': _typing, 'List': _typing, 'Set': _typing, 'Optional': _typing, 'IO': _typing, 'overload': _typing, 'Type': _typing, 'NoReturn': _typing, 'TypedDict': _typing, 'Literal': _typing, 'Mapping': _typing, 'Sequence': _typing, 'Callable': _typing, 'Iterator': _typing, 'Awaitable': _typing, 'AsyncIterator': _typing, 'NotRequired': _typing}

- `FALLBACK`: `dict[str, tuple[tuple[int, int] | None, ImportString]]` - Set of fallback type annotations: {'NotRequired': ((3, 12), _typing_extensions), 'TypedDict': ((3, 12), _typing_extensions), 'Literal': ((3, 12), _typing_extensions)}


Wrapper for `typing` type annotation.

#### Arguments

- `wrapped_type` - Original type annotation as a string.

#### Signature

```python
class TypeAnnotation(FakeAnnotation):
    def __init__(self, wrapped_type: str) -> None: ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)

### TypeAnnotation().__copy__

[Show source in type_annotation.py:114](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_annotation.py#L114)

Create a copy of type annotation wrapper.

#### Signature

```python
def __copy__(self: _R) -> _R: ...
```

### TypeAnnotation()._get_import_records

[Show source in type_annotation.py:76](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_annotation.py#L76)

Create a safe Import Record for annotation.

#### Signature

```python
def _get_import_records(self) -> set[ImportRecord]: ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### TypeAnnotation().get_import_name

[Show source in type_annotation.py:70](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_annotation.py#L70)

Create a safe name for imported annotation.

#### Signature

```python
def get_import_name(self) -> str: ...
```

### TypeAnnotation().is_dict

[Show source in type_annotation.py:96](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_annotation.py#L96)

Whether annotation is a plain Dict.

#### Signature

```python
def is_dict(self) -> bool: ...
```

### TypeAnnotation().is_list

[Show source in type_annotation.py:102](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_annotation.py#L102)

Whether annotation is a plain List.

#### Signature

```python
def is_list(self) -> bool: ...
```

### TypeAnnotation().is_union

[Show source in type_annotation.py:108](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_annotation.py#L108)

Whether annotation is a Union.

#### Signature

```python
def is_union(self) -> bool: ...
```

### TypeAnnotation().render

[Show source in type_annotation.py:61](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_annotation.py#L61)

Render type annotation to a valid Python code for local usage.

#### Returns

A string with a valid type annotation.

#### Signature

```python
def render(self) -> str: ...
```
