# Aioboto3 Processors

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Writers](./index.md#writers) /
Aioboto3 Processors

> Auto-generated documentation for [mypy_boto3_builder.writers.aioboto3_processors](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/aioboto3_processors.py) module.

## process_types_aioboto3

[Show source in aioboto3_processors.py:19](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/aioboto3_processors.py#L19)

Parse and write stubs package `types-aioboto3`.

#### Arguments

- `session` - boto3 session
- `output_path` - Package output path
- `service_names` - List of known service names
- `generate_setup` - Generate ready-to-install or to-use package
- `version` - Package version

#### Returns

Parsed TypesAioBoto3Package.

#### Signature

```python
def process_types_aioboto3(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
) -> TypesAioBoto3Package:
    ...
```

#### See also

- [ServiceName](../service_name.md#servicename)
- [TypesAioBoto3Package](../structures/types_aioboto3_package.md#typesaioboto3package)



## process_types_aioboto3_docs

[Show source in aioboto3_processors.py:88](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/aioboto3_processors.py#L88)

Parse and write master package docs.

#### Arguments

- `session` - boto3 session
- `output_path` - Package output path
- `service_names` - List of known service names

#### Returns

Parsed AioBotocoreStubsPackage.

#### Signature

```python
def process_types_aioboto3_docs(
    session: Session, output_path: Path, service_names: Iterable[ServiceName]
) -> TypesAioBoto3Package:
    ...
```

#### See also

- [ServiceName](../service_name.md#servicename)
- [TypesAioBoto3Package](../structures/types_aioboto3_package.md#typesaioboto3package)



## process_types_aioboto3_lite

[Show source in aioboto3_processors.py:53](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/aioboto3_processors.py#L53)

Parse and write stubs package `types-aioboto3-lite`.

#### Arguments

- `session` - boto3 session
- `output_path` - Package output path
- `service_names` - List of known service names
- `generate_setup` - Generate ready-to-install or to-use package
- `version` - Package version

#### Returns

Parsed AioBotocoreStubsPackage.

#### Signature

```python
def process_types_aioboto3_lite(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
) -> TypesAioBoto3Package:
    ...
```

#### See also

- [ServiceName](../service_name.md#servicename)
- [TypesAioBoto3Package](../structures/types_aioboto3_package.md#typesaioboto3package)



