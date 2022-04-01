# Method

> Auto-generated documentation for [mypy_boto3_builder.structures.method](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/method.py) module.

Class method.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / Method
    - [Method](#method)
        - [Method().call_arguments](#methodcall_arguments)

## Method

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/method.py#L8)

```python
class Method(Function):
```

Class method.

#### See also

- [Function](function.md#function)

### Method().call_arguments

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/method.py#L13)

```python
@property
def call_arguments() -> list[Argument]:
```

Arguments that are used in method call.

#### See also

- [Argument](argument.md#argument)
