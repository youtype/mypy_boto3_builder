# AioBotocoreGenerator

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Generators](./index.md#generators) / AioBotocoreGenerator

> Auto-generated documentation for [mypy_boto3_builder.generators.aiobotocore_generator](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/aiobotocore_generator.py) module.

## AioBotocoreGenerator

[Show source in aiobotocore_generator.py:21](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/aiobotocore_generator.py#L21)

AioBotocore stubs/docs generator.

#### Signature

```python
class AioBotocoreGenerator(BaseGenerator): ...
```

#### See also

- [BaseGenerator](./base_generator.md#basegenerator)

### AioBotocoreGenerator().generate_docs

[Show source in aiobotocore_generator.py:78](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/aiobotocore_generator.py#L78)

Generate service and master docs.

#### Signature

```python
def generate_docs(self) -> None: ...
```

### AioBotocoreGenerator().generate_stubs

[Show source in aiobotocore_generator.py:41](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/aiobotocore_generator.py#L41)

Generate `aiobotocore-stubs` package.

#### Signature

```python
def generate_stubs(self) -> None: ...
```

### AioBotocoreGenerator().get_library_version

[Show source in aiobotocore_generator.py:29](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/aiobotocore_generator.py#L29)

Get underlying library version.

#### Signature

```python
def get_library_version(self) -> str: ...
```

### AioBotocoreGenerator().get_postprocessor

[Show source in aiobotocore_generator.py:35](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/aiobotocore_generator.py#L35)

Get postprocessor for service package.

#### Signature

```python
def get_postprocessor(
    self, service_package: ServicePackage
) -> AioBotocorePostprocessor: ...
```

#### See also

- [AioBotocorePostprocessor](../postprocessors/aiobotocore.md#aiobotocorepostprocessor)
- [ServicePackage](../structures/service_package.md#servicepackage)
