# Argument

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](./index.md#structures) / Argument

> Auto-generated documentation for [mypy_boto3_builder.structures.argument](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py) module.

## Argument

[Show source in argument.py:14](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L14)

Method or function argument.

#### Arguments

- `name` - Argument name.
- `type_annotation` - Argument type annotation.
- `value` - Default argument value.
- `prefix` - Used for starargs.

#### Signature

```python
class Argument:
    def __init__(
        self,
        name: str,
        type_annotation: FakeAnnotation | None,
        default: TypeConstant | None = None,
        prefix: Literal["*", "**", ""] = "",
    ) -> None: ...
```

### Argument().__copy__

[Show source in argument.py:82](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L82)

Deep copy argument.

#### Signature

```python
def __copy__(self: Self) -> Self: ...
```

### Argument().copy

[Show source in argument.py:76](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L76)

Deep copy argument.

#### Signature

```python
def copy(self: Self) -> Self: ...
```

### Argument().is_kwflag

[Show source in argument.py:54](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L54)

Whether argument is a `*` keywords separator.

#### Signature

```python
def is_kwflag(self) -> bool: ...
```

### Argument().iterate_types

[Show source in argument.py:60](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L60)

Extract required type annotations.

#### Signature

```python
def iterate_types(self) -> Iterator[FakeAnnotation]: ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### Argument.kwflag

[Show source in argument.py:47](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L47)

Create `*` keywords separator.

#### Signature

```python
@classmethod
def kwflag(cls: type[Self]) -> Self: ...
```

### Argument().render

[Show source in argument.py:37](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L37)

Render argument to a string.

#### Signature

```python
def render(self) -> str: ...
```

### Argument().required

[Show source in argument.py:69](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L69)

Whether argument does not have a default value and is required.

#### Signature

```python
@property
def required(self) -> bool: ...
```
