# Structures for boto3 CloudHSM module

> [Index](../index.md) > [CloudHSM](./index.md) > Structures

Auto-generated documentation for [CloudHSM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html#CloudHSM)
type annotations stubs module [mypy_boto3_cloudhsm](https://pypi.org/project/mypy-boto3-cloudhsm/).

- [Structures for boto3 CloudHSM module](#structures-for-boto3-cloudhsm-module)
  - [TagTypeDef](#tagtypedef)
  - [AddTagsToResourceResponseTypeDef](#addtagstoresourceresponsetypedef)
  - [CreateHapgResponseTypeDef](#createhapgresponsetypedef)
  - [CreateHsmResponseTypeDef](#createhsmresponsetypedef)
  - [CreateLunaClientResponseTypeDef](#createlunaclientresponsetypedef)
  - [DeleteHapgResponseTypeDef](#deletehapgresponsetypedef)
  - [DeleteHsmResponseTypeDef](#deletehsmresponsetypedef)
  - [DeleteLunaClientResponseTypeDef](#deletelunaclientresponsetypedef)
  - [DescribeHapgResponseTypeDef](#describehapgresponsetypedef)
  - [DescribeHsmResponseTypeDef](#describehsmresponsetypedef)
  - [DescribeLunaClientResponseTypeDef](#describelunaclientresponsetypedef)
  - [GetConfigResponseTypeDef](#getconfigresponsetypedef)
  - [ListAvailableZonesResponseTypeDef](#listavailablezonesresponsetypedef)
  - [ListHapgsResponseTypeDef](#listhapgsresponsetypedef)
  - [ListHsmsResponseTypeDef](#listhsmsresponsetypedef)
  - [ListLunaClientsResponseTypeDef](#listlunaclientsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ModifyHapgResponseTypeDef](#modifyhapgresponsetypedef)
  - [ModifyHsmResponseTypeDef](#modifyhsmresponsetypedef)
  - [ModifyLunaClientResponseTypeDef](#modifylunaclientresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [RemoveTagsFromResourceResponseTypeDef](#removetagsfromresourceresponsetypedef)

## TagTypeDef

```python
from mypy_boto3_cloudhsm.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## AddTagsToResourceResponseTypeDef

```python
from mypy_boto3_cloudhsm.type_defs import AddTagsToResourceResponseTypeDef
```


Required fields:
- `Status`: `str`




## CreateHapgResponseTypeDef

```python
from mypy_boto3_cloudhsm.type_defs import CreateHapgResponseTypeDef
```




Optional fields:
- `HapgArn`: `str`


## CreateHsmResponseTypeDef

```python
from mypy_boto3_cloudhsm.type_defs import CreateHsmResponseTypeDef
```




Optional fields:
- `HsmArn`: `str`


## CreateLunaClientResponseTypeDef

```python
from mypy_boto3_cloudhsm.type_defs import CreateLunaClientResponseTypeDef
```




Optional fields:
- `ClientArn`: `str`


## DeleteHapgResponseTypeDef

```python
from mypy_boto3_cloudhsm.type_defs import DeleteHapgResponseTypeDef
```


Required fields:
- `Status`: `str`




## DeleteHsmResponseTypeDef

```python
from mypy_boto3_cloudhsm.type_defs import DeleteHsmResponseTypeDef
```


Required fields:
- `Status`: `str`




## DeleteLunaClientResponseTypeDef

```python
from mypy_boto3_cloudhsm.type_defs import DeleteLunaClientResponseTypeDef
```


Required fields:
- `Status`: `str`




## DescribeHapgResponseTypeDef

```python
from mypy_boto3_cloudhsm.type_defs import DescribeHapgResponseTypeDef
```




Optional fields:
- `HapgArn`: `str`
- `HapgSerial`: `str`
- `HsmsLastActionFailed`: `List[str]`
- `HsmsPendingDeletion`: `List[str]`
- `HsmsPendingRegistration`: `List[str]`
- `Label`: `str`
- `LastModifiedTimestamp`: `str`
- `PartitionSerialList`: `List[str]`
- `State`: `CloudHsmObjectState`


## DescribeHsmResponseTypeDef

```python
from mypy_boto3_cloudhsm.type_defs import DescribeHsmResponseTypeDef
```




Optional fields:
- `HsmArn`: `str`
- `Status`: `HsmStatus`
- `StatusDetails`: `str`
- `AvailabilityZone`: `str`
- `EniId`: `str`
- `EniIp`: `str`
- `SubscriptionType`: `SubscriptionType`
- `SubscriptionStartDate`: `str`
- `SubscriptionEndDate`: `str`
- `VpcId`: `str`
- `SubnetId`: `str`
- `IamRoleArn`: `str`
- `SerialNumber`: `str`
- `VendorName`: `str`
- `HsmType`: `str`
- `SoftwareVersion`: `str`
- `SshPublicKey`: `str`
- `SshKeyLastUpdated`: `str`
- `ServerCertUri`: `str`
- `ServerCertLastUpdated`: `str`
- `Partitions`: `List[str]`


## DescribeLunaClientResponseTypeDef

```python
from mypy_boto3_cloudhsm.type_defs import DescribeLunaClientResponseTypeDef
```




Optional fields:
- `ClientArn`: `str`
- `Certificate`: `str`
- `CertificateFingerprint`: `str`
- `LastModifiedTimestamp`: `str`
- `Label`: `str`


## GetConfigResponseTypeDef

```python
from mypy_boto3_cloudhsm.type_defs import GetConfigResponseTypeDef
```




Optional fields:
- `ConfigType`: `str`
- `ConfigFile`: `str`
- `ConfigCred`: `str`


## ListAvailableZonesResponseTypeDef

```python
from mypy_boto3_cloudhsm.type_defs import ListAvailableZonesResponseTypeDef
```




Optional fields:
- `AZList`: `List[str]`


## ListHapgsResponseTypeDef

```python
from mypy_boto3_cloudhsm.type_defs import ListHapgsResponseTypeDef
```


Required fields:
- `HapgList`: `List[str]`



Optional fields:
- `NextToken`: `str`


## ListHsmsResponseTypeDef

```python
from mypy_boto3_cloudhsm.type_defs import ListHsmsResponseTypeDef
```




Optional fields:
- `HsmList`: `List[str]`
- `NextToken`: `str`


## ListLunaClientsResponseTypeDef

```python
from mypy_boto3_cloudhsm.type_defs import ListLunaClientsResponseTypeDef
```


Required fields:
- `ClientList`: `List[str]`



Optional fields:
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_cloudhsm.type_defs import ListTagsForResourceResponseTypeDef
```


Required fields:
- `TagList`: `List["TagTypeDef"]`




## ModifyHapgResponseTypeDef

```python
from mypy_boto3_cloudhsm.type_defs import ModifyHapgResponseTypeDef
```




Optional fields:
- `HapgArn`: `str`


## ModifyHsmResponseTypeDef

```python
from mypy_boto3_cloudhsm.type_defs import ModifyHsmResponseTypeDef
```




Optional fields:
- `HsmArn`: `str`


## ModifyLunaClientResponseTypeDef

```python
from mypy_boto3_cloudhsm.type_defs import ModifyLunaClientResponseTypeDef
```




Optional fields:
- `ClientArn`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_cloudhsm.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## RemoveTagsFromResourceResponseTypeDef

```python
from mypy_boto3_cloudhsm.type_defs import RemoveTagsFromResourceResponseTypeDef
```


Required fields:
- `Status`: `str`



