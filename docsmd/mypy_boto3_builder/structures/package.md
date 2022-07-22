# Package

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Structures](./index.md#structures) /
Package

> Auto-generated documentation for [mypy_boto3_builder.structures.package](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py) module.

## Package

[Show source in package.py:12](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L12)

Parent class for all package structures.

#### Signature

```python
class Package:
    def __init__(
        self, data: type[BasePackageData], service_names: Iterable[ServiceName] = tuple()
    ) -> None:
        ...
```

#### See also

- [BasePackageData](../package_data.md#basepackagedata)
- [ServiceName](../service_name.md#servicename)

### Package().directory_name

[Show source in package.py:31](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L31)

Directory name to store generated package.

#### Signature

```python
@property
def directory_name(self) -> str:
    ...
```

### Package().get_local_doc_link

[Show source in package.py:42](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L42)

Get link to local docs.

#### Signature

```python
def get_local_doc_link(self, service_name: ServiceName | None = None) -> str:
    ...
```

### Package().get_module_name

[Show source in package.py:51](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L51)

Get service module name.

#### Signature

```python
def get_module_name(self, service_name: ServiceName) -> str:
    ...
```

#### See also

- [ServiceName](../service_name.md#servicename)

### Package().get_service_pypi_link

[Show source in package.py:63](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L63)

Get link to PyPI.

#### Signature

```python
def get_service_pypi_link(self, service_name: ServiceName) -> str:
    ...
```

#### See also

- [ServiceName](../service_name.md#servicename)

### Package().get_service_pypi_name

[Show source in package.py:57](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L57)

Get PyPI package name for a service package.

#### Signature

```python
def get_service_pypi_name(self, service_name: ServiceName) -> str:
    ...
```

#### See also

- [ServiceName](../service_name.md#servicename)

### Package().max_library_version

[Show source in package.py:76](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L76)

Minimum required library version.

#### Signature

```python
@property
def max_library_version(self) -> str:
    ...
```

### Package().min_library_version

[Show source in package.py:69](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L69)

Minimum required library version.

#### Signature

```python
@property
def min_library_version(self) -> str:
    ...
```



