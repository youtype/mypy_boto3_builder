# SecretsManagerClient for boto3 SecretsManager module

> [Index](../index.md) > [SecretsManager](./index.md) > SecretsManagerClient

Auto-generated documentation for [SecretsManager](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager)
type annotations stubs module [mypy_boto3_secretsmanager](https://pypi.org/project/mypy-boto3-secretsmanager/).

- [SecretsManagerClient for boto3 SecretsManager module](#secretsmanagerclient-for-boto3-secretsmanager-module)
  - [SecretsManagerClient](#secretsmanagerclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [cancel_rotate_secret](#cancel_rotate_secret)
    - [create_secret](#create_secret)
    - [delete_resource_policy](#delete_resource_policy)
    - [delete_secret](#delete_secret)
    - [describe_secret](#describe_secret)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_random_password](#get_random_password)
    - [get_resource_policy](#get_resource_policy)
    - [get_secret_value](#get_secret_value)
    - [list_secret_version_ids](#list_secret_version_ids)
    - [list_secrets](#list_secrets)
    - [put_resource_policy](#put_resource_policy)
    - [put_secret_value](#put_secret_value)
    - [remove_regions_from_replication](#remove_regions_from_replication)
    - [replicate_secret_to_regions](#replicate_secret_to_regions)
    - [restore_secret](#restore_secret)
    - [rotate_secret](#rotate_secret)
    - [stop_replication_to_replica](#stop_replication_to_replica)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_secret](#update_secret)
    - [update_secret_version_stage](#update_secret_version_stage)
    - [validate_resource_policy](#validate_resource_policy)
    - [get_paginator](#get_paginator)

## SecretsManagerClient

Type annotations for `boto3.client("secretsmanager")`

Can be used directly:

```python
from mypy_boto3_secretsmanager.client import SecretsManagerClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_secretsmanager.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.DecryptionFailure`
- `Exceptions.EncryptionFailure`
- `Exceptions.InternalServiceError`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.InvalidParameterException`
- `Exceptions.InvalidRequestException`
- `Exceptions.LimitExceededException`
- `Exceptions.MalformedPolicyDocumentException`
- `Exceptions.PreconditionNotMetException`
- `Exceptions.PublicPolicyException`
- `Exceptions.ResourceExistsException`
- `Exceptions.ResourceNotFoundException`


## Methods


### can_paginate

Type annotations for `boto3.client("secretsmanager").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_rotate_secret

Type annotations for `boto3.client("secretsmanager").cancel_rotate_secret` method.

[Client.cancel_rotate_secret documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.cancel_rotate_secret)

```python
def cancel_rotate_secret(
    self,
    SecretId: str
) -> CancelRotateSecretResponseTypeDef:
    pass
```

### create_secret

Type annotations for `boto3.client("secretsmanager").create_secret` method.

[Client.create_secret documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.create_secret)

```python
def create_secret(
    self,
    Name: str,
    ClientRequestToken: str = None,
    Description: str = None,
    KmsKeyId: str = None,
    SecretBinary: Union[bytes, IO[bytes]] = None,
    SecretString: str = None,
    Tags: List["TagTypeDef"] = None,
    AddReplicaRegions: List[ReplicaRegionTypeTypeDef] = None,
    ForceOverwriteReplicaSecret: bool = None
) -> CreateSecretResponseTypeDef:
    pass
```

### delete_resource_policy

Type annotations for `boto3.client("secretsmanager").delete_resource_policy` method.

[Client.delete_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.delete_resource_policy)

```python
def delete_resource_policy(
    self,
    SecretId: str
) -> DeleteResourcePolicyResponseTypeDef:
    pass
```

### delete_secret

Type annotations for `boto3.client("secretsmanager").delete_secret` method.

[Client.delete_secret documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.delete_secret)

```python
def delete_secret(
    self,
    SecretId: str,
    RecoveryWindowInDays: int = None,
    ForceDeleteWithoutRecovery: bool = None
) -> DeleteSecretResponseTypeDef:
    pass
```

### describe_secret

Type annotations for `boto3.client("secretsmanager").describe_secret` method.

[Client.describe_secret documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.describe_secret)

```python
def describe_secret(
    self,
    SecretId: str
) -> DescribeSecretResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("secretsmanager").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.generate_presigned_url)

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

### get_random_password

Type annotations for `boto3.client("secretsmanager").get_random_password` method.

[Client.get_random_password documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.get_random_password)

```python
def get_random_password(
    self,
    PasswordLength: int = None,
    ExcludeCharacters: str = None,
    ExcludeNumbers: bool = None,
    ExcludePunctuation: bool = None,
    ExcludeUppercase: bool = None,
    ExcludeLowercase: bool = None,
    IncludeSpace: bool = None,
    RequireEachIncludedType: bool = None
) -> GetRandomPasswordResponseTypeDef:
    pass
```

### get_resource_policy

Type annotations for `boto3.client("secretsmanager").get_resource_policy` method.

[Client.get_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.get_resource_policy)

```python
def get_resource_policy(
    self,
    SecretId: str
) -> GetResourcePolicyResponseTypeDef:
    pass
```

### get_secret_value

Type annotations for `boto3.client("secretsmanager").get_secret_value` method.

[Client.get_secret_value documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.get_secret_value)

```python
def get_secret_value(
    self,
    SecretId: str,
    VersionId: str = None,
    VersionStage: str = None
) -> GetSecretValueResponseTypeDef:
    pass
```

### list_secret_version_ids

Type annotations for `boto3.client("secretsmanager").list_secret_version_ids` method.

[Client.list_secret_version_ids documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.list_secret_version_ids)

```python
def list_secret_version_ids(
    self,
    SecretId: str,
    MaxResults: int = None,
    NextToken: str = None,
    IncludeDeprecated: bool = None
) -> ListSecretVersionIdsResponseTypeDef:
    pass
```

### list_secrets

Type annotations for `boto3.client("secretsmanager").list_secrets` method.

[Client.list_secrets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.list_secrets)

```python
def list_secrets(
    self,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[FilterTypeDef] = None,
    SortOrder: SortOrderType = None
) -> ListSecretsResponseTypeDef:
    pass
```

### put_resource_policy

Type annotations for `boto3.client("secretsmanager").put_resource_policy` method.

[Client.put_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.put_resource_policy)

```python
def put_resource_policy(
    self,
    SecretId: str,
    ResourcePolicy: str,
    BlockPublicPolicy: bool = None
) -> PutResourcePolicyResponseTypeDef:
    pass
```

### put_secret_value

Type annotations for `boto3.client("secretsmanager").put_secret_value` method.

[Client.put_secret_value documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.put_secret_value)

```python
def put_secret_value(
    self,
    SecretId: str,
    ClientRequestToken: str = None,
    SecretBinary: Union[bytes, IO[bytes]] = None,
    SecretString: str = None,
    VersionStages: List[str] = None
) -> PutSecretValueResponseTypeDef:
    pass
```

### remove_regions_from_replication

Type annotations for `boto3.client("secretsmanager").remove_regions_from_replication` method.

[Client.remove_regions_from_replication documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.remove_regions_from_replication)

```python
def remove_regions_from_replication(
    self,
    SecretId: str,
    RemoveReplicaRegions: List[str]
) -> RemoveRegionsFromReplicationResponseTypeDef:
    pass
```

### replicate_secret_to_regions

Type annotations for `boto3.client("secretsmanager").replicate_secret_to_regions` method.

[Client.replicate_secret_to_regions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.replicate_secret_to_regions)

```python
def replicate_secret_to_regions(
    self,
    SecretId: str,
    AddReplicaRegions: List[ReplicaRegionTypeTypeDef],
    ForceOverwriteReplicaSecret: bool = None
) -> ReplicateSecretToRegionsResponseTypeDef:
    pass
```

### restore_secret

Type annotations for `boto3.client("secretsmanager").restore_secret` method.

[Client.restore_secret documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.restore_secret)

```python
def restore_secret(
    self,
    SecretId: str
) -> RestoreSecretResponseTypeDef:
    pass
```

### rotate_secret

Type annotations for `boto3.client("secretsmanager").rotate_secret` method.

[Client.rotate_secret documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.rotate_secret)

```python
def rotate_secret(
    self,
    SecretId: str,
    ClientRequestToken: str = None,
    RotationLambdaARN: str = None,
    RotationRules: "RotationRulesTypeTypeDef" = None
) -> RotateSecretResponseTypeDef:
    pass
```

### stop_replication_to_replica

Type annotations for `boto3.client("secretsmanager").stop_replication_to_replica` method.

[Client.stop_replication_to_replica documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.stop_replication_to_replica)

```python
def stop_replication_to_replica(
    self,
    SecretId: str
) -> StopReplicationToReplicaResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("secretsmanager").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.tag_resource)

```python
def tag_resource(
    self,
    SecretId: str,
    Tags: List["TagTypeDef"]
) -> None:
    pass
```

### untag_resource

Type annotations for `boto3.client("secretsmanager").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.untag_resource)

```python
def untag_resource(
    self,
    SecretId: str,
    TagKeys: List[str]
) -> None:
    pass
```

### update_secret

Type annotations for `boto3.client("secretsmanager").update_secret` method.

[Client.update_secret documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.update_secret)

```python
def update_secret(
    self,
    SecretId: str,
    ClientRequestToken: str = None,
    Description: str = None,
    KmsKeyId: str = None,
    SecretBinary: Union[bytes, IO[bytes]] = None,
    SecretString: str = None
) -> UpdateSecretResponseTypeDef:
    pass
```

### update_secret_version_stage

Type annotations for `boto3.client("secretsmanager").update_secret_version_stage` method.

[Client.update_secret_version_stage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.update_secret_version_stage)

```python
def update_secret_version_stage(
    self,
    SecretId: str,
    VersionStage: str,
    RemoveFromVersionId: str = None,
    MoveToVersionId: str = None
) -> UpdateSecretVersionStageResponseTypeDef:
    pass
```

### validate_resource_policy

Type annotations for `boto3.client("secretsmanager").validate_resource_policy` method.

[Client.validate_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.validate_resource_policy)

```python
def validate_resource_policy(
    self,
    ResourcePolicy: str,
    SecretId: str = None
) -> ValidateResourcePolicyResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("secretsmanager").get_paginator` method with overloads.

- `client.get_paginator("list_secrets")` -> [ListSecretsPaginator](./paginators.md#listsecretspaginator)


