# Type annotations for boto3 CloudHSMV2 module

> [Index](../index.md) > CloudHSMV2

Auto-generated documentation for [CloudHSMV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2)
type annotations stubs module [mypy_boto3_cloudhsmv2](https://pypi.org/project/mypy-boto3-cloudhsmv2/).

```bash
pip install mypy-boto3-cloudhsmv2
```

- [Type annotations for boto3 CloudHSMV2 module](#type-annotations-for-boto3-cloudhsmv2-module)
  - [CloudHSMV2Client](#cloudhsmv2client)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## CloudHSMV2Client

Type annotations for  `boto3.client("cloudhsmv2")` as [CloudHSMV2Client](./client.md)

Can be used directly:

```python
from mypy_boto3_cloudhsmv2.client import CloudHSMV2Client
```


CloudHSMV2Client [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [copy_backup_to_region](./client.md#copy-backup-to-region)
- [create_cluster](./client.md#create-cluster)
- [create_hsm](./client.md#create-hsm)
- [delete_backup](./client.md#delete-backup)
- [delete_cluster](./client.md#delete-cluster)
- [delete_hsm](./client.md#delete-hsm)
- [describe_backups](./client.md#describe-backups)
- [describe_clusters](./client.md#describe-clusters)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [initialize_cluster](./client.md#initialize-cluster)
- [list_tags](./client.md#list-tags)
- [modify_backup_attributes](./client.md#modify-backup-attributes)
- [modify_cluster](./client.md#modify-cluster)
- [restore_backup](./client.md#restore-backup)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)




### Exceptions
- [ClientError](./client.md#clienterror)
- [CloudHsmAccessDeniedException](./client.md#cloudhsmaccessdeniedexception)
- [CloudHsmInternalFailureException](./client.md#cloudhsminternalfailureexception)
- [CloudHsmInvalidRequestException](./client.md#cloudhsminvalidrequestexception)
- [CloudHsmResourceNotFoundException](./client.md#cloudhsmresourcenotfoundexception)
- [CloudHsmServiceException](./client.md#cloudhsmserviceexception)
- [CloudHsmTagException](./client.md#cloudhsmtagexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("cloudhsmv2").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_cloudhsmv2.paginators import DescribeBackupsPaginator, ...
```

- [DescribeBackupsPaginator](./paginators.md#describebackupspaginator)
- [DescribeClustersPaginator](./paginators.md#describeclusterspaginator)
- [ListTagsPaginator](./paginators.md#listtagspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_cloudhsmv2.literals import BackupPolicy, ...
```

- [BackupPolicy](./literals.md#backuppolicy)
- [BackupRetentionType](./literals.md#backupretentiontype)
- [BackupState](./literals.md#backupstate)
- [ClusterState](./literals.md#clusterstate)
- [DescribeBackupsPaginatorName](./literals.md#describebackupspaginatorname)
- [DescribeClustersPaginatorName](./literals.md#describeclusterspaginatorname)
- [HsmState](./literals.md#hsmstate)
- [ListTagsPaginatorName](./literals.md#listtagspaginatorname)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_cloudhsmv2.type_defs import BackupRetentionPolicyTypeDef, ...
```

- [BackupRetentionPolicyTypeDef](./type_defs.md#backupretentionpolicytypedef)
- [BackupTypeDef](./type_defs.md#backuptypedef)
- [CertificatesTypeDef](./type_defs.md#certificatestypedef)
- [ClusterTypeDef](./type_defs.md#clustertypedef)
- [CopyBackupToRegionResponseTypeDef](./type_defs.md#copybackuptoregionresponsetypedef)
- [CreateClusterResponseTypeDef](./type_defs.md#createclusterresponsetypedef)
- [CreateHsmResponseTypeDef](./type_defs.md#createhsmresponsetypedef)
- [DeleteBackupResponseTypeDef](./type_defs.md#deletebackupresponsetypedef)
- [DeleteClusterResponseTypeDef](./type_defs.md#deleteclusterresponsetypedef)
- [DeleteHsmResponseTypeDef](./type_defs.md#deletehsmresponsetypedef)
- [DescribeBackupsResponseTypeDef](./type_defs.md#describebackupsresponsetypedef)
- [DescribeClustersResponseTypeDef](./type_defs.md#describeclustersresponsetypedef)
- [DestinationBackupTypeDef](./type_defs.md#destinationbackuptypedef)
- [HsmTypeDef](./type_defs.md#hsmtypedef)
- [InitializeClusterResponseTypeDef](./type_defs.md#initializeclusterresponsetypedef)
- [ListTagsResponseTypeDef](./type_defs.md#listtagsresponsetypedef)
- [ModifyBackupAttributesResponseTypeDef](./type_defs.md#modifybackupattributesresponsetypedef)
- [ModifyClusterResponseTypeDef](./type_defs.md#modifyclusterresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [RestoreBackupResponseTypeDef](./type_defs.md#restorebackupresponsetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
