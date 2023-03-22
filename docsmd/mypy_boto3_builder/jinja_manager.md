# JinjaManager

[Mypy_boto3_builder Index](../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](./index.md#mypy-boto3-builder) /
JinjaManager

> Auto-generated documentation for [mypy_boto3_builder.jinja_manager](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/jinja_manager.py) module.

## JinjaManager

[Show source in jinja_manager.py:14](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/jinja_manager.py#L14)

Jinja2 `Environment` manager.

#### Signature

```python
class JinjaManager:
    ...
```

### JinjaManager.escape_md

[Show source in jinja_manager.py:34](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/jinja_manager.py#L34)

Escape underscore characters.

#### Signature

```python
@staticmethod
def escape_md(value: str) -> str:
    ...
```

### JinjaManager.get_environment

[Show source in jinja_manager.py:41](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/jinja_manager.py#L41)

Get `jinja2.Environment`.

#### Signature

```python
@classmethod
def get_environment(cls) -> jinja2.Environment:
    ...
```

### JinjaManager.update_globals

[Show source in jinja_manager.py:24](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/jinja_manager.py#L24)

Update global variables in `jinja2.Environment`.

#### Arguments

- `kwargs` - Globals to set.

#### Signature

```python
@classmethod
def update_globals(cls, **kwargs: str | bool | Callable[..., Any]) -> None:
    ...
```
