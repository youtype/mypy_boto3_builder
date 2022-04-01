# Processors

> Auto-generated documentation for [mypy_boto3_builder.writers.processors](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/processors.py) module.

Processors for parsing and writing `boto3` modules.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Writers](index.md#writers) / Processors
    - [process_boto3_stubs](#process_boto3_stubs)
    - [process_boto3_stubs_docs](#process_boto3_stubs_docs)
    - [process_boto3_stubs_lite](#process_boto3_stubs_lite)
    - [process_botocore_stubs](#process_botocore_stubs)
    - [process_master](#process_master)

## process_boto3_stubs

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/processors.py#L26)

```python
def process_boto3_stubs(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
) -> Boto3StubsPackage:
```

Parse and write stubs package `boto3_stubs`.

#### Arguments

- `session` - boto3 session
- `output_path` - Package output path
- `service_names` - List of known service names
- `generate_setup` - Generate ready-to-install or to-use package
- `version` - Package version

#### Returns

Parsed Boto3StubsPackage.

#### See also

- [Boto3StubsPackage](../structures/boto3_stubs_package.md#boto3stubspackage)
- [ServiceName](../service_name.md#servicename)

## process_boto3_stubs_docs

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/processors.py#L169)

```python
def process_boto3_stubs_docs(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
) -> Boto3StubsPackage:
```

Parse and write master package docs.

#### Arguments

- `session` - boto3 session
- `output_path` - Package output path
- `service_names` - List of known service names

#### Returns

Parsed Boto3StubsPackage.

#### See also

- [Boto3StubsPackage](../structures/boto3_stubs_package.md#boto3stubspackage)
- [ServiceName](../service_name.md#servicename)

## process_boto3_stubs_lite

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/processors.py#L63)

```python
def process_boto3_stubs_lite(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
) -> Boto3StubsPackage:
```

Parse and write stubs package `boto3-stubs-lite`.

#### Arguments

- `session` - boto3 session
- `output_path` - Package output path
- `service_names` - List of known service names
- `generate_setup` - Generate ready-to-install or to-use package
- `version` - Package version

#### Returns

Parsed Boto3StubsPackage.

#### See also

- [Boto3StubsPackage](../structures/boto3_stubs_package.md#boto3stubspackage)
- [ServiceName](../service_name.md#servicename)

## process_botocore_stubs

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/processors.py#L108)

```python
def process_botocore_stubs(
    output_path: Path,
    generate_setup: bool,
    version: str,
) -> None:
```

Parse and write stubs package `botocore_stubs`.

#### Arguments

- `output_path` - Package output path
- `generate_setup` - Generate ready-to-install or to-use package
- `version` - Package version

## process_master

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/processors.py#L134)

```python
def process_master(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
) -> MasterPackage:
```

Parse and write master package `mypy_boto3`.

#### Arguments

- `session` - boto3 session
- `output_path` - Package output path
- `service_names` - List of known service names
- `generate_setup` - Generate ready-to-install or to-use package
- `version` - Package version

#### Returns

Parsed MasterPackage.

#### See also

- [MasterPackage](../structures/master_package.md#masterpackage)
- [ServiceName](../service_name.md#servicename)
