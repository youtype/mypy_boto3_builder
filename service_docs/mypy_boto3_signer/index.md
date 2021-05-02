# Type annotations for boto3 Signer module

> [Index](../index.md) > Signer

Auto-generated documentation for [Signer](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer)
type annotations stubs module [mypy_boto3_signer](https://pypi.org/project/mypy-boto3-signer/).

```bash
pip install mypy-boto3-signer
```

- [Type annotations for boto3 Signer module](#type-annotations-for-boto3-signer-module)
  - [SignerClient](#signerclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## SignerClient

Type annotations for  `boto3.client("signer")` as [SignerClient](./client.md)

Can be used directly:

```python
from mypy_boto3_signer.client import SignerClient
```


SignerClient [exceptions](./client.md#exceptions)



### Methods
- [add_profile_permission](./client.md#add-profile-permission)
- [can_paginate](./client.md#can-paginate)
- [cancel_signing_profile](./client.md#cancel-signing-profile)
- [describe_signing_job](./client.md#describe-signing-job)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_signing_platform](./client.md#get-signing-platform)
- [get_signing_profile](./client.md#get-signing-profile)
- [get_waiter](./client.md#get-waiter)
- [list_profile_permissions](./client.md#list-profile-permissions)
- [list_signing_jobs](./client.md#list-signing-jobs)
- [list_signing_platforms](./client.md#list-signing-platforms)
- [list_signing_profiles](./client.md#list-signing-profiles)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [put_signing_profile](./client.md#put-signing-profile)
- [remove_profile_permission](./client.md#remove-profile-permission)
- [revoke_signature](./client.md#revoke-signature)
- [revoke_signing_profile](./client.md#revoke-signing-profile)
- [start_signing_job](./client.md#start-signing-job)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServiceErrorException](./client.md#internalserviceerrorexception)
- [NotFoundException](./client.md#notfoundexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceLimitExceededException](./client.md#servicelimitexceededexception)
- [ThrottlingException](./client.md#throttlingexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("signer").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_signer.paginators import ListSigningJobsPaginator, ...
```

- [ListSigningJobsPaginator](./paginators.md#listsigningjobspaginator)
- [ListSigningPlatformsPaginator](./paginators.md#listsigningplatformspaginator)
- [ListSigningProfilesPaginator](./paginators.md#listsigningprofilespaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("signer").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_signer.waiters import SuccessfulSigningJobWaiter, ...
```

- [SuccessfulSigningJobWaiter](./waiters.md#successfulsigningjobwaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_signer.literals import Category, ...
```

- [Category](./literals.md#category)
- [EncryptionAlgorithm](./literals.md#encryptionalgorithm)
- [HashAlgorithm](./literals.md#hashalgorithm)
- [ImageFormat](./literals.md#imageformat)
- [ListSigningJobsPaginatorName](./literals.md#listsigningjobspaginatorname)
- [ListSigningPlatformsPaginatorName](./literals.md#listsigningplatformspaginatorname)
- [ListSigningProfilesPaginatorName](./literals.md#listsigningprofilespaginatorname)
- [SigningProfileStatus](./literals.md#signingprofilestatus)
- [SigningStatus](./literals.md#signingstatus)
- [SuccessfulSigningJobWaiterName](./literals.md#successfulsigningjobwaitername)
- [ValidityType](./literals.md#validitytype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_signer.type_defs import EncryptionAlgorithmOptionsTypeDef, ...
```

- [EncryptionAlgorithmOptionsTypeDef](./type_defs.md#encryptionalgorithmoptionstypedef)
- [HashAlgorithmOptionsTypeDef](./type_defs.md#hashalgorithmoptionstypedef)
- [PermissionTypeDef](./type_defs.md#permissiontypedef)
- [S3DestinationTypeDef](./type_defs.md#s3destinationtypedef)
- [S3SignedObjectTypeDef](./type_defs.md#s3signedobjecttypedef)
- [S3SourceTypeDef](./type_defs.md#s3sourcetypedef)
- [SignatureValidityPeriodTypeDef](./type_defs.md#signaturevalidityperiodtypedef)
- [SignedObjectTypeDef](./type_defs.md#signedobjecttypedef)
- [SigningConfigurationOverridesTypeDef](./type_defs.md#signingconfigurationoverridestypedef)
- [SigningConfigurationTypeDef](./type_defs.md#signingconfigurationtypedef)
- [SigningImageFormatTypeDef](./type_defs.md#signingimageformattypedef)
- [SigningJobRevocationRecordTypeDef](./type_defs.md#signingjobrevocationrecordtypedef)
- [SigningJobTypeDef](./type_defs.md#signingjobtypedef)
- [SigningMaterialTypeDef](./type_defs.md#signingmaterialtypedef)
- [SigningPlatformOverridesTypeDef](./type_defs.md#signingplatformoverridestypedef)
- [SigningPlatformTypeDef](./type_defs.md#signingplatformtypedef)
- [SigningProfileRevocationRecordTypeDef](./type_defs.md#signingprofilerevocationrecordtypedef)
- [SigningProfileTypeDef](./type_defs.md#signingprofiletypedef)
- [SourceTypeDef](./type_defs.md#sourcetypedef)
- [AddProfilePermissionResponseTypeDef](./type_defs.md#addprofilepermissionresponsetypedef)
- [DescribeSigningJobResponseTypeDef](./type_defs.md#describesigningjobresponsetypedef)
- [DestinationTypeDef](./type_defs.md#destinationtypedef)
- [GetSigningPlatformResponseTypeDef](./type_defs.md#getsigningplatformresponsetypedef)
- [GetSigningProfileResponseTypeDef](./type_defs.md#getsigningprofileresponsetypedef)
- [ListProfilePermissionsResponseTypeDef](./type_defs.md#listprofilepermissionsresponsetypedef)
- [ListSigningJobsResponseTypeDef](./type_defs.md#listsigningjobsresponsetypedef)
- [ListSigningPlatformsResponseTypeDef](./type_defs.md#listsigningplatformsresponsetypedef)
- [ListSigningProfilesResponseTypeDef](./type_defs.md#listsigningprofilesresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PutSigningProfileResponseTypeDef](./type_defs.md#putsigningprofileresponsetypedef)
- [RemoveProfilePermissionResponseTypeDef](./type_defs.md#removeprofilepermissionresponsetypedef)
- [StartSigningJobResponseTypeDef](./type_defs.md#startsigningjobresponsetypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
