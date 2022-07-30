# Aiobotocore

[mypy-boto3-builder Index](../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Postprocessors](./index.md#postprocessors) /
Aiobotocore

> Auto-generated documentation for [mypy_boto3_builder.postprocessors.aiobotocore](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/postprocessors/aiobotocore.py) module.

- [Aiobotocore](#aiobotocore)
  - [AioBotocorePostprocessor](#aiobotocorepostprocessor)
    - [AioBotocorePostprocessor().process_package](#aiobotocorepostprocessor()process_package)

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

[Show source in aiobotocore.py:65](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/postprocessors/aiobotocore.py#L65)

Convert all methods to asynchronous.

#### Signature

```python
def process_package(self) -> None:
    ...
```


