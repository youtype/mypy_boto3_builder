# Type annotations for boto3 OpsWorksCM module

> [Index](../index.md) > OpsWorksCM

Auto-generated documentation for [OpsWorksCM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM)
type annotations stubs module [mypy_boto3_opsworkscm](https://pypi.org/project/mypy-boto3-opsworkscm/).

```bash
pip install mypy-boto3-opsworkscm
```

- [Type annotations for boto3 OpsWorksCM module](#type-annotations-for-boto3-opsworkscm-module)
  - [OpsWorksCMClient](#opsworkscmclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## OpsWorksCMClient

Type annotations for  `boto3.client("opsworkscm")` as [OpsWorksCMClient](./client.md)

Can be used directly:

```python
from mypy_boto3_opsworkscm.client import OpsWorksCMClient
```


OpsWorksCMClient [exceptions](./client.md#exceptions)



### Methods
- [associate_node](./client.md#associate-node)
- [can_paginate](./client.md#can-paginate)
- [create_backup](./client.md#create-backup)
- [create_server](./client.md#create-server)
- [delete_backup](./client.md#delete-backup)
- [delete_server](./client.md#delete-server)
- [describe_account_attributes](./client.md#describe-account-attributes)
- [describe_backups](./client.md#describe-backups)
- [describe_events](./client.md#describe-events)
- [describe_node_association_status](./client.md#describe-node-association-status)
- [describe_servers](./client.md#describe-servers)
- [disassociate_node](./client.md#disassociate-node)
- [export_server_engine_attribute](./client.md#export-server-engine-attribute)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_waiter](./client.md#get-waiter)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [restore_server](./client.md#restore-server)
- [start_maintenance](./client.md#start-maintenance)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_server](./client.md#update-server)
- [update_server_engine_attributes](./client.md#update-server-engine-attributes)




### Exceptions
- [ClientError](./client.md#clienterror)
- [InvalidNextTokenException](./client.md#invalidnexttokenexception)
- [InvalidStateException](./client.md#invalidstateexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ResourceAlreadyExistsException](./client.md#resourcealreadyexistsexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("opsworkscm").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_opsworkscm.paginators import DescribeBackupsPaginator, ...
```

- [DescribeBackupsPaginator](./paginators.md#describebackupspaginator)
- [DescribeEventsPaginator](./paginators.md#describeeventspaginator)
- [DescribeServersPaginator](./paginators.md#describeserverspaginator)
- [ListTagsForResourcePaginator](./paginators.md#listtagsforresourcepaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("opsworkscm").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_opsworkscm.waiters import NodeAssociatedWaiter, ...
```

- [NodeAssociatedWaiter](./waiters.md#nodeassociatedwaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_opsworkscm.literals import BackupStatus, ...
```

- [BackupStatus](./literals.md#backupstatus)
- [BackupType](./literals.md#backuptype)
- [DescribeBackupsPaginatorName](./literals.md#describebackupspaginatorname)
- [DescribeEventsPaginatorName](./literals.md#describeeventspaginatorname)
- [DescribeServersPaginatorName](./literals.md#describeserverspaginatorname)
- [ListTagsForResourcePaginatorName](./literals.md#listtagsforresourcepaginatorname)
- [MaintenanceStatus](./literals.md#maintenancestatus)
- [NodeAssociatedWaiterName](./literals.md#nodeassociatedwaitername)
- [NodeAssociationStatus](./literals.md#nodeassociationstatus)
- [ServerStatus](./literals.md#serverstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_opsworkscm.type_defs import AccountAttributeTypeDef, ...
```

- [AccountAttributeTypeDef](./type_defs.md#accountattributetypedef)
- [AssociateNodeResponseTypeDef](./type_defs.md#associatenoderesponsetypedef)
- [BackupTypeDef](./type_defs.md#backuptypedef)
- [CreateBackupResponseTypeDef](./type_defs.md#createbackupresponsetypedef)
- [CreateServerResponseTypeDef](./type_defs.md#createserverresponsetypedef)
- [DescribeAccountAttributesResponseTypeDef](./type_defs.md#describeaccountattributesresponsetypedef)
- [DescribeBackupsResponseTypeDef](./type_defs.md#describebackupsresponsetypedef)
- [DescribeEventsResponseTypeDef](./type_defs.md#describeeventsresponsetypedef)
- [DescribeNodeAssociationStatusResponseTypeDef](./type_defs.md#describenodeassociationstatusresponsetypedef)
- [DescribeServersResponseTypeDef](./type_defs.md#describeserversresponsetypedef)
- [DisassociateNodeResponseTypeDef](./type_defs.md#disassociatenoderesponsetypedef)
- [EngineAttributeTypeDef](./type_defs.md#engineattributetypedef)
- [ExportServerEngineAttributeResponseTypeDef](./type_defs.md#exportserverengineattributeresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ServerEventTypeDef](./type_defs.md#servereventtypedef)
- [ServerTypeDef](./type_defs.md#servertypedef)
- [StartMaintenanceResponseTypeDef](./type_defs.md#startmaintenanceresponsetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [UpdateServerEngineAttributesResponseTypeDef](./type_defs.md#updateserverengineattributesresponsetypedef)
- [UpdateServerResponseTypeDef](./type_defs.md#updateserverresponsetypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
