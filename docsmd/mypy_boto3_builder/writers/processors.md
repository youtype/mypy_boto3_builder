# Processors

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Writers](./index.md#writers) /
Processors

> Auto-generated documentation for [mypy_boto3_builder.writers.processors](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/processors.py) module.

## process_boto3_stubs

[Show source in processors.py:22](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/processors.py#L22)

Parse and write stubs package `boto3_stubs`.

#### Arguments

- `session` - boto3 session
- `output_path` - Package output path
- `service_names` - List of known service names
- `generate_setup` - Generate ready-to-install or to-use package
- `version` - Package version

#### Returns

Parsed Boto3StubsPackage.

#### Signature

```python
def process_boto3_stubs(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
) -> Boto3StubsPackage: ...
```

#### See also

- [Boto3StubsPackage](../structures/boto3_stubs_package.md#boto3stubspackage)
- [ServiceName](../service_name.md#servicename)



## process_boto3_stubs_docs

[Show source in processors.py:139](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/processors.py#L139)

Parse and write master package docs.

#### Arguments

- `session` - boto3 session
- `output_path` - Package output path
- `service_names` - List of known service names

#### Returns

Parsed Boto3StubsPackage.

#### Signature

```python
def process_boto3_stubs_docs(
    session: Session, output_path: Path, service_names: Iterable[ServiceName]
) -> Boto3StubsPackage: ...
```

#### See also

- [Boto3StubsPackage](../structures/boto3_stubs_package.md#boto3stubspackage)
- [ServiceName](../service_name.md#servicename)



## process_boto3_stubs_lite

[Show source in processors.py:59](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/processors.py#L59)

Parse and write stubs package `boto3-stubs-lite`.

#### Arguments

- `session` - boto3 session
- `output_path` - Package output path
- `service_names` - List of known service names
- `generate_setup` - Generate ready-to-install or to-use package
- `version` - Package version

#### Returns

Parsed Boto3StubsPackage.

#### Signature

```python
def process_boto3_stubs_lite(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
) -> Boto3StubsPackage: ...
```

#### See also

- [Boto3StubsPackage](../structures/boto3_stubs_package.md#boto3stubspackage)
- [ServiceName](../service_name.md#servicename)



## process_master

[Show source in processors.py:104](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/processors.py#L104)

Parse and write master package `mypy_boto3`.

#### Arguments

- `session` - boto3 session
- `output_path` - Package output path
- `service_names` - List of known service names
- `generate_setup` - Generate ready-to-install or to-use package
- `version` - Package version

#### Returns

Parsed MasterPackage.

#### Signature

```python
def process_master(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
) -> MasterPackage: ...
```

#### See also

- [MasterPackage](../structures/master_package.md#masterpackage)
- [ServiceName](../service_name.md#servicename)
