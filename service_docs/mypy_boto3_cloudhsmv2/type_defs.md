# Structures for boto3 CloudHSMV2 module

> [Index](../index.md) > [CloudHSMV2](./index.md) > Structures

Auto-generated documentation for [CloudHSMV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2)
type annotations stubs module [mypy_boto3_cloudhsmv2](https://pypi.org/project/mypy-boto3-cloudhsmv2/).

- [Structures for boto3 CloudHSMV2 module](#structures-for-boto3-cloudhsmv2-module)
  - [BackupRetentionPolicyTypeDef](#backupretentionpolicytypedef)
  - [BackupTypeDef](#backuptypedef)
  - [CertificatesTypeDef](#certificatestypedef)
  - [ClusterTypeDef](#clustertypedef)
  - [DestinationBackupTypeDef](#destinationbackuptypedef)
  - [HsmTypeDef](#hsmtypedef)
  - [TagTypeDef](#tagtypedef)
  - [CopyBackupToRegionResponseTypeDef](#copybackuptoregionresponsetypedef)
  - [CreateClusterResponseTypeDef](#createclusterresponsetypedef)
  - [CreateHsmResponseTypeDef](#createhsmresponsetypedef)
  - [DeleteBackupResponseTypeDef](#deletebackupresponsetypedef)
  - [DeleteClusterResponseTypeDef](#deleteclusterresponsetypedef)
  - [DeleteHsmResponseTypeDef](#deletehsmresponsetypedef)
  - [DescribeBackupsResponseTypeDef](#describebackupsresponsetypedef)
  - [DescribeClustersResponseTypeDef](#describeclustersresponsetypedef)
  - [InitializeClusterResponseTypeDef](#initializeclusterresponsetypedef)
  - [ListTagsResponseTypeDef](#listtagsresponsetypedef)
  - [ModifyBackupAttributesResponseTypeDef](#modifybackupattributesresponsetypedef)
  - [ModifyClusterResponseTypeDef](#modifyclusterresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [RestoreBackupResponseTypeDef](#restorebackupresponsetypedef)

## BackupRetentionPolicyTypeDef

```python
from mypy_boto3_cloudhsmv2.type_defs import BackupRetentionPolicyTypeDef
```




Optional fields:
- `Type`: `BackupRetentionType`
- `Value`: `str`


## BackupTypeDef

```python
from mypy_boto3_cloudhsmv2.type_defs import BackupTypeDef
```


Required fields:
- `BackupId`: `str`



Optional fields:
- `BackupState`: `BackupState`
- `ClusterId`: `str`
- `CreateTimestamp`: `datetime`
- `CopyTimestamp`: `datetime`
- `NeverExpires`: `bool`
- `SourceRegion`: `str`
- `SourceBackup`: `str`
- `SourceCluster`: `str`
- `DeleteTimestamp`: `datetime`
- `TagList`: `List["TagTypeDef"]`


## CertificatesTypeDef

```python
from mypy_boto3_cloudhsmv2.type_defs import CertificatesTypeDef
```




Optional fields:
- `ClusterCsr`: `str`
- `HsmCertificate`: `str`
- `AwsHardwareCertificate`: `str`
- `ManufacturerHardwareCertificate`: `str`
- `ClusterCertificate`: `str`


## ClusterTypeDef

```python
from mypy_boto3_cloudhsmv2.type_defs import ClusterTypeDef
```




Optional fields:
- `BackupPolicy`: `BackupPolicy`
- `BackupRetentionPolicy`: `"BackupRetentionPolicyTypeDef"`
- `ClusterId`: `str`
- `CreateTimestamp`: `datetime`
- `Hsms`: `List["HsmTypeDef"]`
- `HsmType`: `str`
- `PreCoPassword`: `str`
- `SecurityGroup`: `str`
- `SourceBackupId`: `str`
- `State`: `ClusterState`
- `StateMessage`: `str`
- `SubnetMapping`: `Dict[str, str]`
- `VpcId`: `str`
- `Certificates`: `"CertificatesTypeDef"`
- `TagList`: `List["TagTypeDef"]`


## DestinationBackupTypeDef

```python
from mypy_boto3_cloudhsmv2.type_defs import DestinationBackupTypeDef
```




Optional fields:
- `CreateTimestamp`: `datetime`
- `SourceRegion`: `str`
- `SourceBackup`: `str`
- `SourceCluster`: `str`


## HsmTypeDef

```python
from mypy_boto3_cloudhsmv2.type_defs import HsmTypeDef
```


Required fields:
- `HsmId`: `str`



Optional fields:
- `AvailabilityZone`: `str`
- `ClusterId`: `str`
- `SubnetId`: `str`
- `EniId`: `str`
- `EniIp`: `str`
- `State`: `HsmState`
- `StateMessage`: `str`


## TagTypeDef

```python
from mypy_boto3_cloudhsmv2.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## CopyBackupToRegionResponseTypeDef

```python
from mypy_boto3_cloudhsmv2.type_defs import CopyBackupToRegionResponseTypeDef
```




Optional fields:
- `DestinationBackup`: `"DestinationBackupTypeDef"`


## CreateClusterResponseTypeDef

```python
from mypy_boto3_cloudhsmv2.type_defs import CreateClusterResponseTypeDef
```




Optional fields:
- `Cluster`: `"ClusterTypeDef"`


## CreateHsmResponseTypeDef

```python
from mypy_boto3_cloudhsmv2.type_defs import CreateHsmResponseTypeDef
```




Optional fields:
- `Hsm`: `"HsmTypeDef"`


## DeleteBackupResponseTypeDef

```python
from mypy_boto3_cloudhsmv2.type_defs import DeleteBackupResponseTypeDef
```




Optional fields:
- `Backup`: `"BackupTypeDef"`


## DeleteClusterResponseTypeDef

```python
from mypy_boto3_cloudhsmv2.type_defs import DeleteClusterResponseTypeDef
```




Optional fields:
- `Cluster`: `"ClusterTypeDef"`


## DeleteHsmResponseTypeDef

```python
from mypy_boto3_cloudhsmv2.type_defs import DeleteHsmResponseTypeDef
```




Optional fields:
- `HsmId`: `str`


## DescribeBackupsResponseTypeDef

```python
from mypy_boto3_cloudhsmv2.type_defs import DescribeBackupsResponseTypeDef
```




Optional fields:
- `Backups`: `List["BackupTypeDef"]`
- `NextToken`: `str`


## DescribeClustersResponseTypeDef

```python
from mypy_boto3_cloudhsmv2.type_defs import DescribeClustersResponseTypeDef
```




Optional fields:
- `Clusters`: `List["ClusterTypeDef"]`
- `NextToken`: `str`


## InitializeClusterResponseTypeDef

```python
from mypy_boto3_cloudhsmv2.type_defs import InitializeClusterResponseTypeDef
```




Optional fields:
- `State`: `ClusterState`
- `StateMessage`: `str`


## ListTagsResponseTypeDef

```python
from mypy_boto3_cloudhsmv2.type_defs import ListTagsResponseTypeDef
```


Required fields:
- `TagList`: `List["TagTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ModifyBackupAttributesResponseTypeDef

```python
from mypy_boto3_cloudhsmv2.type_defs import ModifyBackupAttributesResponseTypeDef
```




Optional fields:
- `Backup`: `"BackupTypeDef"`


## ModifyClusterResponseTypeDef

```python
from mypy_boto3_cloudhsmv2.type_defs import ModifyClusterResponseTypeDef
```




Optional fields:
- `Cluster`: `"ClusterTypeDef"`


## PaginatorConfigTypeDef

```python
from mypy_boto3_cloudhsmv2.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## RestoreBackupResponseTypeDef

```python
from mypy_boto3_cloudhsmv2.type_defs import RestoreBackupResponseTypeDef
```




Optional fields:
- `Backup`: `"BackupTypeDef"`

