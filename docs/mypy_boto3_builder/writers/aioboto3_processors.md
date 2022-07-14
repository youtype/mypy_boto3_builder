# Aioboto3 Processors

> Auto-generated documentation for [mypy_boto3_builder.writers.aioboto3_processors](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/aioboto3_processors.py) module.

Processors for parsing and writing `aioboto3` modules.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Writers](index.md#writers) / Aioboto3 Processors
    - [process_types_aioboto3](#process_types_aioboto3)
    - [process_types_aioboto3_lite](#process_types_aioboto3_lite)

## process_types_aioboto3

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/aioboto3_processors.py#L19)

```python
def process_types_aioboto3(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
) -> TypesAioBoto3Package:
```

Parse and write stubs package `types-aioboto3`.

#### Arguments

- `session` - boto3 session
- `output_path` - Package output path
- `service_names` - List of known service names
- `generate_setup` - Generate ready-to-install or to-use package
- `version` - Package version

#### Returns

Parsed TypesAioBoto3Package.

#### See also

- [ServiceName](../service_name.md#servicename)
- [TypesAioBoto3Package](../structures/types_aioboto3_package.md#typesaioboto3package)

## process_types_aioboto3_lite

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/aioboto3_processors.py#L53)

```python
def process_types_aioboto3_lite(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
) -> TypesAioBoto3Package:
```

Parse and write stubs package `types-aioboto3-lite`.

#### Arguments

- `session` - boto3 session
- `output_path` - Package output path
- `service_names` - List of known service names
- `generate_setup` - Generate ready-to-install or to-use package
- `version` - Package version

#### Returns

Parsed AioBotocoreStubsPackage.

#### See also

- [ServiceName](../service_name.md#servicename)
- [TypesAioBoto3Package](../structures/types_aioboto3_package.md#typesaioboto3package)
