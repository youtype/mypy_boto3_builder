# Utils

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Writers](./index.md#writers) /
Utils

> Auto-generated documentation for [mypy_boto3_builder.writers.utils](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/utils.py) module.

## blackify

[Show source in utils.py:25](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/utils.py#L25)

Format `content` with `black` if `file_path` is `*.py` or `*.pyi`.

On error writes invalid `content` to `file_path` to check for errors.

#### Arguments

- `content` - Python code to format.
- `file_path` - Target file path.

#### Returns

Formatted python code.

#### Raises

- `ValueError` - If `content` is not a valid Python code.

#### Signature

```python
def blackify(content: str, file_path: Path) -> str: ...
```



## blackify_markdown

[Show source in utils.py:163](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/utils.py#L163)

Blackify python codeblocks.

#### Signature

```python
def blackify_markdown(text: str) -> str: ...
```



## format_md

[Show source in utils.py:150](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/utils.py#L150)

Format MarkDown with mdformat.

#### Signature

```python
def format_md(text: str) -> str: ...
```



## insert_md_toc

[Show source in utils.py:126](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/utils.py#L126)

Insert Table of Contents before the first second-level header.

#### Signature

```python
def insert_md_toc(text: str) -> str: ...
```



## render_jinja2_package_template

[Show source in utils.py:108](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/utils.py#L108)

Render Jinja2 package template to a string.

#### Arguments

- `template_path` - Relative path to template in `TEMPLATES_PATH`
- `package` - Service or wrapper package

#### Returns

A rendered template.

#### Signature

```python
def render_jinja2_package_template(template_path: Path, package: Package) -> str: ...
```

#### See also

- [Package](../structures/package.md#package)



## sort_imports

[Show source in utils.py:67](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/utils.py#L67)

Sort imports with `isort`.

#### Arguments

- `content` - File content.
- `module_name` - Current module name.
- `extension` - py or pyi
- `third_party` - List of module names to be marked as third-party.

#### Returns

New file content.

#### Signature

```python
def sort_imports(
    content: str,
    module_name: str,
    extension: Literal["py", "pyi"] = "py",
    third_party: Iterable[str] = (),
) -> str: ...
```
