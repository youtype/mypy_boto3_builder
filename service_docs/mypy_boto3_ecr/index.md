# Type annotations for boto3 ECR module

> [Index](../index.md) > ECR

Auto-generated documentation for [ECR](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR)
type annotations stubs module [mypy_boto3_ecr](https://pypi.org/project/mypy-boto3-ecr/).

```bash
pip install mypy-boto3-ecr
```

- [Type annotations for boto3 ECR module](#type-annotations-for-boto3-ecr-module)
  - [ECRClient](#ecrclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## ECRClient

Type annotations for  `boto3.client("ecr")` as [ECRClient](./client.md)

Can be used directly:

```python
from mypy_boto3_ecr.client import ECRClient
```


ECRClient [exceptions](./client.md#exceptions)



### Methods
- [batch_check_layer_availability](./client.md#batch-check-layer-availability)
- [batch_delete_image](./client.md#batch-delete-image)
- [batch_get_image](./client.md#batch-get-image)
- [can_paginate](./client.md#can-paginate)
- [complete_layer_upload](./client.md#complete-layer-upload)
- [create_repository](./client.md#create-repository)
- [delete_lifecycle_policy](./client.md#delete-lifecycle-policy)
- [delete_registry_policy](./client.md#delete-registry-policy)
- [delete_repository](./client.md#delete-repository)
- [delete_repository_policy](./client.md#delete-repository-policy)
- [describe_image_scan_findings](./client.md#describe-image-scan-findings)
- [describe_images](./client.md#describe-images)
- [describe_registry](./client.md#describe-registry)
- [describe_repositories](./client.md#describe-repositories)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_authorization_token](./client.md#get-authorization-token)
- [get_download_url_for_layer](./client.md#get-download-url-for-layer)
- [get_lifecycle_policy](./client.md#get-lifecycle-policy)
- [get_lifecycle_policy_preview](./client.md#get-lifecycle-policy-preview)
- [get_paginator](./client.md#get-paginator)
- [get_registry_policy](./client.md#get-registry-policy)
- [get_repository_policy](./client.md#get-repository-policy)
- [get_waiter](./client.md#get-waiter)
- [initiate_layer_upload](./client.md#initiate-layer-upload)
- [list_images](./client.md#list-images)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [put_image](./client.md#put-image)
- [put_image_scanning_configuration](./client.md#put-image-scanning-configuration)
- [put_image_tag_mutability](./client.md#put-image-tag-mutability)
- [put_lifecycle_policy](./client.md#put-lifecycle-policy)
- [put_registry_policy](./client.md#put-registry-policy)
- [put_replication_configuration](./client.md#put-replication-configuration)
- [set_repository_policy](./client.md#set-repository-policy)
- [start_image_scan](./client.md#start-image-scan)
- [start_lifecycle_policy_preview](./client.md#start-lifecycle-policy-preview)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [upload_layer_part](./client.md#upload-layer-part)




### Exceptions
- [ClientError](./client.md#clienterror)
- [EmptyUploadException](./client.md#emptyuploadexception)
- [ImageAlreadyExistsException](./client.md#imagealreadyexistsexception)
- [ImageDigestDoesNotMatchException](./client.md#imagedigestdoesnotmatchexception)
- [ImageNotFoundException](./client.md#imagenotfoundexception)
- [ImageTagAlreadyExistsException](./client.md#imagetagalreadyexistsexception)
- [InvalidLayerException](./client.md#invalidlayerexception)
- [InvalidLayerPartException](./client.md#invalidlayerpartexception)
- [InvalidParameterException](./client.md#invalidparameterexception)
- [InvalidTagParameterException](./client.md#invalidtagparameterexception)
- [KmsException](./client.md#kmsexception)
- [LayerAlreadyExistsException](./client.md#layeralreadyexistsexception)
- [LayerInaccessibleException](./client.md#layerinaccessibleexception)
- [LayerPartTooSmallException](./client.md#layerparttoosmallexception)
- [LayersNotFoundException](./client.md#layersnotfoundexception)
- [LifecyclePolicyNotFoundException](./client.md#lifecyclepolicynotfoundexception)
- [LifecyclePolicyPreviewInProgressException](./client.md#lifecyclepolicypreviewinprogressexception)
- [LifecyclePolicyPreviewNotFoundException](./client.md#lifecyclepolicypreviewnotfoundexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ReferencedImagesNotFoundException](./client.md#referencedimagesnotfoundexception)
- [RegistryPolicyNotFoundException](./client.md#registrypolicynotfoundexception)
- [RepositoryAlreadyExistsException](./client.md#repositoryalreadyexistsexception)
- [RepositoryNotEmptyException](./client.md#repositorynotemptyexception)
- [RepositoryNotFoundException](./client.md#repositorynotfoundexception)
- [RepositoryPolicyNotFoundException](./client.md#repositorypolicynotfoundexception)
- [ScanNotFoundException](./client.md#scannotfoundexception)
- [ServerException](./client.md#serverexception)
- [TooManyTagsException](./client.md#toomanytagsexception)
- [UnsupportedImageTypeException](./client.md#unsupportedimagetypeexception)
- [UploadNotFoundException](./client.md#uploadnotfoundexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("ecr").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_ecr.paginators import DescribeImageScanFindingsPaginator, ...
```

- [DescribeImageScanFindingsPaginator](./paginators.md#describeimagescanfindingspaginator)
- [DescribeImagesPaginator](./paginators.md#describeimagespaginator)
- [DescribeRepositoriesPaginator](./paginators.md#describerepositoriespaginator)
- [GetLifecyclePolicyPreviewPaginator](./paginators.md#getlifecyclepolicypreviewpaginator)
- [ListImagesPaginator](./paginators.md#listimagespaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("ecr").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_ecr.waiters import ImageScanCompleteWaiter, ...
```

- [ImageScanCompleteWaiter](./waiters.md#imagescancompletewaiter)
- [LifecyclePolicyPreviewCompleteWaiter](./waiters.md#lifecyclepolicypreviewcompletewaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_ecr.literals import DescribeImageScanFindingsPaginatorName, ...
```

- [DescribeImageScanFindingsPaginatorName](./literals.md#describeimagescanfindingspaginatorname)
- [DescribeImagesPaginatorName](./literals.md#describeimagespaginatorname)
- [DescribeRepositoriesPaginatorName](./literals.md#describerepositoriespaginatorname)
- [EncryptionType](./literals.md#encryptiontype)
- [FindingSeverity](./literals.md#findingseverity)
- [GetLifecyclePolicyPreviewPaginatorName](./literals.md#getlifecyclepolicypreviewpaginatorname)
- [ImageActionType](./literals.md#imageactiontype)
- [ImageFailureCode](./literals.md#imagefailurecode)
- [ImageScanCompleteWaiterName](./literals.md#imagescancompletewaitername)
- [ImageTagMutability](./literals.md#imagetagmutability)
- [LayerAvailability](./literals.md#layeravailability)
- [LayerFailureCode](./literals.md#layerfailurecode)
- [LifecyclePolicyPreviewCompleteWaiterName](./literals.md#lifecyclepolicypreviewcompletewaitername)
- [LifecyclePolicyPreviewStatus](./literals.md#lifecyclepolicypreviewstatus)
- [ListImagesPaginatorName](./literals.md#listimagespaginatorname)
- [ScanStatus](./literals.md#scanstatus)
- [TagStatus](./literals.md#tagstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_ecr.type_defs import AttributeTypeDef, ...
```

- [AttributeTypeDef](./type_defs.md#attributetypedef)
- [AuthorizationDataTypeDef](./type_defs.md#authorizationdatatypedef)
- [EncryptionConfigurationTypeDef](./type_defs.md#encryptionconfigurationtypedef)
- [ImageDetailTypeDef](./type_defs.md#imagedetailtypedef)
- [ImageFailureTypeDef](./type_defs.md#imagefailuretypedef)
- [ImageIdentifierTypeDef](./type_defs.md#imageidentifiertypedef)
- [ImageScanFindingTypeDef](./type_defs.md#imagescanfindingtypedef)
- [ImageScanFindingsSummaryTypeDef](./type_defs.md#imagescanfindingssummarytypedef)
- [ImageScanFindingsTypeDef](./type_defs.md#imagescanfindingstypedef)
- [ImageScanStatusTypeDef](./type_defs.md#imagescanstatustypedef)
- [ImageScanningConfigurationTypeDef](./type_defs.md#imagescanningconfigurationtypedef)
- [ImageTypeDef](./type_defs.md#imagetypedef)
- [LayerFailureTypeDef](./type_defs.md#layerfailuretypedef)
- [LayerTypeDef](./type_defs.md#layertypedef)
- [LifecyclePolicyPreviewResultTypeDef](./type_defs.md#lifecyclepolicypreviewresulttypedef)
- [LifecyclePolicyPreviewSummaryTypeDef](./type_defs.md#lifecyclepolicypreviewsummarytypedef)
- [LifecyclePolicyRuleActionTypeDef](./type_defs.md#lifecyclepolicyruleactiontypedef)
- [ReplicationConfigurationTypeDef](./type_defs.md#replicationconfigurationtypedef)
- [ReplicationDestinationTypeDef](./type_defs.md#replicationdestinationtypedef)
- [ReplicationRuleTypeDef](./type_defs.md#replicationruletypedef)
- [RepositoryTypeDef](./type_defs.md#repositorytypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [BatchCheckLayerAvailabilityResponseTypeDef](./type_defs.md#batchchecklayeravailabilityresponsetypedef)
- [BatchDeleteImageResponseTypeDef](./type_defs.md#batchdeleteimageresponsetypedef)
- [BatchGetImageResponseTypeDef](./type_defs.md#batchgetimageresponsetypedef)
- [CompleteLayerUploadResponseTypeDef](./type_defs.md#completelayeruploadresponsetypedef)
- [CreateRepositoryResponseTypeDef](./type_defs.md#createrepositoryresponsetypedef)
- [DeleteLifecyclePolicyResponseTypeDef](./type_defs.md#deletelifecyclepolicyresponsetypedef)
- [DeleteRegistryPolicyResponseTypeDef](./type_defs.md#deleteregistrypolicyresponsetypedef)
- [DeleteRepositoryPolicyResponseTypeDef](./type_defs.md#deleterepositorypolicyresponsetypedef)
- [DeleteRepositoryResponseTypeDef](./type_defs.md#deleterepositoryresponsetypedef)
- [DescribeImageScanFindingsResponseTypeDef](./type_defs.md#describeimagescanfindingsresponsetypedef)
- [DescribeImagesFilterTypeDef](./type_defs.md#describeimagesfiltertypedef)
- [DescribeImagesResponseTypeDef](./type_defs.md#describeimagesresponsetypedef)
- [DescribeRegistryResponseTypeDef](./type_defs.md#describeregistryresponsetypedef)
- [DescribeRepositoriesResponseTypeDef](./type_defs.md#describerepositoriesresponsetypedef)
- [GetAuthorizationTokenResponseTypeDef](./type_defs.md#getauthorizationtokenresponsetypedef)
- [GetDownloadUrlForLayerResponseTypeDef](./type_defs.md#getdownloadurlforlayerresponsetypedef)
- [GetLifecyclePolicyPreviewResponseTypeDef](./type_defs.md#getlifecyclepolicypreviewresponsetypedef)
- [GetLifecyclePolicyResponseTypeDef](./type_defs.md#getlifecyclepolicyresponsetypedef)
- [GetRegistryPolicyResponseTypeDef](./type_defs.md#getregistrypolicyresponsetypedef)
- [GetRepositoryPolicyResponseTypeDef](./type_defs.md#getrepositorypolicyresponsetypedef)
- [InitiateLayerUploadResponseTypeDef](./type_defs.md#initiatelayeruploadresponsetypedef)
- [LifecyclePolicyPreviewFilterTypeDef](./type_defs.md#lifecyclepolicypreviewfiltertypedef)
- [ListImagesFilterTypeDef](./type_defs.md#listimagesfiltertypedef)
- [ListImagesResponseTypeDef](./type_defs.md#listimagesresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PutImageResponseTypeDef](./type_defs.md#putimageresponsetypedef)
- [PutImageScanningConfigurationResponseTypeDef](./type_defs.md#putimagescanningconfigurationresponsetypedef)
- [PutImageTagMutabilityResponseTypeDef](./type_defs.md#putimagetagmutabilityresponsetypedef)
- [PutLifecyclePolicyResponseTypeDef](./type_defs.md#putlifecyclepolicyresponsetypedef)
- [PutRegistryPolicyResponseTypeDef](./type_defs.md#putregistrypolicyresponsetypedef)
- [PutReplicationConfigurationResponseTypeDef](./type_defs.md#putreplicationconfigurationresponsetypedef)
- [SetRepositoryPolicyResponseTypeDef](./type_defs.md#setrepositorypolicyresponsetypedef)
- [StartImageScanResponseTypeDef](./type_defs.md#startimagescanresponsetypedef)
- [StartLifecyclePolicyPreviewResponseTypeDef](./type_defs.md#startlifecyclepolicypreviewresponsetypedef)
- [UploadLayerPartResponseTypeDef](./type_defs.md#uploadlayerpartresponsetypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
