# PackageWriter

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Writers](./index.md#writers) /
PackageWriter

> Auto-generated documentation for [mypy_boto3_builder.writers.package_writer](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/package_writer.py) module.

## PackageWriter

[Show source in package_writer.py:25](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/package_writer.py#L25)

Writer for package static and template files.

#### Arguments

- `output_path` - Output path
- `generate_setup` - Whether to generate setup files

#### Signature

```python
class PackageWriter:
    def __init__(self, output_path: Path, generate_setup: bool = True) -> None:
        ...
```

### PackageWriter().write_docs

[Show source in package_writer.py:205](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/package_writer.py#L205)

Generate docs for a package.

#### Signature

```python
def write_docs(self, package: Package, templates_path: Path) -> None:
    ...
```

#### See also

- [Package](../structures/package.md#package)

### PackageWriter().write_package

[Show source in package_writer.py:175](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/package_writer.py#L175)

Generate files for a package.

#### Arguments

- `package` - Package to render
- `templates_path` - Path to Jinja templates for package
- `static_files_path` - Path to static files for package
- `exclude_template_names` - Do not render templates with these names

#### Signature

```python
def write_package(
    self,
    package: Package,
    templates_path: Path | None = None,
    static_files_path: Path | None = None,
    exclude_template_names: Sequence[str] = tuple(),
) -> None:
    ...
```

#### See also

- [Package](../structures/package.md#package)

### PackageWriter().write_service_docs

[Show source in package_writer.py:326](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/package_writer.py#L326)

Create service docs files.

#### Arguments

- `package` - Service package.
- `output_path` - Path to output folder.

#### Signature

```python
def write_service_docs(self, package: ServicePackage, templates_path: Path) -> None:
    ...
```

#### See also

- [ServicePackage](../structures/service_package.md#servicepackage)

### PackageWriter().write_service_package

[Show source in package_writer.py:305](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/writers/package_writer.py#L305)

Create stubs files for service.

#### Arguments

- `package` - Service package.

#### Signature

```python
def write_service_package(self, package: ServicePackage, templates_path: Path) -> None:
    ...
```

#### See also

- [ServicePackage](../structures/service_package.md#servicepackage)



