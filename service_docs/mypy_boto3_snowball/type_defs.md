# Structures for boto3 Snowball module

> [Index](../index.md) > [Snowball](./index.md) > Structures

Auto-generated documentation for [Snowball](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball)
type annotations stubs module [mypy_boto3_snowball](https://pypi.org/project/mypy-boto3-snowball/).

- [Structures for boto3 Snowball module](#structures-for-boto3-snowball-module)
  - [AddressTypeDef](#addresstypedef)
  - [ClusterListEntryTypeDef](#clusterlistentrytypedef)
  - [ClusterMetadataTypeDef](#clustermetadatatypedef)
  - [CompatibleImageTypeDef](#compatibleimagetypedef)
  - [DataTransferTypeDef](#datatransfertypedef)
  - [DeviceConfigurationTypeDef](#deviceconfigurationtypedef)
  - [Ec2AmiResourceTypeDef](#ec2amiresourcetypedef)
  - [EventTriggerDefinitionTypeDef](#eventtriggerdefinitiontypedef)
  - [INDTaxDocumentsTypeDef](#indtaxdocumentstypedef)
  - [JobListEntryTypeDef](#joblistentrytypedef)
  - [JobLogsTypeDef](#joblogstypedef)
  - [JobMetadataTypeDef](#jobmetadatatypedef)
  - [JobResourceTypeDef](#jobresourcetypedef)
  - [KeyRangeTypeDef](#keyrangetypedef)
  - [LambdaResourceTypeDef](#lambdaresourcetypedef)
  - [NotificationTypeDef](#notificationtypedef)
  - [S3ResourceTypeDef](#s3resourcetypedef)
  - [ShipmentTypeDef](#shipmenttypedef)
  - [ShippingDetailsTypeDef](#shippingdetailstypedef)
  - [SnowconeDeviceConfigurationTypeDef](#snowconedeviceconfigurationtypedef)
  - [TaxDocumentsTypeDef](#taxdocumentstypedef)
  - [WirelessConnectionTypeDef](#wirelessconnectiontypedef)
  - [CreateAddressResultTypeDef](#createaddressresulttypedef)
  - [CreateClusterResultTypeDef](#createclusterresulttypedef)
  - [CreateJobResultTypeDef](#createjobresulttypedef)
  - [CreateReturnShippingLabelResultTypeDef](#createreturnshippinglabelresulttypedef)
  - [DescribeAddressResultTypeDef](#describeaddressresulttypedef)
  - [DescribeAddressesResultTypeDef](#describeaddressesresulttypedef)
  - [DescribeClusterResultTypeDef](#describeclusterresulttypedef)
  - [DescribeJobResultTypeDef](#describejobresulttypedef)
  - [DescribeReturnShippingLabelResultTypeDef](#describereturnshippinglabelresulttypedef)
  - [GetJobManifestResultTypeDef](#getjobmanifestresulttypedef)
  - [GetJobUnlockCodeResultTypeDef](#getjobunlockcoderesulttypedef)
  - [GetSnowballUsageResultTypeDef](#getsnowballusageresulttypedef)
  - [GetSoftwareUpdatesResultTypeDef](#getsoftwareupdatesresulttypedef)
  - [ListClusterJobsResultTypeDef](#listclusterjobsresulttypedef)
  - [ListClustersResultTypeDef](#listclustersresulttypedef)
  - [ListCompatibleImagesResultTypeDef](#listcompatibleimagesresulttypedef)
  - [ListJobsResultTypeDef](#listjobsresulttypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)

## AddressTypeDef

```python
from mypy_boto3_snowball.type_defs import AddressTypeDef
```




Optional fields:
- `AddressId`: `str`
- `Name`: `str`
- `Company`: `str`
- `Street1`: `str`
- `Street2`: `str`
- `Street3`: `str`
- `City`: `str`
- `StateOrProvince`: `str`
- `PrefectureOrDistrict`: `str`
- `Landmark`: `str`
- `Country`: `str`
- `PostalCode`: `str`
- `PhoneNumber`: `str`
- `IsRestricted`: `bool`


## ClusterListEntryTypeDef

```python
from mypy_boto3_snowball.type_defs import ClusterListEntryTypeDef
```




Optional fields:
- `ClusterId`: `str`
- `ClusterState`: `ClusterState`
- `CreationDate`: `datetime`
- `Description`: `str`


## ClusterMetadataTypeDef

```python
from mypy_boto3_snowball.type_defs import ClusterMetadataTypeDef
```




Optional fields:
- `ClusterId`: `str`
- `Description`: `str`
- `KmsKeyARN`: `str`
- `RoleARN`: `str`
- `ClusterState`: `ClusterState`
- `JobType`: `JobType`
- `SnowballType`: `SnowballType`
- `CreationDate`: `datetime`
- `Resources`: `"JobResourceTypeDef"`
- `AddressId`: `str`
- `ShippingOption`: `ShippingOption`
- `Notification`: `"NotificationTypeDef"`
- `ForwardingAddressId`: `str`
- `TaxDocuments`: `"TaxDocumentsTypeDef"`


## CompatibleImageTypeDef

```python
from mypy_boto3_snowball.type_defs import CompatibleImageTypeDef
```




Optional fields:
- `AmiId`: `str`
- `Name`: `str`


## DataTransferTypeDef

```python
from mypy_boto3_snowball.type_defs import DataTransferTypeDef
```




Optional fields:
- `BytesTransferred`: `int`
- `ObjectsTransferred`: `int`
- `TotalBytes`: `int`
- `TotalObjects`: `int`


## DeviceConfigurationTypeDef

```python
from mypy_boto3_snowball.type_defs import DeviceConfigurationTypeDef
```




Optional fields:
- `SnowconeDeviceConfiguration`: `"SnowconeDeviceConfigurationTypeDef"`


## Ec2AmiResourceTypeDef

```python
from mypy_boto3_snowball.type_defs import Ec2AmiResourceTypeDef
```


Required fields:
- `AmiId`: `str`



Optional fields:
- `SnowballAmiId`: `str`


## EventTriggerDefinitionTypeDef

```python
from mypy_boto3_snowball.type_defs import EventTriggerDefinitionTypeDef
```




Optional fields:
- `EventResourceARN`: `str`


## INDTaxDocumentsTypeDef

```python
from mypy_boto3_snowball.type_defs import INDTaxDocumentsTypeDef
```




Optional fields:
- `GSTIN`: `str`


## JobListEntryTypeDef

```python
from mypy_boto3_snowball.type_defs import JobListEntryTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobState`: `JobState`
- `IsMaster`: `bool`
- `JobType`: `JobType`
- `SnowballType`: `SnowballType`
- `CreationDate`: `datetime`
- `Description`: `str`


## JobLogsTypeDef

```python
from mypy_boto3_snowball.type_defs import JobLogsTypeDef
```




Optional fields:
- `JobCompletionReportURI`: `str`
- `JobSuccessLogURI`: `str`
- `JobFailureLogURI`: `str`


## JobMetadataTypeDef

```python
from mypy_boto3_snowball.type_defs import JobMetadataTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobState`: `JobState`
- `JobType`: `JobType`
- `SnowballType`: `SnowballType`
- `CreationDate`: `datetime`
- `Resources`: `"JobResourceTypeDef"`
- `Description`: `str`
- `KmsKeyARN`: `str`
- `RoleARN`: `str`
- `AddressId`: `str`
- `ShippingDetails`: `"ShippingDetailsTypeDef"`
- `SnowballCapacityPreference`: `SnowballCapacity`
- `Notification`: `"NotificationTypeDef"`
- `DataTransferProgress`: `"DataTransferTypeDef"`
- `JobLogInfo`: `"JobLogsTypeDef"`
- `ClusterId`: `str`
- `ForwardingAddressId`: `str`
- `TaxDocuments`: `"TaxDocumentsTypeDef"`
- `DeviceConfiguration`: `"DeviceConfigurationTypeDef"`


## JobResourceTypeDef

```python
from mypy_boto3_snowball.type_defs import JobResourceTypeDef
```




Optional fields:
- `S3Resources`: `List["S3ResourceTypeDef"]`
- `LambdaResources`: `List["LambdaResourceTypeDef"]`
- `Ec2AmiResources`: `List["Ec2AmiResourceTypeDef"]`


## KeyRangeTypeDef

```python
from mypy_boto3_snowball.type_defs import KeyRangeTypeDef
```




Optional fields:
- `BeginMarker`: `str`
- `EndMarker`: `str`


## LambdaResourceTypeDef

```python
from mypy_boto3_snowball.type_defs import LambdaResourceTypeDef
```




Optional fields:
- `LambdaArn`: `str`
- `EventTriggers`: `List["EventTriggerDefinitionTypeDef"]`


## NotificationTypeDef

```python
from mypy_boto3_snowball.type_defs import NotificationTypeDef
```




Optional fields:
- `SnsTopicARN`: `str`
- `JobStatesToNotify`: `List[JobState]`
- `NotifyAll`: `bool`


## S3ResourceTypeDef

```python
from mypy_boto3_snowball.type_defs import S3ResourceTypeDef
```




Optional fields:
- `BucketArn`: `str`
- `KeyRange`: `"KeyRangeTypeDef"`


## ShipmentTypeDef

```python
from mypy_boto3_snowball.type_defs import ShipmentTypeDef
```




Optional fields:
- `Status`: `str`
- `TrackingNumber`: `str`


## ShippingDetailsTypeDef

```python
from mypy_boto3_snowball.type_defs import ShippingDetailsTypeDef
```




Optional fields:
- `ShippingOption`: `ShippingOption`
- `InboundShipment`: `"ShipmentTypeDef"`
- `OutboundShipment`: `"ShipmentTypeDef"`


## SnowconeDeviceConfigurationTypeDef

```python
from mypy_boto3_snowball.type_defs import SnowconeDeviceConfigurationTypeDef
```




Optional fields:
- `WirelessConnection`: `"WirelessConnectionTypeDef"`


## TaxDocumentsTypeDef

```python
from mypy_boto3_snowball.type_defs import TaxDocumentsTypeDef
```




Optional fields:
- `IND`: `"INDTaxDocumentsTypeDef"`


## WirelessConnectionTypeDef

```python
from mypy_boto3_snowball.type_defs import WirelessConnectionTypeDef
```




Optional fields:
- `IsWifiEnabled`: `bool`


## CreateAddressResultTypeDef

```python
from mypy_boto3_snowball.type_defs import CreateAddressResultTypeDef
```




Optional fields:
- `AddressId`: `str`


## CreateClusterResultTypeDef

```python
from mypy_boto3_snowball.type_defs import CreateClusterResultTypeDef
```




Optional fields:
- `ClusterId`: `str`


## CreateJobResultTypeDef

```python
from mypy_boto3_snowball.type_defs import CreateJobResultTypeDef
```




Optional fields:
- `JobId`: `str`


## CreateReturnShippingLabelResultTypeDef

```python
from mypy_boto3_snowball.type_defs import CreateReturnShippingLabelResultTypeDef
```




Optional fields:
- `Status`: `ShippingLabelStatus`


## DescribeAddressResultTypeDef

```python
from mypy_boto3_snowball.type_defs import DescribeAddressResultTypeDef
```




Optional fields:
- `Address`: `"AddressTypeDef"`


## DescribeAddressesResultTypeDef

```python
from mypy_boto3_snowball.type_defs import DescribeAddressesResultTypeDef
```




Optional fields:
- `Addresses`: `List["AddressTypeDef"]`
- `NextToken`: `str`


## DescribeClusterResultTypeDef

```python
from mypy_boto3_snowball.type_defs import DescribeClusterResultTypeDef
```




Optional fields:
- `ClusterMetadata`: `"ClusterMetadataTypeDef"`


## DescribeJobResultTypeDef

```python
from mypy_boto3_snowball.type_defs import DescribeJobResultTypeDef
```




Optional fields:
- `JobMetadata`: `"JobMetadataTypeDef"`
- `SubJobMetadata`: `List["JobMetadataTypeDef"]`


## DescribeReturnShippingLabelResultTypeDef

```python
from mypy_boto3_snowball.type_defs import DescribeReturnShippingLabelResultTypeDef
```




Optional fields:
- `Status`: `ShippingLabelStatus`
- `ExpirationDate`: `datetime`


## GetJobManifestResultTypeDef

```python
from mypy_boto3_snowball.type_defs import GetJobManifestResultTypeDef
```




Optional fields:
- `ManifestURI`: `str`


## GetJobUnlockCodeResultTypeDef

```python
from mypy_boto3_snowball.type_defs import GetJobUnlockCodeResultTypeDef
```




Optional fields:
- `UnlockCode`: `str`


## GetSnowballUsageResultTypeDef

```python
from mypy_boto3_snowball.type_defs import GetSnowballUsageResultTypeDef
```




Optional fields:
- `SnowballLimit`: `int`
- `SnowballsInUse`: `int`


## GetSoftwareUpdatesResultTypeDef

```python
from mypy_boto3_snowball.type_defs import GetSoftwareUpdatesResultTypeDef
```




Optional fields:
- `UpdatesURI`: `str`


## ListClusterJobsResultTypeDef

```python
from mypy_boto3_snowball.type_defs import ListClusterJobsResultTypeDef
```




Optional fields:
- `JobListEntries`: `List["JobListEntryTypeDef"]`
- `NextToken`: `str`


## ListClustersResultTypeDef

```python
from mypy_boto3_snowball.type_defs import ListClustersResultTypeDef
```




Optional fields:
- `ClusterListEntries`: `List["ClusterListEntryTypeDef"]`
- `NextToken`: `str`


## ListCompatibleImagesResultTypeDef

```python
from mypy_boto3_snowball.type_defs import ListCompatibleImagesResultTypeDef
```




Optional fields:
- `CompatibleImages`: `List["CompatibleImageTypeDef"]`
- `NextToken`: `str`


## ListJobsResultTypeDef

```python
from mypy_boto3_snowball.type_defs import ListJobsResultTypeDef
```




Optional fields:
- `JobListEntries`: `List["JobListEntryTypeDef"]`
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_snowball.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`

