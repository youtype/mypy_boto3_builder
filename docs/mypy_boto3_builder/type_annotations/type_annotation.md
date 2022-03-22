# TypeAnnotation

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.type_annotation](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_annotation.py) module.

Wrapper for `typing` type annotation.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / TypeAnnotation
    - [TypeAnnotation](#typeannotation)
        - [TypeAnnotation().copy](#typeannotationcopy)
        - [TypeAnnotation().get_import_name](#typeannotationget_import_name)
        - [TypeAnnotation().get_import_record](#typeannotationget_import_record)
        - [TypeAnnotation().has_fallback](#typeannotationhas_fallback)
        - [TypeAnnotation().is_dict](#typeannotationis_dict)
        - [TypeAnnotation().is_list](#typeannotationis_list)
        - [TypeAnnotation().is_union](#typeannotationis_union)
        - [TypeAnnotation().render](#typeannotationrender)

## TypeAnnotation

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_annotation.py#L13)

```python
class TypeAnnotation(FakeAnnotation):
    def __init__(wrapped_type: str) -> None:
```

Wrapper for `typing` type annotation.

#### Arguments

- `wrapped_type` - Original type annotation as a string.

#### See also

- [FakeAnnotation](fake_annotation.md#fakeannotation)

### TypeAnnotation().copy

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_annotation.py#L106)

```python
def copy() -> _R:
```

Create a copy of type annotation wrapper.

### TypeAnnotation().get_import_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_annotation.py#L61)

```python
def get_import_name() -> str:
```

Create a safe name for imported annotation.

### TypeAnnotation().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_annotation.py#L67)

```python
def get_import_record() -> ImportRecord:
```

Create a safe Import Record for annotation.

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### TypeAnnotation().has_fallback

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_annotation.py#L112)

```python
def has_fallback() -> bool:
```

Whether type should be imported from `typing_extensions` as a py37 fallback.

### TypeAnnotation().is_dict

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_annotation.py#L88)

```python
def is_dict() -> bool:
```

Whether annotation is a plain Dict.

### TypeAnnotation().is_list

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_annotation.py#L94)

```python
def is_list() -> bool:
```

Whether annotation is a plain List.

### TypeAnnotation().is_union

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_annotation.py#L100)

```python
def is_union() -> bool:
```

Whether annotation is a Union.

### TypeAnnotation().render

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_annotation.py#L52)

```python
def render(parent_name: str = '') -> str:
```

Render type annotation to a valid Python code for local usage.

#### Returns

A string with a valid type annotation.
