# Structures for boto3 SecretsManager module

> [Index](../index.md) > [SecretsManager](./index.md) > Structures

Auto-generated documentation for [SecretsManager](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager)
type annotations stubs module [mypy_boto3_secretsmanager](https://pypi.org/project/mypy-boto3-secretsmanager/).

- [Structures for boto3 SecretsManager module](#structures-for-boto3-secretsmanager-module)
  - [CancelRotateSecretResponseTypeDef](#cancelrotatesecretresponsetypedef)
  - [CreateSecretResponseTypeDef](#createsecretresponsetypedef)
  - [DeleteResourcePolicyResponseTypeDef](#deleteresourcepolicyresponsetypedef)
  - [DeleteSecretResponseTypeDef](#deletesecretresponsetypedef)
  - [DescribeSecretResponseTypeDef](#describesecretresponsetypedef)
  - [FilterTypeDef](#filtertypedef)
  - [GetRandomPasswordResponseTypeDef](#getrandompasswordresponsetypedef)
  - [GetResourcePolicyResponseTypeDef](#getresourcepolicyresponsetypedef)
  - [GetSecretValueResponseTypeDef](#getsecretvalueresponsetypedef)
  - [ListSecretVersionIdsResponseTypeDef](#listsecretversionidsresponsetypedef)
  - [ListSecretsResponseTypeDef](#listsecretsresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PutResourcePolicyResponseTypeDef](#putresourcepolicyresponsetypedef)
  - [PutSecretValueResponseTypeDef](#putsecretvalueresponsetypedef)
  - [RemoveRegionsFromReplicationResponseTypeDef](#removeregionsfromreplicationresponsetypedef)
  - [ReplicaRegionTypeTypeDef](#replicaregiontypetypedef)
  - [ReplicateSecretToRegionsResponseTypeDef](#replicatesecrettoregionsresponsetypedef)
  - [ReplicationStatusTypeTypeDef](#replicationstatustypetypedef)
  - [RestoreSecretResponseTypeDef](#restoresecretresponsetypedef)
  - [RotateSecretResponseTypeDef](#rotatesecretresponsetypedef)
  - [RotationRulesTypeTypeDef](#rotationrulestypetypedef)
  - [SecretListEntryTypeDef](#secretlistentrytypedef)
  - [SecretVersionsListEntryTypeDef](#secretversionslistentrytypedef)
  - [StopReplicationToReplicaResponseTypeDef](#stopreplicationtoreplicaresponsetypedef)
  - [TagTypeDef](#tagtypedef)
  - [UpdateSecretResponseTypeDef](#updatesecretresponsetypedef)
  - [UpdateSecretVersionStageResponseTypeDef](#updatesecretversionstageresponsetypedef)
  - [ValidateResourcePolicyResponseTypeDef](#validateresourcepolicyresponsetypedef)
  - [ValidationErrorsEntryTypeDef](#validationerrorsentrytypedef)

## CancelRotateSecretResponseTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import CancelRotateSecretResponseTypeDef
```




Optional fields:
- `ARN`: `str`
- `Name`: `str`
- `VersionId`: `str`


## CreateSecretResponseTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import CreateSecretResponseTypeDef
```




Optional fields:
- `ARN`: `str`
- `Name`: `str`
- `VersionId`: `str`
- `ReplicationStatus`: `List["ReplicationStatusTypeTypeDef"]`


## DeleteResourcePolicyResponseTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import DeleteResourcePolicyResponseTypeDef
```




Optional fields:
- `ARN`: `str`
- `Name`: `str`


## DeleteSecretResponseTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import DeleteSecretResponseTypeDef
```




Optional fields:
- `ARN`: `str`
- `Name`: `str`
- `DeletionDate`: `datetime`


## DescribeSecretResponseTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import DescribeSecretResponseTypeDef
```




Optional fields:
- `ARN`: `str`
- `Name`: `str`
- `Description`: `str`
- `KmsKeyId`: `str`
- `RotationEnabled`: `bool`
- `RotationLambdaARN`: `str`
- `RotationRules`: `"RotationRulesTypeTypeDef"`
- `LastRotatedDate`: `datetime`
- `LastChangedDate`: `datetime`
- `LastAccessedDate`: `datetime`
- `DeletedDate`: `datetime`
- `Tags`: `List["TagTypeDef"]`
- `VersionIdsToStages`: `Dict[str, List[str]]`
- `OwningService`: `str`
- `CreatedDate`: `datetime`
- `PrimaryRegion`: `str`
- `ReplicationStatus`: `List["ReplicationStatusTypeTypeDef"]`


## FilterTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import FilterTypeDef
```




Optional fields:
- `Key`: `FilterNameStringType`
- `Values`: `List[str]`


## GetRandomPasswordResponseTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import GetRandomPasswordResponseTypeDef
```




Optional fields:
- `RandomPassword`: `str`


## GetResourcePolicyResponseTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import GetResourcePolicyResponseTypeDef
```




Optional fields:
- `ARN`: `str`
- `Name`: `str`
- `ResourcePolicy`: `str`


## GetSecretValueResponseTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import GetSecretValueResponseTypeDef
```




Optional fields:
- `ARN`: `str`
- `Name`: `str`
- `VersionId`: `str`
- `SecretBinary`: `Union[bytes, IO[bytes]]`
- `SecretString`: `str`
- `VersionStages`: `List[str]`
- `CreatedDate`: `datetime`


## ListSecretVersionIdsResponseTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import ListSecretVersionIdsResponseTypeDef
```




Optional fields:
- `Versions`: `List["SecretVersionsListEntryTypeDef"]`
- `NextToken`: `str`
- `ARN`: `str`
- `Name`: `str`


## ListSecretsResponseTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import ListSecretsResponseTypeDef
```




Optional fields:
- `SecretList`: `List["SecretListEntryTypeDef"]`
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PutResourcePolicyResponseTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import PutResourcePolicyResponseTypeDef
```




Optional fields:
- `ARN`: `str`
- `Name`: `str`


## PutSecretValueResponseTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import PutSecretValueResponseTypeDef
```




Optional fields:
- `ARN`: `str`
- `Name`: `str`
- `VersionId`: `str`
- `VersionStages`: `List[str]`


## RemoveRegionsFromReplicationResponseTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import RemoveRegionsFromReplicationResponseTypeDef
```




Optional fields:
- `ARN`: `str`
- `ReplicationStatus`: `List["ReplicationStatusTypeTypeDef"]`


## ReplicaRegionTypeTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import ReplicaRegionTypeTypeDef
```




Optional fields:
- `Region`: `str`
- `KmsKeyId`: `str`


## ReplicateSecretToRegionsResponseTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import ReplicateSecretToRegionsResponseTypeDef
```




Optional fields:
- `ARN`: `str`
- `ReplicationStatus`: `List["ReplicationStatusTypeTypeDef"]`


## ReplicationStatusTypeTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import ReplicationStatusTypeTypeDef
```




Optional fields:
- `Region`: `str`
- `KmsKeyId`: `str`
- `Status`: `StatusType`
- `StatusMessage`: `str`
- `LastAccessedDate`: `datetime`


## RestoreSecretResponseTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import RestoreSecretResponseTypeDef
```




Optional fields:
- `ARN`: `str`
- `Name`: `str`


## RotateSecretResponseTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import RotateSecretResponseTypeDef
```




Optional fields:
- `ARN`: `str`
- `Name`: `str`
- `VersionId`: `str`


## RotationRulesTypeTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import RotationRulesTypeTypeDef
```




Optional fields:
- `AutomaticallyAfterDays`: `int`


## SecretListEntryTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import SecretListEntryTypeDef
```




Optional fields:
- `ARN`: `str`
- `Name`: `str`
- `Description`: `str`
- `KmsKeyId`: `str`
- `RotationEnabled`: `bool`
- `RotationLambdaARN`: `str`
- `RotationRules`: `"RotationRulesTypeTypeDef"`
- `LastRotatedDate`: `datetime`
- `LastChangedDate`: `datetime`
- `LastAccessedDate`: `datetime`
- `DeletedDate`: `datetime`
- `Tags`: `List["TagTypeDef"]`
- `SecretVersionsToStages`: `Dict[str, List[str]]`
- `OwningService`: `str`
- `CreatedDate`: `datetime`
- `PrimaryRegion`: `str`


## SecretVersionsListEntryTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import SecretVersionsListEntryTypeDef
```




Optional fields:
- `VersionId`: `str`
- `VersionStages`: `List[str]`
- `LastAccessedDate`: `datetime`
- `CreatedDate`: `datetime`


## StopReplicationToReplicaResponseTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import StopReplicationToReplicaResponseTypeDef
```




Optional fields:
- `ARN`: `str`


## TagTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import TagTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## UpdateSecretResponseTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import UpdateSecretResponseTypeDef
```




Optional fields:
- `ARN`: `str`
- `Name`: `str`
- `VersionId`: `str`


## UpdateSecretVersionStageResponseTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import UpdateSecretVersionStageResponseTypeDef
```




Optional fields:
- `ARN`: `str`
- `Name`: `str`


## ValidateResourcePolicyResponseTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import ValidateResourcePolicyResponseTypeDef
```




Optional fields:
- `PolicyValidationPassed`: `bool`
- `ValidationErrors`: `List["ValidationErrorsEntryTypeDef"]`


## ValidationErrorsEntryTypeDef

```python
from mypy_boto3_secretsmanager.type_defs import ValidationErrorsEntryTypeDef
```




Optional fields:
- `CheckName`: `str`
- `ErrorMessage`: `str`

