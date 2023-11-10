# Function

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Structures](./index.md#structures) /
Function

> Auto-generated documentation for [mypy_boto3_builder.structures.function](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py) module.

## Function

[Show source in function.py:19](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L19)

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

### Function().__copy__

[Show source in function.py:145](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L145)

Deep copy function.

#### Signature

```python
def __copy__(self: _R) -> _R: ...
```

### Function().body

[Show source in function.py:86](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L86)

Function body as a string.

#### Signature

```python
@property
def body(self) -> str: ...
```

### Function().copy

[Show source in function.py:139](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L139)

Deep copy function.

#### Signature

```python
def copy(self: _R) -> _R: ...
```

### Function().create_request_type_annotation

[Show source in function.py:65](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L65)

Create and set `request_type_annotation` TypedDict based on function arguments.

#### Signature

```python
def create_request_type_annotation(self, name: str) -> None: ...
```

### Function().get_required_import_records

[Show source in function.py:103](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L103)

Extract required import records.

#### Signature

```python
def get_required_import_records(self) -> set[ImportRecord]: ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### Function().is_kw_only

[Show source in function.py:120](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L120)

Whether method arguments can be passed only as kwargs.

#### Signature

```python
def is_kw_only(self) -> bool: ...
```

### Function().iterate_types

[Show source in function.py:93](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L93)

Iterate over required type annotations.

#### Signature

```python
def iterate_types(self) -> Iterator[FakeAnnotation]: ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### Function().remove_argument

[Show source in function.py:160](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L160)

Remove argument by name.

#### Signature

```python
def remove_argument(self, *names: str) -> Self: ...
```

### Function().returns_none

[Show source in function.py:113](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L113)

Whether return type is None.

#### Signature

```python
@property
def returns_none(self) -> bool: ...
```

### Function().short_docstring

[Show source in function.py:52](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L52)

Docstring without documentation links.

#### Signature

```python
@property
def short_docstring(self) -> str: ...
```

### Function().type_hint_annotations

[Show source in function.py:126](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L126)

Type annotations list from arguments and return type with internal types.

#### Signature

```python
@property
def type_hint_annotations(self) -> list[FakeAnnotation]: ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)
