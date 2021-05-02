# Type annotations for boto3 IoTSecureTunneling module

> [Index](../index.md) > IoTSecureTunneling

Auto-generated documentation for [IoTSecureTunneling](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsecuretunneling.html#IoTSecureTunneling)
type annotations stubs module [mypy_boto3_iotsecuretunneling](https://pypi.org/project/mypy-boto3-iotsecuretunneling/).

```bash
pip install mypy-boto3-iotsecuretunneling
```

- [Type annotations for boto3 IoTSecureTunneling module](#type-annotations-for-boto3-iotsecuretunneling-module)
  - [IoTSecureTunnelingClient](#iotsecuretunnelingclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## IoTSecureTunnelingClient

Type annotations for  `boto3.client("iotsecuretunneling")` as [IoTSecureTunnelingClient](./client.md)

Can be used directly:

```python
from mypy_boto3_iotsecuretunneling.client import IoTSecureTunnelingClient
```


IoTSecureTunnelingClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [close_tunnel](./client.md#close-tunnel)
- [describe_tunnel](./client.md#describe-tunnel)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_tunnels](./client.md#list-tunnels)
- [open_tunnel](./client.md#open-tunnel)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)




### Exceptions
- [ClientError](./client.md#clienterror)
- [LimitExceededException](./client.md#limitexceededexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_iotsecuretunneling.literals import ConnectionStatus, ...
```

- [ConnectionStatus](./literals.md#connectionstatus)
- [TunnelStatus](./literals.md#tunnelstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_iotsecuretunneling.type_defs import ConnectionStateTypeDef, ...
```

- [ConnectionStateTypeDef](./type_defs.md#connectionstatetypedef)
- [DescribeTunnelResponseTypeDef](./type_defs.md#describetunnelresponsetypedef)
- [DestinationConfigTypeDef](./type_defs.md#destinationconfigtypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ListTunnelsResponseTypeDef](./type_defs.md#listtunnelsresponsetypedef)
- [OpenTunnelResponseTypeDef](./type_defs.md#opentunnelresponsetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TimeoutConfigTypeDef](./type_defs.md#timeoutconfigtypedef)
- [TunnelSummaryTypeDef](./type_defs.md#tunnelsummarytypedef)
- [TunnelTypeDef](./type_defs.md#tunneltypedef)
