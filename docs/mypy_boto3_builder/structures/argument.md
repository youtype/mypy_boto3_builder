# Argument

> Auto-generated documentation for [mypy_boto3_builder.structures.argument](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py) module.

Method or function argument.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / Argument
    - [Argument](#argument)
        - [Argument().get_types](#argumentget_types)
        - [Argument().is_kwflag](#argumentis_kwflag)
        - [Argument.kwflag](#argumentkwflag)
        - [Argument().render](#argumentrender)
        - [Argument().required](#argumentrequired)

## Argument

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L12)

```python
class Argument():
    def __init__(
        name: str,
        type_annotation: FakeAnnotation | None,
        default: TypeConstant | None = None,
        prefix: str = '',
    ):
```

Method or function argument.

#### Arguments

- `name` - Argument name.
- `type_annotation` - Argument type annotation.
- `value` - Default argument value.
- `prefix` - Used for starargs.

### Argument().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L57)

```python
def get_types() -> set[FakeAnnotation]:
```

Extract required type annotations.

### Argument().is_kwflag

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L51)

```python
def is_kwflag() -> bool:
```

Whether argument is a `*` keywords separator.

### Argument.kwflag

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L44)

```python
@classmethod
def kwflag() -> _R:
```

Create `*` keywords separator.

### Argument().render

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L35)

```python
def render() -> str:
```

Render argument to a string.

### Argument().required

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/argument.py#L69)

```python
@property
def required() -> bool:
```

Whether argument does not have a default value and is required.
