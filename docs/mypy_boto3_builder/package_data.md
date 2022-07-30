# Package Data

[mypy-boto3-builder Index](../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](./index.md#mypy-boto3-builder) /
Package Data

> Auto-generated documentation for [mypy_boto3_builder.package_data](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py) module.

- [Package Data](#package-data)
  - [BasePackageData](#basepackagedata)
    - [BasePackageData.get_library_version](#basepackagedataget_library_version)
    - [BasePackageData.get_service_package_name](#basepackagedataget_service_package_name)
    - [BasePackageData.get_service_pypi_link](#basepackagedataget_service_pypi_link)
    - [BasePackageData.get_service_pypi_name](#basepackagedataget_service_pypi_name)
  - [Boto3StubsLitePackageData](#boto3stubslitepackagedata)
  - [Boto3StubsPackageData](#boto3stubspackagedata)
  - [MypyBoto3PackageData](#mypyboto3packagedata)
  - [TypesAioBoto3LitePackageData](#typesaioboto3litepackagedata)
  - [TypesAioBoto3PackageData](#typesaioboto3packagedata)
    - [TypesAioBoto3PackageData.get_library_version](#typesaioboto3packagedataget_library_version)
  - [TypesAioBotocoreLitePackageData](#typesaiobotocorelitepackagedata)
  - [TypesAioBotocorePackageData](#typesaiobotocorepackagedata)
    - [TypesAioBotocorePackageData.get_library_version](#typesaiobotocorepackagedataget_library_version)

## BasePackageData

[Show source in package_data.py:13](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L13)

Generic package data.

#### Signature

```python
class BasePackageData:
    ...
```

### BasePackageData.get_library_version

[Show source in package_data.py:42](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L42)

Get underlying library version.

#### Signature

```python
@staticmethod
def get_library_version() -> str:
    ...
```

### BasePackageData.get_service_package_name

[Show source in package_data.py:28](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L28)

Get service package name.

#### Signature

```python
@classmethod
def get_service_package_name(cls, service_name: ServiceName) -> str:
    ...
```

#### See also

- [ServiceName](./service_name.md#servicename)

### BasePackageData.get_service_pypi_link

[Show source in package_data.py:49](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L49)

Get link to PyPI.

#### Signature

```python
@classmethod
def get_service_pypi_link(cls, service_name: ServiceName) -> str:
    ...
```

#### See also

- [ServiceName](./service_name.md#servicename)

### BasePackageData.get_service_pypi_name

[Show source in package_data.py:35](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L35)

Get service package PyPI name.

#### Signature

```python
@classmethod
def get_service_pypi_name(cls, service_name: ServiceName) -> str:
    ...
```

#### See also

- [ServiceName](./service_name.md#servicename)



## Boto3StubsLitePackageData

[Show source in package_data.py:101](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L101)

boto3-stubs-lite package data.

#### Signature

```python
class Boto3StubsLitePackageData(Boto3StubsPackageData):
    ...
```

#### See also

- [Boto3StubsPackageData](#boto3stubspackagedata)



## Boto3StubsPackageData

[Show source in package_data.py:87](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L87)

boto3-stubs package data.

#### Signature

```python
class Boto3StubsPackageData(BasePackageData):
    ...
```

#### See also

- [BasePackageData](#basepackagedata)



## MypyBoto3PackageData

[Show source in package_data.py:110](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L110)

mypy-boto3 package data.

#### Signature

```python
class MypyBoto3PackageData(BasePackageData):
    ...
```

#### See also

- [BasePackageData](#basepackagedata)



## TypesAioBoto3LitePackageData

[Show source in package_data.py:141](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L141)

types-aioboto3-lite package data.

#### Signature

```python
class TypesAioBoto3LitePackageData(TypesAioBoto3PackageData):
    ...
```

#### See also

- [TypesAioBoto3PackageData](#typesaioboto3packagedata)



## TypesAioBoto3PackageData

[Show source in package_data.py:120](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L120)

types-aioboto3 package data.

#### Signature

```python
class TypesAioBoto3PackageData(BasePackageData):
    ...
```

#### See also

- [BasePackageData](#basepackagedata)

### TypesAioBoto3PackageData.get_library_version

[Show source in package_data.py:133](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L133)

Get underlying library version.

#### Signature

```python
@staticmethod
def get_library_version() -> str:
    ...
```



## TypesAioBotocoreLitePackageData

[Show source in package_data.py:78](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L78)

types-aiobotocore-lite package data.

#### Signature

```python
class TypesAioBotocoreLitePackageData(TypesAioBotocorePackageData):
    ...
```

#### See also

- [TypesAioBotocorePackageData](#typesaiobotocorepackagedata)



## TypesAioBotocorePackageData

[Show source in package_data.py:57](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L57)

types-aiobotocore package data.

#### Signature

```python
class TypesAioBotocorePackageData(BasePackageData):
    ...
```

#### See also

- [BasePackageData](#basepackagedata)

### TypesAioBotocorePackageData.get_library_version

[Show source in package_data.py:70](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L70)

Get underlying library version.

#### Signature

```python
@staticmethod
def get_library_version() -> str:
    ...
```


