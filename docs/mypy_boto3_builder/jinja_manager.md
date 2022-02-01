# JinjaManager

> Auto-generated documentation for [mypy_boto3_builder.jinja_manager](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/jinja_manager.py) module.

Jinja2 `Environment` manager.

- [mypy-boto3-builder](../README.md#mypy_boto3_builder) / [Modules](../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / JinjaManager
    - [JinjaManager](#jinjamanager)
        - [JinjaManager.get_environment](#jinjamanagerget_environment)
        - [JinjaManager.update_globals](#jinjamanagerupdate_globals)

## JinjaManager

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/jinja_manager.py#L11)

```python
class JinjaManager():
```

Jinja2 `Environment` manager.

### JinjaManager.get_environment

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/jinja_manager.py#L31)

```python
@classmethod
def get_environment() -> jinja2.Environment:
```

Get `jinja2.Environment`.

### JinjaManager.update_globals

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/jinja_manager.py#L21)

```python
@classmethod
def update_globals(**kwargs: object) -> None:
```

Update global variables in `jinja2.Environment`.

#### Arguments

- `kwargs` - Globals to set.
