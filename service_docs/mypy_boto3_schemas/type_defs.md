# Structures for boto3 Schemas module

> [Index](../index.md) > [Schemas](./index.md) > Structures

Auto-generated documentation for [Schemas](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas)
type annotations stubs module [mypy_boto3_schemas](https://pypi.org/project/mypy-boto3-schemas/).

- [Structures for boto3 Schemas module](#structures-for-boto3-schemas-module)
  - [DiscovererSummaryTypeDef](#discoverersummarytypedef)
  - [RegistrySummaryTypeDef](#registrysummarytypedef)
  - [SchemaSummaryTypeDef](#schemasummarytypedef)
  - [SchemaVersionSummaryTypeDef](#schemaversionsummarytypedef)
  - [SearchSchemaSummaryTypeDef](#searchschemasummarytypedef)
  - [SearchSchemaVersionSummaryTypeDef](#searchschemaversionsummarytypedef)
  - [CreateDiscovererResponseTypeDef](#creatediscovererresponsetypedef)
  - [CreateRegistryResponseTypeDef](#createregistryresponsetypedef)
  - [CreateSchemaResponseTypeDef](#createschemaresponsetypedef)
  - [DescribeCodeBindingResponseTypeDef](#describecodebindingresponsetypedef)
  - [DescribeDiscovererResponseTypeDef](#describediscovererresponsetypedef)
  - [DescribeRegistryResponseTypeDef](#describeregistryresponsetypedef)
  - [DescribeSchemaResponseTypeDef](#describeschemaresponsetypedef)
  - [ExportSchemaResponseTypeDef](#exportschemaresponsetypedef)
  - [GetCodeBindingSourceResponseTypeDef](#getcodebindingsourceresponsetypedef)
  - [GetDiscoveredSchemaResponseTypeDef](#getdiscoveredschemaresponsetypedef)
  - [GetResourcePolicyResponseTypeDef](#getresourcepolicyresponsetypedef)
  - [ListDiscoverersResponseTypeDef](#listdiscoverersresponsetypedef)
  - [ListRegistriesResponseTypeDef](#listregistriesresponsetypedef)
  - [ListSchemaVersionsResponseTypeDef](#listschemaversionsresponsetypedef)
  - [ListSchemasResponseTypeDef](#listschemasresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PutCodeBindingResponseTypeDef](#putcodebindingresponsetypedef)
  - [PutResourcePolicyResponseTypeDef](#putresourcepolicyresponsetypedef)
  - [SearchSchemasResponseTypeDef](#searchschemasresponsetypedef)
  - [StartDiscovererResponseTypeDef](#startdiscovererresponsetypedef)
  - [StopDiscovererResponseTypeDef](#stopdiscovererresponsetypedef)
  - [UpdateDiscovererResponseTypeDef](#updatediscovererresponsetypedef)
  - [UpdateRegistryResponseTypeDef](#updateregistryresponsetypedef)
  - [UpdateSchemaResponseTypeDef](#updateschemaresponsetypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## DiscovererSummaryTypeDef

```python
from mypy_boto3_schemas.type_defs import DiscovererSummaryTypeDef
```




Optional fields:
- `DiscovererArn`: `str`
- `DiscovererId`: `str`
- `SourceArn`: `str`
- `State`: `DiscovererState`
- `Tags`: `Dict[str, str]`


## RegistrySummaryTypeDef

```python
from mypy_boto3_schemas.type_defs import RegistrySummaryTypeDef
```




Optional fields:
- `RegistryArn`: `str`
- `RegistryName`: `str`
- `Tags`: `Dict[str, str]`


## SchemaSummaryTypeDef

```python
from mypy_boto3_schemas.type_defs import SchemaSummaryTypeDef
```




Optional fields:
- `LastModified`: `datetime`
- `SchemaArn`: `str`
- `SchemaName`: `str`
- `Tags`: `Dict[str, str]`
- `VersionCount`: `int`


## SchemaVersionSummaryTypeDef

```python
from mypy_boto3_schemas.type_defs import SchemaVersionSummaryTypeDef
```




Optional fields:
- `SchemaArn`: `str`
- `SchemaName`: `str`
- `SchemaVersion`: `str`
- `Type`: `TypeType`


## SearchSchemaSummaryTypeDef

```python
from mypy_boto3_schemas.type_defs import SearchSchemaSummaryTypeDef
```




Optional fields:
- `RegistryName`: `str`
- `SchemaArn`: `str`
- `SchemaName`: `str`
- `SchemaVersions`: `List["SearchSchemaVersionSummaryTypeDef"]`


## SearchSchemaVersionSummaryTypeDef

```python
from mypy_boto3_schemas.type_defs import SearchSchemaVersionSummaryTypeDef
```




Optional fields:
- `CreatedDate`: `datetime`
- `SchemaVersion`: `str`
- `Type`: `TypeType`


## CreateDiscovererResponseTypeDef

```python
from mypy_boto3_schemas.type_defs import CreateDiscovererResponseTypeDef
```




Optional fields:
- `Description`: `str`
- `DiscovererArn`: `str`
- `DiscovererId`: `str`
- `SourceArn`: `str`
- `State`: `DiscovererState`
- `Tags`: `Dict[str, str]`


## CreateRegistryResponseTypeDef

```python
from mypy_boto3_schemas.type_defs import CreateRegistryResponseTypeDef
```




Optional fields:
- `Description`: `str`
- `RegistryArn`: `str`
- `RegistryName`: `str`
- `Tags`: `Dict[str, str]`


## CreateSchemaResponseTypeDef

```python
from mypy_boto3_schemas.type_defs import CreateSchemaResponseTypeDef
```




Optional fields:
- `Description`: `str`
- `LastModified`: `datetime`
- `SchemaArn`: `str`
- `SchemaName`: `str`
- `SchemaVersion`: `str`
- `Tags`: `Dict[str, str]`
- `Type`: `str`
- `VersionCreatedDate`: `datetime`


## DescribeCodeBindingResponseTypeDef

```python
from mypy_boto3_schemas.type_defs import DescribeCodeBindingResponseTypeDef
```




Optional fields:
- `CreationDate`: `datetime`
- `LastModified`: `datetime`
- `SchemaVersion`: `str`
- `Status`: `CodeGenerationStatus`


## DescribeDiscovererResponseTypeDef

```python
from mypy_boto3_schemas.type_defs import DescribeDiscovererResponseTypeDef
```




Optional fields:
- `Description`: `str`
- `DiscovererArn`: `str`
- `DiscovererId`: `str`
- `SourceArn`: `str`
- `State`: `DiscovererState`
- `Tags`: `Dict[str, str]`


## DescribeRegistryResponseTypeDef

```python
from mypy_boto3_schemas.type_defs import DescribeRegistryResponseTypeDef
```




Optional fields:
- `Description`: `str`
- `RegistryArn`: `str`
- `RegistryName`: `str`
- `Tags`: `Dict[str, str]`


## DescribeSchemaResponseTypeDef

```python
from mypy_boto3_schemas.type_defs import DescribeSchemaResponseTypeDef
```




Optional fields:
- `Content`: `str`
- `Description`: `str`
- `LastModified`: `datetime`
- `SchemaArn`: `str`
- `SchemaName`: `str`
- `SchemaVersion`: `str`
- `Tags`: `Dict[str, str]`
- `Type`: `str`
- `VersionCreatedDate`: `datetime`


## ExportSchemaResponseTypeDef

```python
from mypy_boto3_schemas.type_defs import ExportSchemaResponseTypeDef
```




Optional fields:
- `Content`: `str`
- `SchemaArn`: `str`
- `SchemaName`: `str`
- `SchemaVersion`: `str`
- `Type`: `str`


## GetCodeBindingSourceResponseTypeDef

```python
from mypy_boto3_schemas.type_defs import GetCodeBindingSourceResponseTypeDef
```




Optional fields:
- `Body`: `Union[bytes, IO[bytes]]`


## GetDiscoveredSchemaResponseTypeDef

```python
from mypy_boto3_schemas.type_defs import GetDiscoveredSchemaResponseTypeDef
```




Optional fields:
- `Content`: `str`


## GetResourcePolicyResponseTypeDef

```python
from mypy_boto3_schemas.type_defs import GetResourcePolicyResponseTypeDef
```




Optional fields:
- `Policy`: `str`
- `RevisionId`: `str`


## ListDiscoverersResponseTypeDef

```python
from mypy_boto3_schemas.type_defs import ListDiscoverersResponseTypeDef
```




Optional fields:
- `Discoverers`: `List["DiscovererSummaryTypeDef"]`
- `NextToken`: `str`


## ListRegistriesResponseTypeDef

```python
from mypy_boto3_schemas.type_defs import ListRegistriesResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Registries`: `List["RegistrySummaryTypeDef"]`


## ListSchemaVersionsResponseTypeDef

```python
from mypy_boto3_schemas.type_defs import ListSchemaVersionsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `SchemaVersions`: `List["SchemaVersionSummaryTypeDef"]`


## ListSchemasResponseTypeDef

```python
from mypy_boto3_schemas.type_defs import ListSchemasResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Schemas`: `List["SchemaSummaryTypeDef"]`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_schemas.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_schemas.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PutCodeBindingResponseTypeDef

```python
from mypy_boto3_schemas.type_defs import PutCodeBindingResponseTypeDef
```




Optional fields:
- `CreationDate`: `datetime`
- `LastModified`: `datetime`
- `SchemaVersion`: `str`
- `Status`: `CodeGenerationStatus`


## PutResourcePolicyResponseTypeDef

```python
from mypy_boto3_schemas.type_defs import PutResourcePolicyResponseTypeDef
```




Optional fields:
- `Policy`: `str`
- `RevisionId`: `str`


## SearchSchemasResponseTypeDef

```python
from mypy_boto3_schemas.type_defs import SearchSchemasResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Schemas`: `List["SearchSchemaSummaryTypeDef"]`


## StartDiscovererResponseTypeDef

```python
from mypy_boto3_schemas.type_defs import StartDiscovererResponseTypeDef
```




Optional fields:
- `DiscovererId`: `str`
- `State`: `DiscovererState`


## StopDiscovererResponseTypeDef

```python
from mypy_boto3_schemas.type_defs import StopDiscovererResponseTypeDef
```




Optional fields:
- `DiscovererId`: `str`
- `State`: `DiscovererState`


## UpdateDiscovererResponseTypeDef

```python
from mypy_boto3_schemas.type_defs import UpdateDiscovererResponseTypeDef
```




Optional fields:
- `Description`: `str`
- `DiscovererArn`: `str`
- `DiscovererId`: `str`
- `SourceArn`: `str`
- `State`: `DiscovererState`
- `Tags`: `Dict[str, str]`


## UpdateRegistryResponseTypeDef

```python
from mypy_boto3_schemas.type_defs import UpdateRegistryResponseTypeDef
```




Optional fields:
- `Description`: `str`
- `RegistryArn`: `str`
- `RegistryName`: `str`
- `Tags`: `Dict[str, str]`


## UpdateSchemaResponseTypeDef

```python
from mypy_boto3_schemas.type_defs import UpdateSchemaResponseTypeDef
```




Optional fields:
- `Description`: `str`
- `LastModified`: `datetime`
- `SchemaArn`: `str`
- `SchemaName`: `str`
- `SchemaVersion`: `str`
- `Tags`: `Dict[str, str]`
- `Type`: `str`
- `VersionCreatedDate`: `datetime`


## WaiterConfigTypeDef

```python
from mypy_boto3_schemas.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

