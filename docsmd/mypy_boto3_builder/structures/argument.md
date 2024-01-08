# Argument

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](./index.md#structures) / Argument

> Auto-generated documentation for [mypy_boto3_builder.structures.argument](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py) module.

## Argument

[Show source in argument.py:16](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L16)

Method or function argument.

#### Arguments

- `name` - Argument name.
- `type_annotation` - Argument type annotation.
- `value` - Default argument value.
- `prefix` - Used for starargs.

#### Signature

```python
class Argument: ...
```

### Argument().__copy__

[Show source in argument.py:79](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L79)

Deep copy argument.

#### Signature

```python
def __copy__(self: _R) -> _R: ...
```

### Argument().copy

[Show source in argument.py:73](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L73)

Deep copy argument.

#### Signature

```python
def copy(self: _R) -> _R: ...
```

### Argument().is_kwflag

[Show source in argument.py:51](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L51)

Whether argument is a `*` keywords separator.

#### Signature

```python
def is_kwflag(self) -> bool: ...
```

### Argument().iterate_types

[Show source in argument.py:57](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L57)

Extract required type annotations.

#### Signature

```python
def iterate_types(self) -> Iterator[FakeAnnotation]: ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### Argument.kwflag

[Show source in argument.py:44](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L44)

Create `*` keywords separator.

#### Signature

```python
@classmethod
def kwflag(cls: type[_R]) -> _R: ...
```

### Argument().render

[Show source in argument.py:32](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L32)

Render argument to a string.

#### Signature

```python
def render(self) -> str: ...
```

### Argument().required

[Show source in argument.py:66](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L66)

Whether argument does not have a default value and is required.

#### Signature

```python
@property
def required(self) -> bool: ...
```
