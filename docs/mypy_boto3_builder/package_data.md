# Package Data

> Auto-generated documentation for [mypy_boto3_builder.package_data](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py) module.

PyPI package data constants.

- [mypy-boto3-builder](../README.md#mypy_boto3_builder) / [Modules](../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / Package Data
    - [BasePackageData](#basepackagedata)
        - [BasePackageData.get_library_version](#basepackagedataget_library_version)
        - [BasePackageData.get_service_package_name](#basepackagedataget_service_package_name)
        - [BasePackageData.get_service_pypi_link](#basepackagedataget_service_pypi_link)
        - [BasePackageData.get_service_pypi_name](#basepackagedataget_service_pypi_name)
    - [Boto3StubsLitePackageData](#boto3stubslitepackagedata)
    - [Boto3StubsPackageData](#boto3stubspackagedata)
    - [BotocoreStubsPackageData](#botocorestubspackagedata)
        - [BotocoreStubsPackageData.get_library_version](#botocorestubspackagedataget_library_version)
    - [MypyBoto3PackageData](#mypyboto3packagedata)
    - [TypesAioBoto3LitePackageData](#typesaioboto3litepackagedata)
    - [TypesAioBoto3PackageData](#typesaioboto3packagedata)
        - [TypesAioBoto3PackageData.get_library_version](#typesaioboto3packagedataget_library_version)
    - [TypesAioBotocoreLitePackageData](#typesaiobotocorelitepackagedata)
    - [TypesAioBotocorePackageData](#typesaiobotocorepackagedata)
        - [TypesAioBotocorePackageData.get_library_version](#typesaiobotocorepackagedataget_library_version)

## BasePackageData

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L14)

```python
class BasePackageData():
```

Generic package data.

### BasePackageData.get_library_version

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L41)

```python
@staticmethod
def get_library_version() -> str:
```

Get underlying library version.

### BasePackageData.get_service_package_name

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L27)

```python
@classmethod
def get_service_package_name(service_name: ServiceName) -> str:
```

Get service package name.

#### See also

- [ServiceName](service_name.md#servicename)

### BasePackageData.get_service_pypi_link

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L48)

```python
@classmethod
def get_service_pypi_link(service_name: ServiceName) -> str:
```

Get link to PyPI.

#### See also

- [ServiceName](service_name.md#servicename)

### BasePackageData.get_service_pypi_name

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L34)

```python
@classmethod
def get_service_pypi_name(service_name: ServiceName) -> str:
```

Get service package PyPI name.

#### See also

- [ServiceName](service_name.md#servicename)

## Boto3StubsLitePackageData

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L115)

```python
class Boto3StubsLitePackageData(Boto3StubsPackageData):
```

boto3-stubs-lite package data.

#### See also

- [Boto3StubsPackageData](#boto3stubspackagedata)

## Boto3StubsPackageData

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L103)

```python
class Boto3StubsPackageData(BasePackageData):
```

boto3-stubs package data.

#### See also

- [BasePackageData](#basepackagedata)

## BotocoreStubsPackageData

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L56)

```python
class BotocoreStubsPackageData(BasePackageData):
```

botocore-stubs package data.

#### See also

- [BasePackageData](#basepackagedata)

### BotocoreStubsPackageData.get_library_version

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L65)

```python
@staticmethod
def get_library_version() -> str:
```

Get underlying library version.

## MypyBoto3PackageData

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L124)

```python
class MypyBoto3PackageData(BasePackageData):
```

mypy-boto3 package data.

#### See also

- [BasePackageData](#basepackagedata)

## TypesAioBoto3LitePackageData

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L155)

```python
class TypesAioBoto3LitePackageData(TypesAioBoto3PackageData):
```

types-aioboto3-lite package data.

#### See also

- [TypesAioBoto3PackageData](#typesaioboto3packagedata)

## TypesAioBoto3PackageData

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L134)

```python
class TypesAioBoto3PackageData(BasePackageData):
```

types-aioboto3 package data.

#### See also

- [BasePackageData](#basepackagedata)

### TypesAioBoto3PackageData.get_library_version

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L147)

```python
@staticmethod
def get_library_version() -> str:
```

Get underlying library version.

## TypesAioBotocoreLitePackageData

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L94)

```python
class TypesAioBotocoreLitePackageData(TypesAioBotocorePackageData):
```

types-aiobotocore-lite package data.

#### See also

- [TypesAioBotocorePackageData](#typesaiobotocorepackagedata)

## TypesAioBotocorePackageData

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L73)

```python
class TypesAioBotocorePackageData(BasePackageData):
```

types-aiobotocore package data.

#### See also

- [BasePackageData](#basepackagedata)

### TypesAioBotocorePackageData.get_library_version

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L86)

```python
@staticmethod
def get_library_version() -> str:
```

Get underlying library version.
