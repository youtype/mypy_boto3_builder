# Aiobotocore

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Postprocessors](./index.md#postprocessors) /
Aiobotocore

> Auto-generated documentation for [mypy_boto3_builder.postprocessors.aiobotocore](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/postprocessors/aiobotocore.py) module.

## AioBotocorePostprocessor

[Show source in aiobotocore.py:18](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/postprocessors/aiobotocore.py#L18)

Postprocessor for aiobotocore classes and methods.

#### Signature

```python
class AioBotocorePostprocessor(BasePostprocessor):
    ...
```

#### See also

- [BasePostprocessor](./base.md#basepostprocessor)

### AioBotocorePostprocessor().process_package

[Show source in aiobotocore.py:68](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/postprocessors/aiobotocore.py#L68)

Convert all methods to asynchronous.

#### Signature

```python
def process_package(self) -> None:
    ...
```



