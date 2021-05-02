# Type annotations for boto3 ECRPublic module

> [Index](../index.md) > ECRPublic

Auto-generated documentation for [ECRPublic](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic)
type annotations stubs module [mypy_boto3_ecr_public](https://pypi.org/project/mypy-boto3-ecr-public/).

```bash
pip install mypy-boto3-ecr-public
```

- [Type annotations for boto3 ECRPublic module](#type-annotations-for-boto3-ecrpublic-module)
  - [ECRPublicClient](#ecrpublicclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## ECRPublicClient

Type annotations for  `boto3.client("ecr-public")` as [ECRPublicClient](./client.md)

Can be used directly:

```python
from mypy_boto3_ecr_public.client import ECRPublicClient
```


ECRPublicClient [exceptions](./client.md#exceptions)



### Methods
- [batch_check_layer_availability](./client.md#batch-check-layer-availability)
- [batch_delete_image](./client.md#batch-delete-image)
- [can_paginate](./client.md#can-paginate)
- [complete_layer_upload](./client.md#complete-layer-upload)
- [create_repository](./client.md#create-repository)
- [delete_repository](./client.md#delete-repository)
- [delete_repository_policy](./client.md#delete-repository-policy)
- [describe_image_tags](./client.md#describe-image-tags)
- [describe_images](./client.md#describe-images)
- [describe_registries](./client.md#describe-registries)
- [describe_repositories](./client.md#describe-repositories)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_authorization_token](./client.md#get-authorization-token)
- [get_paginator](./client.md#get-paginator)
- [get_registry_catalog_data](./client.md#get-registry-catalog-data)
- [get_repository_catalog_data](./client.md#get-repository-catalog-data)
- [get_repository_policy](./client.md#get-repository-policy)
- [initiate_layer_upload](./client.md#initiate-layer-upload)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [put_image](./client.md#put-image)
- [put_registry_catalog_data](./client.md#put-registry-catalog-data)
- [put_repository_catalog_data](./client.md#put-repository-catalog-data)
- [set_repository_policy](./client.md#set-repository-policy)
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
- [LayerAlreadyExistsException](./client.md#layeralreadyexistsexception)
- [LayerPartTooSmallException](./client.md#layerparttoosmallexception)
- [LayersNotFoundException](./client.md#layersnotfoundexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ReferencedImagesNotFoundException](./client.md#referencedimagesnotfoundexception)
- [RegistryNotFoundException](./client.md#registrynotfoundexception)
- [RepositoryAlreadyExistsException](./client.md#repositoryalreadyexistsexception)
- [RepositoryNotEmptyException](./client.md#repositorynotemptyexception)
- [RepositoryNotFoundException](./client.md#repositorynotfoundexception)
- [RepositoryPolicyNotFoundException](./client.md#repositorypolicynotfoundexception)
- [ServerException](./client.md#serverexception)
- [TooManyTagsException](./client.md#toomanytagsexception)
- [UnsupportedCommandException](./client.md#unsupportedcommandexception)
- [UploadNotFoundException](./client.md#uploadnotfoundexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("ecr-public").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_ecr_public.paginators import DescribeImageTagsPaginator, ...
```

- [DescribeImageTagsPaginator](./paginators.md#describeimagetagspaginator)
- [DescribeImagesPaginator](./paginators.md#describeimagespaginator)
- [DescribeRegistriesPaginator](./paginators.md#describeregistriespaginator)
- [DescribeRepositoriesPaginator](./paginators.md#describerepositoriespaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_ecr_public.literals import DescribeImageTagsPaginatorName, ...
```

- [DescribeImageTagsPaginatorName](./literals.md#describeimagetagspaginatorname)
- [DescribeImagesPaginatorName](./literals.md#describeimagespaginatorname)
- [DescribeRegistriesPaginatorName](./literals.md#describeregistriespaginatorname)
- [DescribeRepositoriesPaginatorName](./literals.md#describerepositoriespaginatorname)
- [ImageFailureCode](./literals.md#imagefailurecode)
- [LayerAvailability](./literals.md#layeravailability)
- [LayerFailureCode](./literals.md#layerfailurecode)
- [RegistryAliasStatus](./literals.md#registryaliasstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_ecr_public.type_defs import AuthorizationDataTypeDef, ...
```

- [AuthorizationDataTypeDef](./type_defs.md#authorizationdatatypedef)
- [BatchCheckLayerAvailabilityResponseTypeDef](./type_defs.md#batchchecklayeravailabilityresponsetypedef)
- [BatchDeleteImageResponseTypeDef](./type_defs.md#batchdeleteimageresponsetypedef)
- [CompleteLayerUploadResponseTypeDef](./type_defs.md#completelayeruploadresponsetypedef)
- [CreateRepositoryResponseTypeDef](./type_defs.md#createrepositoryresponsetypedef)
- [DeleteRepositoryPolicyResponseTypeDef](./type_defs.md#deleterepositorypolicyresponsetypedef)
- [DeleteRepositoryResponseTypeDef](./type_defs.md#deleterepositoryresponsetypedef)
- [DescribeImageTagsResponseTypeDef](./type_defs.md#describeimagetagsresponsetypedef)
- [DescribeImagesResponseTypeDef](./type_defs.md#describeimagesresponsetypedef)
- [DescribeRegistriesResponseTypeDef](./type_defs.md#describeregistriesresponsetypedef)
- [DescribeRepositoriesResponseTypeDef](./type_defs.md#describerepositoriesresponsetypedef)
- [GetAuthorizationTokenResponseTypeDef](./type_defs.md#getauthorizationtokenresponsetypedef)
- [GetRegistryCatalogDataResponseTypeDef](./type_defs.md#getregistrycatalogdataresponsetypedef)
- [GetRepositoryCatalogDataResponseTypeDef](./type_defs.md#getrepositorycatalogdataresponsetypedef)
- [GetRepositoryPolicyResponseTypeDef](./type_defs.md#getrepositorypolicyresponsetypedef)
- [ImageDetailTypeDef](./type_defs.md#imagedetailtypedef)
- [ImageFailureTypeDef](./type_defs.md#imagefailuretypedef)
- [ImageIdentifierTypeDef](./type_defs.md#imageidentifiertypedef)
- [ImageTagDetailTypeDef](./type_defs.md#imagetagdetailtypedef)
- [ImageTypeDef](./type_defs.md#imagetypedef)
- [InitiateLayerUploadResponseTypeDef](./type_defs.md#initiatelayeruploadresponsetypedef)
- [LayerFailureTypeDef](./type_defs.md#layerfailuretypedef)
- [LayerTypeDef](./type_defs.md#layertypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PutImageResponseTypeDef](./type_defs.md#putimageresponsetypedef)
- [PutRegistryCatalogDataResponseTypeDef](./type_defs.md#putregistrycatalogdataresponsetypedef)
- [PutRepositoryCatalogDataResponseTypeDef](./type_defs.md#putrepositorycatalogdataresponsetypedef)
- [ReferencedImageDetailTypeDef](./type_defs.md#referencedimagedetailtypedef)
- [RegistryAliasTypeDef](./type_defs.md#registryaliastypedef)
- [RegistryCatalogDataTypeDef](./type_defs.md#registrycatalogdatatypedef)
- [RegistryTypeDef](./type_defs.md#registrytypedef)
- [RepositoryCatalogDataInputTypeDef](./type_defs.md#repositorycatalogdatainputtypedef)
- [RepositoryCatalogDataTypeDef](./type_defs.md#repositorycatalogdatatypedef)
- [RepositoryTypeDef](./type_defs.md#repositorytypedef)
- [SetRepositoryPolicyResponseTypeDef](./type_defs.md#setrepositorypolicyresponsetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [UploadLayerPartResponseTypeDef](./type_defs.md#uploadlayerpartresponsetypedef)
