# GlacierServiceResource for boto3 Glacier module

> [Index](../index.md) > [Glacier](./index.md) > GlacierServiceResource

Auto-generated documentation for [Glacier](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier)
type annotations stubs module [mypy_boto3_glacier](https://pypi.org/project/mypy-boto3-glacier/).

- [GlacierServiceResource for boto3 Glacier module](#glacierserviceresource-for-boto3-glacier-module)
  - [GlacierServiceResource](#glacierserviceresource)
  - [Methods](#methods)
    - [GlacierServiceResource.Account](#glacierserviceresourceaccount)
    - [GlacierServiceResource.Archive](#glacierserviceresourcearchive)
    - [GlacierServiceResource.Job](#glacierserviceresourcejob)
    - [GlacierServiceResource.MultipartUpload](#glacierserviceresourcemultipartupload)
    - [GlacierServiceResource.Notification](#glacierserviceresourcenotification)
    - [GlacierServiceResource.Vault](#glacierserviceresourcevault)
    - [GlacierServiceResource.create_vault](#glacierserviceresourcecreate_vault)
    - [GlacierServiceResource.get_available_subresources](#glacierserviceresourceget_available_subresources)
  - [Collections](#collections)
    - [GlacierServiceResource.vaults](#glacierserviceresourcevaults)
  - [Account](#account)
    - [Account attributes](#account-attributes)
    - [Account methods](#account-methods)
    - [Account collections](#account-collections)
  - [Archive](#archive)
    - [Archive attributes](#archive-attributes)
    - [Archive methods](#archive-methods)
  - [Job](#job)
    - [Job attributes](#job-attributes)
    - [Job methods](#job-methods)
  - [MultipartUpload](#multipartupload)
    - [MultipartUpload attributes](#multipartupload-attributes)
    - [MultipartUpload methods](#multipartupload-methods)
  - [Notification](#notification)
    - [Notification attributes](#notification-attributes)
    - [Notification methods](#notification-methods)
  - [Vault](#vault)
    - [Vault attributes](#vault-attributes)
    - [Vault methods](#vault-methods)
    - [Vault collections](#vault-collections)

## GlacierServiceResource

Type annotations for `boto3.resource("glacier")`, included resources and collections.

Can be used directly:

```python
from mypy_boto3_glacier.service_resource import GlacierServiceResource
```



## Methods

### GlacierServiceResource.Account

Type annotations for `boto3.resource("glacier").Account` method.

[ServiceResource.Account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.ServiceResource.Account)

Definition:

```python
def Account(
    self,
    id: str
) -> _Account:
    pass
```

### GlacierServiceResource.Archive

Type annotations for `boto3.resource("glacier").Archive` method.

[ServiceResource.Archive documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.ServiceResource.Archive)

Definition:

```python
def Archive(
    self,
    account_id: str,
    vault_name: str,
    id: str
) -> _Archive:
    pass
```

### GlacierServiceResource.Job

Type annotations for `boto3.resource("glacier").Job` method.

[ServiceResource.Job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.ServiceResource.Job)

Definition:

```python
def Job(
    self,
    account_id: str,
    vault_name: str,
    id: str
) -> _Job:
    pass
```

### GlacierServiceResource.MultipartUpload

Type annotations for `boto3.resource("glacier").MultipartUpload` method.

[ServiceResource.MultipartUpload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.ServiceResource.MultipartUpload)

Definition:

```python
def MultipartUpload(
    self,
    account_id: str,
    vault_name: str,
    id: str
) -> _MultipartUpload:
    pass
```

### GlacierServiceResource.Notification

Type annotations for `boto3.resource("glacier").Notification` method.

[ServiceResource.Notification documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.ServiceResource.Notification)

Definition:

```python
def Notification(
    self,
    account_id: str,
    vault_name: str
) -> _Notification:
    pass
```

### GlacierServiceResource.Vault

Type annotations for `boto3.resource("glacier").Vault` method.

[ServiceResource.Vault documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.ServiceResource.Vault)

Definition:

```python
def Vault(
    self,
    account_id: str,
    name: str
) -> _Vault:
    pass
```

### GlacierServiceResource.create_vault

Type annotations for `boto3.resource("glacier").create_vault` method.

[ServiceResource.create_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.ServiceResource.create_vault)

Definition:

```python
def create_vault(
    self,
    accountId: str,
    vaultName: str
) -> _Vault:
    pass
```

### GlacierServiceResource.get_available_subresources

Type annotations for `boto3.resource("glacier").get_available_subresources` method.

[ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.ServiceResource.get_available_subresources)

Definition:

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```




## Collections

### GlacierServiceResource.vaults

Type annotations for `boto3.resource("glacier").vaults` collection.

Can be used directly:

```python
from mypy_boto3_glacier.service_resource import ServiceResourceVaultsCollection,

def get_collection() -> ServiceResourceVaultsCollection:
    return boto3.resource("glacier").vaults(
        ...
    )
```

[ServiceResource.vaults documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.ServiceResource.vaults)

Definition:

```python
class ServiceResourceVaultsCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceVaultsCollection":
        pass

    def filter(  # type: ignore
        self,
        marker: str = None,
        limit: str = None
    ) -> "ServiceResourceVaultsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceVaultsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceVaultsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Vault"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Vault"]:
        pass
```




## Account

Type annotations for `boto3.resource("glacier").Account` class.

Can be used directly:

```python
from mypy_boto3_glacier.service_resource import Account

def get_resource() -> Account:
    return boto3.resource("glacier").Account(...)
```

[Account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.ServiceResource.Account)


### Account attributes


- `id`: `str`

- `vaults`: `AccountVaultsCollection`




### Account methods


#### Account.Vault

Type annotations for `boto3.resource("glacier").Vault` method.

[Account.Vault documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Account.Vault)

```python
def Vault(
    self,
    name: str
) -> _Vault:
    pass
```

#### Account.create_vault

Type annotations for `boto3.resource("glacier").create_vault` method.

[Account.create_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Account.create_vault)

```python
def create_vault(
    self,
    vaultName: str
) -> _Vault:
    pass
```

#### Account.get_available_subresources

Type annotations for `boto3.resource("glacier").get_available_subresources` method.

[Account.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Account.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```




### Account collections


#### Account.vaults

Type annotations for `boto3.resource("glacier").Account(...).vaults` collection.

Can be used directly:

```python
from mypy_boto3_glacier.service_resource import AccountVaultsCollection,

def get_collection() -> AccountVaultsCollection:
    resource = boto3.resource("glacier").Account(...)
    return resource.vaults
```

[Account.vaults documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Account.vaults)

```python
class AccountVaultsCollection(ResourceCollection):
    def all(
        self
    ) -> "AccountVaultsCollection":
        pass

    def filter(  # type: ignore
        self,
        marker: str = None,
        limit: str = None
    ) -> "AccountVaultsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "AccountVaultsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "AccountVaultsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Vault"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Vault"]:
        pass
```




## Archive

Type annotations for `boto3.resource("glacier").Archive` class.

Can be used directly:

```python
from mypy_boto3_glacier.service_resource import Archive

def get_resource() -> Archive:
    return boto3.resource("glacier").Archive(...)
```

[Archive documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.ServiceResource.Archive)


### Archive attributes


- `account_id`: `str`

- `vault_name`: `str`

- `id`: `str`




### Archive methods


#### Archive.Vault

Type annotations for `boto3.resource("glacier").Vault` method.

[Archive.Vault documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Archive.Vault)

```python
def Vault(
    self
) -> _Vault:
    pass
```

#### Archive.delete

Type annotations for `boto3.resource("glacier").delete` method.

[Archive.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Archive.delete)

```python
def delete(
    self
) -> None:
    pass
```

#### Archive.get_available_subresources

Type annotations for `boto3.resource("glacier").get_available_subresources` method.

[Archive.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Archive.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### Archive.initiate_archive_retrieval

Type annotations for `boto3.resource("glacier").initiate_archive_retrieval` method.

[Archive.initiate_archive_retrieval documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Archive.initiate_archive_retrieval)

```python
def initiate_archive_retrieval(
    self,
    jobParameters: JobParametersTypeDef = None
) -> _Job:
    pass
```






## Job

Type annotations for `boto3.resource("glacier").Job` class.

Can be used directly:

```python
from mypy_boto3_glacier.service_resource import Job

def get_resource() -> Job:
    return boto3.resource("glacier").Job(...)
```

[Job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.ServiceResource.Job)


### Job attributes


- `job_id`: `str`

- `job_description`: `str`

- `action`: `str`

- `archive_id`: `str`

- `vault_arn`: `str`

- `creation_date`: `str`

- `completed`: `bool`

- `status_code`: `str`

- `status_message`: `str`

- `archive_size_in_bytes`: `int`

- `inventory_size_in_bytes`: `int`

- `sns_topic`: `str`

- `completion_date`: `str`

- `sha256_tree_hash`: `str`

- `archive_sha256_tree_hash`: `str`

- `retrieval_byte_range`: `str`

- `tier`: `str`

- `inventory_retrieval_parameters`: `Dict[str, Any]`

- `job_output_path`: `str`

- `select_parameters`: `Dict[str, Any]`

- `output_location`: `Dict[str, Any]`

- `account_id`: `str`

- `vault_name`: `str`

- `id`: `str`




### Job methods


#### Job.Vault

Type annotations for `boto3.resource("glacier").Vault` method.

[Job.Vault documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Job.Vault)

```python
def Vault(
    self
) -> _Vault:
    pass
```

#### Job.get_available_subresources

Type annotations for `boto3.resource("glacier").get_available_subresources` method.

[Job.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Job.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### Job.get_output

Type annotations for `boto3.resource("glacier").get_output` method.

[Job.get_output documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Job.get_output)

```python
def get_output(
    self,
    range: str = None
) -> GetJobOutputOutputTypeDef:
    pass
```

#### Job.load

Type annotations for `boto3.resource("glacier").load` method.

[Job.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Job.load)

```python
def load(
    self
) -> None:
    pass
```

#### Job.reload

Type annotations for `boto3.resource("glacier").reload` method.

[Job.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Job.reload)

```python
def reload(
    self
) -> None:
    pass
```






## MultipartUpload

Type annotations for `boto3.resource("glacier").MultipartUpload` class.

Can be used directly:

```python
from mypy_boto3_glacier.service_resource import MultipartUpload

def get_resource() -> MultipartUpload:
    return boto3.resource("glacier").MultipartUpload(...)
```

[MultipartUpload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.ServiceResource.MultipartUpload)


### MultipartUpload attributes


- `multipart_upload_id`: `str`

- `vault_arn`: `str`

- `archive_description`: `str`

- `part_size_in_bytes`: `int`

- `creation_date`: `str`

- `account_id`: `str`

- `vault_name`: `str`

- `id`: `str`




### MultipartUpload methods


#### MultipartUpload.Vault

Type annotations for `boto3.resource("glacier").Vault` method.

[MultipartUpload.Vault documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.MultipartUpload.Vault)

```python
def Vault(
    self
) -> _Vault:
    pass
```

#### MultipartUpload.abort

Type annotations for `boto3.resource("glacier").abort` method.

[MultipartUpload.abort documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.MultipartUpload.abort)

```python
def abort(
    self
) -> None:
    pass
```

#### MultipartUpload.complete

Type annotations for `boto3.resource("glacier").complete` method.

[MultipartUpload.complete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.MultipartUpload.complete)

```python
def complete(
    self,
    archiveSize: str = None,
    checksum: str = None
) -> ArchiveCreationOutputTypeDef:
    pass
```

#### MultipartUpload.get_available_subresources

Type annotations for `boto3.resource("glacier").get_available_subresources` method.

[MultipartUpload.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.MultipartUpload.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### MultipartUpload.parts

Type annotations for `boto3.resource("glacier").parts` method.

[MultipartUpload.parts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.MultipartUpload.parts)

```python
def parts(
    self,
    marker: str = None,
    limit: str = None
) -> ListPartsOutputTypeDef:
    pass
```

#### MultipartUpload.upload_part

Type annotations for `boto3.resource("glacier").upload_part` method.

[MultipartUpload.upload_part documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.MultipartUpload.upload_part)

```python
def upload_part(
    self,
    checksum: str = None,
    range: str = None,
    body: Union[bytes, IO[bytes]] = None
) -> UploadMultipartPartOutputTypeDef:
    pass
```






## Notification

Type annotations for `boto3.resource("glacier").Notification` class.

Can be used directly:

```python
from mypy_boto3_glacier.service_resource import Notification

def get_resource() -> Notification:
    return boto3.resource("glacier").Notification(...)
```

[Notification documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.ServiceResource.Notification)


### Notification attributes


- `sns_topic`: `str`

- `events`: `List[Any]`

- `account_id`: `str`

- `vault_name`: `str`




### Notification methods


#### Notification.Vault

Type annotations for `boto3.resource("glacier").Vault` method.

[Notification.Vault documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Notification.Vault)

```python
def Vault(
    self
) -> _Vault:
    pass
```

#### Notification.delete

Type annotations for `boto3.resource("glacier").delete` method.

[Notification.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Notification.delete)

```python
def delete(
    self
) -> None:
    pass
```

#### Notification.get_available_subresources

Type annotations for `boto3.resource("glacier").get_available_subresources` method.

[Notification.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Notification.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### Notification.load

Type annotations for `boto3.resource("glacier").load` method.

[Notification.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Notification.load)

```python
def load(
    self
) -> None:
    pass
```

#### Notification.reload

Type annotations for `boto3.resource("glacier").reload` method.

[Notification.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Notification.reload)

```python
def reload(
    self
) -> None:
    pass
```

#### Notification.set

Type annotations for `boto3.resource("glacier").set` method.

[Notification.set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Notification.set)

```python
def set(
    self,
    vaultNotificationConfig: "VaultNotificationConfigTypeDef" = None
) -> None:
    pass
```






## Vault

Type annotations for `boto3.resource("glacier").Vault` class.

Can be used directly:

```python
from mypy_boto3_glacier.service_resource import Vault

def get_resource() -> Vault:
    return boto3.resource("glacier").Vault(...)
```

[Vault documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.ServiceResource.Vault)


### Vault attributes


- `vault_arn`: `str`

- `vault_name`: `str`

- `creation_date`: `str`

- `last_inventory_date`: `str`

- `number_of_archives`: `int`

- `size_in_bytes`: `int`

- `account_id`: `str`

- `name`: `str`

- `completed_jobs`: `VaultCompletedJobsCollection`

- `failed_jobs`: `VaultFailedJobsCollection`

- `jobs`: `VaultJobsCollection`

- `jobs_in_progress`: `VaultJobsInProgressCollection`

- `multipart_uplaods`: `VaultMultipartUplaodsCollection`

- `multipart_uploads`: `VaultMultipartUploadsCollection`

- `succeeded_jobs`: `VaultSucceededJobsCollection`




### Vault methods


#### Vault.Account

Type annotations for `boto3.resource("glacier").Account` method.

[Vault.Account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Vault.Account)

```python
def Account(
    self
) -> _Account:
    pass
```

#### Vault.Archive

Type annotations for `boto3.resource("glacier").Archive` method.

[Vault.Archive documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Vault.Archive)

```python
def Archive(
    self,
    id: str
) -> _Archive:
    pass
```

#### Vault.Job

Type annotations for `boto3.resource("glacier").Job` method.

[Vault.Job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Vault.Job)

```python
def Job(
    self,
    id: str
) -> _Job:
    pass
```

#### Vault.MultipartUpload

Type annotations for `boto3.resource("glacier").MultipartUpload` method.

[Vault.MultipartUpload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Vault.MultipartUpload)

```python
def MultipartUpload(
    self,
    id: str
) -> _MultipartUpload:
    pass
```

#### Vault.Notification

Type annotations for `boto3.resource("glacier").Notification` method.

[Vault.Notification documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Vault.Notification)

```python
def Notification(
    self
) -> _Notification:
    pass
```

#### Vault.create

Type annotations for `boto3.resource("glacier").create` method.

[Vault.create documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Vault.create)

```python
def create(
    self
) -> CreateVaultOutputTypeDef:
    pass
```

#### Vault.delete

Type annotations for `boto3.resource("glacier").delete` method.

[Vault.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Vault.delete)

```python
def delete(
    self
) -> None:
    pass
```

#### Vault.get_available_subresources

Type annotations for `boto3.resource("glacier").get_available_subresources` method.

[Vault.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Vault.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### Vault.initiate_inventory_retrieval

Type annotations for `boto3.resource("glacier").initiate_inventory_retrieval` method.

[Vault.initiate_inventory_retrieval documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Vault.initiate_inventory_retrieval)

```python
def initiate_inventory_retrieval(
    self,
    jobParameters: JobParametersTypeDef = None
) -> _Job:
    pass
```

#### Vault.initiate_multipart_upload

Type annotations for `boto3.resource("glacier").initiate_multipart_upload` method.

[Vault.initiate_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Vault.initiate_multipart_upload)

```python
def initiate_multipart_upload(
    self,
    archiveDescription: str = None,
    partSize: str = None
) -> _MultipartUpload:
    pass
```

#### Vault.load

Type annotations for `boto3.resource("glacier").load` method.

[Vault.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Vault.load)

```python
def load(
    self
) -> None:
    pass
```

#### Vault.reload

Type annotations for `boto3.resource("glacier").reload` method.

[Vault.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Vault.reload)

```python
def reload(
    self
) -> None:
    pass
```

#### Vault.upload_archive

Type annotations for `boto3.resource("glacier").upload_archive` method.

[Vault.upload_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Vault.upload_archive)

```python
def upload_archive(
    self,
    archiveDescription: str = None,
    checksum: str = None,
    body: Union[bytes, IO[bytes]] = None
) -> _Archive:
    pass
```




### Vault collections


#### Vault.completed_jobs

Type annotations for `boto3.resource("glacier").Vault(...).completed_jobs` collection.

Can be used directly:

```python
from mypy_boto3_glacier.service_resource import VaultCompletedJobsCollection,

def get_collection() -> VaultCompletedJobsCollection:
    resource = boto3.resource("glacier").Vault(...)
    return resource.completed_jobs
```

[Vault.completed_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Vault.completed_jobs)

```python
class VaultCompletedJobsCollection(ResourceCollection):
    def all(
        self
    ) -> "VaultCompletedJobsCollection":
        pass

    def filter(  # type: ignore
        self,
        limit: str = None,
        marker: str = None,
        statuscode: str = None,
        completed: str = None
    ) -> "VaultCompletedJobsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "VaultCompletedJobsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "VaultCompletedJobsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Job"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Job"]:
        pass
```

#### Vault.failed_jobs

Type annotations for `boto3.resource("glacier").Vault(...).failed_jobs` collection.

Can be used directly:

```python
from mypy_boto3_glacier.service_resource import VaultFailedJobsCollection,

def get_collection() -> VaultFailedJobsCollection:
    resource = boto3.resource("glacier").Vault(...)
    return resource.failed_jobs
```

[Vault.failed_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Vault.failed_jobs)

```python
class VaultFailedJobsCollection(ResourceCollection):
    def all(
        self
    ) -> "VaultFailedJobsCollection":
        pass

    def filter(  # type: ignore
        self,
        limit: str = None,
        marker: str = None,
        statuscode: str = None,
        completed: str = None
    ) -> "VaultFailedJobsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "VaultFailedJobsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "VaultFailedJobsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Job"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Job"]:
        pass
```

#### Vault.jobs

Type annotations for `boto3.resource("glacier").Vault(...).jobs` collection.

Can be used directly:

```python
from mypy_boto3_glacier.service_resource import VaultJobsCollection,

def get_collection() -> VaultJobsCollection:
    resource = boto3.resource("glacier").Vault(...)
    return resource.jobs
```

[Vault.jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Vault.jobs)

```python
class VaultJobsCollection(ResourceCollection):
    def all(
        self
    ) -> "VaultJobsCollection":
        pass

    def filter(  # type: ignore
        self,
        limit: str = None,
        marker: str = None,
        statuscode: str = None,
        completed: str = None
    ) -> "VaultJobsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "VaultJobsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "VaultJobsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Job"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Job"]:
        pass
```

#### Vault.jobs_in_progress

Type annotations for `boto3.resource("glacier").Vault(...).jobs_in_progress` collection.

Can be used directly:

```python
from mypy_boto3_glacier.service_resource import VaultJobsInProgressCollection,

def get_collection() -> VaultJobsInProgressCollection:
    resource = boto3.resource("glacier").Vault(...)
    return resource.jobs_in_progress
```

[Vault.jobs_in_progress documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Vault.jobs_in_progress)

```python
class VaultJobsInProgressCollection(ResourceCollection):
    def all(
        self
    ) -> "VaultJobsInProgressCollection":
        pass

    def filter(  # type: ignore
        self,
        limit: str = None,
        marker: str = None,
        statuscode: str = None,
        completed: str = None
    ) -> "VaultJobsInProgressCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "VaultJobsInProgressCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "VaultJobsInProgressCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Job"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Job"]:
        pass
```

#### Vault.multipart_uplaods

Type annotations for `boto3.resource("glacier").Vault(...).multipart_uplaods` collection.

Can be used directly:

```python
from mypy_boto3_glacier.service_resource import VaultMultipartUplaodsCollection,

def get_collection() -> VaultMultipartUplaodsCollection:
    resource = boto3.resource("glacier").Vault(...)
    return resource.multipart_uplaods
```

[Vault.multipart_uplaods documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Vault.multipart_uplaods)

```python
class VaultMultipartUplaodsCollection(ResourceCollection):
    def all(
        self
    ) -> "VaultMultipartUplaodsCollection":
        pass

    def filter(  # type: ignore
        self,
        marker: str = None,
        limit: str = None
    ) -> "VaultMultipartUplaodsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "VaultMultipartUplaodsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "VaultMultipartUplaodsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["MultipartUpload"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["MultipartUpload"]:
        pass
```

#### Vault.multipart_uploads

Type annotations for `boto3.resource("glacier").Vault(...).multipart_uploads` collection.

Can be used directly:

```python
from mypy_boto3_glacier.service_resource import VaultMultipartUploadsCollection,

def get_collection() -> VaultMultipartUploadsCollection:
    resource = boto3.resource("glacier").Vault(...)
    return resource.multipart_uploads
```

[Vault.multipart_uploads documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Vault.multipart_uploads)

```python
class VaultMultipartUploadsCollection(ResourceCollection):
    def all(
        self
    ) -> "VaultMultipartUploadsCollection":
        pass

    def filter(  # type: ignore
        self,
        marker: str = None,
        limit: str = None
    ) -> "VaultMultipartUploadsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "VaultMultipartUploadsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "VaultMultipartUploadsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["MultipartUpload"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["MultipartUpload"]:
        pass
```

#### Vault.succeeded_jobs

Type annotations for `boto3.resource("glacier").Vault(...).succeeded_jobs` collection.

Can be used directly:

```python
from mypy_boto3_glacier.service_resource import VaultSucceededJobsCollection,

def get_collection() -> VaultSucceededJobsCollection:
    resource = boto3.resource("glacier").Vault(...)
    return resource.succeeded_jobs
```

[Vault.succeeded_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Vault.succeeded_jobs)

```python
class VaultSucceededJobsCollection(ResourceCollection):
    def all(
        self
    ) -> "VaultSucceededJobsCollection":
        pass

    def filter(  # type: ignore
        self,
        limit: str = None,
        marker: str = None,
        statuscode: str = None,
        completed: str = None
    ) -> "VaultSucceededJobsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "VaultSucceededJobsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "VaultSucceededJobsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Job"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Job"]:
        pass
```


