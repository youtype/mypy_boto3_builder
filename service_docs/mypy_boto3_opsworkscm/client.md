# OpsWorksCMClient for boto3 OpsWorksCM module

> [Index](../index.md) > [OpsWorksCM](./index.md) > OpsWorksCMClient

Auto-generated documentation for [OpsWorksCM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM)
type annotations stubs module [mypy_boto3_opsworkscm](https://pypi.org/project/mypy-boto3-opsworkscm/).

- [OpsWorksCMClient for boto3 OpsWorksCM module](#opsworkscmclient-for-boto3-opsworkscm-module)
  - [OpsWorksCMClient](#opsworkscmclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_node](#associate_node)
    - [can_paginate](#can_paginate)
    - [create_backup](#create_backup)
    - [create_server](#create_server)
    - [delete_backup](#delete_backup)
    - [delete_server](#delete_server)
    - [describe_account_attributes](#describe_account_attributes)
    - [describe_backups](#describe_backups)
    - [describe_events](#describe_events)
    - [describe_node_association_status](#describe_node_association_status)
    - [describe_servers](#describe_servers)
    - [disassociate_node](#disassociate_node)
    - [export_server_engine_attribute](#export_server_engine_attribute)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [restore_server](#restore_server)
    - [start_maintenance](#start_maintenance)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_server](#update_server)
    - [update_server_engine_attributes](#update_server_engine_attributes)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_waiter](#get_waiter)

## OpsWorksCMClient

Type annotations for `boto3.client("opsworkscm")`

Can be used directly:

```python
from mypy_boto3_opsworkscm.client import OpsWorksCMClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_opsworkscm.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.InvalidStateException`
- `Exceptions.LimitExceededException`
- `Exceptions.ResourceAlreadyExistsException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ValidationException`


## Methods


### associate_node

Type annotations for `boto3.client("opsworkscm").associate_node` method.

[Client.associate_node documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.associate_node)

```python
def associate_node(
    self,
    ServerName: str,
    NodeName: str,
    EngineAttributes: List["EngineAttributeTypeDef"]
) -> AssociateNodeResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("opsworkscm").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_backup

Type annotations for `boto3.client("opsworkscm").create_backup` method.

[Client.create_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.create_backup)

```python
def create_backup(
    self,
    ServerName: str,
    Description: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateBackupResponseTypeDef:
    pass
```

### create_server

Type annotations for `boto3.client("opsworkscm").create_server` method.

[Client.create_server documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.create_server)

```python
def create_server(
    self,
    Engine: str,
    ServerName: str,
    InstanceProfileArn: str,
    InstanceType: str,
    ServiceRoleArn: str,
    AssociatePublicIpAddress: bool = None,
    CustomDomain: str = None,
    CustomCertificate: str = None,
    CustomPrivateKey: str = None,
    DisableAutomatedBackup: bool = None,
    EngineModel: str = None,
    EngineVersion: str = None,
    EngineAttributes: List["EngineAttributeTypeDef"] = None,
    BackupRetentionCount: int = None,
    KeyPair: str = None,
    PreferredMaintenanceWindow: str = None,
    PreferredBackupWindow: str = None,
    SecurityGroupIds: List[str] = None,
    SubnetIds: List[str] = None,
    Tags: List["TagTypeDef"] = None,
    BackupId: str = None
) -> CreateServerResponseTypeDef:
    pass
```

### delete_backup

Type annotations for `boto3.client("opsworkscm").delete_backup` method.

[Client.delete_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.delete_backup)

```python
def delete_backup(
    self,
    BackupId: str
) -> Dict[str, Any]:
    pass
```

### delete_server

Type annotations for `boto3.client("opsworkscm").delete_server` method.

[Client.delete_server documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.delete_server)

```python
def delete_server(
    self,
    ServerName: str
) -> Dict[str, Any]:
    pass
```

### describe_account_attributes

Type annotations for `boto3.client("opsworkscm").describe_account_attributes` method.

[Client.describe_account_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_account_attributes)

```python
def describe_account_attributes(
    self
) -> DescribeAccountAttributesResponseTypeDef:
    pass
```

### describe_backups

Type annotations for `boto3.client("opsworkscm").describe_backups` method.

[Client.describe_backups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_backups)

```python
def describe_backups(
    self,
    BackupId: str = None,
    ServerName: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeBackupsResponseTypeDef:
    pass
```

### describe_events

Type annotations for `boto3.client("opsworkscm").describe_events` method.

[Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_events)

```python
def describe_events(
    self,
    ServerName: str,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeEventsResponseTypeDef:
    pass
```

### describe_node_association_status

Type annotations for `boto3.client("opsworkscm").describe_node_association_status` method.

[Client.describe_node_association_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_node_association_status)

```python
def describe_node_association_status(
    self,
    NodeAssociationStatusToken: str,
    ServerName: str
) -> DescribeNodeAssociationStatusResponseTypeDef:
    pass
```

### describe_servers

Type annotations for `boto3.client("opsworkscm").describe_servers` method.

[Client.describe_servers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_servers)

```python
def describe_servers(
    self,
    ServerName: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeServersResponseTypeDef:
    pass
```

### disassociate_node

Type annotations for `boto3.client("opsworkscm").disassociate_node` method.

[Client.disassociate_node documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.disassociate_node)

```python
def disassociate_node(
    self,
    ServerName: str,
    NodeName: str,
    EngineAttributes: List["EngineAttributeTypeDef"] = None
) -> DisassociateNodeResponseTypeDef:
    pass
```

### export_server_engine_attribute

Type annotations for `boto3.client("opsworkscm").export_server_engine_attribute` method.

[Client.export_server_engine_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.export_server_engine_attribute)

```python
def export_server_engine_attribute(
    self,
    ExportAttributeName: str,
    ServerName: str,
    InputAttributes: List["EngineAttributeTypeDef"] = None
) -> ExportServerEngineAttributeResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("opsworkscm").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("opsworkscm").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### restore_server

Type annotations for `boto3.client("opsworkscm").restore_server` method.

[Client.restore_server documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.restore_server)

```python
def restore_server(
    self,
    BackupId: str,
    ServerName: str,
    InstanceType: str = None,
    KeyPair: str = None
) -> Dict[str, Any]:
    pass
```

### start_maintenance

Type annotations for `boto3.client("opsworkscm").start_maintenance` method.

[Client.start_maintenance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.start_maintenance)

```python
def start_maintenance(
    self,
    ServerName: str,
    EngineAttributes: List["EngineAttributeTypeDef"] = None
) -> StartMaintenanceResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("opsworkscm").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("opsworkscm").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_server

Type annotations for `boto3.client("opsworkscm").update_server` method.

[Client.update_server documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.update_server)

```python
def update_server(
    self,
    ServerName: str,
    DisableAutomatedBackup: bool = None,
    BackupRetentionCount: int = None,
    PreferredMaintenanceWindow: str = None,
    PreferredBackupWindow: str = None
) -> UpdateServerResponseTypeDef:
    pass
```

### update_server_engine_attributes

Type annotations for `boto3.client("opsworkscm").update_server_engine_attributes` method.

[Client.update_server_engine_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.update_server_engine_attributes)

```python
def update_server_engine_attributes(
    self,
    ServerName: str,
    AttributeName: str,
    AttributeValue: str = None
) -> UpdateServerEngineAttributesResponseTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("opsworkscm").get_paginator` method.

[Paginator.DescribeBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeBackups)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeBackupsPaginatorName
) -> DescribeBackupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("opsworkscm").get_paginator` method.

[Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeEvents)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeEventsPaginatorName
) -> DescribeEventsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("opsworkscm").get_paginator` method.

[Paginator.DescribeServers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeServers)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeServersPaginatorName
) -> DescribeServersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("opsworkscm").get_paginator` method.

[Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Paginator.ListTagsForResource)

```python
@overload
def get_paginator(
    self,
    operation_name: ListTagsForResourcePaginatorName
) -> ListTagsForResourcePaginator:
    pass
```

### get_waiter

Type annotations for `boto3.client("opsworkscm").get_waiter` method.

[Waiter.NodeAssociated documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Waiter.NodeAssociated)

```python
def get_waiter(
    self,
    waiter_name: NodeAssociatedWaiterName
) -> NodeAssociatedWaiter:
    pass
```