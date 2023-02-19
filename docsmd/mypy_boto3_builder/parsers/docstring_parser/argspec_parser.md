# ArgSpecParser

[Mypy_boto3_builder Index](../../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../../index.md#mypy-boto3-builder) /
[Parsers](../index.md#parsers) /
[Docstring Parser](./index.md#docstring-parser) /
ArgSpecParser

> Auto-generated documentation for [mypy_boto3_builder.parsers.docstring_parser.argspec_parser](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/argspec_parser.py) module.

## ArgSpecParser

[Show source in argspec_parser.py:16](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/argspec_parser.py#L16)

Converter of function argspec to `Argument` list.

#### Signature

```python
class ArgSpecParser:
    def __init__(self, prefix: str, service_name: ServiceName) -> None:
        ...
```

#### See also

- [ServiceName](../../service_name.md#servicename)

### ArgSpecParser().get_arguments

[Show source in argspec_parser.py:59](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/argspec_parser.py#L59)

Get arguments from `class_name.method_name` method `func`.

#### Signature

```python
def get_arguments(
    self, class_name: str, method_name: str, func: MethodType
) -> list[Argument]:
    ...
```

#### See also

- [Argument](../../structures/argument.md#argument)

### ArgSpecParser().get_return_type

[Show source in argspec_parser.py:77](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/argspec_parser.py#L77)

Get `class_name.method_name` return type annotation.

#### Signature

```python
def get_return_type(self, class_name: str, method_name: str) -> FakeAnnotation | None:
    ...
```
