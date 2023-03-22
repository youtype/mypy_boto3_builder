# Argument

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Structures](./index.md#structures) /
Argument

> Auto-generated documentation for [mypy_boto3_builder.structures.argument](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py) module.

## Argument

[Show source in argument.py:13](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L13)

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
    ):
        ...
```

### Argument().copy

[Show source in argument.py:77](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L77)

Deep copy argument.

#### Signature

```python
def copy(self: _R) -> _R:
    ...
```

### Argument().is_kwflag

[Show source in argument.py:55](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L55)

Whether argument is a `*` keywords separator.

#### Signature

```python
def is_kwflag(self) -> bool:
    ...
```

### Argument().iterate_types

[Show source in argument.py:61](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L61)

Extract required type annotations.

#### Signature

```python
def iterate_types(self) -> Iterator[FakeAnnotation]:
    ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### Argument.kwflag

[Show source in argument.py:48](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L48)

Create `*` keywords separator.

#### Signature

```python
@classmethod
def kwflag(cls: type[_R]) -> _R:
    ...
```

### Argument().render

[Show source in argument.py:36](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L36)

Render argument to a string.

#### Signature

```python
def render(self) -> str:
    ...
```

### Argument().required

[Show source in argument.py:70](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L70)

Whether argument does not have a default value and is required.

#### Signature

```python
@property
def required(self) -> bool:
    ...
```
