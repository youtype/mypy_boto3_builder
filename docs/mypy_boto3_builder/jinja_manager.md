# JinjaManager

[mypy-boto3-builder Index](../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](./index.md#mypy-boto3-builder) /
JinjaManager

> Auto-generated documentation for [mypy_boto3_builder.jinja_manager](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/jinja_manager.py) module.

- [JinjaManager](#jinjamanager)
  - [JinjaManager](#jinjamanager-1)
    - [JinjaManager.escape_md](#jinjamanagerescape_md)
    - [JinjaManager.get_environment](#jinjamanagerget_environment)
    - [JinjaManager.update_globals](#jinjamanagerupdate_globals)

## JinjaManager

[Show source in jinja_manager.py:11](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/jinja_manager.py#L11)

Jinja2 `Environment` manager.

#### Signature

```python
class JinjaManager:
    ...
```

### JinjaManager.escape_md

[Show source in jinja_manager.py:31](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/jinja_manager.py#L31)

Escape underscore characters.

#### Signature

```python
@staticmethod
def escape_md(value: str) -> str:
    ...
```

### JinjaManager.get_environment

[Show source in jinja_manager.py:38](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/jinja_manager.py#L38)

Get `jinja2.Environment`.

#### Signature

```python
@classmethod
def get_environment(cls) -> jinja2.Environment:
    ...
```

### JinjaManager.update_globals

[Show source in jinja_manager.py:21](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/jinja_manager.py#L21)

Update global variables in `jinja2.Environment`.

#### Arguments

- `kwargs` - Globals to set.

#### Signature

```python
@classmethod
def update_globals(cls, **kwargs: object) -> None:
    ...
```


