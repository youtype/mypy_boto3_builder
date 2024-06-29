# Package Data

[Mypy_boto3_builder Index](../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](./index.md#mypy-boto3-builder) / Package Data

> Auto-generated documentation for [mypy_boto3_builder.package_data](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py) module.

## BasePackageData

[Show source in package_data.py:14](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L14)

Generic package data.

#### Signature

```python
class BasePackageData: ...
```

### BasePackageData.get_botocore_version

[Show source in package_data.py:51](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L51)

Get underlying botocore version.

#### Signature

```python
@staticmethod
def get_botocore_version() -> str: ...
```

### BasePackageData.get_library_version

[Show source in package_data.py:44](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L44)

Get underlying library version.

#### Signature

```python
@staticmethod
def get_library_version() -> str: ...
```

### BasePackageData.get_service_package_name

[Show source in package_data.py:30](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L30)

Get service package name.

#### Signature

```python
@classmethod
def get_service_package_name(cls, service_name: ServiceName) -> str: ...
```

#### See also

- [ServiceName](./service_name.md#servicename)

### BasePackageData.get_service_pypi_link

[Show source in package_data.py:58](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L58)

Get link to PyPI.

#### Signature

```python
@classmethod
def get_service_pypi_link(cls, service_name: ServiceName) -> str: ...
```

#### See also

- [ServiceName](./service_name.md#servicename)

### BasePackageData.get_service_pypi_name

[Show source in package_data.py:37](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L37)

Get service package PyPI name.

#### Signature

```python
@classmethod
def get_service_pypi_name(cls, service_name: ServiceName) -> str: ...
```

#### See also

- [ServiceName](./service_name.md#servicename)



## Boto3StubsFullPackageData

[Show source in package_data.py:145](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L145)

boto3-stubs-full package data.

#### Signature

```python
class Boto3StubsFullPackageData(Boto3StubsPackageData): ...
```

#### See also

- [Boto3StubsPackageData](#boto3stubspackagedata)

### Boto3StubsFullPackageData.get_service_pypi_name

[Show source in package_data.py:154](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L154)

Get service package PyPI name.

#### Signature

```python
@classmethod
def get_service_pypi_name(cls, service_name: ServiceName) -> str: ...
```

#### See also

- [ServiceName](./service_name.md#servicename)



## Boto3StubsLitePackageData

[Show source in package_data.py:136](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L136)

boto3-stubs-lite package data.

#### Signature

```python
class Boto3StubsLitePackageData(Boto3StubsPackageData): ...
```

#### See also

- [Boto3StubsPackageData](#boto3stubspackagedata)



## Boto3StubsPackageData

[Show source in package_data.py:121](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L121)

boto3-stubs package data.

#### Signature

```python
class Boto3StubsPackageData(BasePackageData): ...
```

#### See also

- [BasePackageData](#basepackagedata)



## MypyBoto3PackageData

[Show source in package_data.py:162](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L162)

mypy-boto3 package data.

#### Signature

```python
class MypyBoto3PackageData(BasePackageData): ...
```

#### See also

- [BasePackageData](#basepackagedata)



## TypesAioBoto3LitePackageData

[Show source in package_data.py:194](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L194)

types-aioboto3-lite package data.

#### Signature

```python
class TypesAioBoto3LitePackageData(TypesAioBoto3PackageData): ...
```

#### See also

- [TypesAioBoto3PackageData](#typesaioboto3packagedata)



## TypesAioBoto3PackageData

[Show source in package_data.py:172](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L172)

types-aioboto3 package data.

#### Signature

```python
class TypesAioBoto3PackageData(BasePackageData): ...
```

#### See also

- [BasePackageData](#basepackagedata)

### TypesAioBoto3PackageData.get_library_version

[Show source in package_data.py:186](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L186)

Get underlying library version.

#### Signature

```python
@staticmethod
def get_library_version() -> str: ...
```



## TypesAioBotocoreFullPackageData

[Show source in package_data.py:97](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L97)

types-aiobotocore-full package data.

#### Signature

```python
class TypesAioBotocoreFullPackageData(TypesAioBotocorePackageData): ...
```

#### See also

- [TypesAioBotocorePackageData](#typesaiobotocorepackagedata)

### TypesAioBotocoreFullPackageData.get_service_package_name

[Show source in package_data.py:106](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L106)

Get service package name.

#### Signature

```python
@classmethod
def get_service_package_name(cls, service_name: ServiceName) -> str: ...
```

#### See also

- [ServiceName](./service_name.md#servicename)

### TypesAioBotocoreFullPackageData.get_service_pypi_name

[Show source in package_data.py:113](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L113)

Get service package PyPI name.

#### Signature

```python
@classmethod
def get_service_pypi_name(cls, service_name: ServiceName) -> str: ...
```

#### See also

- [ServiceName](./service_name.md#servicename)



## TypesAioBotocoreLitePackageData

[Show source in package_data.py:88](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L88)

types-aiobotocore-lite package data.

#### Signature

```python
class TypesAioBotocoreLitePackageData(TypesAioBotocorePackageData): ...
```

#### See also

- [TypesAioBotocorePackageData](#typesaiobotocorepackagedata)



## TypesAioBotocorePackageData

[Show source in package_data.py:66](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L66)

types-aiobotocore package data.

#### Signature

```python
class TypesAioBotocorePackageData(BasePackageData): ...
```

#### See also

- [BasePackageData](#basepackagedata)

### TypesAioBotocorePackageData.get_library_version

[Show source in package_data.py:80](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/package_data.py#L80)

Get underlying library version.

#### Signature

```python
@staticmethod
def get_library_version() -> str: ...
```
