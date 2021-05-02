# Structures for boto3 OpsWorksCM module

> [Index](../index.md) > [OpsWorksCM](./index.md) > Structures

Auto-generated documentation for [OpsWorksCM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM)
type annotations stubs module [mypy_boto3_opsworkscm](https://pypi.org/project/mypy-boto3-opsworkscm/).

- [Structures for boto3 OpsWorksCM module](#structures-for-boto3-opsworkscm-module)
  - [AccountAttributeTypeDef](#accountattributetypedef)
  - [AssociateNodeResponseTypeDef](#associatenoderesponsetypedef)
  - [BackupTypeDef](#backuptypedef)
  - [CreateBackupResponseTypeDef](#createbackupresponsetypedef)
  - [CreateServerResponseTypeDef](#createserverresponsetypedef)
  - [DescribeAccountAttributesResponseTypeDef](#describeaccountattributesresponsetypedef)
  - [DescribeBackupsResponseTypeDef](#describebackupsresponsetypedef)
  - [DescribeEventsResponseTypeDef](#describeeventsresponsetypedef)
  - [DescribeNodeAssociationStatusResponseTypeDef](#describenodeassociationstatusresponsetypedef)
  - [DescribeServersResponseTypeDef](#describeserversresponsetypedef)
  - [DisassociateNodeResponseTypeDef](#disassociatenoderesponsetypedef)
  - [EngineAttributeTypeDef](#engineattributetypedef)
  - [ExportServerEngineAttributeResponseTypeDef](#exportserverengineattributeresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ServerEventTypeDef](#servereventtypedef)
  - [ServerTypeDef](#servertypedef)
  - [StartMaintenanceResponseTypeDef](#startmaintenanceresponsetypedef)
  - [TagTypeDef](#tagtypedef)
  - [UpdateServerEngineAttributesResponseTypeDef](#updateserverengineattributesresponsetypedef)
  - [UpdateServerResponseTypeDef](#updateserverresponsetypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## AccountAttributeTypeDef

```python
from mypy_boto3_opsworkscm.type_defs import AccountAttributeTypeDef
```




Optional fields:
- `Name`: `str`
- `Maximum`: `int`
- `Used`: `int`


## AssociateNodeResponseTypeDef

```python
from mypy_boto3_opsworkscm.type_defs import AssociateNodeResponseTypeDef
```




Optional fields:
- `NodeAssociationStatusToken`: `str`


## BackupTypeDef

```python
from mypy_boto3_opsworkscm.type_defs import BackupTypeDef
```




Optional fields:
- `BackupArn`: `str`
- `BackupId`: `str`
- `BackupType`: `BackupType`
- `CreatedAt`: `datetime`
- `Description`: `str`
- `Engine`: `str`
- `EngineModel`: `str`
- `EngineVersion`: `str`
- `InstanceProfileArn`: `str`
- `InstanceType`: `str`
- `KeyPair`: `str`
- `PreferredBackupWindow`: `str`
- `PreferredMaintenanceWindow`: `str`
- `S3DataSize`: `int`
- `S3DataUrl`: `str`
- `S3LogUrl`: `str`
- `SecurityGroupIds`: `List[str]`
- `ServerName`: `str`
- `ServiceRoleArn`: `str`
- `Status`: `BackupStatus`
- `StatusDescription`: `str`
- `SubnetIds`: `List[str]`
- `ToolsVersion`: `str`
- `UserArn`: `str`


## CreateBackupResponseTypeDef

```python
from mypy_boto3_opsworkscm.type_defs import CreateBackupResponseTypeDef
```




Optional fields:
- `Backup`: `"BackupTypeDef"`


## CreateServerResponseTypeDef

```python
from mypy_boto3_opsworkscm.type_defs import CreateServerResponseTypeDef
```




Optional fields:
- `Server`: `"ServerTypeDef"`


## DescribeAccountAttributesResponseTypeDef

```python
from mypy_boto3_opsworkscm.type_defs import DescribeAccountAttributesResponseTypeDef
```




Optional fields:
- `Attributes`: `List["AccountAttributeTypeDef"]`


## DescribeBackupsResponseTypeDef

```python
from mypy_boto3_opsworkscm.type_defs import DescribeBackupsResponseTypeDef
```




Optional fields:
- `Backups`: `List["BackupTypeDef"]`
- `NextToken`: `str`


## DescribeEventsResponseTypeDef

```python
from mypy_boto3_opsworkscm.type_defs import DescribeEventsResponseTypeDef
```




Optional fields:
- `ServerEvents`: `List["ServerEventTypeDef"]`
- `NextToken`: `str`


## DescribeNodeAssociationStatusResponseTypeDef

```python
from mypy_boto3_opsworkscm.type_defs import DescribeNodeAssociationStatusResponseTypeDef
```




Optional fields:
- `NodeAssociationStatus`: `NodeAssociationStatus`
- `EngineAttributes`: `List["EngineAttributeTypeDef"]`


## DescribeServersResponseTypeDef

```python
from mypy_boto3_opsworkscm.type_defs import DescribeServersResponseTypeDef
```




Optional fields:
- `Servers`: `List["ServerTypeDef"]`
- `NextToken`: `str`


## DisassociateNodeResponseTypeDef

```python
from mypy_boto3_opsworkscm.type_defs import DisassociateNodeResponseTypeDef
```




Optional fields:
- `NodeAssociationStatusToken`: `str`


## EngineAttributeTypeDef

```python
from mypy_boto3_opsworkscm.type_defs import EngineAttributeTypeDef
```




Optional fields:
- `Name`: `str`
- `Value`: `str`


## ExportServerEngineAttributeResponseTypeDef

```python
from mypy_boto3_opsworkscm.type_defs import ExportServerEngineAttributeResponseTypeDef
```




Optional fields:
- `EngineAttribute`: `"EngineAttributeTypeDef"`
- `ServerName`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_opsworkscm.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_opsworkscm.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ServerEventTypeDef

```python
from mypy_boto3_opsworkscm.type_defs import ServerEventTypeDef
```




Optional fields:
- `CreatedAt`: `datetime`
- `ServerName`: `str`
- `Message`: `str`
- `LogUrl`: `str`


## ServerTypeDef

```python
from mypy_boto3_opsworkscm.type_defs import ServerTypeDef
```




Optional fields:
- `AssociatePublicIpAddress`: `bool`
- `BackupRetentionCount`: `int`
- `ServerName`: `str`
- `CreatedAt`: `datetime`
- `CloudFormationStackArn`: `str`
- `CustomDomain`: `str`
- `DisableAutomatedBackup`: `bool`
- `Endpoint`: `str`
- `Engine`: `str`
- `EngineModel`: `str`
- `EngineAttributes`: `List["EngineAttributeTypeDef"]`
- `EngineVersion`: `str`
- `InstanceProfileArn`: `str`
- `InstanceType`: `str`
- `KeyPair`: `str`
- `MaintenanceStatus`: `MaintenanceStatus`
- `PreferredMaintenanceWindow`: `str`
- `PreferredBackupWindow`: `str`
- `SecurityGroupIds`: `List[str]`
- `ServiceRoleArn`: `str`
- `Status`: `ServerStatus`
- `StatusReason`: `str`
- `SubnetIds`: `List[str]`
- `ServerArn`: `str`


## StartMaintenanceResponseTypeDef

```python
from mypy_boto3_opsworkscm.type_defs import StartMaintenanceResponseTypeDef
```




Optional fields:
- `Server`: `"ServerTypeDef"`


## TagTypeDef

```python
from mypy_boto3_opsworkscm.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## UpdateServerEngineAttributesResponseTypeDef

```python
from mypy_boto3_opsworkscm.type_defs import UpdateServerEngineAttributesResponseTypeDef
```




Optional fields:
- `Server`: `"ServerTypeDef"`


## UpdateServerResponseTypeDef

```python
from mypy_boto3_opsworkscm.type_defs import UpdateServerResponseTypeDef
```




Optional fields:
- `Server`: `"ServerTypeDef"`


## WaiterConfigTypeDef

```python
from mypy_boto3_opsworkscm.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

