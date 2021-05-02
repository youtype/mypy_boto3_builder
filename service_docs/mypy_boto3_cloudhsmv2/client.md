# CloudHSMV2Client for boto3 CloudHSMV2 module

> [Index](../index.md) > [CloudHSMV2](./index.md) > CloudHSMV2Client

Auto-generated documentation for [CloudHSMV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2)
type annotations stubs module [mypy_boto3_cloudhsmv2](https://pypi.org/project/mypy-boto3-cloudhsmv2/).

- [CloudHSMV2Client for boto3 CloudHSMV2 module](#cloudhsmv2client-for-boto3-cloudhsmv2-module)
  - [CloudHSMV2Client](#cloudhsmv2client)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [copy_backup_to_region](#copy_backup_to_region)
    - [create_cluster](#create_cluster)
    - [create_hsm](#create_hsm)
    - [delete_backup](#delete_backup)
    - [delete_cluster](#delete_cluster)
    - [delete_hsm](#delete_hsm)
    - [describe_backups](#describe_backups)
    - [describe_clusters](#describe_clusters)
    - [generate_presigned_url](#generate_presigned_url)
    - [initialize_cluster](#initialize_cluster)
    - [list_tags](#list_tags)
    - [modify_backup_attributes](#modify_backup_attributes)
    - [modify_cluster](#modify_cluster)
    - [restore_backup](#restore_backup)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)

## CloudHSMV2Client

Type annotations for `boto3.client("cloudhsmv2")`

Can be used directly:

```python
from mypy_boto3_cloudhsmv2.client import CloudHSMV2Client
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_cloudhsmv2.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.CloudHsmAccessDeniedException`
- `Exceptions.CloudHsmInternalFailureException`
- `Exceptions.CloudHsmInvalidRequestException`
- `Exceptions.CloudHsmResourceNotFoundException`
- `Exceptions.CloudHsmServiceException`
- `Exceptions.CloudHsmTagException`


## Methods


### can_paginate

Type annotations for `boto3.client("cloudhsmv2").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### copy_backup_to_region

Type annotations for `boto3.client("cloudhsmv2").copy_backup_to_region` method.

[Client.copy_backup_to_region documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.copy_backup_to_region)

```python
def copy_backup_to_region(
    self,
    DestinationRegion: str,
    BackupId: str,
    TagList: List["TagTypeDef"] = None
) -> CopyBackupToRegionResponseTypeDef:
    pass
```

### create_cluster

Type annotations for `boto3.client("cloudhsmv2").create_cluster` method.

[Client.create_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.create_cluster)

```python
def create_cluster(
    self,
    HsmType: str,
    SubnetIds: List[str],
    BackupRetentionPolicy: "BackupRetentionPolicyTypeDef" = None,
    SourceBackupId: str = None,
    TagList: List["TagTypeDef"] = None
) -> CreateClusterResponseTypeDef:
    pass
```

### create_hsm

Type annotations for `boto3.client("cloudhsmv2").create_hsm` method.

[Client.create_hsm documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.create_hsm)

```python
def create_hsm(
    self,
    ClusterId: str,
    AvailabilityZone: str,
    IpAddress: str = None
) -> CreateHsmResponseTypeDef:
    pass
```

### delete_backup

Type annotations for `boto3.client("cloudhsmv2").delete_backup` method.

[Client.delete_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.delete_backup)

```python
def delete_backup(
    self,
    BackupId: str
) -> DeleteBackupResponseTypeDef:
    pass
```

### delete_cluster

Type annotations for `boto3.client("cloudhsmv2").delete_cluster` method.

[Client.delete_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.delete_cluster)

```python
def delete_cluster(
    self,
    ClusterId: str
) -> DeleteClusterResponseTypeDef:
    pass
```

### delete_hsm

Type annotations for `boto3.client("cloudhsmv2").delete_hsm` method.

[Client.delete_hsm documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.delete_hsm)

```python
def delete_hsm(
    self,
    ClusterId: str,
    HsmId: str = None,
    EniId: str = None,
    EniIp: str = None
) -> DeleteHsmResponseTypeDef:
    pass
```

### describe_backups

Type annotations for `boto3.client("cloudhsmv2").describe_backups` method.

[Client.describe_backups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.describe_backups)

```python
def describe_backups(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    Filters: Dict[str, List[str]] = None,
    SortAscending: bool = None
) -> DescribeBackupsResponseTypeDef:
    pass
```

### describe_clusters

Type annotations for `boto3.client("cloudhsmv2").describe_clusters` method.

[Client.describe_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.describe_clusters)

```python
def describe_clusters(
    self,
    Filters: Dict[str, List[str]] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeClustersResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("cloudhsmv2").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.generate_presigned_url)

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

### initialize_cluster

Type annotations for `boto3.client("cloudhsmv2").initialize_cluster` method.

[Client.initialize_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.initialize_cluster)

```python
def initialize_cluster(
    self,
    ClusterId: str,
    SignedCert: str,
    TrustAnchor: str
) -> InitializeClusterResponseTypeDef:
    pass
```

### list_tags

Type annotations for `boto3.client("cloudhsmv2").list_tags` method.

[Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.list_tags)

```python
def list_tags(
    self,
    ResourceId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListTagsResponseTypeDef:
    pass
```

### modify_backup_attributes

Type annotations for `boto3.client("cloudhsmv2").modify_backup_attributes` method.

[Client.modify_backup_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.modify_backup_attributes)

```python
def modify_backup_attributes(
    self,
    BackupId: str,
    NeverExpires: bool
) -> ModifyBackupAttributesResponseTypeDef:
    pass
```

### modify_cluster

Type annotations for `boto3.client("cloudhsmv2").modify_cluster` method.

[Client.modify_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.modify_cluster)

```python
def modify_cluster(
    self,
    BackupRetentionPolicy: "BackupRetentionPolicyTypeDef",
    ClusterId: str
) -> ModifyClusterResponseTypeDef:
    pass
```

### restore_backup

Type annotations for `boto3.client("cloudhsmv2").restore_backup` method.

[Client.restore_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.restore_backup)

```python
def restore_backup(
    self,
    BackupId: str
) -> RestoreBackupResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("cloudhsmv2").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceId: str,
    TagList: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("cloudhsmv2").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceId: str,
    TagKeyList: List[str]
) -> Dict[str, Any]:
    pass
```

### get_paginator

Type annotations for `boto3.client("cloudhsmv2").get_paginator` method.

[Paginator.DescribeBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Paginator.DescribeBackups)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeBackupsPaginatorName
) -> DescribeBackupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("cloudhsmv2").get_paginator` method.

[Paginator.DescribeClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Paginator.DescribeClusters)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeClustersPaginatorName
) -> DescribeClustersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("cloudhsmv2").get_paginator` method.

[Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Paginator.ListTags)

```python
@overload
def get_paginator(
    self,
    operation_name: ListTagsPaginatorName
) -> ListTagsPaginator:
    pass
```