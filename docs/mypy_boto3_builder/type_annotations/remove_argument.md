# RemoveArgument

[mypy-boto3-builder Index](../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Type Annotations](./index.md#type-annotations) /
RemoveArgument

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.remove_argument](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/remove_argument.py) module.

- [RemoveArgument](#removeargument)
  - [RemoveArgument](#removeargument-1)
    - [RemoveArgument().copy](#removeargument()copy)
    - [RemoveArgument().get_import_record](#removeargument()get_import_record)
    - [RemoveArgument().render](#removeargument()render)

## RemoveArgument

[Show source in remove_argument.py:12](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/remove_argument.py#L12)

Annotation to mark argument for removal.

#### Signature

```python
class RemoveArgument(FakeAnnotation):
    ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)

### RemoveArgument().copy

[Show source in remove_argument.py:23](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/remove_argument.py#L23)

Not used.

#### Signature

```python
def copy(self: _R) -> _R:
    ...
```

### RemoveArgument().get_import_record

[Show source in remove_argument.py:29](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/remove_argument.py#L29)

Not used.

#### Signature

```python
def get_import_record(self) -> ImportRecord:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### RemoveArgument().render

[Show source in remove_argument.py:17](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/remove_argument.py#L17)

Not used.

#### Signature

```python
def render(self, parent_name: str = "") -> str:
    ...
```


