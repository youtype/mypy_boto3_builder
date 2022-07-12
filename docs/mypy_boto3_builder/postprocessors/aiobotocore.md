# Aiobotocore

> Auto-generated documentation for [mypy_boto3_builder.postprocessors.aiobotocore](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/postprocessors/aiobotocore.py) module.

Postprocessor for aiobotocore classes and methods.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Postprocessors](index.md#postprocessors) / Aiobotocore
    - [AioBotocorePostprocessor](#aiobotocorepostprocessor)
        - [AioBotocorePostprocessor().process_package](#aiobotocorepostprocessorprocess_package)

## AioBotocorePostprocessor

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/postprocessors/aiobotocore.py#L18)

```python
class AioBotocorePostprocessor(BasePostprocessor):
```

Postprocessor for aiobotocore classes and methods.

#### See also

- [BasePostprocessor](base.md#basepostprocessor)

### AioBotocorePostprocessor().process_package

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/postprocessors/aiobotocore.py#L44)

```python
def process_package() -> None:
```

Convert all methods to asynchronous.
