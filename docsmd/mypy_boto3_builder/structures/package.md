# Package

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](./index.md#structures) / Package

> Auto-generated documentation for [mypy_boto3_builder.structures.package](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py) module.

## Package

[Show source in package.py:17](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L17)

Parent class for all package structures.

#### Signature

```python
class Package:
    def __init__(
        self, data: type[BasePackageData], service_names: Iterable[ServiceName] = ()
    ) -> None: ...
```

#### See also

- [BasePackageData](../package_data.md#basepackagedata)
- [ServiceName](../service_name.md#servicename)

### Package().__str__

[Show source in package.py:54](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L54)

Get string representation for debugging.

#### Signature

```python
def __str__(self) -> str: ...
```

### Package().directory_name

[Show source in package.py:46](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L46)

Directory name to store generated package.

#### Signature

```python
@property
def directory_name(self) -> str: ...
```

### Package().get_classifiers

[Show source in package.py:108](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L108)

Get classifiers for package.

#### Signature

```python
def get_classifiers(self) -> list[str]: ...
```

### Package().get_local_doc_link

[Show source in package.py:60](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L60)

Get link to local docs.

#### Signature

```python
def get_local_doc_link(self, service_name: ServiceName | None = None) -> str: ...
```

### Package().get_module_name

[Show source in package.py:69](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L69)

Get service module name.

#### Signature

```python
def get_module_name(self, service_name: ServiceName) -> str: ...
```

#### See also

- [ServiceName](../service_name.md#servicename)

### Package().get_service_pypi_link

[Show source in package.py:81](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L81)

Get link to PyPI.

#### Signature

```python
def get_service_pypi_link(self, service_name: ServiceName) -> str: ...
```

#### See also

- [ServiceName](../service_name.md#servicename)

### Package().get_service_pypi_name

[Show source in package.py:75](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L75)

Get PyPI package name for a service package.

#### Signature

```python
def get_service_pypi_name(self, service_name: ServiceName) -> str: ...
```

#### See also

- [ServiceName](../service_name.md#servicename)

### Package().max_library_version

[Show source in package.py:94](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L94)

Minimum required library version.

#### Signature

```python
@property
def max_library_version(self) -> str: ...
```

### Package().min_library_version

[Show source in package.py:87](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L87)

Minimum required library version.

#### Signature

```python
@property
def min_library_version(self) -> str: ...
```

### Package().min_python_version

[Show source in package.py:101](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L101)

Minimum required python version.

#### Signature

```python
@property
def min_python_version(self) -> str: ...
```

### Package().service_name

[Show source in package.py:37](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/package.py#L37)

Service name for the package.

#### Signature

```python
@property
def service_name(self) -> ServiceName: ...
```

#### See also

- [ServiceName](../service_name.md#servicename)
