# Package

> Auto-generated documentation for [mypy_boto3_builder.structures.package](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py) module.

Parent class for all package structures.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / Package
    - [Package](#package)
        - [Package().directory_name](#packagedirectory_name)
        - [Package().docs_lite_package_name](#packagedocs_lite_package_name)
        - [Package().docs_package_name](#packagedocs_package_name)
        - [Package().get_local_doc_link](#packageget_local_doc_link)
        - [Package().get_module_name](#packageget_module_name)
        - [Package().get_service_pypi_link](#packageget_service_pypi_link)
        - [Package().get_service_pypi_name](#packageget_service_pypi_name)

## Package

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L17)

```python
class Package():
    def __init__(
        name: str,
        pypi_name: str,
        service_names: Iterable[ServiceName] = tuple(),
    ) -> None:
```

Parent class for all package structures.

### Package().directory_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L54)

```python
@property
def directory_name() -> str:
```

Directory name to store generated package.

### Package().docs_lite_package_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L45)

```python
@property
def docs_lite_package_name() -> str:
```

Docs lite library name.

### Package().docs_package_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L36)

```python
@property
def docs_package_name() -> str:
```

Docs library name.

### Package().get_local_doc_link

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L65)

```python
def get_local_doc_link(service_name: ServiceName | None = None) -> str:
```

Get link to local docs.

### Package().get_module_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L79)

```python
def get_module_name(service_name: ServiceName) -> str:
```

Get service module name.

#### See also

- [ServiceName](../service_name.md#servicename)

### Package().get_service_pypi_link

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L99)

```python
def get_service_pypi_link(service_name: ServiceName) -> str:
```

Get link to PyPI.

#### See also

- [ServiceName](../service_name.md#servicename)

### Package().get_service_pypi_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L89)

```python
def get_service_pypi_name(service_name: ServiceName) -> str:
```

Get PyPI package name for a service package.

#### See also

- [ServiceName](../service_name.md#servicename)
