# Structures for boto3 Glacier module

> [Index](../index.md) > [Glacier](./index.md) > Structures

Auto-generated documentation for [Glacier](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier)
type annotations stubs module [mypy_boto3_glacier](https://pypi.org/project/mypy-boto3-glacier/).

- [Structures for boto3 Glacier module](#structures-for-boto3-glacier-module)
  - [ArchiveCreationOutputTypeDef](#archivecreationoutputtypedef)
  - [CSVInputTypeDef](#csvinputtypedef)
  - [CSVOutputTypeDef](#csvoutputtypedef)
  - [CreateVaultOutputTypeDef](#createvaultoutputtypedef)
  - [DataRetrievalPolicyTypeDef](#dataretrievalpolicytypedef)
  - [DataRetrievalRuleTypeDef](#dataretrievalruletypedef)
  - [DescribeVaultOutputTypeDef](#describevaultoutputtypedef)
  - [EncryptionTypeDef](#encryptiontypedef)
  - [GetDataRetrievalPolicyOutputTypeDef](#getdataretrievalpolicyoutputtypedef)
  - [GetJobOutputOutputTypeDef](#getjoboutputoutputtypedef)
  - [GetVaultAccessPolicyOutputTypeDef](#getvaultaccesspolicyoutputtypedef)
  - [GetVaultLockOutputTypeDef](#getvaultlockoutputtypedef)
  - [GetVaultNotificationsOutputTypeDef](#getvaultnotificationsoutputtypedef)
  - [GlacierJobDescriptionTypeDef](#glacierjobdescriptiontypedef)
  - [GrantTypeDef](#granttypedef)
  - [GranteeTypeDef](#granteetypedef)
  - [InitiateJobOutputTypeDef](#initiatejoboutputtypedef)
  - [InitiateMultipartUploadOutputTypeDef](#initiatemultipartuploadoutputtypedef)
  - [InitiateVaultLockOutputTypeDef](#initiatevaultlockoutputtypedef)
  - [InputSerializationTypeDef](#inputserializationtypedef)
  - [InventoryRetrievalJobDescriptionTypeDef](#inventoryretrievaljobdescriptiontypedef)
  - [InventoryRetrievalJobInputTypeDef](#inventoryretrievaljobinputtypedef)
  - [JobParametersTypeDef](#jobparameterstypedef)
  - [ListJobsOutputTypeDef](#listjobsoutputtypedef)
  - [ListMultipartUploadsOutputTypeDef](#listmultipartuploadsoutputtypedef)
  - [ListPartsOutputTypeDef](#listpartsoutputtypedef)
  - [ListProvisionedCapacityOutputTypeDef](#listprovisionedcapacityoutputtypedef)
  - [ListTagsForVaultOutputTypeDef](#listtagsforvaultoutputtypedef)
  - [ListVaultsOutputTypeDef](#listvaultsoutputtypedef)
  - [OutputLocationTypeDef](#outputlocationtypedef)
  - [OutputSerializationTypeDef](#outputserializationtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PartListElementTypeDef](#partlistelementtypedef)
  - [ProvisionedCapacityDescriptionTypeDef](#provisionedcapacitydescriptiontypedef)
  - [PurchaseProvisionedCapacityOutputTypeDef](#purchaseprovisionedcapacityoutputtypedef)
  - [ResponseMetadata](#responsemetadata)
  - [S3LocationTypeDef](#s3locationtypedef)
  - [SelectParametersTypeDef](#selectparameterstypedef)
  - [UploadListElementTypeDef](#uploadlistelementtypedef)
  - [UploadMultipartPartOutputTypeDef](#uploadmultipartpartoutputtypedef)
  - [VaultAccessPolicyTypeDef](#vaultaccesspolicytypedef)
  - [VaultLockPolicyTypeDef](#vaultlockpolicytypedef)
  - [VaultNotificationConfigTypeDef](#vaultnotificationconfigtypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## ArchiveCreationOutputTypeDef

```python
from mypy_boto3_glacier.type_defs import ArchiveCreationOutputTypeDef
```




Optional fields:
- `location`: `str`
- `checksum`: `str`
- `archiveId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CSVInputTypeDef

```python
from mypy_boto3_glacier.type_defs import CSVInputTypeDef
```




Optional fields:
- `FileHeaderInfo`: `FileHeaderInfo`
- `Comments`: `str`
- `QuoteEscapeCharacter`: `str`
- `RecordDelimiter`: `str`
- `FieldDelimiter`: `str`
- `QuoteCharacter`: `str`


## CSVOutputTypeDef

```python
from mypy_boto3_glacier.type_defs import CSVOutputTypeDef
```




Optional fields:
- `QuoteFields`: `QuoteFields`
- `QuoteEscapeCharacter`: `str`
- `RecordDelimiter`: `str`
- `FieldDelimiter`: `str`
- `QuoteCharacter`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateVaultOutputTypeDef

```python
from mypy_boto3_glacier.type_defs import CreateVaultOutputTypeDef
```




Optional fields:
- `location`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DataRetrievalPolicyTypeDef

```python
from mypy_boto3_glacier.type_defs import DataRetrievalPolicyTypeDef
```




Optional fields:
- `Rules`: `List["DataRetrievalRuleTypeDef"]`


## DataRetrievalRuleTypeDef

```python
from mypy_boto3_glacier.type_defs import DataRetrievalRuleTypeDef
```




Optional fields:
- `Strategy`: `str`
- `BytesPerHour`: `int`


## DescribeVaultOutputTypeDef

```python
from mypy_boto3_glacier.type_defs import DescribeVaultOutputTypeDef
```




Optional fields:
- `VaultARN`: `str`
- `VaultName`: `str`
- `CreationDate`: `str`
- `LastInventoryDate`: `str`
- `NumberOfArchives`: `int`
- `SizeInBytes`: `int`
- `ResponseMetadata`: `"ResponseMetadata"`


## EncryptionTypeDef

```python
from mypy_boto3_glacier.type_defs import EncryptionTypeDef
```




Optional fields:
- `EncryptionType`: `EncryptionType`
- `KMSKeyId`: `str`
- `KMSContext`: `str`


## GetDataRetrievalPolicyOutputTypeDef

```python
from mypy_boto3_glacier.type_defs import GetDataRetrievalPolicyOutputTypeDef
```




Optional fields:
- `Policy`: `"DataRetrievalPolicyTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetJobOutputOutputTypeDef

```python
from mypy_boto3_glacier.type_defs import GetJobOutputOutputTypeDef
```




Optional fields:
- `body`: `StreamingBody`
- `checksum`: `str`
- `status`: `int`
- `contentRange`: `str`
- `acceptRanges`: `str`
- `contentType`: `str`
- `archiveDescription`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetVaultAccessPolicyOutputTypeDef

```python
from mypy_boto3_glacier.type_defs import GetVaultAccessPolicyOutputTypeDef
```




Optional fields:
- `policy`: `"VaultAccessPolicyTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetVaultLockOutputTypeDef

```python
from mypy_boto3_glacier.type_defs import GetVaultLockOutputTypeDef
```




Optional fields:
- `Policy`: `str`
- `State`: `str`
- `ExpirationDate`: `str`
- `CreationDate`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetVaultNotificationsOutputTypeDef

```python
from mypy_boto3_glacier.type_defs import GetVaultNotificationsOutputTypeDef
```




Optional fields:
- `vaultNotificationConfig`: `"VaultNotificationConfigTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GlacierJobDescriptionTypeDef

```python
from mypy_boto3_glacier.type_defs import GlacierJobDescriptionTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobDescription`: `str`
- `Action`: `ActionCode`
- `ArchiveId`: `str`
- `VaultARN`: `str`
- `CreationDate`: `str`
- `Completed`: `bool`
- `StatusCode`: `StatusCode`
- `StatusMessage`: `str`
- `ArchiveSizeInBytes`: `int`
- `InventorySizeInBytes`: `int`
- `SNSTopic`: `str`
- `CompletionDate`: `str`
- `SHA256TreeHash`: `str`
- `ArchiveSHA256TreeHash`: `str`
- `RetrievalByteRange`: `str`
- `Tier`: `str`
- `InventoryRetrievalParameters`: `"InventoryRetrievalJobDescriptionTypeDef"`
- `JobOutputPath`: `str`
- `SelectParameters`: `"SelectParametersTypeDef"`
- `OutputLocation`: `"OutputLocationTypeDef"`


## GrantTypeDef

```python
from mypy_boto3_glacier.type_defs import GrantTypeDef
```




Optional fields:
- `Grantee`: `"GranteeTypeDef"`
- `Permission`: `Permission`


## GranteeTypeDef

```python
from mypy_boto3_glacier.type_defs import GranteeTypeDef
```


Required fields:
- `Type`: `TypeType`



Optional fields:
- `DisplayName`: `str`
- `URI`: `str`
- `ID`: `str`
- `EmailAddress`: `str`


## InitiateJobOutputTypeDef

```python
from mypy_boto3_glacier.type_defs import InitiateJobOutputTypeDef
```




Optional fields:
- `location`: `str`
- `jobId`: `str`
- `jobOutputPath`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## InitiateMultipartUploadOutputTypeDef

```python
from mypy_boto3_glacier.type_defs import InitiateMultipartUploadOutputTypeDef
```




Optional fields:
- `location`: `str`
- `uploadId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## InitiateVaultLockOutputTypeDef

```python
from mypy_boto3_glacier.type_defs import InitiateVaultLockOutputTypeDef
```




Optional fields:
- `lockId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## InputSerializationTypeDef

```python
from mypy_boto3_glacier.type_defs import InputSerializationTypeDef
```




Optional fields:
- `csv`: `"CSVInputTypeDef"`


## InventoryRetrievalJobDescriptionTypeDef

```python
from mypy_boto3_glacier.type_defs import InventoryRetrievalJobDescriptionTypeDef
```




Optional fields:
- `Format`: `str`
- `StartDate`: `str`
- `EndDate`: `str`
- `Limit`: `str`
- `Marker`: `str`


## InventoryRetrievalJobInputTypeDef

```python
from mypy_boto3_glacier.type_defs import InventoryRetrievalJobInputTypeDef
```




Optional fields:
- `StartDate`: `str`
- `EndDate`: `str`
- `Limit`: `str`
- `Marker`: `str`


## JobParametersTypeDef

```python
from mypy_boto3_glacier.type_defs import JobParametersTypeDef
```




Optional fields:
- `Format`: `str`
- `Type`: `str`
- `ArchiveId`: `str`
- `Description`: `str`
- `SNSTopic`: `str`
- `RetrievalByteRange`: `str`
- `Tier`: `str`
- `InventoryRetrievalParameters`: `"InventoryRetrievalJobInputTypeDef"`
- `SelectParameters`: `"SelectParametersTypeDef"`
- `OutputLocation`: `"OutputLocationTypeDef"`


## ListJobsOutputTypeDef

```python
from mypy_boto3_glacier.type_defs import ListJobsOutputTypeDef
```




Optional fields:
- `JobList`: `List["GlacierJobDescriptionTypeDef"]`
- `Marker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListMultipartUploadsOutputTypeDef

```python
from mypy_boto3_glacier.type_defs import ListMultipartUploadsOutputTypeDef
```




Optional fields:
- `UploadsList`: `List["UploadListElementTypeDef"]`
- `Marker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListPartsOutputTypeDef

```python
from mypy_boto3_glacier.type_defs import ListPartsOutputTypeDef
```




Optional fields:
- `MultipartUploadId`: `str`
- `VaultARN`: `str`
- `ArchiveDescription`: `str`
- `PartSizeInBytes`: `int`
- `CreationDate`: `str`
- `Parts`: `List["PartListElementTypeDef"]`
- `Marker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListProvisionedCapacityOutputTypeDef

```python
from mypy_boto3_glacier.type_defs import ListProvisionedCapacityOutputTypeDef
```




Optional fields:
- `ProvisionedCapacityList`: `List["ProvisionedCapacityDescriptionTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTagsForVaultOutputTypeDef

```python
from mypy_boto3_glacier.type_defs import ListTagsForVaultOutputTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListVaultsOutputTypeDef

```python
from mypy_boto3_glacier.type_defs import ListVaultsOutputTypeDef
```




Optional fields:
- `VaultList`: `List["DescribeVaultOutputTypeDef"]`
- `Marker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## OutputLocationTypeDef

```python
from mypy_boto3_glacier.type_defs import OutputLocationTypeDef
```




Optional fields:
- `S3`: `"S3LocationTypeDef"`


## OutputSerializationTypeDef

```python
from mypy_boto3_glacier.type_defs import OutputSerializationTypeDef
```




Optional fields:
- `csv`: `"CSVOutputTypeDef"`


## PaginatorConfigTypeDef

```python
from mypy_boto3_glacier.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PartListElementTypeDef

```python
from mypy_boto3_glacier.type_defs import PartListElementTypeDef
```




Optional fields:
- `RangeInBytes`: `str`
- `SHA256TreeHash`: `str`


## ProvisionedCapacityDescriptionTypeDef

```python
from mypy_boto3_glacier.type_defs import ProvisionedCapacityDescriptionTypeDef
```




Optional fields:
- `CapacityId`: `str`
- `StartDate`: `str`
- `ExpirationDate`: `str`


## PurchaseProvisionedCapacityOutputTypeDef

```python
from mypy_boto3_glacier.type_defs import PurchaseProvisionedCapacityOutputTypeDef
```




Optional fields:
- `capacityId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ResponseMetadata

```python
from mypy_boto3_glacier.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## S3LocationTypeDef

```python
from mypy_boto3_glacier.type_defs import S3LocationTypeDef
```




Optional fields:
- `BucketName`: `str`
- `Prefix`: `str`
- `Encryption`: `"EncryptionTypeDef"`
- `CannedACL`: `CannedACL`
- `AccessControlList`: `List["GrantTypeDef"]`
- `Tagging`: `Dict[str, str]`
- `UserMetadata`: `Dict[str, str]`
- `StorageClass`: `StorageClass`


## SelectParametersTypeDef

```python
from mypy_boto3_glacier.type_defs import SelectParametersTypeDef
```




Optional fields:
- `InputSerialization`: `"InputSerializationTypeDef"`
- `ExpressionType`: `Literal['SQL']`
- `Expression`: `str`
- `OutputSerialization`: `"OutputSerializationTypeDef"`


## UploadListElementTypeDef

```python
from mypy_boto3_glacier.type_defs import UploadListElementTypeDef
```




Optional fields:
- `MultipartUploadId`: `str`
- `VaultARN`: `str`
- `ArchiveDescription`: `str`
- `PartSizeInBytes`: `int`
- `CreationDate`: `str`


## UploadMultipartPartOutputTypeDef

```python
from mypy_boto3_glacier.type_defs import UploadMultipartPartOutputTypeDef
```




Optional fields:
- `checksum`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## VaultAccessPolicyTypeDef

```python
from mypy_boto3_glacier.type_defs import VaultAccessPolicyTypeDef
```




Optional fields:
- `Policy`: `str`


## VaultLockPolicyTypeDef

```python
from mypy_boto3_glacier.type_defs import VaultLockPolicyTypeDef
```




Optional fields:
- `Policy`: `str`


## VaultNotificationConfigTypeDef

```python
from mypy_boto3_glacier.type_defs import VaultNotificationConfigTypeDef
```




Optional fields:
- `SNSTopic`: `str`
- `Events`: `List[str]`


## WaiterConfigTypeDef

```python
from mypy_boto3_glacier.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

