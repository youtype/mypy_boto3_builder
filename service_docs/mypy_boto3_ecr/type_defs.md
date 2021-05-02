# Structures for boto3 ECR module

> [Index](../index.md) > [ECR](./index.md) > Structures

Auto-generated documentation for [ECR](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR)
type annotations stubs module [mypy_boto3_ecr](https://pypi.org/project/mypy-boto3-ecr/).

- [Structures for boto3 ECR module](#structures-for-boto3-ecr-module)
  - [AttributeTypeDef](#attributetypedef)
  - [AuthorizationDataTypeDef](#authorizationdatatypedef)
  - [EncryptionConfigurationTypeDef](#encryptionconfigurationtypedef)
  - [ImageDetailTypeDef](#imagedetailtypedef)
  - [ImageFailureTypeDef](#imagefailuretypedef)
  - [ImageIdentifierTypeDef](#imageidentifiertypedef)
  - [ImageScanFindingTypeDef](#imagescanfindingtypedef)
  - [ImageScanFindingsSummaryTypeDef](#imagescanfindingssummarytypedef)
  - [ImageScanFindingsTypeDef](#imagescanfindingstypedef)
  - [ImageScanStatusTypeDef](#imagescanstatustypedef)
  - [ImageScanningConfigurationTypeDef](#imagescanningconfigurationtypedef)
  - [ImageTypeDef](#imagetypedef)
  - [LayerFailureTypeDef](#layerfailuretypedef)
  - [LayerTypeDef](#layertypedef)
  - [LifecyclePolicyPreviewResultTypeDef](#lifecyclepolicypreviewresulttypedef)
  - [LifecyclePolicyPreviewSummaryTypeDef](#lifecyclepolicypreviewsummarytypedef)
  - [LifecyclePolicyRuleActionTypeDef](#lifecyclepolicyruleactiontypedef)
  - [ReplicationConfigurationTypeDef](#replicationconfigurationtypedef)
  - [ReplicationDestinationTypeDef](#replicationdestinationtypedef)
  - [ReplicationRuleTypeDef](#replicationruletypedef)
  - [RepositoryTypeDef](#repositorytypedef)
  - [TagTypeDef](#tagtypedef)
  - [BatchCheckLayerAvailabilityResponseTypeDef](#batchchecklayeravailabilityresponsetypedef)
  - [BatchDeleteImageResponseTypeDef](#batchdeleteimageresponsetypedef)
  - [BatchGetImageResponseTypeDef](#batchgetimageresponsetypedef)
  - [CompleteLayerUploadResponseTypeDef](#completelayeruploadresponsetypedef)
  - [CreateRepositoryResponseTypeDef](#createrepositoryresponsetypedef)
  - [DeleteLifecyclePolicyResponseTypeDef](#deletelifecyclepolicyresponsetypedef)
  - [DeleteRegistryPolicyResponseTypeDef](#deleteregistrypolicyresponsetypedef)
  - [DeleteRepositoryPolicyResponseTypeDef](#deleterepositorypolicyresponsetypedef)
  - [DeleteRepositoryResponseTypeDef](#deleterepositoryresponsetypedef)
  - [DescribeImageScanFindingsResponseTypeDef](#describeimagescanfindingsresponsetypedef)
  - [DescribeImagesFilterTypeDef](#describeimagesfiltertypedef)
  - [DescribeImagesResponseTypeDef](#describeimagesresponsetypedef)
  - [DescribeRegistryResponseTypeDef](#describeregistryresponsetypedef)
  - [DescribeRepositoriesResponseTypeDef](#describerepositoriesresponsetypedef)
  - [GetAuthorizationTokenResponseTypeDef](#getauthorizationtokenresponsetypedef)
  - [GetDownloadUrlForLayerResponseTypeDef](#getdownloadurlforlayerresponsetypedef)
  - [GetLifecyclePolicyPreviewResponseTypeDef](#getlifecyclepolicypreviewresponsetypedef)
  - [GetLifecyclePolicyResponseTypeDef](#getlifecyclepolicyresponsetypedef)
  - [GetRegistryPolicyResponseTypeDef](#getregistrypolicyresponsetypedef)
  - [GetRepositoryPolicyResponseTypeDef](#getrepositorypolicyresponsetypedef)
  - [InitiateLayerUploadResponseTypeDef](#initiatelayeruploadresponsetypedef)
  - [LifecyclePolicyPreviewFilterTypeDef](#lifecyclepolicypreviewfiltertypedef)
  - [ListImagesFilterTypeDef](#listimagesfiltertypedef)
  - [ListImagesResponseTypeDef](#listimagesresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PutImageResponseTypeDef](#putimageresponsetypedef)
  - [PutImageScanningConfigurationResponseTypeDef](#putimagescanningconfigurationresponsetypedef)
  - [PutImageTagMutabilityResponseTypeDef](#putimagetagmutabilityresponsetypedef)
  - [PutLifecyclePolicyResponseTypeDef](#putlifecyclepolicyresponsetypedef)
  - [PutRegistryPolicyResponseTypeDef](#putregistrypolicyresponsetypedef)
  - [PutReplicationConfigurationResponseTypeDef](#putreplicationconfigurationresponsetypedef)
  - [SetRepositoryPolicyResponseTypeDef](#setrepositorypolicyresponsetypedef)
  - [StartImageScanResponseTypeDef](#startimagescanresponsetypedef)
  - [StartLifecyclePolicyPreviewResponseTypeDef](#startlifecyclepolicypreviewresponsetypedef)
  - [UploadLayerPartResponseTypeDef](#uploadlayerpartresponsetypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## AttributeTypeDef

```python
from mypy_boto3_ecr.type_defs import AttributeTypeDef
```


Required fields:
- `key`: `str`



Optional fields:
- `value`: `str`


## AuthorizationDataTypeDef

```python
from mypy_boto3_ecr.type_defs import AuthorizationDataTypeDef
```




Optional fields:
- `authorizationToken`: `str`
- `expiresAt`: `datetime`
- `proxyEndpoint`: `str`


## EncryptionConfigurationTypeDef

```python
from mypy_boto3_ecr.type_defs import EncryptionConfigurationTypeDef
```


Required fields:
- `encryptionType`: `EncryptionType`



Optional fields:
- `kmsKey`: `str`


## ImageDetailTypeDef

```python
from mypy_boto3_ecr.type_defs import ImageDetailTypeDef
```




Optional fields:
- `registryId`: `str`
- `repositoryName`: `str`
- `imageDigest`: `str`
- `imageTags`: `List[str]`
- `imageSizeInBytes`: `int`
- `imagePushedAt`: `datetime`
- `imageScanStatus`: `"ImageScanStatusTypeDef"`
- `imageScanFindingsSummary`: `"ImageScanFindingsSummaryTypeDef"`
- `imageManifestMediaType`: `str`
- `artifactMediaType`: `str`


## ImageFailureTypeDef

```python
from mypy_boto3_ecr.type_defs import ImageFailureTypeDef
```




Optional fields:
- `imageId`: `"ImageIdentifierTypeDef"`
- `failureCode`: `ImageFailureCode`
- `failureReason`: `str`


## ImageIdentifierTypeDef

```python
from mypy_boto3_ecr.type_defs import ImageIdentifierTypeDef
```




Optional fields:
- `imageDigest`: `str`
- `imageTag`: `str`


## ImageScanFindingTypeDef

```python
from mypy_boto3_ecr.type_defs import ImageScanFindingTypeDef
```




Optional fields:
- `name`: `str`
- `description`: `str`
- `uri`: `str`
- `severity`: `FindingSeverity`
- `attributes`: `List["AttributeTypeDef"]`


## ImageScanFindingsSummaryTypeDef

```python
from mypy_boto3_ecr.type_defs import ImageScanFindingsSummaryTypeDef
```




Optional fields:
- `imageScanCompletedAt`: `datetime`
- `vulnerabilitySourceUpdatedAt`: `datetime`
- `findingSeverityCounts`: `Dict[FindingSeverity, int]`


## ImageScanFindingsTypeDef

```python
from mypy_boto3_ecr.type_defs import ImageScanFindingsTypeDef
```




Optional fields:
- `imageScanCompletedAt`: `datetime`
- `vulnerabilitySourceUpdatedAt`: `datetime`
- `findings`: `List["ImageScanFindingTypeDef"]`
- `findingSeverityCounts`: `Dict[FindingSeverity, int]`


## ImageScanStatusTypeDef

```python
from mypy_boto3_ecr.type_defs import ImageScanStatusTypeDef
```




Optional fields:
- `status`: `ScanStatus`
- `description`: `str`


## ImageScanningConfigurationTypeDef

```python
from mypy_boto3_ecr.type_defs import ImageScanningConfigurationTypeDef
```




Optional fields:
- `scanOnPush`: `bool`


## ImageTypeDef

```python
from mypy_boto3_ecr.type_defs import ImageTypeDef
```




Optional fields:
- `registryId`: `str`
- `repositoryName`: `str`
- `imageId`: `"ImageIdentifierTypeDef"`
- `imageManifest`: `str`
- `imageManifestMediaType`: `str`


## LayerFailureTypeDef

```python
from mypy_boto3_ecr.type_defs import LayerFailureTypeDef
```




Optional fields:
- `layerDigest`: `str`
- `failureCode`: `LayerFailureCode`
- `failureReason`: `str`


## LayerTypeDef

```python
from mypy_boto3_ecr.type_defs import LayerTypeDef
```




Optional fields:
- `layerDigest`: `str`
- `layerAvailability`: `LayerAvailability`
- `layerSize`: `int`
- `mediaType`: `str`


## LifecyclePolicyPreviewResultTypeDef

```python
from mypy_boto3_ecr.type_defs import LifecyclePolicyPreviewResultTypeDef
```




Optional fields:
- `imageTags`: `List[str]`
- `imageDigest`: `str`
- `imagePushedAt`: `datetime`
- `action`: `"LifecyclePolicyRuleActionTypeDef"`
- `appliedRulePriority`: `int`


## LifecyclePolicyPreviewSummaryTypeDef

```python
from mypy_boto3_ecr.type_defs import LifecyclePolicyPreviewSummaryTypeDef
```




Optional fields:
- `expiringImageTotalCount`: `int`


## LifecyclePolicyRuleActionTypeDef

```python
from mypy_boto3_ecr.type_defs import LifecyclePolicyRuleActionTypeDef
```




Optional fields:
- `type`: `ImageActionType`


## ReplicationConfigurationTypeDef

```python
from mypy_boto3_ecr.type_defs import ReplicationConfigurationTypeDef
```


Required fields:
- `rules`: `List["ReplicationRuleTypeDef"]`




## ReplicationDestinationTypeDef

```python
from mypy_boto3_ecr.type_defs import ReplicationDestinationTypeDef
```


Required fields:
- `region`: `str`
- `registryId`: `str`




## ReplicationRuleTypeDef

```python
from mypy_boto3_ecr.type_defs import ReplicationRuleTypeDef
```


Required fields:
- `destinations`: `List["ReplicationDestinationTypeDef"]`




## RepositoryTypeDef

```python
from mypy_boto3_ecr.type_defs import RepositoryTypeDef
```




Optional fields:
- `repositoryArn`: `str`
- `registryId`: `str`
- `repositoryName`: `str`
- `repositoryUri`: `str`
- `createdAt`: `datetime`
- `imageTagMutability`: `ImageTagMutability`
- `imageScanningConfiguration`: `"ImageScanningConfigurationTypeDef"`
- `encryptionConfiguration`: `"EncryptionConfigurationTypeDef"`


## TagTypeDef

```python
from mypy_boto3_ecr.type_defs import TagTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## BatchCheckLayerAvailabilityResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import BatchCheckLayerAvailabilityResponseTypeDef
```




Optional fields:
- `layers`: `List["LayerTypeDef"]`
- `failures`: `List["LayerFailureTypeDef"]`


## BatchDeleteImageResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import BatchDeleteImageResponseTypeDef
```




Optional fields:
- `imageIds`: `List["ImageIdentifierTypeDef"]`
- `failures`: `List["ImageFailureTypeDef"]`


## BatchGetImageResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import BatchGetImageResponseTypeDef
```




Optional fields:
- `images`: `List["ImageTypeDef"]`
- `failures`: `List["ImageFailureTypeDef"]`


## CompleteLayerUploadResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import CompleteLayerUploadResponseTypeDef
```




Optional fields:
- `registryId`: `str`
- `repositoryName`: `str`
- `uploadId`: `str`
- `layerDigest`: `str`


## CreateRepositoryResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import CreateRepositoryResponseTypeDef
```




Optional fields:
- `repository`: `"RepositoryTypeDef"`


## DeleteLifecyclePolicyResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import DeleteLifecyclePolicyResponseTypeDef
```




Optional fields:
- `registryId`: `str`
- `repositoryName`: `str`
- `lifecyclePolicyText`: `str`
- `lastEvaluatedAt`: `datetime`


## DeleteRegistryPolicyResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import DeleteRegistryPolicyResponseTypeDef
```




Optional fields:
- `registryId`: `str`
- `policyText`: `str`


## DeleteRepositoryPolicyResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import DeleteRepositoryPolicyResponseTypeDef
```




Optional fields:
- `registryId`: `str`
- `repositoryName`: `str`
- `policyText`: `str`


## DeleteRepositoryResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import DeleteRepositoryResponseTypeDef
```




Optional fields:
- `repository`: `"RepositoryTypeDef"`


## DescribeImageScanFindingsResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import DescribeImageScanFindingsResponseTypeDef
```




Optional fields:
- `registryId`: `str`
- `repositoryName`: `str`
- `imageId`: `"ImageIdentifierTypeDef"`
- `imageScanStatus`: `"ImageScanStatusTypeDef"`
- `imageScanFindings`: `"ImageScanFindingsTypeDef"`
- `nextToken`: `str`


## DescribeImagesFilterTypeDef

```python
from mypy_boto3_ecr.type_defs import DescribeImagesFilterTypeDef
```




Optional fields:
- `tagStatus`: `TagStatus`


## DescribeImagesResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import DescribeImagesResponseTypeDef
```




Optional fields:
- `imageDetails`: `List["ImageDetailTypeDef"]`
- `nextToken`: `str`


## DescribeRegistryResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import DescribeRegistryResponseTypeDef
```




Optional fields:
- `registryId`: `str`
- `replicationConfiguration`: `"ReplicationConfigurationTypeDef"`


## DescribeRepositoriesResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import DescribeRepositoriesResponseTypeDef
```




Optional fields:
- `repositories`: `List["RepositoryTypeDef"]`
- `nextToken`: `str`


## GetAuthorizationTokenResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import GetAuthorizationTokenResponseTypeDef
```




Optional fields:
- `authorizationData`: `List["AuthorizationDataTypeDef"]`


## GetDownloadUrlForLayerResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import GetDownloadUrlForLayerResponseTypeDef
```




Optional fields:
- `downloadUrl`: `str`
- `layerDigest`: `str`


## GetLifecyclePolicyPreviewResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import GetLifecyclePolicyPreviewResponseTypeDef
```




Optional fields:
- `registryId`: `str`
- `repositoryName`: `str`
- `lifecyclePolicyText`: `str`
- `status`: `LifecyclePolicyPreviewStatus`
- `nextToken`: `str`
- `previewResults`: `List["LifecyclePolicyPreviewResultTypeDef"]`
- `summary`: `"LifecyclePolicyPreviewSummaryTypeDef"`


## GetLifecyclePolicyResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import GetLifecyclePolicyResponseTypeDef
```




Optional fields:
- `registryId`: `str`
- `repositoryName`: `str`
- `lifecyclePolicyText`: `str`
- `lastEvaluatedAt`: `datetime`


## GetRegistryPolicyResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import GetRegistryPolicyResponseTypeDef
```




Optional fields:
- `registryId`: `str`
- `policyText`: `str`


## GetRepositoryPolicyResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import GetRepositoryPolicyResponseTypeDef
```




Optional fields:
- `registryId`: `str`
- `repositoryName`: `str`
- `policyText`: `str`


## InitiateLayerUploadResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import InitiateLayerUploadResponseTypeDef
```




Optional fields:
- `uploadId`: `str`
- `partSize`: `int`


## LifecyclePolicyPreviewFilterTypeDef

```python
from mypy_boto3_ecr.type_defs import LifecyclePolicyPreviewFilterTypeDef
```




Optional fields:
- `tagStatus`: `TagStatus`


## ListImagesFilterTypeDef

```python
from mypy_boto3_ecr.type_defs import ListImagesFilterTypeDef
```




Optional fields:
- `tagStatus`: `TagStatus`


## ListImagesResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import ListImagesResponseTypeDef
```




Optional fields:
- `imageIds`: `List["ImageIdentifierTypeDef"]`
- `nextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `List["TagTypeDef"]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_ecr.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PutImageResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import PutImageResponseTypeDef
```




Optional fields:
- `image`: `"ImageTypeDef"`


## PutImageScanningConfigurationResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import PutImageScanningConfigurationResponseTypeDef
```




Optional fields:
- `registryId`: `str`
- `repositoryName`: `str`
- `imageScanningConfiguration`: `"ImageScanningConfigurationTypeDef"`


## PutImageTagMutabilityResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import PutImageTagMutabilityResponseTypeDef
```




Optional fields:
- `registryId`: `str`
- `repositoryName`: `str`
- `imageTagMutability`: `ImageTagMutability`


## PutLifecyclePolicyResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import PutLifecyclePolicyResponseTypeDef
```




Optional fields:
- `registryId`: `str`
- `repositoryName`: `str`
- `lifecyclePolicyText`: `str`


## PutRegistryPolicyResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import PutRegistryPolicyResponseTypeDef
```




Optional fields:
- `registryId`: `str`
- `policyText`: `str`


## PutReplicationConfigurationResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import PutReplicationConfigurationResponseTypeDef
```




Optional fields:
- `replicationConfiguration`: `"ReplicationConfigurationTypeDef"`


## SetRepositoryPolicyResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import SetRepositoryPolicyResponseTypeDef
```




Optional fields:
- `registryId`: `str`
- `repositoryName`: `str`
- `policyText`: `str`


## StartImageScanResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import StartImageScanResponseTypeDef
```




Optional fields:
- `registryId`: `str`
- `repositoryName`: `str`
- `imageId`: `"ImageIdentifierTypeDef"`
- `imageScanStatus`: `"ImageScanStatusTypeDef"`


## StartLifecyclePolicyPreviewResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import StartLifecyclePolicyPreviewResponseTypeDef
```




Optional fields:
- `registryId`: `str`
- `repositoryName`: `str`
- `lifecyclePolicyText`: `str`
- `status`: `LifecyclePolicyPreviewStatus`


## UploadLayerPartResponseTypeDef

```python
from mypy_boto3_ecr.type_defs import UploadLayerPartResponseTypeDef
```




Optional fields:
- `registryId`: `str`
- `repositoryName`: `str`
- `uploadId`: `str`
- `lastByteReceived`: `int`


## WaiterConfigTypeDef

```python
from mypy_boto3_ecr.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

