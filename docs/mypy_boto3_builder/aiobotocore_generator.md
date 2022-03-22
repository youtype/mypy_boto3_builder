# AioBotocoreGenerator

> Auto-generated documentation for [mypy_boto3_builder.aiobotocore_generator](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/aiobotocore_generator.py) module.

AIOBotocore stubs/docs generator.

- [mypy-boto3-builder](../README.md#mypy_boto3_builder) / [Modules](../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / AioBotocoreGenerator
    - [AioBotocoreGenerator](#aiobotocoregenerator)
        - [AioBotocoreGenerator().generate_docs](#aiobotocoregeneratorgenerate_docs)
        - [AioBotocoreGenerator().generate_service_stubs](#aiobotocoregeneratorgenerate_service_stubs)
        - [AioBotocoreGenerator().generate_stubs](#aiobotocoregeneratorgenerate_stubs)

## AioBotocoreGenerator

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/aiobotocore_generator.py#L26)

```python
class AioBotocoreGenerator():
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

AioBotocore stubs/docs generator.

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

#### See also

- [ServiceName](service_name.md#servicename)

### AioBotocoreGenerator().generate_docs

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/aiobotocore_generator.py#L144)

```python
def generate_docs() -> None:
```

Generate service and master docs.

### AioBotocoreGenerator().generate_service_stubs

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/aiobotocore_generator.py#L116)

```python
def generate_service_stubs() -> None:
```

Generate service stubs.

### AioBotocoreGenerator().generate_stubs

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/aiobotocore_generator.py#L77)

```python
def generate_stubs() -> None:
```

Generate `aiobotocore-stubs` package.
