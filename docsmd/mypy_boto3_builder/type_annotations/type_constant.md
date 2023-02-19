# TypeConstant

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Type Annotations](./index.md#type-annotations) /
TypeConstant

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.type_constant](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_constant.py) module.

## TypeConstant

[Show source in type_constant.py:8](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_constant.py#L8)

Wrapper for constant like `False` or `"test"`.

#### Arguments

- `value` - Constant value.

#### Signature

```python
class TypeConstant(FakeAnnotation):
    def __init__(self, value: object) -> None:
        ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)

### TypeConstant().copy

[Show source in type_constant.py:37](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_constant.py#L37)

Create a copy of type annotation wrapper.

#### Signature

```python
def copy(self) -> "TypeConstant":
    ...
```

### TypeConstant().get_import_record

[Show source in type_constant.py:31](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_constant.py#L31)

Get empty import record, because constants do not require imports.

#### Signature

```python
def get_import_record(self) -> ImportRecord:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### TypeConstant().is_none

[Show source in type_constant.py:43](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_constant.py#L43)

Whether value is None.

#### Signature

```python
def is_none(self) -> bool:
    ...
```

### TypeConstant().render

[Show source in type_constant.py:19](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_constant.py#L19)

Render type annotation to a valid Python code for local usage.

#### Returns

A string with a valid type annotation.

#### Signature

```python
def render(self, parent_name: str = "") -> str:
    ...
```
