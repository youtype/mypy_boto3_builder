# Helpers

[mypy-boto3-builder Index](../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Parsers](./index.md#parsers) /
Helpers

> Auto-generated documentation for [mypy_boto3_builder.parsers.helpers](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/helpers.py) module.

- [Helpers](#helpers)
  - [get_public_methods](#get_public_methods)
  - [parse_method](#parse_method)

## get_public_methods

[Show source in helpers.py:18](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/helpers.py#L18)

Extract public methods from any class.

#### Arguments

- `inspect_class` - Inspect class.

#### Returns

A dictionary of method name and method.

#### Signature

```python
def get_public_methods(inspect_class: object) -> dict[str, MethodType]:
    ...
```



## parse_method

[Show source in helpers.py:42](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/helpers.py#L42)

Parse method to a structure.

#### Arguments

- `parent_name` - Parent class name.
- `method` - Inspect method.

#### Returns

Method structure.

#### Signature

```python
def parse_method(
    parent_name: str, name: str, method: MethodType, service_name: ServiceName
) -> Method:
    ...
```

#### See also

- [Method](../structures/method.md#method)
- [ServiceName](../service_name.md#servicename)


