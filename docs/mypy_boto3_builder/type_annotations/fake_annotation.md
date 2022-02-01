# FakeAnnotation

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.fake_annotation](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/fake_annotation.py) module.

Parent class for all type annotation wrappers.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / FakeAnnotation
    - [FakeAnnotation](#fakeannotation)
        - [FakeAnnotation().add_child](#fakeannotationadd_child)
        - [FakeAnnotation().copy](#fakeannotationcopy)
        - [FakeAnnotation().get_import_record](#fakeannotationget_import_record)
        - [FakeAnnotation().get_sort_key](#fakeannotationget_sort_key)
        - [FakeAnnotation().get_types](#fakeannotationget_types)
        - [FakeAnnotation().is_dict](#fakeannotationis_dict)
        - [FakeAnnotation().is_list](#fakeannotationis_list)
        - [FakeAnnotation().is_literal](#fakeannotationis_literal)
        - [FakeAnnotation().is_typed_dict](#fakeannotationis_typed_dict)
        - [FakeAnnotation().render](#fakeannotationrender)

## FakeAnnotation

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/fake_annotation.py#L9)

```python
class FakeAnnotation(ABC):
```

Parent class for all type annotation wrappers.

### FakeAnnotation().add_child

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/fake_annotation.py#L62)

```python
def add_child(child: 'FakeAnnotation') -> None:
```

Add new child to `TypeSubscript` or `TypeTypedDict` annotation.

### FakeAnnotation().copy

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/fake_annotation.py#L91)

```python
@abstractmethod
def copy() -> 'FakeAnnotation':
```

Create a copy of type annotation wrapper.

### FakeAnnotation().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/fake_annotation.py#L50)

```python
@abstractmethod
def get_import_record() -> ImportRecord:
```

Get import record required for using type annotation.

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### FakeAnnotation().get_sort_key

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/fake_annotation.py#L35)

```python
def get_sort_key() -> str:
```

Get string to sort annotations.

### FakeAnnotation().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/fake_annotation.py#L56)

```python
def get_types() -> set['FakeAnnotation']:
```

Get all used type annotations recursively including self.

### FakeAnnotation().is_dict

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/fake_annotation.py#L67)

```python
def is_dict() -> bool:
```

Whether type annotation is `Dict` or `TypedDict`.

### FakeAnnotation().is_list

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/fake_annotation.py#L79)

```python
def is_list() -> bool:
```

Whether type annotation is `List`.

### FakeAnnotation().is_literal

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/fake_annotation.py#L85)

```python
def is_literal() -> bool:
```

Whether type annotation is `Literal`.

### FakeAnnotation().is_typed_dict

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/fake_annotation.py#L73)

```python
def is_typed_dict() -> bool:
```

Whether type annotation is `TypedDict`.

### FakeAnnotation().render

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/fake_annotation.py#L44)

```python
@abstractmethod
def render(parent_name: str = '') -> str:
```

Render type annotation to a valid Python code for local usage.
