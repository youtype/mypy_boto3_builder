# Structures for boto3 LakeFormation module

> [Index](../index.md) > [LakeFormation](./index.md) > Structures

Auto-generated documentation for [LakeFormation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation)
type annotations stubs module [mypy_boto3_lakeformation](https://pypi.org/project/mypy-boto3-lakeformation/).

- [Structures for boto3 LakeFormation module](#structures-for-boto3-lakeformation-module)
  - [BatchPermissionsFailureEntryTypeDef](#batchpermissionsfailureentrytypedef)
  - [BatchPermissionsRequestEntryTypeDef](#batchpermissionsrequestentrytypedef)
  - [ColumnWildcardTypeDef](#columnwildcardtypedef)
  - [DataLakePrincipalTypeDef](#datalakeprincipaltypedef)
  - [DataLakeSettingsTypeDef](#datalakesettingstypedef)
  - [DataLocationResourceTypeDef](#datalocationresourcetypedef)
  - [DatabaseResourceTypeDef](#databaseresourcetypedef)
  - [DetailsMapTypeDef](#detailsmaptypedef)
  - [ErrorDetailTypeDef](#errordetailtypedef)
  - [PrincipalPermissionsTypeDef](#principalpermissionstypedef)
  - [PrincipalResourcePermissionsTypeDef](#principalresourcepermissionstypedef)
  - [ResourceInfoTypeDef](#resourceinfotypedef)
  - [ResourceTypeDef](#resourcetypedef)
  - [TableResourceTypeDef](#tableresourcetypedef)
  - [TableWithColumnsResourceTypeDef](#tablewithcolumnsresourcetypedef)
  - [BatchGrantPermissionsResponseTypeDef](#batchgrantpermissionsresponsetypedef)
  - [BatchRevokePermissionsResponseTypeDef](#batchrevokepermissionsresponsetypedef)
  - [DescribeResourceResponseTypeDef](#describeresourceresponsetypedef)
  - [FilterConditionTypeDef](#filterconditiontypedef)
  - [GetDataLakeSettingsResponseTypeDef](#getdatalakesettingsresponsetypedef)
  - [GetEffectivePermissionsForPathResponseTypeDef](#geteffectivepermissionsforpathresponsetypedef)
  - [ListPermissionsResponseTypeDef](#listpermissionsresponsetypedef)
  - [ListResourcesResponseTypeDef](#listresourcesresponsetypedef)

## BatchPermissionsFailureEntryTypeDef

```python
from mypy_boto3_lakeformation.type_defs import BatchPermissionsFailureEntryTypeDef
```




Optional fields:
- `RequestEntry`: `"BatchPermissionsRequestEntryTypeDef"`
- `Error`: `"ErrorDetailTypeDef"`


## BatchPermissionsRequestEntryTypeDef

```python
from mypy_boto3_lakeformation.type_defs import BatchPermissionsRequestEntryTypeDef
```


Required fields:
- `Id`: `str`



Optional fields:
- `Principal`: `"DataLakePrincipalTypeDef"`
- `Resource`: `"ResourceTypeDef"`
- `Permissions`: `List[Permission]`
- `PermissionsWithGrantOption`: `List[Permission]`


## ColumnWildcardTypeDef

```python
from mypy_boto3_lakeformation.type_defs import ColumnWildcardTypeDef
```




Optional fields:
- `ExcludedColumnNames`: `List[str]`


## DataLakePrincipalTypeDef

```python
from mypy_boto3_lakeformation.type_defs import DataLakePrincipalTypeDef
```




Optional fields:
- `DataLakePrincipalIdentifier`: `str`


## DataLakeSettingsTypeDef

```python
from mypy_boto3_lakeformation.type_defs import DataLakeSettingsTypeDef
```




Optional fields:
- `DataLakeAdmins`: `List["DataLakePrincipalTypeDef"]`
- `CreateDatabaseDefaultPermissions`: `List["PrincipalPermissionsTypeDef"]`
- `CreateTableDefaultPermissions`: `List["PrincipalPermissionsTypeDef"]`
- `TrustedResourceOwners`: `List[str]`


## DataLocationResourceTypeDef

```python
from mypy_boto3_lakeformation.type_defs import DataLocationResourceTypeDef
```


Required fields:
- `ResourceArn`: `str`



Optional fields:
- `CatalogId`: `str`


## DatabaseResourceTypeDef

```python
from mypy_boto3_lakeformation.type_defs import DatabaseResourceTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `CatalogId`: `str`


## DetailsMapTypeDef

```python
from mypy_boto3_lakeformation.type_defs import DetailsMapTypeDef
```




Optional fields:
- `ResourceShare`: `List[str]`


## ErrorDetailTypeDef

```python
from mypy_boto3_lakeformation.type_defs import ErrorDetailTypeDef
```




Optional fields:
- `ErrorCode`: `str`
- `ErrorMessage`: `str`


## PrincipalPermissionsTypeDef

```python
from mypy_boto3_lakeformation.type_defs import PrincipalPermissionsTypeDef
```




Optional fields:
- `Principal`: `"DataLakePrincipalTypeDef"`
- `Permissions`: `List[Permission]`


## PrincipalResourcePermissionsTypeDef

```python
from mypy_boto3_lakeformation.type_defs import PrincipalResourcePermissionsTypeDef
```




Optional fields:
- `Principal`: `"DataLakePrincipalTypeDef"`
- `Resource`: `"ResourceTypeDef"`
- `Permissions`: `List[Permission]`
- `PermissionsWithGrantOption`: `List[Permission]`
- `AdditionalDetails`: `"DetailsMapTypeDef"`


## ResourceInfoTypeDef

```python
from mypy_boto3_lakeformation.type_defs import ResourceInfoTypeDef
```




Optional fields:
- `ResourceArn`: `str`
- `RoleArn`: `str`
- `LastModified`: `datetime`


## ResourceTypeDef

```python
from mypy_boto3_lakeformation.type_defs import ResourceTypeDef
```




Optional fields:
- `Catalog`: `Dict[str, Any]`
- `Database`: `"DatabaseResourceTypeDef"`
- `Table`: `"TableResourceTypeDef"`
- `TableWithColumns`: `"TableWithColumnsResourceTypeDef"`
- `DataLocation`: `"DataLocationResourceTypeDef"`


## TableResourceTypeDef

```python
from mypy_boto3_lakeformation.type_defs import TableResourceTypeDef
```


Required fields:
- `DatabaseName`: `str`



Optional fields:
- `CatalogId`: `str`
- `Name`: `str`
- `TableWildcard`: `Dict[str, Any]`


## TableWithColumnsResourceTypeDef

```python
from mypy_boto3_lakeformation.type_defs import TableWithColumnsResourceTypeDef
```


Required fields:
- `DatabaseName`: `str`
- `Name`: `str`



Optional fields:
- `CatalogId`: `str`
- `ColumnNames`: `List[str]`
- `ColumnWildcard`: `"ColumnWildcardTypeDef"`


## BatchGrantPermissionsResponseTypeDef

```python
from mypy_boto3_lakeformation.type_defs import BatchGrantPermissionsResponseTypeDef
```




Optional fields:
- `Failures`: `List["BatchPermissionsFailureEntryTypeDef"]`


## BatchRevokePermissionsResponseTypeDef

```python
from mypy_boto3_lakeformation.type_defs import BatchRevokePermissionsResponseTypeDef
```




Optional fields:
- `Failures`: `List["BatchPermissionsFailureEntryTypeDef"]`


## DescribeResourceResponseTypeDef

```python
from mypy_boto3_lakeformation.type_defs import DescribeResourceResponseTypeDef
```




Optional fields:
- `ResourceInfo`: `"ResourceInfoTypeDef"`


## FilterConditionTypeDef

```python
from mypy_boto3_lakeformation.type_defs import FilterConditionTypeDef
```




Optional fields:
- `Field`: `FieldNameString`
- `ComparisonOperator`: `ComparisonOperator`
- `StringValueList`: `List[str]`


## GetDataLakeSettingsResponseTypeDef

```python
from mypy_boto3_lakeformation.type_defs import GetDataLakeSettingsResponseTypeDef
```




Optional fields:
- `DataLakeSettings`: `"DataLakeSettingsTypeDef"`


## GetEffectivePermissionsForPathResponseTypeDef

```python
from mypy_boto3_lakeformation.type_defs import GetEffectivePermissionsForPathResponseTypeDef
```




Optional fields:
- `Permissions`: `List["PrincipalResourcePermissionsTypeDef"]`
- `NextToken`: `str`


## ListPermissionsResponseTypeDef

```python
from mypy_boto3_lakeformation.type_defs import ListPermissionsResponseTypeDef
```




Optional fields:
- `PrincipalResourcePermissions`: `List["PrincipalResourcePermissionsTypeDef"]`
- `NextToken`: `str`


## ListResourcesResponseTypeDef

```python
from mypy_boto3_lakeformation.type_defs import ListResourcesResponseTypeDef
```




Optional fields:
- `ResourceInfoList`: `List["ResourceInfoTypeDef"]`
- `NextToken`: `str`

