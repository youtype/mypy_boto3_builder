# Package Data

[Mypy_boto3_builder Index](../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](./index.md#mypy-boto3-builder) /
Package Data

> Auto-generated documentation for [mypy_boto3_builder.package_data](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py) module.

## BasePackageData

[Show source in package_data.py:14](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L14)

Generic package data.

#### Signature

```python
class BasePackageData: ...
```

### BasePackageData.get_botocore_version

[Show source in package_data.py:50](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L50)

Get underlying botocore version.

#### Signature

```python
@staticmethod
def get_botocore_version() -> str: ...
```

### BasePackageData.get_library_version

[Show source in package_data.py:43](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L43)

Get underlying library version.

#### Signature

```python
@staticmethod
def get_library_version() -> str: ...
```

### BasePackageData.get_service_package_name

[Show source in package_data.py:29](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L29)

Get service package name.

#### Signature

```python
@classmethod
def get_service_package_name(cls, service_name: ServiceName) -> str: ...
```

#### See also

- [ServiceName](./service_name.md#servicename)

### BasePackageData.get_service_pypi_link

[Show source in package_data.py:57](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L57)

Get link to PyPI.

#### Signature

```python
@classmethod
def get_service_pypi_link(cls, service_name: ServiceName) -> str: ...
```

#### See also

- [ServiceName](./service_name.md#servicename)

### BasePackageData.get_service_pypi_name

[Show source in package_data.py:36](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L36)

Get service package PyPI name.

#### Signature

```python
@classmethod
def get_service_pypi_name(cls, service_name: ServiceName) -> str: ...
```

#### See also

- [ServiceName](./service_name.md#servicename)



## Boto3StubsLitePackageData

[Show source in package_data.py:109](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L109)

boto3-stubs-lite package data.

#### Signature

```python
class Boto3StubsLitePackageData(Boto3StubsPackageData): ...
```

#### See also

- [Boto3StubsPackageData](#boto3stubspackagedata)



## Boto3StubsPackageData

[Show source in package_data.py:95](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L95)

boto3-stubs package data.

#### Signature

```python
class Boto3StubsPackageData(BasePackageData): ...
```

#### See also

- [BasePackageData](#basepackagedata)



## MypyBoto3PackageData

[Show source in package_data.py:118](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L118)

mypy-boto3 package data.

#### Signature

```python
class MypyBoto3PackageData(BasePackageData): ...
```

#### See also

- [BasePackageData](#basepackagedata)



## TypesAioBoto3LitePackageData

[Show source in package_data.py:150](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L150)

types-aioboto3-lite package data.

#### Signature

```python
class TypesAioBoto3LitePackageData(TypesAioBoto3PackageData): ...
```

#### See also

- [TypesAioBoto3PackageData](#typesaioboto3packagedata)



## TypesAioBoto3PackageData

[Show source in package_data.py:128](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L128)

types-aioboto3 package data.

#### Signature

```python
class TypesAioBoto3PackageData(BasePackageData): ...
```

#### See also

- [BasePackageData](#basepackagedata)

### TypesAioBoto3PackageData.get_library_version

[Show source in package_data.py:142](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L142)

Get underlying library version.

#### Signature

```python
@staticmethod
def get_library_version() -> str: ...
```



## TypesAioBotocoreLitePackageData

[Show source in package_data.py:86](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L86)

types-aiobotocore-lite package data.

#### Signature

```python
class TypesAioBotocoreLitePackageData(TypesAioBotocorePackageData): ...
```

#### See also

- [TypesAioBotocorePackageData](#typesaiobotocorepackagedata)



## TypesAioBotocorePackageData

[Show source in package_data.py:65](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L65)

types-aiobotocore package data.

#### Signature

```python
class TypesAioBotocorePackageData(BasePackageData): ...
```

#### See also

- [BasePackageData](#basepackagedata)

### TypesAioBotocorePackageData.get_library_version

[Show source in package_data.py:78](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L78)

Get underlying library version.

#### Signature

```python
@staticmethod
def get_library_version() -> str: ...
```
