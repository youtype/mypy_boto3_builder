# Helpers

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](./index.md#parsers) / Helpers

> Auto-generated documentation for [mypy_boto3_builder.parsers.helpers](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/helpers.py) module.

## get_dummy_method

[Show source in helpers.py:37](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/helpers.py#L37)

Get a dummy method in case we cannot parse it.

#### Arguments

- `name` - Method name.

#### Returns

Method structure.

#### Signature

```python
def get_dummy_method(name: str) -> Method: ...
```

#### See also

- [Method](../structures/method.md#method)



## get_public_methods

[Show source in helpers.py:13](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/helpers.py#L13)

Extract public methods from any class.

#### Arguments

- `inspect_class` - Inspect class.

#### Returns

A dictionary of method name and method.

#### Signature

```python
def get_public_methods(inspect_class: object) -> dict[str, MethodType]: ...
```
