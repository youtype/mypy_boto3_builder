# TypeAnnotation

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.type_annotation](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_annotation.py) module.

Wrapper for simple type annotation like `str` or `Dict`.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / TypeAnnotation
    - [TypeAnnotation](#typeannotation)
        - [TypeAnnotation().copy](#typeannotationcopy)
        - [TypeAnnotation().get_import_name](#typeannotationget_import_name)
        - [TypeAnnotation().get_import_record](#typeannotationget_import_record)
        - [TypeAnnotation().is_dict](#typeannotationis_dict)
        - [TypeAnnotation().is_list](#typeannotationis_list)
        - [TypeAnnotation().render](#typeannotationrender)

## TypeAnnotation

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_annotation.py#L25)

```python
class TypeAnnotation(FakeAnnotation):
    def __init__(wrapped_type: Any) -> None:
```

Wrapper for simple type annotation like `str` or `Dict`.

#### Arguments

- `wrapped_type` - Original type annotation.

#### See also

- [FakeAnnotation](fake_annotation.md#fakeannotation)

### TypeAnnotation().copy

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_annotation.py#L143)

```python
def copy() -> 'TypeAnnotation':
```

Create a copy of type annotation wrapper.

### TypeAnnotation().get_import_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_annotation.py#L116)

```python
def get_import_name() -> str:
```

Create a safe name for imported annotation.

### TypeAnnotation().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_annotation.py#L125)

```python
def get_import_record() -> ImportRecord:
```

Create a safe Import Record for annotation.

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### TypeAnnotation().is_dict

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_annotation.py#L131)

```python
def is_dict() -> bool:
```

Whether annotation is a plain Dict.

### TypeAnnotation().is_list

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_annotation.py#L137)

```python
def is_list() -> bool:
```

Whether annotation is a plain List.

### TypeAnnotation().render

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_annotation.py#L107)

```python
def render(parent_name: str = '') -> str:
```

Render type annotation to a valid Python code for local usage.

#### Returns

A string with a valid type annotation.
