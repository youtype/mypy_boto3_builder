# Jinja2

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Utils](./index.md#utils) /
Jinja2

> Auto-generated documentation for [mypy_boto3_builder.utils.jinja2](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/jinja2.py) module.

## render_jinja2_template

[Show source in jinja2.py:11](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/jinja2.py#L11)

Render Jinja2 template to a string.

#### Arguments

- `template_path` - Relative path to template in `TEMPLATES_PATH`
- `kwargs` - Render arguments

#### Returns

A rendered template.

#### Signature

```python
def render_jinja2_template(template_path: Path, **kwargs: Any) -> str: ...
```
