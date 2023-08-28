# JinjaManager

[Mypy_boto3_builder Index](../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](./index.md#mypy-boto3-builder) /
JinjaManager

> Auto-generated documentation for [mypy_boto3_builder.jinja_manager](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/jinja_manager.py) module.

## JinjaManager

[Show source in jinja_manager.py:17](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/jinja_manager.py#L17)

Jinja2 `Environment` manager.

#### Signature

```python
class JinjaManager:
    def __init__(self) -> None:
        ...
```

### JinjaManager.escape_md

[Show source in jinja_manager.py:50](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/jinja_manager.py#L50)

Escape underscore characters.

#### Signature

```python
@staticmethod
def escape_md(value: str) -> str:
    ...
```

### JinjaManager().get_environment

[Show source in jinja_manager.py:57](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/jinja_manager.py#L57)

Get `jinja2.Environment`.

#### Signature

```python
def get_environment(self) -> jinja2.Environment:
    ...
```

### JinjaManager.update_globals

[Show source in jinja_manager.py:40](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/jinja_manager.py#L40)

Update global variables in `jinja2.Environment`.

#### Arguments

- `kwargs` - Globals to set.

#### Signature

```python
@classmethod
def update_globals(cls, **kwargs: str | bool | Callable[..., Any]) -> None:
    ...
```
