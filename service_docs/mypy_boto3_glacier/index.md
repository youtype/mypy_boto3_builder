# Type annotations for boto3 Glacier module

> [Index](../index.md) > Glacier

Auto-generated documentation for [Glacier](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier)
type annotations stubs module [mypy_boto3_glacier](https://pypi.org/project/mypy-boto3-glacier/).

```bash
pip install mypy-boto3-glacier
```

- [Type annotations for boto3 Glacier module](#type-annotations-for-boto3-glacier-module)
  - [GlacierClient](#glacierclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [GlacierServiceResource](#glacierserviceresource)
    - [Collections](#collections)
    - [Resources](#resources)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## GlacierClient

Type annotations for  `boto3.client("glacier")` as [GlacierClient](./client.md)

Can be used directly:

```python
from mypy_boto3_glacier.client import GlacierClient
```


GlacierClient [exceptions](./client.md#exceptions)



### Methods
- [abort_multipart_upload](./client.md#abort-multipart-upload)
- [abort_vault_lock](./client.md#abort-vault-lock)
- [add_tags_to_vault](./client.md#add-tags-to-vault)
- [can_paginate](./client.md#can-paginate)
- [complete_multipart_upload](./client.md#complete-multipart-upload)
- [complete_vault_lock](./client.md#complete-vault-lock)
- [create_vault](./client.md#create-vault)
- [delete_archive](./client.md#delete-archive)
- [delete_vault](./client.md#delete-vault)
- [delete_vault_access_policy](./client.md#delete-vault-access-policy)
- [delete_vault_notifications](./client.md#delete-vault-notifications)
- [describe_job](./client.md#describe-job)
- [describe_vault](./client.md#describe-vault)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_data_retrieval_policy](./client.md#get-data-retrieval-policy)
- [get_job_output](./client.md#get-job-output)
- [get_paginator](./client.md#get-paginator)
- [get_vault_access_policy](./client.md#get-vault-access-policy)
- [get_vault_lock](./client.md#get-vault-lock)
- [get_vault_notifications](./client.md#get-vault-notifications)
- [get_waiter](./client.md#get-waiter)
- [initiate_job](./client.md#initiate-job)
- [initiate_multipart_upload](./client.md#initiate-multipart-upload)
- [initiate_vault_lock](./client.md#initiate-vault-lock)
- [list_jobs](./client.md#list-jobs)
- [list_multipart_uploads](./client.md#list-multipart-uploads)
- [list_parts](./client.md#list-parts)
- [list_provisioned_capacity](./client.md#list-provisioned-capacity)
- [list_tags_for_vault](./client.md#list-tags-for-vault)
- [list_vaults](./client.md#list-vaults)
- [purchase_provisioned_capacity](./client.md#purchase-provisioned-capacity)
- [remove_tags_from_vault](./client.md#remove-tags-from-vault)
- [set_data_retrieval_policy](./client.md#set-data-retrieval-policy)
- [set_vault_access_policy](./client.md#set-vault-access-policy)
- [set_vault_notifications](./client.md#set-vault-notifications)
- [upload_archive](./client.md#upload-archive)
- [upload_multipart_part](./client.md#upload-multipart-part)




### Exceptions
- [ClientError](./client.md#clienterror)
- [InsufficientCapacityException](./client.md#insufficientcapacityexception)
- [InvalidParameterValueException](./client.md#invalidparametervalueexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [MissingParameterValueException](./client.md#missingparametervalueexception)
- [PolicyEnforcedException](./client.md#policyenforcedexception)
- [RequestTimeoutException](./client.md#requesttimeoutexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)




## GlacierServiceResource

Type annotations for  `boto3.resource("glacier")` as [GlacierServiceResource](./service_resource.md)

Can be used directly:

```python
from mypy_boto3_glacier.service_resource import GlacierServiceResource
```


### Collections

Type annotations for collections from `boto3.resource("glacier").*`.

Can be used directly:

```python
from mypy_boto3_glacier.service_resource import ServiceResourceVaultsCollection, ...
```

- [ServiceResourceVaultsCollection](./service_resource.md#glacierserviceresource.vaults)




### Resources

Type annotations for additional resources from `boto3.resource("glacier").*`.

Can be used directly:

```python
from mypy_boto3_glacier.service_resource import Account, ...
```

- [Account](./service_resource.md#account)
- [Archive](./service_resource.md#archive)
- [Job](./service_resource.md#job)
- [MultipartUpload](./service_resource.md#multipartupload)
- [Notification](./service_resource.md#notification)
- [Vault](./service_resource.md#vault)





## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("glacier").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_glacier.paginators import ListJobsPaginator, ...
```

- [ListJobsPaginator](./paginators.md#listjobspaginator)
- [ListMultipartUploadsPaginator](./paginators.md#listmultipartuploadspaginator)
- [ListPartsPaginator](./paginators.md#listpartspaginator)
- [ListVaultsPaginator](./paginators.md#listvaultspaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("glacier").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_glacier.waiters import VaultExistsWaiter, ...
```

- [VaultExistsWaiter](./waiters.md#vaultexistswaiter)
- [VaultNotExistsWaiter](./waiters.md#vaultnotexistswaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_glacier.literals import ActionCode, ...
```

- [ActionCode](./literals.md#actioncode)
- [CannedACL](./literals.md#cannedacl)
- [EncryptionType](./literals.md#encryptiontype)
- [ExpressionType](./literals.md#expressiontype)
- [FileHeaderInfo](./literals.md#fileheaderinfo)
- [ListJobsPaginatorName](./literals.md#listjobspaginatorname)
- [ListMultipartUploadsPaginatorName](./literals.md#listmultipartuploadspaginatorname)
- [ListPartsPaginatorName](./literals.md#listpartspaginatorname)
- [ListVaultsPaginatorName](./literals.md#listvaultspaginatorname)
- [Permission](./literals.md#permission)
- [QuoteFields](./literals.md#quotefields)
- [StatusCode](./literals.md#statuscode)
- [StorageClass](./literals.md#storageclass)
- [TypeType](./literals.md#typetype)
- [VaultExistsWaiterName](./literals.md#vaultexistswaitername)
- [VaultNotExistsWaiterName](./literals.md#vaultnotexistswaitername)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_glacier.type_defs import ArchiveCreationOutputTypeDef, ...
```

- [ArchiveCreationOutputTypeDef](./type_defs.md#archivecreationoutputtypedef)
- [CSVInputTypeDef](./type_defs.md#csvinputtypedef)
- [CSVOutputTypeDef](./type_defs.md#csvoutputtypedef)
- [CreateVaultOutputTypeDef](./type_defs.md#createvaultoutputtypedef)
- [DataRetrievalPolicyTypeDef](./type_defs.md#dataretrievalpolicytypedef)
- [DataRetrievalRuleTypeDef](./type_defs.md#dataretrievalruletypedef)
- [DescribeVaultOutputTypeDef](./type_defs.md#describevaultoutputtypedef)
- [EncryptionTypeDef](./type_defs.md#encryptiontypedef)
- [GetDataRetrievalPolicyOutputTypeDef](./type_defs.md#getdataretrievalpolicyoutputtypedef)
- [GetJobOutputOutputTypeDef](./type_defs.md#getjoboutputoutputtypedef)
- [GetVaultAccessPolicyOutputTypeDef](./type_defs.md#getvaultaccesspolicyoutputtypedef)
- [GetVaultLockOutputTypeDef](./type_defs.md#getvaultlockoutputtypedef)
- [GetVaultNotificationsOutputTypeDef](./type_defs.md#getvaultnotificationsoutputtypedef)
- [GlacierJobDescriptionTypeDef](./type_defs.md#glacierjobdescriptiontypedef)
- [GrantTypeDef](./type_defs.md#granttypedef)
- [GranteeTypeDef](./type_defs.md#granteetypedef)
- [InitiateJobOutputTypeDef](./type_defs.md#initiatejoboutputtypedef)
- [InitiateMultipartUploadOutputTypeDef](./type_defs.md#initiatemultipartuploadoutputtypedef)
- [InitiateVaultLockOutputTypeDef](./type_defs.md#initiatevaultlockoutputtypedef)
- [InputSerializationTypeDef](./type_defs.md#inputserializationtypedef)
- [InventoryRetrievalJobDescriptionTypeDef](./type_defs.md#inventoryretrievaljobdescriptiontypedef)
- [InventoryRetrievalJobInputTypeDef](./type_defs.md#inventoryretrievaljobinputtypedef)
- [JobParametersTypeDef](./type_defs.md#jobparameterstypedef)
- [ListJobsOutputTypeDef](./type_defs.md#listjobsoutputtypedef)
- [ListMultipartUploadsOutputTypeDef](./type_defs.md#listmultipartuploadsoutputtypedef)
- [ListPartsOutputTypeDef](./type_defs.md#listpartsoutputtypedef)
- [ListProvisionedCapacityOutputTypeDef](./type_defs.md#listprovisionedcapacityoutputtypedef)
- [ListTagsForVaultOutputTypeDef](./type_defs.md#listtagsforvaultoutputtypedef)
- [ListVaultsOutputTypeDef](./type_defs.md#listvaultsoutputtypedef)
- [OutputLocationTypeDef](./type_defs.md#outputlocationtypedef)
- [OutputSerializationTypeDef](./type_defs.md#outputserializationtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PartListElementTypeDef](./type_defs.md#partlistelementtypedef)
- [ProvisionedCapacityDescriptionTypeDef](./type_defs.md#provisionedcapacitydescriptiontypedef)
- [PurchaseProvisionedCapacityOutputTypeDef](./type_defs.md#purchaseprovisionedcapacityoutputtypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [S3LocationTypeDef](./type_defs.md#s3locationtypedef)
- [SelectParametersTypeDef](./type_defs.md#selectparameterstypedef)
- [UploadListElementTypeDef](./type_defs.md#uploadlistelementtypedef)
- [UploadMultipartPartOutputTypeDef](./type_defs.md#uploadmultipartpartoutputtypedef)
- [VaultAccessPolicyTypeDef](./type_defs.md#vaultaccesspolicytypedef)
- [VaultLockPolicyTypeDef](./type_defs.md#vaultlockpolicytypedef)
- [VaultNotificationConfigTypeDef](./type_defs.md#vaultnotificationconfigtypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
