# JinjaManager

[Mypy_boto3_builder Index](../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](./index.md#mypy-boto3-builder) / JinjaManager

> Auto-generated documentation for [mypy_boto3_builder.jinja_manager](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/jinja_manager.py) module.

## JinjaManager

[Show source in jinja_manager.py:28](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/jinja_manager.py#L28)

Jinja2 `Environment` manager.

#### Signature

```python
class JinjaManager:
    def __init__(self) -> None: ...
```

### JinjaManager.escape_md

[Show source in jinja_manager.py:72](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/jinja_manager.py#L72)

Escape underscore characters.

#### Signature

```python
@staticmethod
def escape_md(value: str) -> str: ...
```

### JinjaManager().get_template

[Show source in jinja_manager.py:79](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/jinja_manager.py#L79)

Get `jinja2.Template`.

#### Signature

```python
def get_template(self, template_path: Path) -> Template: ...
```

### JinjaManager.singleton

[Show source in jinja_manager.py:53](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/jinja_manager.py#L53)

Get singleton instance.

#### Signature

```python
@classmethod
def singleton(cls) -> "JinjaManager": ...
```

### JinjaManager.update_globals

[Show source in jinja_manager.py:62](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/jinja_manager.py#L62)

Update global variables in `jinja2.Environment`.

#### Arguments

- `kwargs` - Globals to set.

#### Signature

```python
@classmethod
def update_globals(cls, **kwargs: str | bool | Callable[..., Any]) -> None: ...
```



## JinjaManagerError

[Show source in jinja_manager.py:22](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/jinja_manager.py#L22)

Base JinjaManager exception.

#### Signature

```python
class JinjaManagerError(Exception): ...
```
