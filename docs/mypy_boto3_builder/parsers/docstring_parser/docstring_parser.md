# DocstringParser

> Auto-generated documentation for [mypy_boto3_builder.parsers.docstring_parser.docstring_parser](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/docstring_parser/docstring_parser.py) module.

Botocore docstring parser.

- [mypy-boto3-builder](../../../README.md#mypy_boto3_builder) / [Modules](../../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../../index.md#mypy-boto3-builder) / [Parsers](../index.md#parsers) / [Docstring Parser](index.md#docstring-parser) / DocstringParser
    - [DocstringParser](#docstringparser)
        - [DocstringParser().get_arguments](#docstringparserget_arguments)
        - [DocstringParser().get_return_type](#docstringparserget_return_type)

## DocstringParser

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/docstring_parser/docstring_parser.py#L27)

```python
class DocstringParser():
    def __init__(
        service_name: ServiceName,
        class_name: str,
        method_name: str,
        arguments: List[Argument],
    ) -> None:
```

Botocore docstring parser.

#### Arguments

- `prefix` - Prefix for generated TypeDict names.
- `class_name` - Parent class name.
- `method_name` - Method name.
- `arguments` - List of arguments extracted from argspec.

#### See also

- [ServiceName](../../service_name.md#servicename)

### DocstringParser().get_arguments

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/docstring_parser/docstring_parser.py#L196)

```python
def get_arguments(input_string: str) -> List[Argument]:
```

Get list of function arguments with type annottions.

#### Arguments

- `input_string` - Function docstring.

#### Returns

A list of `Argument` structures.

### DocstringParser().get_return_type

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/docstring_parser/docstring_parser.py#L312)

```python
def get_return_type(input_string: str) -> FakeAnnotation:
```

Get function return type annotation.

#### Arguments

- `input_string` - Function docstring.

#### Returns

A valid type annotation.

#### See also

- [FakeAnnotation](../../type_annotations/fake_annotation.md#fakeannotation)
