# Function

> Auto-generated documentation for [mypy_boto3_builder.structures.function](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/function.py) module.

Module-level function.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / Function
    - [Function](#function)
        - [Function().body](#functionbody)
        - [Function().get_required_import_records](#functionget_required_import_records)
        - [Function().get_types](#functionget_types)

## Function

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/function.py#L12)

```python
dataclass
class Function():
```

Module-level function.

### Function().body

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/function.py#L25)

```python
@property
def body() -> str:
```

### Function().get_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/function.py#L38)

```python
def get_required_import_records() -> Set[ImportRecord]:
```

### Function().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/function.py#L29)

```python
def get_types() -> Set[FakeAnnotation]:
```
