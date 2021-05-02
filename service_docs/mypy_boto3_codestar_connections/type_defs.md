# Structures for boto3 CodeStarconnections module

> [Index](../index.md) > [CodeStarconnections](./index.md) > Structures

Auto-generated documentation for [CodeStarconnections](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections)
type annotations stubs module [mypy_boto3_codestar_connections](https://pypi.org/project/mypy-boto3-codestar-connections/).

- [Structures for boto3 CodeStarconnections module](#structures-for-boto3-codestarconnections-module)
  - [ConnectionTypeDef](#connectiontypedef)
  - [CreateConnectionOutputTypeDef](#createconnectionoutputtypedef)
  - [CreateHostOutputTypeDef](#createhostoutputtypedef)
  - [GetConnectionOutputTypeDef](#getconnectionoutputtypedef)
  - [GetHostOutputTypeDef](#gethostoutputtypedef)
  - [HostTypeDef](#hosttypedef)
  - [ListConnectionsOutputTypeDef](#listconnectionsoutputtypedef)
  - [ListHostsOutputTypeDef](#listhostsoutputtypedef)
  - [ListTagsForResourceOutputTypeDef](#listtagsforresourceoutputtypedef)
  - [ResponseMetadata](#responsemetadata)
  - [TagTypeDef](#tagtypedef)
  - [VpcConfigurationTypeDef](#vpcconfigurationtypedef)

## ConnectionTypeDef

```python
from mypy_boto3_codestar_connections.type_defs import ConnectionTypeDef
```




Optional fields:
- `ConnectionName`: `str`
- `ConnectionArn`: `str`
- `ProviderType`: `ProviderType`
- `OwnerAccountId`: `str`
- `ConnectionStatus`: `ConnectionStatus`
- `HostArn`: `str`


## CreateConnectionOutputTypeDef

```python
from mypy_boto3_codestar_connections.type_defs import CreateConnectionOutputTypeDef
```


Required fields:
- `ConnectionArn`: `str`



Optional fields:
- `Tags`: `List["TagTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateHostOutputTypeDef

```python
from mypy_boto3_codestar_connections.type_defs import CreateHostOutputTypeDef
```




Optional fields:
- `HostArn`: `str`
- `Tags`: `List["TagTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetConnectionOutputTypeDef

```python
from mypy_boto3_codestar_connections.type_defs import GetConnectionOutputTypeDef
```




Optional fields:
- `Connection`: `"ConnectionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetHostOutputTypeDef

```python
from mypy_boto3_codestar_connections.type_defs import GetHostOutputTypeDef
```




Optional fields:
- `Name`: `str`
- `Status`: `str`
- `ProviderType`: `ProviderType`
- `ProviderEndpoint`: `str`
- `VpcConfiguration`: `"VpcConfigurationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## HostTypeDef

```python
from mypy_boto3_codestar_connections.type_defs import HostTypeDef
```




Optional fields:
- `Name`: `str`
- `HostArn`: `str`
- `ProviderType`: `ProviderType`
- `ProviderEndpoint`: `str`
- `VpcConfiguration`: `"VpcConfigurationTypeDef"`
- `Status`: `str`
- `StatusMessage`: `str`


## ListConnectionsOutputTypeDef

```python
from mypy_boto3_codestar_connections.type_defs import ListConnectionsOutputTypeDef
```




Optional fields:
- `Connections`: `List["ConnectionTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListHostsOutputTypeDef

```python
from mypy_boto3_codestar_connections.type_defs import ListHostsOutputTypeDef
```




Optional fields:
- `Hosts`: `List["HostTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTagsForResourceOutputTypeDef

```python
from mypy_boto3_codestar_connections.type_defs import ListTagsForResourceOutputTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ResponseMetadata

```python
from mypy_boto3_codestar_connections.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## TagTypeDef

```python
from mypy_boto3_codestar_connections.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## VpcConfigurationTypeDef

```python
from mypy_boto3_codestar_connections.type_defs import VpcConfigurationTypeDef
```


Required fields:
- `VpcId`: `str`
- `SubnetIds`: `List[str]`
- `SecurityGroupIds`: `List[str]`



Optional fields:
- `TlsCertificate`: `str`

