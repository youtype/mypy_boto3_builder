# Function

> Auto-generated documentation for [mypy_boto3_builder.structures.function](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/function.py) module.

Module-level function.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / Function
    - [Function](#function)
        - [Function().body](#functionbody)
        - [Function().get_required_import_records](#functionget_required_import_records)
        - [Function().get_types](#functionget_types)
        - [Function().is_kw_only](#functionis_kw_only)
        - [Function().returns_none](#functionreturns_none)

## Function

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/function.py#L12)

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
    ):
```

Module-level function.

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### Function().body

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/function.py#L35)

```python
@property
def body() -> str:
```

Function body as a string.

### Function().get_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/function.py#L54)

```python
def get_required_import_records() -> Set[ImportRecord]:
```

Extract required import records.

### Function().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/function.py#L42)

```python
def get_types() -> Set[FakeAnnotation]:
```

Extract required type annotations.

### Function().is_kw_only

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/function.py#L74)

```python
def is_kw_only() -> bool:
```

Whether method arguments can be passed only as kwargs.

### Function().returns_none

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/function.py#L67)

```python
@property
def returns_none() -> bool:
```

Whether return type is None
