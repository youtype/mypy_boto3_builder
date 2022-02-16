# PackageWriter

> Auto-generated documentation for [mypy_boto3_builder.writers.package_writer](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/package_writer.py) module.

Writer for package static and template files.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Writers](index.md#writers) / PackageWriter
    - [PackageWriter](#packagewriter)
        - [PackageWriter().write_docs](#packagewriterwrite_docs)
        - [PackageWriter().write_package](#packagewriterwrite_package)
        - [PackageWriter().write_service_docs](#packagewriterwrite_service_docs)
        - [PackageWriter().write_service_package](#packagewriterwrite_service_package)

## PackageWriter

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/package_writer.py#L23)

```python
class PackageWriter():
    def __init__(output_path: Path, generate_setup: bool = True) -> None:
```

Writer for package static and template files.

#### Arguments

- `output_path` - Output path
- `generate_setup` - Whether to generate setup files

### PackageWriter().write_docs

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/package_writer.py#L175)

```python
def write_docs(package: Package, templates_path: Path) -> None:
```

Generate docs for a package.

#### See also

- [Package](../structures/package.md#package)

### PackageWriter().write_package

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/package_writer.py#L145)

```python
def write_package(
    package: Package,
    templates_path: Path | None = None,
    static_files_path: Path | None = None,
    exclude_template_names: Sequence[str] = tuple(),
) -> None:
```

Generate files for a package.

#### Arguments

- `package` - Package to render
- `templates_path` - Path to Jinja templates for package
- `static_files_path` - Path to static files for package
- `exclude_template_names` - Do not render templates with these names

#### See also

- [Package](../structures/package.md#package)

### PackageWriter().write_service_docs

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/package_writer.py#L305)

```python
def write_service_docs(package: ServicePackage, templates_path: Path) -> None:
```

Create service docs files.

#### Arguments

- `package` - Service package.
- `output_path` - Path to output folder.

#### See also

- [ServicePackage](../structures/service_package.md#servicepackage)

### PackageWriter().write_service_package

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/package_writer.py#L284)

```python
def write_service_package(
    package: ServicePackage,
    templates_path: Path,
) -> None:
```

Create stubs files for service.

#### Arguments

- `package` - Service package.

#### See also

- [ServicePackage](../structures/service_package.md#servicepackage)
