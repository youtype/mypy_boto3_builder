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
    - [TypesAioBotocoreLitePackageData](#typesaiobotocorelitepackagedata)
    - [TypesAioBotocorePackageData](#typesaiobotocorepackagedata)
        - [TypesAioBotocorePackageData.get_library_version](#typesaiobotocorepackagedataget_library_version)

## BasePackageData

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L13)

```python
class BasePackageData():
```

Generic package data.

### BasePackageData.get_library_version

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L40)

```python
@staticmethod
def get_library_version() -> str:
```

Get underlying library version.

### BasePackageData.get_service_package_name

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L26)

```python
@classmethod
def get_service_package_name(service_name: ServiceName) -> str:
```

Get service package name.

#### See also

- [ServiceName](service_name.md#servicename)

### BasePackageData.get_service_pypi_link

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L47)

```python
@classmethod
def get_service_pypi_link(service_name: ServiceName) -> str:
```

Get link to PyPI.

#### See also

- [ServiceName](service_name.md#servicename)

### BasePackageData.get_service_pypi_name

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L33)

```python
@classmethod
def get_service_pypi_name(service_name: ServiceName) -> str:
```

Get service package PyPI name.

#### See also

- [ServiceName](service_name.md#servicename)

## Boto3StubsLitePackageData

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L114)

```python
class Boto3StubsLitePackageData(Boto3StubsPackageData):
```

boto3-stubs-lite package data.

#### See also

- [Boto3StubsPackageData](#boto3stubspackagedata)

## Boto3StubsPackageData

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L102)

```python
class Boto3StubsPackageData(BasePackageData):
```

boto3-stubs package data.

#### See also

- [BasePackageData](#basepackagedata)

## BotocoreStubsPackageData

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L55)

```python
class BotocoreStubsPackageData(BasePackageData):
```

botocore-stubs package data.

#### See also

- [BasePackageData](#basepackagedata)

### BotocoreStubsPackageData.get_library_version

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L64)

```python
@staticmethod
def get_library_version() -> str:
```

Get underlying library version.

## MypyBoto3PackageData

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L123)

```python
class MypyBoto3PackageData(BasePackageData):
```

mypy-boto3 package data.

#### See also

- [BasePackageData](#basepackagedata)

## TypesAioBotocoreLitePackageData

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L93)

```python
class TypesAioBotocoreLitePackageData(TypesAioBotocorePackageData):
```

types-aiobotocore-lite package data.

#### See also

- [TypesAioBotocorePackageData](#typesaiobotocorepackagedata)

## TypesAioBotocorePackageData

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L72)

```python
class TypesAioBotocorePackageData(BasePackageData):
```

aiobotocore-stubs package data.

#### See also

- [BasePackageData](#basepackagedata)

### TypesAioBotocorePackageData.get_library_version

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L85)

```python
@staticmethod
def get_library_version() -> str:
```

Get underlying library version.
