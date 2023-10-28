# Function

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Structures](./index.md#structures) /
Function

> Auto-generated documentation for [mypy_boto3_builder.structures.function](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py) module.

## Function

[Show source in function.py:17](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L17)

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
        decorators: Iterable[FakeAnnotation] = (),
        body_lines: Iterable[str] = (),
        type_ignore: bool = False,
        is_async: bool = False,
    ): ...
```

#### See also

- [Argument](./argument.md#argument)
- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### Function().body

[Show source in function.py:84](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L84)

Function body as a string.

#### Signature

```python
@property
def body(self) -> str: ...
```

### Function().copy

[Show source in function.py:137](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L137)

Deep copy function.

#### Signature

```python
def copy(self: _R) -> _R: ...
```

### Function().create_request_type_annotation

[Show source in function.py:63](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L63)

Create and set `request_type_annotation` TypedDict based on function arguments.

#### Signature

```python
def create_request_type_annotation(self, name: str) -> None: ...
```

### Function().get_required_import_records

[Show source in function.py:101](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L101)

Extract required import records.

#### Signature

```python
def get_required_import_records(self) -> set[ImportRecord]: ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### Function().is_kw_only

[Show source in function.py:118](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L118)

Whether method arguments can be passed only as kwargs.

#### Signature

```python
def is_kw_only(self) -> bool: ...
```

### Function().iterate_types

[Show source in function.py:91](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L91)

Iterate over required type annotations.

#### Signature

```python
def iterate_types(self) -> Iterator[FakeAnnotation]: ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### Function().remove_argument

[Show source in function.py:152](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L152)

Remove argument by name.

#### Signature

```python
def remove_argument(self: _R, *names: str) -> _R: ...
```

### Function().returns_none

[Show source in function.py:111](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L111)

Whether return type is None.

#### Signature

```python
@property
def returns_none(self) -> bool: ...
```

### Function().short_docstring

[Show source in function.py:50](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L50)

Docstring without documentation links.

#### Signature

```python
@property
def short_docstring(self) -> str: ...
```

### Function().type_hint_annotations

[Show source in function.py:124](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L124)

Type annotations list from arguments and return type with internal types.

#### Signature

```python
@property
def type_hint_annotations(self) -> list[FakeAnnotation]: ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)
