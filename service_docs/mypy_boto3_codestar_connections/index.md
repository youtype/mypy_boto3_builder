# Type annotations for boto3 CodeStarconnections module

> [Index](../index.md) > CodeStarconnections

Auto-generated documentation for [CodeStarconnections](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html#CodeStarconnections)
type annotations stubs module [mypy_boto3_codestar_connections](https://pypi.org/project/mypy-boto3-codestar-connections/).

```bash
pip install mypy-boto3-codestar-connections
```

- [Type annotations for boto3 CodeStarconnections module](#type-annotations-for-boto3-codestarconnections-module)
  - [CodeStarconnectionsClient](#codestarconnectionsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## CodeStarconnectionsClient

Type annotations for  `boto3.client("codestar-connections")` as [CodeStarconnectionsClient](./client.md)

Can be used directly:

```python
from mypy_boto3_codestar_connections.client import CodeStarconnectionsClient
```


CodeStarconnectionsClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_connection](./client.md#create-connection)
- [create_host](./client.md#create-host)
- [delete_connection](./client.md#delete-connection)
- [delete_host](./client.md#delete-host)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_connection](./client.md#get-connection)
- [get_host](./client.md#get-host)
- [list_connections](./client.md#list-connections)
- [list_hosts](./client.md#list-hosts)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_host](./client.md#update-host)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ResourceUnavailableException](./client.md#resourceunavailableexception)
- [UnsupportedOperationException](./client.md#unsupportedoperationexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_codestar_connections.literals import ConnectionStatus, ...
```

- [ConnectionStatus](./literals.md#connectionstatus)
- [ProviderType](./literals.md#providertype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_codestar_connections.type_defs import ConnectionTypeDef, ...
```

- [ConnectionTypeDef](./type_defs.md#connectiontypedef)
- [CreateConnectionOutputTypeDef](./type_defs.md#createconnectionoutputtypedef)
- [CreateHostOutputTypeDef](./type_defs.md#createhostoutputtypedef)
- [GetConnectionOutputTypeDef](./type_defs.md#getconnectionoutputtypedef)
- [GetHostOutputTypeDef](./type_defs.md#gethostoutputtypedef)
- [HostTypeDef](./type_defs.md#hosttypedef)
- [ListConnectionsOutputTypeDef](./type_defs.md#listconnectionsoutputtypedef)
- [ListHostsOutputTypeDef](./type_defs.md#listhostsoutputtypedef)
- [ListTagsForResourceOutputTypeDef](./type_defs.md#listtagsforresourceoutputtypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [VpcConfigurationTypeDef](./type_defs.md#vpcconfigurationtypedef)
