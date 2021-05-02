# Type annotations for boto3 LakeFormation module

> [Index](../index.md) > LakeFormation

Auto-generated documentation for [LakeFormation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation)
type annotations stubs module [mypy_boto3_lakeformation](https://pypi.org/project/mypy-boto3-lakeformation/).

```bash
pip install mypy-boto3-lakeformation
```

- [Type annotations for boto3 LakeFormation module](#type-annotations-for-boto3-lakeformation-module)
  - [LakeFormationClient](#lakeformationclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## LakeFormationClient

Type annotations for  `boto3.client("lakeformation")` as [LakeFormationClient](./client.md)

Can be used directly:

```python
from mypy_boto3_lakeformation.client import LakeFormationClient
```


LakeFormationClient [exceptions](./client.md#exceptions)



### Methods
- [batch_grant_permissions](./client.md#batch-grant-permissions)
- [batch_revoke_permissions](./client.md#batch-revoke-permissions)
- [can_paginate](./client.md#can-paginate)
- [deregister_resource](./client.md#deregister-resource)
- [describe_resource](./client.md#describe-resource)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_data_lake_settings](./client.md#get-data-lake-settings)
- [get_effective_permissions_for_path](./client.md#get-effective-permissions-for-path)
- [grant_permissions](./client.md#grant-permissions)
- [list_permissions](./client.md#list-permissions)
- [list_resources](./client.md#list-resources)
- [put_data_lake_settings](./client.md#put-data-lake-settings)
- [register_resource](./client.md#register-resource)
- [revoke_permissions](./client.md#revoke-permissions)
- [update_resource](./client.md#update-resource)




### Exceptions
- [AlreadyExistsException](./client.md#alreadyexistsexception)
- [ClientError](./client.md#clienterror)
- [ConcurrentModificationException](./client.md#concurrentmodificationexception)
- [EntityNotFoundException](./client.md#entitynotfoundexception)
- [InternalServiceException](./client.md#internalserviceexception)
- [InvalidInputException](./client.md#invalidinputexception)
- [OperationTimeoutException](./client.md#operationtimeoutexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_lakeformation.literals import ComparisonOperator, ...
```

- [ComparisonOperator](./literals.md#comparisonoperator)
- [DataLakeResourceType](./literals.md#datalakeresourcetype)
- [FieldNameString](./literals.md#fieldnamestring)
- [Permission](./literals.md#permission)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_lakeformation.type_defs import BatchGrantPermissionsResponseTypeDef, ...
```

- [BatchGrantPermissionsResponseTypeDef](./type_defs.md#batchgrantpermissionsresponsetypedef)
- [BatchPermissionsFailureEntryTypeDef](./type_defs.md#batchpermissionsfailureentrytypedef)
- [BatchPermissionsRequestEntryTypeDef](./type_defs.md#batchpermissionsrequestentrytypedef)
- [BatchRevokePermissionsResponseTypeDef](./type_defs.md#batchrevokepermissionsresponsetypedef)
- [ColumnWildcardTypeDef](./type_defs.md#columnwildcardtypedef)
- [DataLakePrincipalTypeDef](./type_defs.md#datalakeprincipaltypedef)
- [DataLakeSettingsTypeDef](./type_defs.md#datalakesettingstypedef)
- [DataLocationResourceTypeDef](./type_defs.md#datalocationresourcetypedef)
- [DatabaseResourceTypeDef](./type_defs.md#databaseresourcetypedef)
- [DescribeResourceResponseTypeDef](./type_defs.md#describeresourceresponsetypedef)
- [DetailsMapTypeDef](./type_defs.md#detailsmaptypedef)
- [ErrorDetailTypeDef](./type_defs.md#errordetailtypedef)
- [FilterConditionTypeDef](./type_defs.md#filterconditiontypedef)
- [GetDataLakeSettingsResponseTypeDef](./type_defs.md#getdatalakesettingsresponsetypedef)
- [GetEffectivePermissionsForPathResponseTypeDef](./type_defs.md#geteffectivepermissionsforpathresponsetypedef)
- [ListPermissionsResponseTypeDef](./type_defs.md#listpermissionsresponsetypedef)
- [ListResourcesResponseTypeDef](./type_defs.md#listresourcesresponsetypedef)
- [PrincipalPermissionsTypeDef](./type_defs.md#principalpermissionstypedef)
- [PrincipalResourcePermissionsTypeDef](./type_defs.md#principalresourcepermissionstypedef)
- [ResourceInfoTypeDef](./type_defs.md#resourceinfotypedef)
- [ResourceTypeDef](./type_defs.md#resourcetypedef)
- [TableResourceTypeDef](./type_defs.md#tableresourcetypedef)
- [TableWithColumnsResourceTypeDef](./type_defs.md#tablewithcolumnsresourcetypedef)
