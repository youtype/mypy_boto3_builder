# Markdown

> Auto-generated documentation for [mypy_boto3_builder.utils.markdown](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/markdown.py) module.

Utils for markdown rendering.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Utils](index.md#utils) / Markdown
    - [Header](#header)
        - [Header().anchor](#headeranchor)
        - [Header().render](#headerrender)
    - [TableOfContents](#tableofcontents)
        - [TableOfContents.parse](#tableofcontentsparse)
        - [TableOfContents().render](#tableofcontentsrender)
    - [fix_pypi_headers](#fix_pypi_headers)

## Header

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/markdown.py#L12)

```python
class Header():
    def __init__(title: str, level: int) -> None:
```

Markdown header.

#### Arguments

- `title` - Header title
- `level` - Header level, 1-6

### Header().anchor

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/markdown.py#L25)

```python
@property
def anchor() -> str:
```

Anchor link for title.

### Header().render

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/markdown.py#L32)

```python
def render() -> str:
```

Render menu item to string.

## TableOfContents

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/markdown.py#L40)

```python
class TableOfContents():
    def __init__(headers: Iterable[Header]) -> None:
```

MarkDown Table of Contents.

#### Arguments

- `headers` - List of headers

#### See also

- [Header](#header)

### TableOfContents.parse

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/markdown.py#L51)

```python
@classmethod
def parse(text: str) -> _R:
```

Parse table of Contents for MarkDown text.

#### Arguments

- `text` - MarkDown text.

### TableOfContents().render

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/markdown.py#L74)

```python
def render(max_level: int = 3) -> str:
```

Render ToC to string.

## fix_pypi_headers

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/markdown.py#L86)

```python
def fix_pypi_headers(text: str) -> str:
```

Parse table of Contents for MarkDown text.

#### Arguments

- `text` - MarkDown text.
