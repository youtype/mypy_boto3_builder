# AioBoto3Generator

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Generators](./index.md#generators) /
AioBoto3Generator

> Auto-generated documentation for [mypy_boto3_builder.generators.aioboto3_generator](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/aioboto3_generator.py) module.

## AioBoto3Generator

[Show source in aioboto3_generator.py:17](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/aioboto3_generator.py#L17)

AioBoto3 stubs generator.

#### Signature

```python
class AioBoto3Generator(BaseGenerator):
    ...
```

#### See also

- [BaseGenerator](./base_generator.md#basegenerator)

### AioBoto3Generator().generate_docs

[Show source in aioboto3_generator.py:74](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/aioboto3_generator.py#L74)

Generate service and master docs.

#### Signature

```python
def generate_docs(self) -> None:
    ...
```

### AioBoto3Generator().generate_service_stubs

[Show source in aioboto3_generator.py:98](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/aioboto3_generator.py#L98)

Do nothing.

#### Signature

```python
def generate_service_stubs(self) -> None:
    ...
```

### AioBoto3Generator().generate_stubs

[Show source in aioboto3_generator.py:37](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/aioboto3_generator.py#L37)

Generate `types-aioboto3` package.

#### Signature

```python
def generate_stubs(self) -> None:
    ...
```

### AioBoto3Generator().get_library_version

[Show source in aioboto3_generator.py:25](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/aioboto3_generator.py#L25)

Get underlying library version.

#### Signature

```python
def get_library_version(self) -> str:
    ...
```

### AioBoto3Generator().get_postprocessor

[Show source in aioboto3_generator.py:31](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/aioboto3_generator.py#L31)

Get postprocessor for service package.

#### Signature

```python
def get_postprocessor(self, service_package: ServicePackage) -> AioBotocorePostprocessor:
    ...
```

#### See also

- [AioBotocorePostprocessor](../postprocessors/aiobotocore.md#aiobotocorepostprocessor)
- [ServicePackage](../structures/service_package.md#servicepackage)



