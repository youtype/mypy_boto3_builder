# Aiobotocore Processors

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Writers](./index.md#writers) / Aiobotocore Processors

> Auto-generated documentation for [mypy_boto3_builder.writers.aiobotocore_processors](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/aiobotocore_processors.py) module.

## process_aiobotocore_stubs

[Show source in aiobotocore_processors.py:23](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/aiobotocore_processors.py#L23)

Parse and write stubs package `aiobotocore-stubs`.

#### Arguments

- `session` - boto3 session
- `output_path` - Package output path
- `service_names` - List of known service names
- `generate_setup` - Generate ready-to-install or to-use package
- `version` - Package version

#### Returns

Parsed TypesAioBotocorePackage.

#### Signature

```python
def process_aiobotocore_stubs(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
) -> TypesAioBotocorePackage: ...
```

#### See also

- [ServiceName](../service_name.md#servicename)
- [TypesAioBotocorePackage](../structures/types_aiobotocore_package.md#typesaiobotocorepackage)



## process_aiobotocore_stubs_docs

[Show source in aiobotocore_processors.py:96](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/aiobotocore_processors.py#L96)

Parse and write master package docs.

#### Arguments

- `session` - boto3 session
- `output_path` - Package output path
- `service_names` - List of known service names

#### Returns

Parsed TypesAioBotocorePackage.

#### Signature

```python
def process_aiobotocore_stubs_docs(
    session: Session, output_path: Path, service_names: Iterable[ServiceName]
) -> TypesAioBotocorePackage: ...
```

#### See also

- [ServiceName](../service_name.md#servicename)
- [TypesAioBotocorePackage](../structures/types_aiobotocore_package.md#typesaiobotocorepackage)



## process_aiobotocore_stubs_lite

[Show source in aiobotocore_processors.py:59](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/aiobotocore_processors.py#L59)

Parse and write stubs package `aiobotocore-stubs-lite`.

#### Arguments

- `session` - boto3 session
- `output_path` - Package output path
- `service_names` - List of known service names
- `generate_setup` - Generate ready-to-install or to-use package
- `version` - Package version

#### Returns

Parsed TypesAioBotocorePackage.

#### Signature

```python
def process_aiobotocore_stubs_lite(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
) -> TypesAioBotocorePackage: ...
```

#### See also

- [ServiceName](../service_name.md#servicename)
- [TypesAioBotocorePackage](../structures/types_aiobotocore_package.md#typesaiobotocorepackage)
