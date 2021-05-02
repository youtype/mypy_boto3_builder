# GlacierClient for boto3 Glacier module

> [Index](../index.md) > [Glacier](./index.md) > GlacierClient

Auto-generated documentation for [Glacier](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier)
type annotations stubs module [mypy_boto3_glacier](https://pypi.org/project/mypy-boto3-glacier/).

- [GlacierClient for boto3 Glacier module](#glacierclient-for-boto3-glacier-module)
  - [GlacierClient](#glacierclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [abort_multipart_upload](#abort_multipart_upload)
    - [abort_vault_lock](#abort_vault_lock)
    - [add_tags_to_vault](#add_tags_to_vault)
    - [can_paginate](#can_paginate)
    - [complete_multipart_upload](#complete_multipart_upload)
    - [complete_vault_lock](#complete_vault_lock)
    - [create_vault](#create_vault)
    - [delete_archive](#delete_archive)
    - [delete_vault](#delete_vault)
    - [delete_vault_access_policy](#delete_vault_access_policy)
    - [delete_vault_notifications](#delete_vault_notifications)
    - [describe_job](#describe_job)
    - [describe_vault](#describe_vault)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_data_retrieval_policy](#get_data_retrieval_policy)
    - [get_job_output](#get_job_output)
    - [get_vault_access_policy](#get_vault_access_policy)
    - [get_vault_lock](#get_vault_lock)
    - [get_vault_notifications](#get_vault_notifications)
    - [initiate_job](#initiate_job)
    - [initiate_multipart_upload](#initiate_multipart_upload)
    - [initiate_vault_lock](#initiate_vault_lock)
    - [list_jobs](#list_jobs)
    - [list_multipart_uploads](#list_multipart_uploads)
    - [list_parts](#list_parts)
    - [list_provisioned_capacity](#list_provisioned_capacity)
    - [list_tags_for_vault](#list_tags_for_vault)
    - [list_vaults](#list_vaults)
    - [purchase_provisioned_capacity](#purchase_provisioned_capacity)
    - [remove_tags_from_vault](#remove_tags_from_vault)
    - [set_data_retrieval_policy](#set_data_retrieval_policy)
    - [set_vault_access_policy](#set_vault_access_policy)
    - [set_vault_notifications](#set_vault_notifications)
    - [upload_archive](#upload_archive)
    - [upload_multipart_part](#upload_multipart_part)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_waiter](#get_waiter)
    - [get_waiter](#get_waiter-1)

## GlacierClient

Type annotations for `boto3.client("glacier")`

Can be used directly:

```python
from mypy_boto3_glacier.client import GlacierClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_glacier.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InsufficientCapacityException`
- `Exceptions.InvalidParameterValueException`
- `Exceptions.LimitExceededException`
- `Exceptions.MissingParameterValueException`
- `Exceptions.PolicyEnforcedException`
- `Exceptions.RequestTimeoutException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceUnavailableException`


## Methods


### abort_multipart_upload

Type annotations for `boto3.client("glacier").abort_multipart_upload` method.

[Client.abort_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.abort_multipart_upload)

```python
def abort_multipart_upload(
    self,
    accountId: str,
    vaultName: str,
    uploadId: str
) -> None:
    pass
```

### abort_vault_lock

Type annotations for `boto3.client("glacier").abort_vault_lock` method.

[Client.abort_vault_lock documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.abort_vault_lock)

```python
def abort_vault_lock(
    self,
    accountId: str,
    vaultName: str
) -> None:
    pass
```

### add_tags_to_vault

Type annotations for `boto3.client("glacier").add_tags_to_vault` method.

[Client.add_tags_to_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.add_tags_to_vault)

```python
def add_tags_to_vault(
    self,
    accountId: str,
    vaultName: str,
    Tags: Dict[str, str] = None
) -> None:
    pass
```

### can_paginate

Type annotations for `boto3.client("glacier").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### complete_multipart_upload

Type annotations for `boto3.client("glacier").complete_multipart_upload` method.

[Client.complete_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.complete_multipart_upload)

```python
def complete_multipart_upload(
    self,
    accountId: str,
    vaultName: str,
    uploadId: str,
    archiveSize: str = None,
    checksum: str = None
) -> ArchiveCreationOutputTypeDef:
    pass
```

### complete_vault_lock

Type annotations for `boto3.client("glacier").complete_vault_lock` method.

[Client.complete_vault_lock documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.complete_vault_lock)

```python
def complete_vault_lock(
    self,
    accountId: str,
    vaultName: str,
    lockId: str
) -> None:
    pass
```

### create_vault

Type annotations for `boto3.client("glacier").create_vault` method.

[Client.create_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.create_vault)

```python
def create_vault(
    self,
    accountId: str,
    vaultName: str
) -> CreateVaultOutputTypeDef:
    pass
```

### delete_archive

Type annotations for `boto3.client("glacier").delete_archive` method.

[Client.delete_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.delete_archive)

```python
def delete_archive(
    self,
    accountId: str,
    vaultName: str,
    archiveId: str
) -> None:
    pass
```

### delete_vault

Type annotations for `boto3.client("glacier").delete_vault` method.

[Client.delete_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.delete_vault)

```python
def delete_vault(
    self,
    accountId: str,
    vaultName: str
) -> None:
    pass
```

### delete_vault_access_policy

Type annotations for `boto3.client("glacier").delete_vault_access_policy` method.

[Client.delete_vault_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.delete_vault_access_policy)

```python
def delete_vault_access_policy(
    self,
    accountId: str,
    vaultName: str
) -> None:
    pass
```

### delete_vault_notifications

Type annotations for `boto3.client("glacier").delete_vault_notifications` method.

[Client.delete_vault_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.delete_vault_notifications)

```python
def delete_vault_notifications(
    self,
    accountId: str,
    vaultName: str
) -> None:
    pass
```

### describe_job

Type annotations for `boto3.client("glacier").describe_job` method.

[Client.describe_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.describe_job)

```python
def describe_job(
    self,
    accountId: str,
    vaultName: str,
    jobId: str
) -> "GlacierJobDescriptionTypeDef":
    pass
```

### describe_vault

Type annotations for `boto3.client("glacier").describe_vault` method.

[Client.describe_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.describe_vault)

```python
def describe_vault(
    self,
    accountId: str,
    vaultName: str
) -> "DescribeVaultOutputTypeDef":
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("glacier").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.generate_presigned_url)

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

### get_data_retrieval_policy

Type annotations for `boto3.client("glacier").get_data_retrieval_policy` method.

[Client.get_data_retrieval_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.get_data_retrieval_policy)

```python
def get_data_retrieval_policy(
    self,
    accountId: str
) -> GetDataRetrievalPolicyOutputTypeDef:
    pass
```

### get_job_output

Type annotations for `boto3.client("glacier").get_job_output` method.

[Client.get_job_output documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.get_job_output)

```python
def get_job_output(
    self,
    accountId: str,
    vaultName: str,
    jobId: str,
    range: str = None
) -> GetJobOutputOutputTypeDef:
    pass
```

### get_vault_access_policy

Type annotations for `boto3.client("glacier").get_vault_access_policy` method.

[Client.get_vault_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.get_vault_access_policy)

```python
def get_vault_access_policy(
    self,
    accountId: str,
    vaultName: str
) -> GetVaultAccessPolicyOutputTypeDef:
    pass
```

### get_vault_lock

Type annotations for `boto3.client("glacier").get_vault_lock` method.

[Client.get_vault_lock documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.get_vault_lock)

```python
def get_vault_lock(
    self,
    accountId: str,
    vaultName: str
) -> GetVaultLockOutputTypeDef:
    pass
```

### get_vault_notifications

Type annotations for `boto3.client("glacier").get_vault_notifications` method.

[Client.get_vault_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.get_vault_notifications)

```python
def get_vault_notifications(
    self,
    accountId: str,
    vaultName: str
) -> GetVaultNotificationsOutputTypeDef:
    pass
```

### initiate_job

Type annotations for `boto3.client("glacier").initiate_job` method.

[Client.initiate_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.initiate_job)

```python
def initiate_job(
    self,
    accountId: str,
    vaultName: str,
    jobParameters: JobParametersTypeDef = None
) -> InitiateJobOutputTypeDef:
    pass
```

### initiate_multipart_upload

Type annotations for `boto3.client("glacier").initiate_multipart_upload` method.

[Client.initiate_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.initiate_multipart_upload)

```python
def initiate_multipart_upload(
    self,
    accountId: str,
    vaultName: str,
    archiveDescription: str = None,
    partSize: str = None
) -> InitiateMultipartUploadOutputTypeDef:
    pass
```

### initiate_vault_lock

Type annotations for `boto3.client("glacier").initiate_vault_lock` method.

[Client.initiate_vault_lock documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.initiate_vault_lock)

```python
def initiate_vault_lock(
    self,
    accountId: str,
    vaultName: str,
    policy: VaultLockPolicyTypeDef = None
) -> InitiateVaultLockOutputTypeDef:
    pass
```

### list_jobs

Type annotations for `boto3.client("glacier").list_jobs` method.

[Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.list_jobs)

```python
def list_jobs(
    self,
    accountId: str,
    vaultName: str,
    limit: str = None,
    marker: str = None,
    statuscode: str = None,
    completed: str = None
) -> ListJobsOutputTypeDef:
    pass
```

### list_multipart_uploads

Type annotations for `boto3.client("glacier").list_multipart_uploads` method.

[Client.list_multipart_uploads documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.list_multipart_uploads)

```python
def list_multipart_uploads(
    self,
    accountId: str,
    vaultName: str,
    marker: str = None,
    limit: str = None
) -> ListMultipartUploadsOutputTypeDef:
    pass
```

### list_parts

Type annotations for `boto3.client("glacier").list_parts` method.

[Client.list_parts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.list_parts)

```python
def list_parts(
    self,
    accountId: str,
    vaultName: str,
    uploadId: str,
    marker: str = None,
    limit: str = None
) -> ListPartsOutputTypeDef:
    pass
```

### list_provisioned_capacity

Type annotations for `boto3.client("glacier").list_provisioned_capacity` method.

[Client.list_provisioned_capacity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.list_provisioned_capacity)

```python
def list_provisioned_capacity(
    self,
    accountId: str
) -> ListProvisionedCapacityOutputTypeDef:
    pass
```

### list_tags_for_vault

Type annotations for `boto3.client("glacier").list_tags_for_vault` method.

[Client.list_tags_for_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.list_tags_for_vault)

```python
def list_tags_for_vault(
    self,
    accountId: str,
    vaultName: str
) -> ListTagsForVaultOutputTypeDef:
    pass
```

### list_vaults

Type annotations for `boto3.client("glacier").list_vaults` method.

[Client.list_vaults documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.list_vaults)

```python
def list_vaults(
    self,
    accountId: str,
    marker: str = None,
    limit: str = None
) -> ListVaultsOutputTypeDef:
    pass
```

### purchase_provisioned_capacity

Type annotations for `boto3.client("glacier").purchase_provisioned_capacity` method.

[Client.purchase_provisioned_capacity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.purchase_provisioned_capacity)

```python
def purchase_provisioned_capacity(
    self,
    accountId: str
) -> PurchaseProvisionedCapacityOutputTypeDef:
    pass
```

### remove_tags_from_vault

Type annotations for `boto3.client("glacier").remove_tags_from_vault` method.

[Client.remove_tags_from_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.remove_tags_from_vault)

```python
def remove_tags_from_vault(
    self,
    accountId: str,
    vaultName: str,
    TagKeys: List[str] = None
) -> None:
    pass
```

### set_data_retrieval_policy

Type annotations for `boto3.client("glacier").set_data_retrieval_policy` method.

[Client.set_data_retrieval_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.set_data_retrieval_policy)

```python
def set_data_retrieval_policy(
    self,
    accountId: str,
    Policy: "DataRetrievalPolicyTypeDef" = None
) -> None:
    pass
```

### set_vault_access_policy

Type annotations for `boto3.client("glacier").set_vault_access_policy` method.

[Client.set_vault_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.set_vault_access_policy)

```python
def set_vault_access_policy(
    self,
    accountId: str,
    vaultName: str,
    policy: "VaultAccessPolicyTypeDef" = None
) -> None:
    pass
```

### set_vault_notifications

Type annotations for `boto3.client("glacier").set_vault_notifications` method.

[Client.set_vault_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.set_vault_notifications)

```python
def set_vault_notifications(
    self,
    accountId: str,
    vaultName: str,
    vaultNotificationConfig: "VaultNotificationConfigTypeDef" = None
) -> None:
    pass
```

### upload_archive

Type annotations for `boto3.client("glacier").upload_archive` method.

[Client.upload_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.upload_archive)

```python
def upload_archive(
    self,
    vaultName: str,
    accountId: str,
    archiveDescription: str = None,
    checksum: str = None,
    body: Union[bytes, IO[bytes]] = None
) -> ArchiveCreationOutputTypeDef:
    pass
```

### upload_multipart_part

Type annotations for `boto3.client("glacier").upload_multipart_part` method.

[Client.upload_multipart_part documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.upload_multipart_part)

```python
def upload_multipart_part(
    self,
    accountId: str,
    vaultName: str,
    uploadId: str,
    checksum: str = None,
    range: str = None,
    body: Union[bytes, IO[bytes]] = None
) -> UploadMultipartPartOutputTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("glacier").get_paginator` method.

[Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Paginator.ListJobs)

```python
@overload
def get_paginator(
    self,
    operation_name: ListJobsPaginatorName
) -> ListJobsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("glacier").get_paginator` method.

[Paginator.ListMultipartUploads documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Paginator.ListMultipartUploads)

```python
@overload
def get_paginator(
    self,
    operation_name: ListMultipartUploadsPaginatorName
) -> ListMultipartUploadsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("glacier").get_paginator` method.

[Paginator.ListParts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Paginator.ListParts)

```python
@overload
def get_paginator(
    self,
    operation_name: ListPartsPaginatorName
) -> ListPartsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("glacier").get_paginator` method.

[Paginator.ListVaults documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Paginator.ListVaults)

```python
@overload
def get_paginator(
    self,
    operation_name: ListVaultsPaginatorName
) -> ListVaultsPaginator:
    pass
```

### get_waiter

Type annotations for `boto3.client("glacier").get_waiter` method.

[Waiter.VaultExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Waiter.VaultExists)

```python
@overload
def get_waiter(
    self,
    waiter_name: VaultExistsWaiterName
) -> VaultExistsWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("glacier").get_waiter` method.

[Waiter.VaultNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Waiter.VaultNotExists)

```python
@overload
def get_waiter(
    self,
    waiter_name: VaultNotExistsWaiterName
) -> VaultNotExistsWaiter:
    pass
```