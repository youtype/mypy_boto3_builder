# Helpers

> Auto-generated documentation for [mypy_boto3_builder.parsers.helpers](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/helpers.py) module.

Helpers for parsing methods and attributes.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / Helpers
    - [get_public_methods](#get_public_methods)
    - [parse_method](#parse_method)

## get_public_methods

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/helpers.py#L18)

```python
def get_public_methods(inspect_class: object) -> dict[(str, MethodType)]:
```

Extract public methods from any class.

#### Arguments

- `inspect_class` - Inspect class.

#### Returns

A dictionary of method name and method.

## parse_method

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/helpers.py#L42)

```python
def parse_method(
    parent_name: str,
    name: str,
    method: MethodType,
    service_name: ServiceName,
) -> Method:
```

Parse method to a structure.

#### Arguments

- `parent_name` - Parent class name.
- `method` - Inspect method.

#### Returns

Method structure.

#### See also

- [Method](../structures/method.md#method)
- [ServiceName](../service_name.md#servicename)
