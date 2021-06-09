# Processors

> Auto-generated documentation for [mypy_boto3_builder.writers.processors](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/writers/processors.py) module.

Processors for parsing and writing modules.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Writers](index.md#writers) / Processors
    - [process_boto3_stubs](#process_boto3_stubs)
    - [process_boto3_stubs_docs](#process_boto3_stubs_docs)
    - [process_botocore_stubs](#process_botocore_stubs)
    - [process_master](#process_master)
    - [process_service](#process_service)
    - [process_service_docs](#process_service_docs)

## process_boto3_stubs

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/writers/processors.py#L27)

```python
def process_boto3_stubs(
    session: Session,
    output_path: Path,
    service_names: List[ServiceName],
    generate_setup: bool,
) -> Boto3StubsPackage:
```

Parse and write stubs package `boto3_stubs`.

#### Arguments

- `session` - boto3 session.
- `output_path` - Package output path.
- `service_names` - List of known service names.
- `generate_setup` - Whether to generate install or installed package.

#### Returns

Parsed Boto3StubsPackage.

#### See also

- [Boto3StubsPackage](../structures/boto3_stubs_package.md#boto3stubspackage)

## process_boto3_stubs_docs

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/writers/processors.py#L172)

```python
def process_boto3_stubs_docs(
    session: Session,
    output_path: Path,
    service_names: List[ServiceName],
) -> Boto3StubsPackage:
```

Parse and write master package docs.

#### Arguments

- `session` - boto3 session.
- `output_path` - Package output path.
- `service_names` - List of known service names.

#### Returns

Parsed Boto3StubsPackage.

#### See also

- [Boto3StubsPackage](../structures/boto3_stubs_package.md#boto3stubspackage)

## process_botocore_stubs

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/writers/processors.py#L59)

```python
def process_botocore_stubs(output_path: Path, generate_setup: bool) -> None:
```

Parse and write stubs package `botocore_stubs`.

#### Arguments

- `output_path` - Package output path.
- `generate_setup` - Whether to generate install or installed package.

## process_master

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/writers/processors.py#L78)

```python
def process_master(
    session: Session,
    output_path: Path,
    service_names: List[ServiceName],
    generate_setup: bool,
) -> MasterPackage:
```

Parse and write master package `mypy_boto3`.

#### Arguments

- `session` - boto3 session.
- `output_path` - Package output path.
- `service_names` - List of known service names.
- `generate_setup` - Whether to generate install or installed package.

#### Returns

Parsed MasterPackage.

#### See also

- [MasterPackage](../structures/master_package.md#masterpackage)

## process_service

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/writers/processors.py#L110)

```python
def process_service(
    session: Session,
    service_name: ServiceName,
    output_path: Path,
    generate_setup: bool,
) -> ServicePackage:
```

Parse and write service package `mypy_boto3_*`.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.
- `output_path` - Package output path.
- `generate_setup` - Whether to generate install or installed package.

#### Returns

Parsed ServicePackage.

#### See also

- [ServiceName](../service_name.md#servicename)
- [ServicePackage](../structures/service_package.md#servicepackage)

## process_service_docs

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/writers/processors.py#L144)

```python
def process_service_docs(
    session: Session,
    service_name: ServiceName,
    output_path: Path,
) -> ServicePackage:
```

Parse and write service package docs.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.
- `output_path` - Package output path.

#### Returns

Parsed ServicePackage.

#### See also

- [ServiceName](../service_name.md#servicename)
- [ServicePackage](../structures/service_package.md#servicepackage)
