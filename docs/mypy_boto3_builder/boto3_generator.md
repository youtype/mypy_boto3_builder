# Boto3Generator

> Auto-generated documentation for [mypy_boto3_builder.boto3_generator](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/boto3_generator.py) module.

Boto3 stubs/docs generator.

- [mypy-boto3-builder](../README.md#mypy_boto3_builder) / [Modules](../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / Boto3Generator
    - [Boto3Generator](#boto3generator)
        - [Boto3Generator().generate_docs](#boto3generatorgenerate_docs)
        - [Boto3Generator().generate_service_stubs](#boto3generatorgenerate_service_stubs)
        - [Boto3Generator().generate_stubs](#boto3generatorgenerate_stubs)

## Boto3Generator

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/boto3_generator.py#L30)

```python
class Boto3Generator():
    def __init__(
        service_names: Sequence[ServiceName],
        available_service_names: Iterable[ServiceName],
        master_service_names: Sequence[ServiceName],
        session: Session,
        output_path: Path,
        generate_setup: bool,
        skip_published: bool,
        disable_smart_version: bool,
        version: str,
    ):
```

Boto3 stubs/docs generator.

#### Arguments

- `service_names` - Enabled service names
- `available_service_names` - All service names
- `master_service_names` - Service names included in master
- `session` - Botocore session
- `output_path` - Path to write generated files
- `generate_setup` - Whether to create package or installed module
- `skip_published` - Whether to skip packages that are already published
- `disable_smart_version` - Whether to create a new postrelease if version is already published
- `version` - Package build version

### Boto3Generator().generate_docs

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/boto3_generator.py#L193)

```python
def generate_docs() -> None:
```

Generate service and master docs.

### Boto3Generator().generate_service_stubs

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/boto3_generator.py#L165)

```python
def generate_service_stubs() -> None:
```

Generate service stubs.

### Boto3Generator().generate_stubs

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/boto3_generator.py#L154)

```python
def generate_stubs() -> None:
```

Generate main stubs.
