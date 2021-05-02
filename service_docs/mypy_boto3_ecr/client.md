# ECRClient for boto3 ECR module

> [Index](../index.md) > [ECR](./index.md) > ECRClient

Auto-generated documentation for [ECR](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR)
type annotations stubs module [mypy_boto3_ecr](https://pypi.org/project/mypy-boto3-ecr/).

- [ECRClient for boto3 ECR module](#ecrclient-for-boto3-ecr-module)
  - [ECRClient](#ecrclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [batch_check_layer_availability](#batch_check_layer_availability)
    - [batch_delete_image](#batch_delete_image)
    - [batch_get_image](#batch_get_image)
    - [can_paginate](#can_paginate)
    - [complete_layer_upload](#complete_layer_upload)
    - [create_repository](#create_repository)
    - [delete_lifecycle_policy](#delete_lifecycle_policy)
    - [delete_registry_policy](#delete_registry_policy)
    - [delete_repository](#delete_repository)
    - [delete_repository_policy](#delete_repository_policy)
    - [describe_image_scan_findings](#describe_image_scan_findings)
    - [describe_images](#describe_images)
    - [describe_registry](#describe_registry)
    - [describe_repositories](#describe_repositories)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_authorization_token](#get_authorization_token)
    - [get_download_url_for_layer](#get_download_url_for_layer)
    - [get_lifecycle_policy](#get_lifecycle_policy)
    - [get_lifecycle_policy_preview](#get_lifecycle_policy_preview)
    - [get_registry_policy](#get_registry_policy)
    - [get_repository_policy](#get_repository_policy)
    - [initiate_layer_upload](#initiate_layer_upload)
    - [list_images](#list_images)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [put_image](#put_image)
    - [put_image_scanning_configuration](#put_image_scanning_configuration)
    - [put_image_tag_mutability](#put_image_tag_mutability)
    - [put_lifecycle_policy](#put_lifecycle_policy)
    - [put_registry_policy](#put_registry_policy)
    - [put_replication_configuration](#put_replication_configuration)
    - [set_repository_policy](#set_repository_policy)
    - [start_image_scan](#start_image_scan)
    - [start_lifecycle_policy_preview](#start_lifecycle_policy_preview)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [upload_layer_part](#upload_layer_part)
    - [get_paginator](#get_paginator)
    - [get_waiter](#get_waiter)

## ECRClient

Type annotations for `boto3.client("ecr")`

Can be used directly:

```python
from mypy_boto3_ecr.client import ECRClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_ecr.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.EmptyUploadException`
- `Exceptions.ImageAlreadyExistsException`
- `Exceptions.ImageDigestDoesNotMatchException`
- `Exceptions.ImageNotFoundException`
- `Exceptions.ImageTagAlreadyExistsException`
- `Exceptions.InvalidLayerException`
- `Exceptions.InvalidLayerPartException`
- `Exceptions.InvalidParameterException`
- `Exceptions.InvalidTagParameterException`
- `Exceptions.KmsException`
- `Exceptions.LayerAlreadyExistsException`
- `Exceptions.LayerInaccessibleException`
- `Exceptions.LayerPartTooSmallException`
- `Exceptions.LayersNotFoundException`
- `Exceptions.LifecyclePolicyNotFoundException`
- `Exceptions.LifecyclePolicyPreviewInProgressException`
- `Exceptions.LifecyclePolicyPreviewNotFoundException`
- `Exceptions.LimitExceededException`
- `Exceptions.ReferencedImagesNotFoundException`
- `Exceptions.RegistryPolicyNotFoundException`
- `Exceptions.RepositoryAlreadyExistsException`
- `Exceptions.RepositoryNotEmptyException`
- `Exceptions.RepositoryNotFoundException`
- `Exceptions.RepositoryPolicyNotFoundException`
- `Exceptions.ScanNotFoundException`
- `Exceptions.ServerException`
- `Exceptions.TooManyTagsException`
- `Exceptions.UnsupportedImageTypeException`
- `Exceptions.UploadNotFoundException`
- `Exceptions.ValidationException`


## Methods


### batch_check_layer_availability

Type annotations for `boto3.client("ecr").batch_check_layer_availability` method.

[Client.batch_check_layer_availability documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.batch_check_layer_availability)

```python
def batch_check_layer_availability(
    self,
    repositoryName: str,
    layerDigests: List[str],
    registryId: str = None
) -> BatchCheckLayerAvailabilityResponseTypeDef:
    pass
```

### batch_delete_image

Type annotations for `boto3.client("ecr").batch_delete_image` method.

[Client.batch_delete_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.batch_delete_image)

```python
def batch_delete_image(
    self,
    repositoryName: str,
    imageIds: List["ImageIdentifierTypeDef"],
    registryId: str = None
) -> BatchDeleteImageResponseTypeDef:
    pass
```

### batch_get_image

Type annotations for `boto3.client("ecr").batch_get_image` method.

[Client.batch_get_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.batch_get_image)

```python
def batch_get_image(
    self,
    repositoryName: str,
    imageIds: List["ImageIdentifierTypeDef"],
    registryId: str = None,
    acceptedMediaTypes: List[str] = None
) -> BatchGetImageResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("ecr").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### complete_layer_upload

Type annotations for `boto3.client("ecr").complete_layer_upload` method.

[Client.complete_layer_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.complete_layer_upload)

```python
def complete_layer_upload(
    self,
    repositoryName: str,
    uploadId: str,
    layerDigests: List[str],
    registryId: str = None
) -> CompleteLayerUploadResponseTypeDef:
    pass
```

### create_repository

Type annotations for `boto3.client("ecr").create_repository` method.

[Client.create_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.create_repository)

```python
def create_repository(
    self,
    repositoryName: str,
    tags: List["TagTypeDef"] = None,
    imageTagMutability: ImageTagMutability = None,
    imageScanningConfiguration: "ImageScanningConfigurationTypeDef" = None,
    encryptionConfiguration: "EncryptionConfigurationTypeDef" = None
) -> CreateRepositoryResponseTypeDef:
    pass
```

### delete_lifecycle_policy

Type annotations for `boto3.client("ecr").delete_lifecycle_policy` method.

[Client.delete_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.delete_lifecycle_policy)

```python
def delete_lifecycle_policy(
    self,
    repositoryName: str,
    registryId: str = None
) -> DeleteLifecyclePolicyResponseTypeDef:
    pass
```

### delete_registry_policy

Type annotations for `boto3.client("ecr").delete_registry_policy` method.

[Client.delete_registry_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.delete_registry_policy)

```python
def delete_registry_policy(
    self
) -> DeleteRegistryPolicyResponseTypeDef:
    pass
```

### delete_repository

Type annotations for `boto3.client("ecr").delete_repository` method.

[Client.delete_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.delete_repository)

```python
def delete_repository(
    self,
    repositoryName: str,
    registryId: str = None,
    force: bool = None
) -> DeleteRepositoryResponseTypeDef:
    pass
```

### delete_repository_policy

Type annotations for `boto3.client("ecr").delete_repository_policy` method.

[Client.delete_repository_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.delete_repository_policy)

```python
def delete_repository_policy(
    self,
    repositoryName: str,
    registryId: str = None
) -> DeleteRepositoryPolicyResponseTypeDef:
    pass
```

### describe_image_scan_findings

Type annotations for `boto3.client("ecr").describe_image_scan_findings` method.

[Client.describe_image_scan_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.describe_image_scan_findings)

```python
def describe_image_scan_findings(
    self,
    repositoryName: str,
    imageId: "ImageIdentifierTypeDef",
    registryId: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> DescribeImageScanFindingsResponseTypeDef:
    pass
```

### describe_images

Type annotations for `boto3.client("ecr").describe_images` method.

[Client.describe_images documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.describe_images)

```python
def describe_images(
    self,
    repositoryName: str,
    registryId: str = None,
    imageIds: List["ImageIdentifierTypeDef"] = None,
    nextToken: str = None,
    maxResults: int = None,
    filter: DescribeImagesFilterTypeDef = None
) -> DescribeImagesResponseTypeDef:
    pass
```

### describe_registry

Type annotations for `boto3.client("ecr").describe_registry` method.

[Client.describe_registry documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.describe_registry)

```python
def describe_registry(
    self
) -> DescribeRegistryResponseTypeDef:
    pass
```

### describe_repositories

Type annotations for `boto3.client("ecr").describe_repositories` method.

[Client.describe_repositories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.describe_repositories)

```python
def describe_repositories(
    self,
    registryId: str = None,
    repositoryNames: List[str] = None,
    nextToken: str = None,
    maxResults: int = None
) -> DescribeRepositoriesResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("ecr").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.generate_presigned_url)

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

### get_authorization_token

Type annotations for `boto3.client("ecr").get_authorization_token` method.

[Client.get_authorization_token documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.get_authorization_token)

```python
def get_authorization_token(
    self,
    registryIds: List[str] = None
) -> GetAuthorizationTokenResponseTypeDef:
    pass
```

### get_download_url_for_layer

Type annotations for `boto3.client("ecr").get_download_url_for_layer` method.

[Client.get_download_url_for_layer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.get_download_url_for_layer)

```python
def get_download_url_for_layer(
    self,
    repositoryName: str,
    layerDigest: str,
    registryId: str = None
) -> GetDownloadUrlForLayerResponseTypeDef:
    pass
```

### get_lifecycle_policy

Type annotations for `boto3.client("ecr").get_lifecycle_policy` method.

[Client.get_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.get_lifecycle_policy)

```python
def get_lifecycle_policy(
    self,
    repositoryName: str,
    registryId: str = None
) -> GetLifecyclePolicyResponseTypeDef:
    pass
```

### get_lifecycle_policy_preview

Type annotations for `boto3.client("ecr").get_lifecycle_policy_preview` method.

[Client.get_lifecycle_policy_preview documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.get_lifecycle_policy_preview)

```python
def get_lifecycle_policy_preview(
    self,
    repositoryName: str,
    registryId: str = None,
    imageIds: List["ImageIdentifierTypeDef"] = None,
    nextToken: str = None,
    maxResults: int = None,
    filter: LifecyclePolicyPreviewFilterTypeDef = None
) -> GetLifecyclePolicyPreviewResponseTypeDef:
    pass
```

### get_registry_policy

Type annotations for `boto3.client("ecr").get_registry_policy` method.

[Client.get_registry_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.get_registry_policy)

```python
def get_registry_policy(
    self
) -> GetRegistryPolicyResponseTypeDef:
    pass
```

### get_repository_policy

Type annotations for `boto3.client("ecr").get_repository_policy` method.

[Client.get_repository_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.get_repository_policy)

```python
def get_repository_policy(
    self,
    repositoryName: str,
    registryId: str = None
) -> GetRepositoryPolicyResponseTypeDef:
    pass
```

### initiate_layer_upload

Type annotations for `boto3.client("ecr").initiate_layer_upload` method.

[Client.initiate_layer_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.initiate_layer_upload)

```python
def initiate_layer_upload(
    self,
    repositoryName: str,
    registryId: str = None
) -> InitiateLayerUploadResponseTypeDef:
    pass
```

### list_images

Type annotations for `boto3.client("ecr").list_images` method.

[Client.list_images documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.list_images)

```python
def list_images(
    self,
    repositoryName: str,
    registryId: str = None,
    nextToken: str = None,
    maxResults: int = None,
    filter: ListImagesFilterTypeDef = None
) -> ListImagesResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("ecr").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### put_image

Type annotations for `boto3.client("ecr").put_image` method.

[Client.put_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.put_image)

```python
def put_image(
    self,
    repositoryName: str,
    imageManifest: str,
    registryId: str = None,
    imageManifestMediaType: str = None,
    imageTag: str = None,
    imageDigest: str = None
) -> PutImageResponseTypeDef:
    pass
```

### put_image_scanning_configuration

Type annotations for `boto3.client("ecr").put_image_scanning_configuration` method.

[Client.put_image_scanning_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.put_image_scanning_configuration)

```python
def put_image_scanning_configuration(
    self,
    repositoryName: str,
    imageScanningConfiguration: "ImageScanningConfigurationTypeDef",
    registryId: str = None
) -> PutImageScanningConfigurationResponseTypeDef:
    pass
```

### put_image_tag_mutability

Type annotations for `boto3.client("ecr").put_image_tag_mutability` method.

[Client.put_image_tag_mutability documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.put_image_tag_mutability)

```python
def put_image_tag_mutability(
    self,
    repositoryName: str,
    imageTagMutability: ImageTagMutability,
    registryId: str = None
) -> PutImageTagMutabilityResponseTypeDef:
    pass
```

### put_lifecycle_policy

Type annotations for `boto3.client("ecr").put_lifecycle_policy` method.

[Client.put_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.put_lifecycle_policy)

```python
def put_lifecycle_policy(
    self,
    repositoryName: str,
    lifecyclePolicyText: str,
    registryId: str = None
) -> PutLifecyclePolicyResponseTypeDef:
    pass
```

### put_registry_policy

Type annotations for `boto3.client("ecr").put_registry_policy` method.

[Client.put_registry_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.put_registry_policy)

```python
def put_registry_policy(
    self,
    policyText: str
) -> PutRegistryPolicyResponseTypeDef:
    pass
```

### put_replication_configuration

Type annotations for `boto3.client("ecr").put_replication_configuration` method.

[Client.put_replication_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.put_replication_configuration)

```python
def put_replication_configuration(
    self,
    replicationConfiguration: "ReplicationConfigurationTypeDef"
) -> PutReplicationConfigurationResponseTypeDef:
    pass
```

### set_repository_policy

Type annotations for `boto3.client("ecr").set_repository_policy` method.

[Client.set_repository_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.set_repository_policy)

```python
def set_repository_policy(
    self,
    repositoryName: str,
    policyText: str,
    registryId: str = None,
    force: bool = None
) -> SetRepositoryPolicyResponseTypeDef:
    pass
```

### start_image_scan

Type annotations for `boto3.client("ecr").start_image_scan` method.

[Client.start_image_scan documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.start_image_scan)

```python
def start_image_scan(
    self,
    repositoryName: str,
    imageId: "ImageIdentifierTypeDef",
    registryId: str = None
) -> StartImageScanResponseTypeDef:
    pass
```

### start_lifecycle_policy_preview

Type annotations for `boto3.client("ecr").start_lifecycle_policy_preview` method.

[Client.start_lifecycle_policy_preview documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.start_lifecycle_policy_preview)

```python
def start_lifecycle_policy_preview(
    self,
    repositoryName: str,
    registryId: str = None,
    lifecyclePolicyText: str = None
) -> StartLifecyclePolicyPreviewResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("ecr").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("ecr").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### upload_layer_part

Type annotations for `boto3.client("ecr").upload_layer_part` method.

[Client.upload_layer_part documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.upload_layer_part)

```python
def upload_layer_part(
    self,
    repositoryName: str,
    uploadId: str,
    partFirstByte: int,
    partLastByte: int,
    layerPartBlob: Union[bytes, IO[bytes]],
    registryId: str = None
) -> UploadLayerPartResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("ecr").get_paginator` method with overloads.

- `client.get_paginator("describe_image_scan_findings")` -> [DescribeImageScanFindingsPaginator](./paginators.md#describeimagescanfindingspaginator)
- `client.get_paginator("describe_images")` -> [DescribeImagesPaginator](./paginators.md#describeimagespaginator)
- `client.get_paginator("describe_repositories")` -> [DescribeRepositoriesPaginator](./paginators.md#describerepositoriespaginator)
- `client.get_paginator("get_lifecycle_policy_preview")` -> [GetLifecyclePolicyPreviewPaginator](./paginators.md#getlifecyclepolicypreviewpaginator)
- `client.get_paginator("list_images")` -> [ListImagesPaginator](./paginators.md#listimagespaginator)




### get_waiter

Type annotations for `boto3.client("ecr").get_waiter` method with overloads.

- `client.get_waiter("image_scan_complete")` -> [ImageScanCompleteWaiter](./waiters.md#imagescancompletewaiter)
- `client.get_waiter("lifecycle_policy_preview_complete")` -> [LifecyclePolicyPreviewCompleteWaiter](./waiters.md#lifecyclepolicypreviewcompletewaiter)
