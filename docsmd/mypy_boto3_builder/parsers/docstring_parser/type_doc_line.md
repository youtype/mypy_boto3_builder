# TypeDocLine

[Mypy_boto3_builder Index](../../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../../index.md#mypy-boto3-builder) /
[Parsers](../index.md#parsers) /
[Docstring Parser](./index.md#docstring-parser) /
TypeDocLine

> Auto-generated documentation for [mypy_boto3_builder.parsers.docstring_parser.type_doc_line](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_doc_line.py) module.

## TypeDocLine

[Show source in type_doc_line.py:10](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_doc_line.py#L10)

Structure for parsed as dict `:type:` or `:rtype:` nested lines.

#### Arguments

- `name` - Argument or TypedDict key name
- `type_name` - Argument or TypedDict key type string.
- `line` - Raw original line parts.
- `description` - Rest of line for argument or TypedDict key definition.
- `indented` - Intended lines.

#### Signature

```python
class TypeDocLine:
    def __init__(
        self,
        name: str = "",
        type_name: str = "",
        line: Iterable[str] = tuple(),
        description: str = "",
        indented: Iterable[Mapping[str, object]] = tuple(),
    ) -> None:
        ...
```

### TypeDocLine().indented

[Show source in type_doc_line.py:36](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_doc_line.py#L36)

Get indented lines list.

#### Returns

A list of [TypeDocLine](#typedocline).

#### Signature

```python
@property
def indented(self: _R) -> list[_R]:
    ...
```

### TypeDocLine().render

[Show source in type_doc_line.py:56](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_doc_line.py#L56)

Get original string with indentation.

#### Returns

A string as close as possible to original.

#### Signature

```python
def render(self) -> str:
    ...
```

### TypeDocLine().required

[Show source in type_doc_line.py:49](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_doc_line.py#L49)

Whether the argument or TypedDict key is required.

#### Signature

```python
@property
def required(self) -> bool:
    ...
```



