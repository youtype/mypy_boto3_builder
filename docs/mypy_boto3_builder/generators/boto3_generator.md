# Boto3Generator

[mypy-boto3-builder Index](../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Generators](./index.md#generators) /
Boto3Generator

> Auto-generated documentation for [mypy_boto3_builder.generators.boto3_generator](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/boto3_generator.py) module.

- [Boto3Generator](#boto3generator)
  - [Boto3Generator](#boto3generator-1)
    - [Boto3Generator().generate_docs](#boto3generator()generate_docs)
    - [Boto3Generator().generate_stubs](#boto3generator()generate_stubs)
    - [Boto3Generator().get_library_version](#boto3generator()get_library_version)
    - [Boto3Generator().get_postprocessor](#boto3generator()get_postprocessor)

## Boto3Generator

[Show source in boto3_generator.py:24](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/boto3_generator.py#L24)

Boto3 stubs/docs generator.

#### Signature

```python
class Boto3Generator(BaseGenerator):
    ...
```

#### See also

- [BaseGenerator](./base_generator.md#basegenerator)

### Boto3Generator().generate_docs

[Show source in boto3_generator.py:125](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/boto3_generator.py#L125)

Generate service and master docs.

#### Signature

```python
def generate_docs(self) -> None:
    ...
```

### Boto3Generator().generate_stubs

[Show source in boto3_generator.py:114](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/boto3_generator.py#L114)

Generate main stubs.

#### Signature

```python
def generate_stubs(self) -> None:
    ...
```

### Boto3Generator().get_library_version

[Show source in boto3_generator.py:32](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/boto3_generator.py#L32)

Get underlying library version.

#### Signature

```python
def get_library_version(self) -> str:
    ...
```

### Boto3Generator().get_postprocessor

[Show source in boto3_generator.py:38](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/boto3_generator.py#L38)

Get postprocessor for service package.

#### Signature

```python
def get_postprocessor(self, service_package: ServicePackage) -> BotocorePostprocessor:
    ...
```

#### See also

- [BotocorePostprocessor](../postprocessors/botocore.md#botocorepostprocessor)
- [ServicePackage](../structures/service_package.md#servicepackage)


