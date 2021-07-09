# Service Package

> Auto-generated documentation for [mypy_boto3_builder.writers.service_package](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/writers/service_package.py) module.

Service package writer.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Writers](index.md#writers) / Service Package
    - [write_service_docs](#write_service_docs)
    - [write_service_package](#write_service_package)

## write_service_docs

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/writers/service_package.py#L156)

```python
def write_service_docs(package: ServicePackage, output_path: Path) -> None:
```

Create service docs files.

#### Arguments

- `package` - Service package.
- `output_path` - Path to output folder.

#### See also

- [ServicePackage](../structures/service_package.md#servicepackage)

## write_service_package

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/writers/service_package.py#L21)

```python
def write_service_package(
    package: ServicePackage,
    output_path: Path,
    generate_setup: bool,
) -> None:
```

Create stubs files for service.

#### Arguments

- `package` - Service package.
- `output_path` - Path to output folder.
- `generate_setup` - Generate ready-to-install or to-use package.

#### See also

- [ServicePackage](../structures/service_package.md#servicepackage)
