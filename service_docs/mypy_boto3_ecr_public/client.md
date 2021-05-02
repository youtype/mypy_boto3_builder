# ECRPublicClient for boto3 ECRPublic module

> [Index](../index.md) > [ECRPublic](./index.md) > ECRPublicClient

Auto-generated documentation for [ECRPublic](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic)
type annotations stubs module [mypy_boto3_ecr_public](https://pypi.org/project/mypy-boto3-ecr-public/).

- [ECRPublicClient for boto3 ECRPublic module](#ecrpublicclient-for-boto3-ecrpublic-module)
  - [ECRPublicClient](#ecrpublicclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [batch_check_layer_availability](#batch_check_layer_availability)
    - [batch_delete_image](#batch_delete_image)
    - [can_paginate](#can_paginate)
    - [complete_layer_upload](#complete_layer_upload)
    - [create_repository](#create_repository)
    - [delete_repository](#delete_repository)
    - [delete_repository_policy](#delete_repository_policy)
    - [describe_image_tags](#describe_image_tags)
    - [describe_images](#describe_images)
    - [describe_registries](#describe_registries)
    - [describe_repositories](#describe_repositories)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_authorization_token](#get_authorization_token)
    - [get_registry_catalog_data](#get_registry_catalog_data)
    - [get_repository_catalog_data](#get_repository_catalog_data)
    - [get_repository_policy](#get_repository_policy)
    - [initiate_layer_upload](#initiate_layer_upload)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [put_image](#put_image)
    - [put_registry_catalog_data](#put_registry_catalog_data)
    - [put_repository_catalog_data](#put_repository_catalog_data)
    - [set_repository_policy](#set_repository_policy)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [upload_layer_part](#upload_layer_part)
    - [get_paginator](#get_paginator)

## ECRPublicClient

Type annotations for `boto3.client("ecr-public")`

Can be used directly:

```python
from mypy_boto3_ecr_public.client import ECRPublicClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_ecr_public.client import Exceptions

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
- `Exceptions.LayerAlreadyExistsException`
- `Exceptions.LayerPartTooSmallException`
- `Exceptions.LayersNotFoundException`
- `Exceptions.LimitExceededException`
- `Exceptions.ReferencedImagesNotFoundException`
- `Exceptions.RegistryNotFoundException`
- `Exceptions.RepositoryAlreadyExistsException`
- `Exceptions.RepositoryNotEmptyException`
- `Exceptions.RepositoryNotFoundException`
- `Exceptions.RepositoryPolicyNotFoundException`
- `Exceptions.ServerException`
- `Exceptions.TooManyTagsException`
- `Exceptions.UnsupportedCommandException`
- `Exceptions.UploadNotFoundException`


## Methods


### batch_check_layer_availability

Type annotations for `boto3.client("ecr-public").batch_check_layer_availability` method.

[Client.batch_check_layer_availability documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic.Client.batch_check_layer_availability)

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

Type annotations for `boto3.client("ecr-public").batch_delete_image` method.

[Client.batch_delete_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic.Client.batch_delete_image)

```python
def batch_delete_image(
    self,
    repositoryName: str,
    imageIds: List["ImageIdentifierTypeDef"],
    registryId: str = None
) -> BatchDeleteImageResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("ecr-public").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### complete_layer_upload

Type annotations for `boto3.client("ecr-public").complete_layer_upload` method.

[Client.complete_layer_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic.Client.complete_layer_upload)

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

Type annotations for `boto3.client("ecr-public").create_repository` method.

[Client.create_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic.Client.create_repository)

```python
def create_repository(
    self,
    repositoryName: str,
    catalogData: RepositoryCatalogDataInputTypeDef = None,
    tags: List["TagTypeDef"] = None
) -> CreateRepositoryResponseTypeDef:
    pass
```

### delete_repository

Type annotations for `boto3.client("ecr-public").delete_repository` method.

[Client.delete_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic.Client.delete_repository)

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

Type annotations for `boto3.client("ecr-public").delete_repository_policy` method.

[Client.delete_repository_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic.Client.delete_repository_policy)

```python
def delete_repository_policy(
    self,
    repositoryName: str,
    registryId: str = None
) -> DeleteRepositoryPolicyResponseTypeDef:
    pass
```

### describe_image_tags

Type annotations for `boto3.client("ecr-public").describe_image_tags` method.

[Client.describe_image_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic.Client.describe_image_tags)

```python
def describe_image_tags(
    self,
    repositoryName: str,
    registryId: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> DescribeImageTagsResponseTypeDef:
    pass
```

### describe_images

Type annotations for `boto3.client("ecr-public").describe_images` method.

[Client.describe_images documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic.Client.describe_images)

```python
def describe_images(
    self,
    repositoryName: str,
    registryId: str = None,
    imageIds: List["ImageIdentifierTypeDef"] = None,
    nextToken: str = None,
    maxResults: int = None
) -> DescribeImagesResponseTypeDef:
    pass
```

### describe_registries

Type annotations for `boto3.client("ecr-public").describe_registries` method.

[Client.describe_registries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic.Client.describe_registries)

```python
def describe_registries(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> DescribeRegistriesResponseTypeDef:
    pass
```

### describe_repositories

Type annotations for `boto3.client("ecr-public").describe_repositories` method.

[Client.describe_repositories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic.Client.describe_repositories)

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

Type annotations for `boto3.client("ecr-public").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic.Client.generate_presigned_url)

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

Type annotations for `boto3.client("ecr-public").get_authorization_token` method.

[Client.get_authorization_token documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic.Client.get_authorization_token)

```python
def get_authorization_token(
    self
) -> GetAuthorizationTokenResponseTypeDef:
    pass
```

### get_registry_catalog_data

Type annotations for `boto3.client("ecr-public").get_registry_catalog_data` method.

[Client.get_registry_catalog_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic.Client.get_registry_catalog_data)

```python
def get_registry_catalog_data(
    self
) -> GetRegistryCatalogDataResponseTypeDef:
    pass
```

### get_repository_catalog_data

Type annotations for `boto3.client("ecr-public").get_repository_catalog_data` method.

[Client.get_repository_catalog_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic.Client.get_repository_catalog_data)

```python
def get_repository_catalog_data(
    self,
    repositoryName: str,
    registryId: str = None
) -> GetRepositoryCatalogDataResponseTypeDef:
    pass
```

### get_repository_policy

Type annotations for `boto3.client("ecr-public").get_repository_policy` method.

[Client.get_repository_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic.Client.get_repository_policy)

```python
def get_repository_policy(
    self,
    repositoryName: str,
    registryId: str = None
) -> GetRepositoryPolicyResponseTypeDef:
    pass
```

### initiate_layer_upload

Type annotations for `boto3.client("ecr-public").initiate_layer_upload` method.

[Client.initiate_layer_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic.Client.initiate_layer_upload)

```python
def initiate_layer_upload(
    self,
    repositoryName: str,
    registryId: str = None
) -> InitiateLayerUploadResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("ecr-public").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### put_image

Type annotations for `boto3.client("ecr-public").put_image` method.

[Client.put_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic.Client.put_image)

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

### put_registry_catalog_data

Type annotations for `boto3.client("ecr-public").put_registry_catalog_data` method.

[Client.put_registry_catalog_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic.Client.put_registry_catalog_data)

```python
def put_registry_catalog_data(
    self,
    displayName: str = None
) -> PutRegistryCatalogDataResponseTypeDef:
    pass
```

### put_repository_catalog_data

Type annotations for `boto3.client("ecr-public").put_repository_catalog_data` method.

[Client.put_repository_catalog_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic.Client.put_repository_catalog_data)

```python
def put_repository_catalog_data(
    self,
    repositoryName: str,
    catalogData: RepositoryCatalogDataInputTypeDef,
    registryId: str = None
) -> PutRepositoryCatalogDataResponseTypeDef:
    pass
```

### set_repository_policy

Type annotations for `boto3.client("ecr-public").set_repository_policy` method.

[Client.set_repository_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic.Client.set_repository_policy)

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

### tag_resource

Type annotations for `boto3.client("ecr-public").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("ecr-public").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### upload_layer_part

Type annotations for `boto3.client("ecr-public").upload_layer_part` method.

[Client.upload_layer_part documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic.Client.upload_layer_part)

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

Type annotations for `boto3.client("ecr-public").get_paginator` method with overloads.

- `client.get_paginator("describe_image_tags")` -> [DescribeImageTagsPaginator](./paginators.md#describeimagetagspaginator)
- `client.get_paginator("describe_images")` -> [DescribeImagesPaginator](./paginators.md#describeimagespaginator)
- `client.get_paginator("describe_registries")` -> [DescribeRegistriesPaginator](./paginators.md#describeregistriespaginator)
- `client.get_paginator("describe_repositories")` -> [DescribeRepositoriesPaginator](./paginators.md#describerepositoriespaginator)


