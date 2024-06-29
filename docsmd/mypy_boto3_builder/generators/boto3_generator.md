# Boto3Generator

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Generators](./index.md#generators) / Boto3Generator

> Auto-generated documentation for [mypy_boto3_builder.generators.boto3_generator](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/boto3_generator.py) module.

## Boto3Generator

[Show source in boto3_generator.py:25](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/boto3_generator.py#L25)

Boto3 stubs/docs generator.

#### Signature

```python
class Boto3Generator(BaseGenerator): ...
```

#### See also

- [BaseGenerator](./base_generator.md#basegenerator)

### Boto3Generator()._generate_master

[Show source in boto3_generator.py:45](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/boto3_generator.py#L45)

Generate `mypy-boto3` package.

#### Signature

```python
def _generate_master(self) -> None: ...
```

### Boto3Generator().generate_docs

[Show source in boto3_generator.py:104](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/boto3_generator.py#L104)

Generate service and master docs.

#### Signature

```python
def generate_docs(self) -> None: ...
```

### Boto3Generator().generate_full_stubs

[Show source in boto3_generator.py:128](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/boto3_generator.py#L128)

Generate full stubs.

#### Signature

```python
def generate_full_stubs(self) -> None: ...
```

### Boto3Generator().generate_stubs

[Show source in boto3_generator.py:94](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/boto3_generator.py#L94)

Generate main stubs.

#### Signature

```python
def generate_stubs(self) -> None: ...
```

### Boto3Generator().get_library_version

[Show source in boto3_generator.py:33](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/boto3_generator.py#L33)

Get underlying library version.

#### Signature

```python
def get_library_version(self) -> str: ...
```

### Boto3Generator().get_postprocessor

[Show source in boto3_generator.py:39](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/boto3_generator.py#L39)

Get postprocessor for service package.

#### Signature

```python
def get_postprocessor(
    self, service_package: ServicePackage
) -> BotocorePostprocessor: ...
```

#### See also

- [BotocorePostprocessor](../postprocessors/botocore.md#botocorepostprocessor)
- [ServicePackage](../structures/service_package.md#servicepackage)
