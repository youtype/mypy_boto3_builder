# TypeConstant

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.type_constant](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_constant.py) module.

Wrapper for constant like `False` or `"test"`.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / TypeConstant
    - [TypeConstant](#typeconstant)
        - [TypeConstant().copy](#typeconstantcopy)
        - [TypeConstant().get_import_record](#typeconstantget_import_record)
        - [TypeConstant().is_none](#typeconstantis_none)
        - [TypeConstant().render](#typeconstantrender)

## TypeConstant

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_constant.py#L8)

```python
class TypeConstant(FakeAnnotation):
    def __init__(value: object) -> None:
```

Wrapper for constant like `False` or `"test"`.

#### Arguments

- `value` - Constant value.

#### See also

- [FakeAnnotation](fake_annotation.md#fakeannotation)

### TypeConstant().copy

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_constant.py#L37)

```python
def copy() -> 'TypeConstant':
```

Create a copy of type annotation wrapper.

### TypeConstant().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_constant.py#L31)

```python
def get_import_record() -> ImportRecord:
```

Get empty import record, because constants do not require imports.

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### TypeConstant().is_none

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_constant.py#L43)

```python
def is_none() -> bool:
```

Whether value is None.

### TypeConstant().render

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_constant.py#L19)

```python
def render(parent_name: str = '') -> str:
```

Render type annotation to a valid Python code for local usage.

#### Returns

A string with a valid type annotation.
