# RemoveArgument

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.remove_argument](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/remove_argument.py) module.

Annotation to mark argument for removal.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / RemoveArgument
    - [RemoveArgument](#removeargument)
        - [RemoveArgument().copy](#removeargumentcopy)
        - [RemoveArgument().get_import_record](#removeargumentget_import_record)
        - [RemoveArgument().render](#removeargumentrender)

## RemoveArgument

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/remove_argument.py#L8)

```python
class RemoveArgument(FakeAnnotation):
```

Annotation to mark argument for removal.

#### See also

- [FakeAnnotation](fake_annotation.md#fakeannotation)

### RemoveArgument().copy

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/remove_argument.py#L19)

```python
def copy() -> FakeAnnotation:
```

Not used.

#### See also

- [FakeAnnotation](fake_annotation.md#fakeannotation)

### RemoveArgument().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/remove_argument.py#L25)

```python
def get_import_record() -> ImportRecord:
```

Not used.

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### RemoveArgument().render

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/remove_argument.py#L13)

```python
def render(parent_name: str = '') -> str:
```

Not used.
