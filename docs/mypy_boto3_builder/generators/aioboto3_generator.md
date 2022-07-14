# AioBoto3Generator

> Auto-generated documentation for [mypy_boto3_builder.generators.aioboto3_generator](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/aioboto3_generator.py) module.

AioBoto3 stubs generator.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Generators](index.md#generators) / AioBoto3Generator
    - [AioBoto3Generator](#aioboto3generator)
        - [AioBoto3Generator().generate_docs](#aioboto3generatorgenerate_docs)
        - [AioBoto3Generator().generate_service_stubs](#aioboto3generatorgenerate_service_stubs)
        - [AioBoto3Generator().generate_stubs](#aioboto3generatorgenerate_stubs)
        - [AioBoto3Generator().get_library_version](#aioboto3generatorget_library_version)
        - [AioBoto3Generator().get_postprocessor](#aioboto3generatorget_postprocessor)

## AioBoto3Generator

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/aioboto3_generator.py#L16)

```python
class AioBoto3Generator(BaseGenerator):
```

AioBoto3 stubs generator.

#### See also

- [BaseGenerator](base_generator.md#basegenerator)

### AioBoto3Generator().generate_docs

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/aioboto3_generator.py#L73)

```python
def generate_docs() -> None:
```

Do nothing.

### AioBoto3Generator().generate_service_stubs

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/aioboto3_generator.py#L78)

```python
def generate_service_stubs() -> None:
```

Do nothing.

### AioBoto3Generator().generate_stubs

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/aioboto3_generator.py#L36)

```python
def generate_stubs() -> None:
```

Generate `types-aioboto3` package.

### AioBoto3Generator().get_library_version

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/aioboto3_generator.py#L24)

```python
def get_library_version() -> str:
```

Get underlying library version.

### AioBoto3Generator().get_postprocessor

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/aioboto3_generator.py#L30)

```python
def get_postprocessor(
    service_package: ServicePackage,
) -> AioBotocorePostprocessor:
```

Get postprocessor for service package.

#### See also

- [AioBotocorePostprocessor](../postprocessors/aiobotocore.md#aiobotocorepostprocessor)
- [ServicePackage](../structures/service_package.md#servicepackage)
