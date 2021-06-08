# Utils

> Auto-generated documentation for [mypy_boto3_builder.writers.utils](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/writers/utils.py) module.

Jinja2 renderer and black formatter.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Writers](index.md#writers) / Utils
    - [blackify](#blackify)
    - [format_md](#format_md)
    - [insert_md_toc](#insert_md_toc)
    - [render_jinja2_template](#render_jinja2_template)
    - [sort_imports](#sort_imports)

## blackify

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/writers/utils.py#L19)

```python
def blackify(content: str, file_path: Path) -> str:
```

Format `content` with `black` if `file_path` is `*.py` or `*.pyi`.

On error writes invalid `content` to `file_path` to check for errors.

#### Arguments

- `content` - Python code to format.
- `file_path` - Target file path.

#### Returns

Formatted python code.

#### Raises

- `ValueError` - If `content` is not a valid Python code.

## format_md

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/writers/utils.py#L123)

```python
def format_md(text: str) -> str:
```

Format MarkDown with mdformat.

## insert_md_toc

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/writers/utils.py#L99)

```python
def insert_md_toc(text: str) -> str:
```

Insert Table of Contents before the first second-level header.

## render_jinja2_template

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/writers/utils.py#L75)

```python
def render_jinja2_template(
    template_path: Path,
    package: Optional[Package] = None,
    service_name: Optional[ServiceName] = None,
) -> str:
```

Render Jinja2 template to a string.

#### Arguments

- `template_path` - Relative path to template in `TEMPLATES_PATH`
- `module` - Module record.
- `service_name` - ServiceName instance.

#### Returns

A rendered template.

## sort_imports

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/writers/utils.py#L50)

```python
def sort_imports(
    content: str,
    module_name: str,
    extension: str = 'py',
    third_party: Iterable[str] = (),
) -> str:
```
