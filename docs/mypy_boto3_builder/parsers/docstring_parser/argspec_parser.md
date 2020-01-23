# ArgSpecParser

> Auto-generated documentation for [mypy_boto3_builder.parsers.docstring_parser.argspec_parser](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/docstring_parser/argspec_parser.py) module.

Converter of function argspec to `Argument` list.

- [mypy-boto3-builder](../../../README.md#mypy_boto3_builder) / [Modules](../../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../../index.md#mypy-boto3-builder) / [Parsers](../index.md#parsers) / [Docstring Parser](index.md#docstring-parser) / ArgSpecParser
    - [ArgSpecParser](#argspecparser)
        - [ArgSpecParser().get_arguments](#argspecparserget_arguments)
        - [ArgSpecParser().get_return_type](#argspecparserget_return_type)

## ArgSpecParser

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/docstring_parser/argspec_parser.py#L18)

```python
class ArgSpecParser():
    def __init__(prefix: str, service_name: ServiceName) -> None:
```

Converter of function argspec to `Argument` list.

#### See also

- [ServiceName](../../service_name.md#servicename)

### ArgSpecParser().get_arguments

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/docstring_parser/argspec_parser.py#L58)

```python
def get_arguments(
    class_name: str,
    method_name: str,
    func: FunctionType,
) -> List[Argument]:
```

### ArgSpecParser().get_return_type

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/docstring_parser/argspec_parser.py#L75)

```python
def get_return_type(
    class_name: str,
    method_name: str,
) -> Optional[FakeAnnotation]:
```
