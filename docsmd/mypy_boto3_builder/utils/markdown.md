# Markdown

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Utils](./index.md#utils) /
Markdown

> Auto-generated documentation for [mypy_boto3_builder.utils.markdown](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/markdown.py) module.

## Header

[Show source in markdown.py:12](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/markdown.py#L12)

Markdown header.

#### Arguments

- `title` - Header title
- `level` - Header level, 1-6

#### Signature

```python
class Header:
    def __init__(self, title: str, level: int) -> None:
        ...
```

### Header().anchor

[Show source in markdown.py:25](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/markdown.py#L25)

Anchor link for title.

#### Signature

```python
@property
def anchor(self) -> str:
    ...
```

### Header().render

[Show source in markdown.py:32](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/markdown.py#L32)

Render menu item to string.

#### Signature

```python
def render(self) -> str:
    ...
```



## TableOfContents

[Show source in markdown.py:40](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/markdown.py#L40)

MarkDown Table of Contents.

#### Arguments

- `headers` - List of headers

#### Signature

```python
class TableOfContents:
    def __init__(self, headers: Iterable[Header]) -> None:
        ...
```

#### See also

- [Header](#header)

### TableOfContents.parse

[Show source in markdown.py:51](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/markdown.py#L51)

Parse table of Contents for MarkDown text.

#### Arguments

- `text` - MarkDown text.

#### Signature

```python
@classmethod
def parse(cls: type[_R], text: str) -> _R:
    ...
```

### TableOfContents().render

[Show source in markdown.py:74](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/markdown.py#L74)

Render ToC to string.

#### Signature

```python
def render(self, max_level: int = 3) -> str:
    ...
```



## fix_pypi_headers

[Show source in markdown.py:86](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/markdown.py#L86)

Parse table of Contents for MarkDown text.

#### Arguments

- `text` - MarkDown text.

#### Signature

```python
def fix_pypi_headers(text: str) -> str:
    ...
```



