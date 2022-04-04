# Boto3Generator

> Auto-generated documentation for [mypy_boto3_builder.generators.boto3_generator](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/boto3_generator.py) module.

Boto3 stubs/docs generator.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Generators](index.md#generators) / Boto3Generator
    - [Boto3Generator](#boto3generator)
        - [Boto3Generator().generate_docs](#boto3generatorgenerate_docs)
        - [Boto3Generator().generate_stubs](#boto3generatorgenerate_stubs)
        - [Boto3Generator().get_library_version](#boto3generatorget_library_version)

## Boto3Generator

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/boto3_generator.py#L22)

```python
class Boto3Generator(BaseGenerator):
```

Boto3 stubs/docs generator.

#### See also

- [BaseGenerator](base_generator.md#basegenerator)

### Boto3Generator().generate_docs

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/boto3_generator.py#L120)

```python
def generate_docs() -> None:
```

Generate service and master docs.

### Boto3Generator().generate_stubs

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/boto3_generator.py#L109)

```python
def generate_stubs() -> None:
```

Generate main stubs.

### Boto3Generator().get_library_version

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/boto3_generator.py#L30)

```python
def get_library_version() -> str:
```

Get underlying library version.
