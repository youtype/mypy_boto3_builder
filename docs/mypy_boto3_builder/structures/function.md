# Function

> Auto-generated documentation for [mypy_boto3_builder.structures.function](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py) module.

Module-level function.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / Function
    - [Function](#function)
        - [Function().body](#functionbody)
        - [Function().create_request_type_annotation](#functioncreate_request_type_annotation)
        - [Function().get_required_import_records](#functionget_required_import_records)
        - [Function().is_kw_only](#functionis_kw_only)
        - [Function().iterate_types](#functioniterate_types)
        - [Function().returns_none](#functionreturns_none)
        - [Function().short_docstring](#functionshort_docstring)
        - [Function().type_hint_annotations](#functiontype_hint_annotations)

## Function

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L14)

```python
class Function():
    def __init__(
        name: str,
        arguments: Iterable[Argument],
        return_type: FakeAnnotation,
        docstring: str = '',
        decorators: Iterable[FakeAnnotation] = tuple(),
        body_lines: Iterable[str] = tuple(),
        type_ignore: bool = False,
        is_async: bool = False,
    ):
```

Module-level function.

#### See also

- [Argument](argument.md#argument)
- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### Function().body

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L74)

```python
@property
def body() -> str:
```

Function body as a string.

### Function().create_request_type_annotation

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L53)

```python
def create_request_type_annotation(name: str) -> None:
```

Create and set `request_type_annotation` TypedDict based on function arguments.

### Function().get_required_import_records

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L91)

```python
def get_required_import_records() -> set[ImportRecord]:
```

Extract required import records.

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### Function().is_kw_only

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L111)

```python
def is_kw_only() -> bool:
```

Whether method arguments can be passed only as kwargs.

### Function().iterate_types

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L81)

```python
def iterate_types() -> Iterator[FakeAnnotation]:
```

Iterate over required type annotations.

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### Function().returns_none

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L104)

```python
@property
def returns_none() -> bool:
```

Whether return type is None.

### Function().short_docstring

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L40)

```python
@property
def short_docstring() -> str:
```

Docstring without documentation links.

### Function().type_hint_annotations

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L117)

```python
@property
def type_hint_annotations() -> list[FakeAnnotation]:
```

Type annotations list from arguments and return type with internal types.

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)
