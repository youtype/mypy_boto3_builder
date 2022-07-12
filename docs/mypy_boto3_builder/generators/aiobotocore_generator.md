# AioBotocoreGenerator

> Auto-generated documentation for [mypy_boto3_builder.generators.aiobotocore_generator](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/aiobotocore_generator.py) module.

AIOBotocore stubs/docs generator.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Generators](index.md#generators) / AioBotocoreGenerator
    - [AioBotocoreGenerator](#aiobotocoregenerator)
        - [AioBotocoreGenerator().generate_docs](#aiobotocoregeneratorgenerate_docs)
        - [AioBotocoreGenerator().generate_stubs](#aiobotocoregeneratorgenerate_stubs)
        - [AioBotocoreGenerator().get_library_version](#aiobotocoregeneratorget_library_version)
        - [AioBotocoreGenerator().get_postprocessor](#aiobotocoregeneratorget_postprocessor)

## AioBotocoreGenerator

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/aiobotocore_generator.py#L20)

```python
class AioBotocoreGenerator(BaseGenerator):
```

AioBotocore stubs/docs generator.

#### See also

- [BaseGenerator](base_generator.md#basegenerator)

### AioBotocoreGenerator().generate_docs

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/aiobotocore_generator.py#L77)

```python
def generate_docs() -> None:
```

Generate service and master docs.

### AioBotocoreGenerator().generate_stubs

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/aiobotocore_generator.py#L40)

```python
def generate_stubs() -> None:
```

Generate `aiobotocore-stubs` package.

### AioBotocoreGenerator().get_library_version

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/aiobotocore_generator.py#L28)

```python
def get_library_version() -> str:
```

Get underlying library version.

### AioBotocoreGenerator().get_postprocessor

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/aiobotocore_generator.py#L34)

```python
def get_postprocessor(
    service_package: ServicePackage,
) -> AioBotocorePostprocessor:
```

Get postprocessor for service package.

#### See also

- [AioBotocorePostprocessor](../postprocessors/aiobotocore.md#aiobotocorepostprocessor)
- [ServicePackage](../structures/service_package.md#servicepackage)
