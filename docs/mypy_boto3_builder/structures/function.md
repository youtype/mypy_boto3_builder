# Function

[mypy-boto3-builder Index](../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Structures](./index.md#structures) /
Function

> Auto-generated documentation for [mypy_boto3_builder.structures.function](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py) module.

- [Function](#function)
  - [Function](#function-1)
    - [Function().body](#function()body)
    - [Function().create_request_type_annotation](#function()create_request_type_annotation)
    - [Function().get_required_import_records](#function()get_required_import_records)
    - [Function().is_kw_only](#function()is_kw_only)
    - [Function().iterate_types](#function()iterate_types)
    - [Function().returns_none](#function()returns_none)
    - [Function().short_docstring](#function()short_docstring)
    - [Function().type_hint_annotations](#function()type_hint_annotations)

## Function

[Show source in function.py:14](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L14)

Module-level function.

#### Signature

```python
class Function:
    def __init__(
        self,
        name: str,
        arguments: Iterable[Argument],
        return_type: FakeAnnotation,
        docstring: str = "",
        decorators: Iterable[FakeAnnotation] = tuple(),
        body_lines: Iterable[str] = tuple(),
        type_ignore: bool = False,
        is_async: bool = False,
    ):
        ...
```

#### See also

- [Argument](./argument.md#argument)
- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### Function().body

[Show source in function.py:74](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L74)

Function body as a string.

#### Signature

```python
@property
def body(self) -> str:
    ...
```

### Function().create_request_type_annotation

[Show source in function.py:53](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L53)

Create and set `request_type_annotation` TypedDict based on function arguments.

#### Signature

```python
def create_request_type_annotation(self, name: str) -> None:
    ...
```

### Function().get_required_import_records

[Show source in function.py:91](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L91)

Extract required import records.

#### Signature

```python
def get_required_import_records(self) -> set[ImportRecord]:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### Function().is_kw_only

[Show source in function.py:111](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L111)

Whether method arguments can be passed only as kwargs.

#### Signature

```python
def is_kw_only(self) -> bool:
    ...
```

### Function().iterate_types

[Show source in function.py:81](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L81)

Iterate over required type annotations.

#### Signature

```python
def iterate_types(self) -> Iterator[FakeAnnotation]:
    ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### Function().returns_none

[Show source in function.py:104](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L104)

Whether return type is None.

#### Signature

```python
@property
def returns_none(self) -> bool:
    ...
```

### Function().short_docstring

[Show source in function.py:40](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L40)

Docstring without documentation links.

#### Signature

```python
@property
def short_docstring(self) -> str:
    ...
```

### Function().type_hint_annotations

[Show source in function.py:117](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L117)

Type annotations list from arguments and return type with internal types.

#### Signature

```python
@property
def type_hint_annotations(self) -> list[FakeAnnotation]:
    ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)


