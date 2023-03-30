# Package

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Structures](./index.md#structures) /
Package

> Auto-generated documentation for [mypy_boto3_builder.structures.package](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py) module.

## Package

[Show source in package.py:14](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L14)

Parent class for all package structures.

#### Signature

```python
class Package:
    def __init__(
        self, data: type[BasePackageData], service_names: Iterable[ServiceName] = ()
    ) -> None:
        ...
```

#### See also

- [BasePackageData](../package_data.md#basepackagedata)
- [ServiceName](../service_name.md#servicename)

### Package().add_fallback_import_record

[Show source in package.py:88](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L88)

Add fallback import record if needed.

Changes `import_records`.

#### Signature

```python
def add_fallback_import_record(self, import_records: set[ImportRecord]) -> None:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### Package().directory_name

[Show source in package.py:36](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L36)

Directory name to store generated package.

#### Signature

```python
@property
def directory_name(self) -> str:
    ...
```

### Package().get_local_doc_link

[Show source in package.py:47](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L47)

Get link to local docs.

#### Signature

```python
def get_local_doc_link(self, service_name: ServiceName | None = None) -> str:
    ...
```

### Package().get_module_name

[Show source in package.py:56](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L56)

Get service module name.

#### Signature

```python
def get_module_name(self, service_name: ServiceName) -> str:
    ...
```

#### See also

- [ServiceName](../service_name.md#servicename)

### Package().get_service_pypi_link

[Show source in package.py:68](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L68)

Get link to PyPI.

#### Signature

```python
def get_service_pypi_link(self, service_name: ServiceName) -> str:
    ...
```

#### See also

- [ServiceName](../service_name.md#servicename)

### Package().get_service_pypi_name

[Show source in package.py:62](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L62)

Get PyPI package name for a service package.

#### Signature

```python
def get_service_pypi_name(self, service_name: ServiceName) -> str:
    ...
```

#### See also

- [ServiceName](../service_name.md#servicename)

### Package().max_library_version

[Show source in package.py:81](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L81)

Minimum required library version.

#### Signature

```python
@property
def max_library_version(self) -> str:
    ...
```

### Package().min_library_version

[Show source in package.py:74](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L74)

Minimum required library version.

#### Signature

```python
@property
def min_library_version(self) -> str:
    ...
```
