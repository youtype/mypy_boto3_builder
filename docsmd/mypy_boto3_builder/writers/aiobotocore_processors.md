# Aiobotocore Processors

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Writers](./index.md#writers) /
Aiobotocore Processors

> Auto-generated documentation for [mypy_boto3_builder.writers.aiobotocore_processors](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/aiobotocore_processors.py) module.

## process_aiobotocore_stubs

[Show source in aiobotocore_processors.py:22](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/aiobotocore_processors.py#L22)

Parse and write stubs package `aiobotocore-stubs`.

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
def process_aiobotocore_stubs(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
) -> AioBotocoreStubsPackage:
    ...
```

#### See also

- [AioBotocoreStubsPackage](../structures/aiobotocore_stubs_package.md#aiobotocorestubspackage)
- [ServiceName](../service_name.md#servicename)



## process_aiobotocore_stubs_docs

[Show source in aiobotocore_processors.py:95](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/aiobotocore_processors.py#L95)

Parse and write master package docs.

#### Arguments

- `session` - boto3 session
- `output_path` - Package output path
- `service_names` - List of known service names

#### Returns

Parsed AioBotocoreStubsPackage.

#### Signature

```python
def process_aiobotocore_stubs_docs(
    session: Session, output_path: Path, service_names: Iterable[ServiceName]
) -> AioBotocoreStubsPackage:
    ...
```

#### See also

- [AioBotocoreStubsPackage](../structures/aiobotocore_stubs_package.md#aiobotocorestubspackage)
- [ServiceName](../service_name.md#servicename)



## process_aiobotocore_stubs_lite

[Show source in aiobotocore_processors.py:58](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/aiobotocore_processors.py#L58)

Parse and write stubs package `aiobotocore-stubs-lite`.

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
def process_aiobotocore_stubs_lite(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
) -> AioBotocoreStubsPackage:
    ...
```

#### See also

- [AioBotocoreStubsPackage](../structures/aiobotocore_stubs_package.md#aiobotocorestubspackage)
- [ServiceName](../service_name.md#servicename)



