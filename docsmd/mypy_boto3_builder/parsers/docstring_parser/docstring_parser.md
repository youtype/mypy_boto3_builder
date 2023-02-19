# DocstringParser

[Mypy_boto3_builder Index](../../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../../index.md#mypy-boto3-builder) /
[Parsers](../index.md#parsers) /
[Docstring Parser](./index.md#docstring-parser) /
DocstringParser

> Auto-generated documentation for [mypy_boto3_builder.parsers.docstring_parser.docstring_parser](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/docstring_parser.py) module.

## DocstringParser

[Show source in docstring_parser.py:26](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/docstring_parser.py#L26)

Botocore docstring parser.

#### Arguments

- `prefix` - Prefix for generated TypeDict names.
- `class_name` - Parent class name.
- `method_name` - Method name.
- `arguments` - List of arguments extracted from argspec.

#### Signature

```python
class DocstringParser:
    def __init__(
        self,
        service_name: ServiceName,
        class_name: str,
        method_name: str,
        arguments: list[Argument],
    ) -> None:
        ...
```

#### See also

- [Argument](../../structures/argument.md#argument)
- [ServiceName](../../service_name.md#servicename)

### DocstringParser().get_arguments

[Show source in docstring_parser.py:191](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/docstring_parser.py#L191)

Get list of function arguments with type annottions.

#### Arguments

- `input_string` - Function docstring.

#### Returns

A list of `Argument` structures.

#### Signature

```python
def get_arguments(self, input_string: str) -> list[Argument]:
    ...
```

#### See also

- [Argument](../../structures/argument.md#argument)

### DocstringParser().get_return_type

[Show source in docstring_parser.py:298](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/docstring_parser.py#L298)

Get function return type annotation.

#### Arguments

- `input_string` - Function docstring.

#### Returns

A valid type annotation.

#### Signature

```python
def get_return_type(self, input_string: str) -> FakeAnnotation:
    ...
```

#### See also

- [FakeAnnotation](../../type_annotations/fake_annotation.md#fakeannotation)
