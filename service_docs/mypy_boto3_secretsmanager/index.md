# Type annotations for boto3 SecretsManager module

> [Index](../index.md) > SecretsManager

Auto-generated documentation for [SecretsManager](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager)
type annotations stubs module [mypy_boto3_secretsmanager](https://pypi.org/project/mypy-boto3-secretsmanager/).

```bash
pip install mypy-boto3-secretsmanager
```

- [Type annotations for boto3 SecretsManager module](#type-annotations-for-boto3-secretsmanager-module)
  - [SecretsManagerClient](#secretsmanagerclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## SecretsManagerClient

Type annotations for  `boto3.client("secretsmanager")` as [SecretsManagerClient](./client.md)

Can be used directly:

```python
from mypy_boto3_secretsmanager.client import SecretsManagerClient
```


SecretsManagerClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [cancel_rotate_secret](./client.md#cancel-rotate-secret)
- [create_secret](./client.md#create-secret)
- [delete_resource_policy](./client.md#delete-resource-policy)
- [delete_secret](./client.md#delete-secret)
- [describe_secret](./client.md#describe-secret)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_random_password](./client.md#get-random-password)
- [get_resource_policy](./client.md#get-resource-policy)
- [get_secret_value](./client.md#get-secret-value)
- [list_secret_version_ids](./client.md#list-secret-version-ids)
- [list_secrets](./client.md#list-secrets)
- [put_resource_policy](./client.md#put-resource-policy)
- [put_secret_value](./client.md#put-secret-value)
- [remove_regions_from_replication](./client.md#remove-regions-from-replication)
- [replicate_secret_to_regions](./client.md#replicate-secret-to-regions)
- [restore_secret](./client.md#restore-secret)
- [rotate_secret](./client.md#rotate-secret)
- [stop_replication_to_replica](./client.md#stop-replication-to-replica)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_secret](./client.md#update-secret)
- [update_secret_version_stage](./client.md#update-secret-version-stage)
- [validate_resource_policy](./client.md#validate-resource-policy)




### Exceptions
- [ClientError](./client.md#clienterror)
- [DecryptionFailure](./client.md#decryptionfailure)
- [EncryptionFailure](./client.md#encryptionfailure)
- [InternalServiceError](./client.md#internalserviceerror)
- [InvalidNextTokenException](./client.md#invalidnexttokenexception)
- [InvalidParameterException](./client.md#invalidparameterexception)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [MalformedPolicyDocumentException](./client.md#malformedpolicydocumentexception)
- [PreconditionNotMetException](./client.md#preconditionnotmetexception)
- [PublicPolicyException](./client.md#publicpolicyexception)
- [ResourceExistsException](./client.md#resourceexistsexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("secretsmanager").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_secretsmanager.paginators import ListSecretsPaginator, ...
```

- [ListSecretsPaginator](./paginators.md#listsecretspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_secretsmanager.literals import FilterNameStringType, ...
```

- [FilterNameStringType](./literals.md#filternamestringtype)
- [ListSecretsPaginatorName](./literals.md#listsecretspaginatorname)
- [SortOrderType](./literals.md#sortordertype)
- [StatusType](./literals.md#statustype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_secretsmanager.type_defs import ReplicationStatusTypeTypeDef, ...
```

- [ReplicationStatusTypeTypeDef](./type_defs.md#replicationstatustypetypedef)
- [RotationRulesTypeTypeDef](./type_defs.md#rotationrulestypetypedef)
- [SecretListEntryTypeDef](./type_defs.md#secretlistentrytypedef)
- [SecretVersionsListEntryTypeDef](./type_defs.md#secretversionslistentrytypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [ValidationErrorsEntryTypeDef](./type_defs.md#validationerrorsentrytypedef)
- [CancelRotateSecretResponseTypeDef](./type_defs.md#cancelrotatesecretresponsetypedef)
- [CreateSecretResponseTypeDef](./type_defs.md#createsecretresponsetypedef)
- [DeleteResourcePolicyResponseTypeDef](./type_defs.md#deleteresourcepolicyresponsetypedef)
- [DeleteSecretResponseTypeDef](./type_defs.md#deletesecretresponsetypedef)
- [DescribeSecretResponseTypeDef](./type_defs.md#describesecretresponsetypedef)
- [FilterTypeDef](./type_defs.md#filtertypedef)
- [GetRandomPasswordResponseTypeDef](./type_defs.md#getrandompasswordresponsetypedef)
- [GetResourcePolicyResponseTypeDef](./type_defs.md#getresourcepolicyresponsetypedef)
- [GetSecretValueResponseTypeDef](./type_defs.md#getsecretvalueresponsetypedef)
- [ListSecretVersionIdsResponseTypeDef](./type_defs.md#listsecretversionidsresponsetypedef)
- [ListSecretsResponseTypeDef](./type_defs.md#listsecretsresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PutResourcePolicyResponseTypeDef](./type_defs.md#putresourcepolicyresponsetypedef)
- [PutSecretValueResponseTypeDef](./type_defs.md#putsecretvalueresponsetypedef)
- [RemoveRegionsFromReplicationResponseTypeDef](./type_defs.md#removeregionsfromreplicationresponsetypedef)
- [ReplicaRegionTypeTypeDef](./type_defs.md#replicaregiontypetypedef)
- [ReplicateSecretToRegionsResponseTypeDef](./type_defs.md#replicatesecrettoregionsresponsetypedef)
- [RestoreSecretResponseTypeDef](./type_defs.md#restoresecretresponsetypedef)
- [RotateSecretResponseTypeDef](./type_defs.md#rotatesecretresponsetypedef)
- [StopReplicationToReplicaResponseTypeDef](./type_defs.md#stopreplicationtoreplicaresponsetypedef)
- [UpdateSecretResponseTypeDef](./type_defs.md#updatesecretresponsetypedef)
- [UpdateSecretVersionStageResponseTypeDef](./type_defs.md#updatesecretversionstageresponsetypedef)
- [ValidateResourcePolicyResponseTypeDef](./type_defs.md#validateresourcepolicyresponsetypedef)
