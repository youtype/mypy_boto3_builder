# Aiobotocore Processors

> Auto-generated documentation for [mypy_boto3_builder.writers.aiobotocore_processors](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/aiobotocore_processors.py) module.

Processors for parsing and writing `aiobotocore` modules.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Writers](index.md#writers) / Aiobotocore Processors
    - [process_aiobotocore_service](#process_aiobotocore_service)
    - [process_aiobotocore_service_docs](#process_aiobotocore_service_docs)
    - [process_aiobotocore_stubs](#process_aiobotocore_stubs)
    - [process_aiobotocore_stubs_docs](#process_aiobotocore_stubs_docs)
    - [process_aiobotocore_stubs_lite](#process_aiobotocore_stubs_lite)

## process_aiobotocore_service

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/aiobotocore_processors.py#L98)

```python
def process_aiobotocore_service(
    session: Session,
    service_name: ServiceName,
    output_path: Path,
    generate_setup: bool,
    service_names: Iterable[ServiceName],
    version: str,
) -> ServicePackage:
```

Parse and write service package `types_aiobotocore_*`.

#### Arguments

- `session` - boto3 session
- `service_name` - Target service name
- `output_path` - Package output path
- `generate_setup` - Generate ready-to-install or to-use package
- `service_names` - List of known service names
- `version` - Package version

#### Returns

Parsed ServicePackage.

#### See also

- [ServiceName](../service_name.md#servicename)
- [ServicePackage](../structures/service_package.md#servicepackage)

## process_aiobotocore_service_docs

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/aiobotocore_processors.py#L175)

```python
def process_aiobotocore_service_docs(
    session: Session,
    service_name: ServiceName,
    output_path: Path,
    service_names: Iterable[ServiceName],
) -> ServicePackage:
```

Parse and write service package docs.

#### Arguments

- `session` - boto3 session
- `service_name` - Target service name
- `output_path` - Package output path
- `service_names` - List of known service names

#### Returns

Parsed ServicePackage.

#### See also

- [ServiceName](../service_name.md#servicename)
- [ServicePackage](../structures/service_package.md#servicepackage)

## process_aiobotocore_stubs

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/aiobotocore_processors.py#L25)

```python
def process_aiobotocore_stubs(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
) -> AioBotocoreStubsPackage:
```

Parse and write stubs package `aiobotocore-stubs`.

#### Arguments

- `session` - boto3 session
- `output_path` - Package output path
- `service_names` - List of known service names
- `generate_setup` - Generate ready-to-install or to-use package
- `version` - Package version

#### Returns

Parsed AioBotocoreStubsPackage.

#### See also

- [AioBotocoreStubsPackage](../structures/aiobotocore_stubs_package.md#aiobotocorestubspackage)
- [ServiceName](../service_name.md#servicename)

## process_aiobotocore_stubs_docs

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/aiobotocore_processors.py#L143)

```python
def process_aiobotocore_stubs_docs(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
) -> AioBotocoreStubsPackage:
```

Parse and write master package docs.

#### Arguments

- `session` - boto3 session
- `output_path` - Package output path
- `service_names` - List of known service names

#### Returns

Parsed AioBotocoreStubsPackage.

#### See also

- [AioBotocoreStubsPackage](../structures/aiobotocore_stubs_package.md#aiobotocorestubspackage)
- [ServiceName](../service_name.md#servicename)

## process_aiobotocore_stubs_lite

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/aiobotocore_processors.py#L61)

```python
def process_aiobotocore_stubs_lite(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
) -> AioBotocoreStubsPackage:
```

Parse and write stubs package `aiobotocore-stubs-lite`.

#### Arguments

- `session` - boto3 session
- `output_path` - Package output path
- `service_names` - List of known service names
- `generate_setup` - Generate ready-to-install or to-use package
- `version` - Package version

#### Returns

Parsed AioBotocoreStubsPackage.

#### See also

- [AioBotocoreStubsPackage](../structures/aiobotocore_stubs_package.md#aiobotocorestubspackage)
- [ServiceName](../service_name.md#servicename)
