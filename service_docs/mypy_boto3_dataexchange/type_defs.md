# Structures for boto3 DataExchange module

> [Index](../index.md) > [DataExchange](./index.md) > Structures

Auto-generated documentation for [DataExchange](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange)
type annotations stubs module [mypy_boto3_dataexchange](https://pypi.org/project/mypy-boto3-dataexchange/).

- [Structures for boto3 DataExchange module](#structures-for-boto3-dataexchange-module)
  - [AssetDestinationEntryTypeDef](#assetdestinationentrytypedef)
  - [AssetDetailsTypeDef](#assetdetailstypedef)
  - [AssetEntryTypeDef](#assetentrytypedef)
  - [AssetSourceEntryTypeDef](#assetsourceentrytypedef)
  - [CreateDataSetResponseTypeDef](#createdatasetresponsetypedef)
  - [CreateJobResponseTypeDef](#createjobresponsetypedef)
  - [CreateRevisionResponseTypeDef](#createrevisionresponsetypedef)
  - [DataSetEntryTypeDef](#datasetentrytypedef)
  - [DetailsTypeDef](#detailstypedef)
  - [ExportAssetToSignedUrlRequestDetailsTypeDef](#exportassettosignedurlrequestdetailstypedef)
  - [ExportAssetToSignedUrlResponseDetailsTypeDef](#exportassettosignedurlresponsedetailstypedef)
  - [ExportAssetsToS3RequestDetailsTypeDef](#exportassetstos3requestdetailstypedef)
  - [ExportAssetsToS3ResponseDetailsTypeDef](#exportassetstos3responsedetailstypedef)
  - [ExportRevisionsToS3RequestDetailsTypeDef](#exportrevisionstos3requestdetailstypedef)
  - [ExportRevisionsToS3ResponseDetailsTypeDef](#exportrevisionstos3responsedetailstypedef)
  - [ExportServerSideEncryptionTypeDef](#exportserversideencryptiontypedef)
  - [GetAssetResponseTypeDef](#getassetresponsetypedef)
  - [GetDataSetResponseTypeDef](#getdatasetresponsetypedef)
  - [GetJobResponseTypeDef](#getjobresponsetypedef)
  - [GetRevisionResponseTypeDef](#getrevisionresponsetypedef)
  - [ImportAssetFromSignedUrlJobErrorDetailsTypeDef](#importassetfromsignedurljoberrordetailstypedef)
  - [ImportAssetFromSignedUrlRequestDetailsTypeDef](#importassetfromsignedurlrequestdetailstypedef)
  - [ImportAssetFromSignedUrlResponseDetailsTypeDef](#importassetfromsignedurlresponsedetailstypedef)
  - [ImportAssetsFromS3RequestDetailsTypeDef](#importassetsfroms3requestdetailstypedef)
  - [ImportAssetsFromS3ResponseDetailsTypeDef](#importassetsfroms3responsedetailstypedef)
  - [JobEntryTypeDef](#jobentrytypedef)
  - [JobErrorTypeDef](#joberrortypedef)
  - [ListDataSetRevisionsResponseTypeDef](#listdatasetrevisionsresponsetypedef)
  - [ListDataSetsResponseTypeDef](#listdatasetsresponsetypedef)
  - [ListJobsResponseTypeDef](#listjobsresponsetypedef)
  - [ListRevisionAssetsResponseTypeDef](#listrevisionassetsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [OriginDetailsTypeDef](#origindetailstypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [RequestDetailsTypeDef](#requestdetailstypedef)
  - [ResponseDetailsTypeDef](#responsedetailstypedef)
  - [RevisionDestinationEntryTypeDef](#revisiondestinationentrytypedef)
  - [RevisionEntryTypeDef](#revisionentrytypedef)
  - [S3SnapshotAssetTypeDef](#s3snapshotassettypedef)
  - [UpdateAssetResponseTypeDef](#updateassetresponsetypedef)
  - [UpdateDataSetResponseTypeDef](#updatedatasetresponsetypedef)
  - [UpdateRevisionResponseTypeDef](#updaterevisionresponsetypedef)

## AssetDestinationEntryTypeDef

```python
from mypy_boto3_dataexchange.type_defs import AssetDestinationEntryTypeDef
```


Required fields:
- `AssetId`: `str`
- `Bucket`: `str`



Optional fields:
- `Key`: `str`


## AssetDetailsTypeDef

```python
from mypy_boto3_dataexchange.type_defs import AssetDetailsTypeDef
```




Optional fields:
- `S3SnapshotAsset`: `"S3SnapshotAssetTypeDef"`


## AssetEntryTypeDef

```python
from mypy_boto3_dataexchange.type_defs import AssetEntryTypeDef
```


Required fields:
- `Arn`: `str`
- `AssetDetails`: `"AssetDetailsTypeDef"`
- `AssetType`: `Literal['S3_SNAPSHOT']`
- `CreatedAt`: `datetime`
- `DataSetId`: `str`
- `Id`: `str`
- `Name`: `str`
- `RevisionId`: `str`
- `UpdatedAt`: `datetime`



Optional fields:
- `SourceId`: `str`


## AssetSourceEntryTypeDef

```python
from mypy_boto3_dataexchange.type_defs import AssetSourceEntryTypeDef
```


Required fields:
- `Bucket`: `str`
- `Key`: `str`




## CreateDataSetResponseTypeDef

```python
from mypy_boto3_dataexchange.type_defs import CreateDataSetResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `AssetType`: `Literal['S3_SNAPSHOT']`
- `CreatedAt`: `datetime`
- `Description`: `str`
- `Id`: `str`
- `Name`: `str`
- `Origin`: `Origin`
- `OriginDetails`: `"OriginDetailsTypeDef"`
- `SourceId`: `str`
- `Tags`: `Dict[str, str]`
- `UpdatedAt`: `datetime`


## CreateJobResponseTypeDef

```python
from mypy_boto3_dataexchange.type_defs import CreateJobResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `CreatedAt`: `datetime`
- `Details`: `"ResponseDetailsTypeDef"`
- `Errors`: `List["JobErrorTypeDef"]`
- `Id`: `str`
- `State`: `State`
- `Type`: `TypeType`
- `UpdatedAt`: `datetime`


## CreateRevisionResponseTypeDef

```python
from mypy_boto3_dataexchange.type_defs import CreateRevisionResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `Comment`: `str`
- `CreatedAt`: `datetime`
- `DataSetId`: `str`
- `Finalized`: `bool`
- `Id`: `str`
- `SourceId`: `str`
- `Tags`: `Dict[str, str]`
- `UpdatedAt`: `datetime`


## DataSetEntryTypeDef

```python
from mypy_boto3_dataexchange.type_defs import DataSetEntryTypeDef
```


Required fields:
- `Arn`: `str`
- `AssetType`: `Literal['S3_SNAPSHOT']`
- `CreatedAt`: `datetime`
- `Description`: `str`
- `Id`: `str`
- `Name`: `str`
- `Origin`: `Origin`
- `UpdatedAt`: `datetime`



Optional fields:
- `OriginDetails`: `"OriginDetailsTypeDef"`
- `SourceId`: `str`


## DetailsTypeDef

```python
from mypy_boto3_dataexchange.type_defs import DetailsTypeDef
```




Optional fields:
- `ImportAssetFromSignedUrlJobErrorDetails`: `"ImportAssetFromSignedUrlJobErrorDetailsTypeDef"`
- `ImportAssetsFromS3JobErrorDetails`: `List["AssetSourceEntryTypeDef"]`


## ExportAssetToSignedUrlRequestDetailsTypeDef

```python
from mypy_boto3_dataexchange.type_defs import ExportAssetToSignedUrlRequestDetailsTypeDef
```


Required fields:
- `AssetId`: `str`
- `DataSetId`: `str`
- `RevisionId`: `str`




## ExportAssetToSignedUrlResponseDetailsTypeDef

```python
from mypy_boto3_dataexchange.type_defs import ExportAssetToSignedUrlResponseDetailsTypeDef
```


Required fields:
- `AssetId`: `str`
- `DataSetId`: `str`
- `RevisionId`: `str`



Optional fields:
- `SignedUrl`: `str`
- `SignedUrlExpiresAt`: `datetime`


## ExportAssetsToS3RequestDetailsTypeDef

```python
from mypy_boto3_dataexchange.type_defs import ExportAssetsToS3RequestDetailsTypeDef
```


Required fields:
- `AssetDestinations`: `List["AssetDestinationEntryTypeDef"]`
- `DataSetId`: `str`
- `RevisionId`: `str`



Optional fields:
- `Encryption`: `"ExportServerSideEncryptionTypeDef"`


## ExportAssetsToS3ResponseDetailsTypeDef

```python
from mypy_boto3_dataexchange.type_defs import ExportAssetsToS3ResponseDetailsTypeDef
```


Required fields:
- `AssetDestinations`: `List["AssetDestinationEntryTypeDef"]`
- `DataSetId`: `str`
- `RevisionId`: `str`



Optional fields:
- `Encryption`: `"ExportServerSideEncryptionTypeDef"`


## ExportRevisionsToS3RequestDetailsTypeDef

```python
from mypy_boto3_dataexchange.type_defs import ExportRevisionsToS3RequestDetailsTypeDef
```


Required fields:
- `DataSetId`: `str`
- `RevisionDestinations`: `List["RevisionDestinationEntryTypeDef"]`



Optional fields:
- `Encryption`: `"ExportServerSideEncryptionTypeDef"`


## ExportRevisionsToS3ResponseDetailsTypeDef

```python
from mypy_boto3_dataexchange.type_defs import ExportRevisionsToS3ResponseDetailsTypeDef
```


Required fields:
- `DataSetId`: `str`
- `RevisionDestinations`: `List["RevisionDestinationEntryTypeDef"]`



Optional fields:
- `Encryption`: `"ExportServerSideEncryptionTypeDef"`


## ExportServerSideEncryptionTypeDef

```python
from mypy_boto3_dataexchange.type_defs import ExportServerSideEncryptionTypeDef
```


Required fields:
- `Type`: `ServerSideEncryptionTypes`



Optional fields:
- `KmsKeyArn`: `str`


## GetAssetResponseTypeDef

```python
from mypy_boto3_dataexchange.type_defs import GetAssetResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `AssetDetails`: `"AssetDetailsTypeDef"`
- `AssetType`: `Literal['S3_SNAPSHOT']`
- `CreatedAt`: `datetime`
- `DataSetId`: `str`
- `Id`: `str`
- `Name`: `str`
- `RevisionId`: `str`
- `SourceId`: `str`
- `UpdatedAt`: `datetime`


## GetDataSetResponseTypeDef

```python
from mypy_boto3_dataexchange.type_defs import GetDataSetResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `AssetType`: `Literal['S3_SNAPSHOT']`
- `CreatedAt`: `datetime`
- `Description`: `str`
- `Id`: `str`
- `Name`: `str`
- `Origin`: `Origin`
- `OriginDetails`: `"OriginDetailsTypeDef"`
- `SourceId`: `str`
- `Tags`: `Dict[str, str]`
- `UpdatedAt`: `datetime`


## GetJobResponseTypeDef

```python
from mypy_boto3_dataexchange.type_defs import GetJobResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `CreatedAt`: `datetime`
- `Details`: `"ResponseDetailsTypeDef"`
- `Errors`: `List["JobErrorTypeDef"]`
- `Id`: `str`
- `State`: `State`
- `Type`: `TypeType`
- `UpdatedAt`: `datetime`


## GetRevisionResponseTypeDef

```python
from mypy_boto3_dataexchange.type_defs import GetRevisionResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `Comment`: `str`
- `CreatedAt`: `datetime`
- `DataSetId`: `str`
- `Finalized`: `bool`
- `Id`: `str`
- `SourceId`: `str`
- `Tags`: `Dict[str, str]`
- `UpdatedAt`: `datetime`


## ImportAssetFromSignedUrlJobErrorDetailsTypeDef

```python
from mypy_boto3_dataexchange.type_defs import ImportAssetFromSignedUrlJobErrorDetailsTypeDef
```


Required fields:
- `AssetName`: `str`




## ImportAssetFromSignedUrlRequestDetailsTypeDef

```python
from mypy_boto3_dataexchange.type_defs import ImportAssetFromSignedUrlRequestDetailsTypeDef
```


Required fields:
- `AssetName`: `str`
- `DataSetId`: `str`
- `Md5Hash`: `str`
- `RevisionId`: `str`




## ImportAssetFromSignedUrlResponseDetailsTypeDef

```python
from mypy_boto3_dataexchange.type_defs import ImportAssetFromSignedUrlResponseDetailsTypeDef
```


Required fields:
- `AssetName`: `str`
- `DataSetId`: `str`
- `RevisionId`: `str`



Optional fields:
- `Md5Hash`: `str`
- `SignedUrl`: `str`
- `SignedUrlExpiresAt`: `datetime`


## ImportAssetsFromS3RequestDetailsTypeDef

```python
from mypy_boto3_dataexchange.type_defs import ImportAssetsFromS3RequestDetailsTypeDef
```


Required fields:
- `AssetSources`: `List["AssetSourceEntryTypeDef"]`
- `DataSetId`: `str`
- `RevisionId`: `str`




## ImportAssetsFromS3ResponseDetailsTypeDef

```python
from mypy_boto3_dataexchange.type_defs import ImportAssetsFromS3ResponseDetailsTypeDef
```


Required fields:
- `AssetSources`: `List["AssetSourceEntryTypeDef"]`
- `DataSetId`: `str`
- `RevisionId`: `str`




## JobEntryTypeDef

```python
from mypy_boto3_dataexchange.type_defs import JobEntryTypeDef
```


Required fields:
- `Arn`: `str`
- `CreatedAt`: `datetime`
- `Details`: `"ResponseDetailsTypeDef"`
- `Id`: `str`
- `State`: `State`
- `Type`: `TypeType`
- `UpdatedAt`: `datetime`



Optional fields:
- `Errors`: `List["JobErrorTypeDef"]`


## JobErrorTypeDef

```python
from mypy_boto3_dataexchange.type_defs import JobErrorTypeDef
```


Required fields:
- `Code`: `Code`
- `Message`: `str`



Optional fields:
- `Details`: `"DetailsTypeDef"`
- `LimitName`: `JobErrorLimitName`
- `LimitValue`: `float`
- `ResourceId`: `str`
- `ResourceType`: `JobErrorResourceTypes`


## ListDataSetRevisionsResponseTypeDef

```python
from mypy_boto3_dataexchange.type_defs import ListDataSetRevisionsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Revisions`: `List["RevisionEntryTypeDef"]`


## ListDataSetsResponseTypeDef

```python
from mypy_boto3_dataexchange.type_defs import ListDataSetsResponseTypeDef
```




Optional fields:
- `DataSets`: `List["DataSetEntryTypeDef"]`
- `NextToken`: `str`


## ListJobsResponseTypeDef

```python
from mypy_boto3_dataexchange.type_defs import ListJobsResponseTypeDef
```




Optional fields:
- `Jobs`: `List["JobEntryTypeDef"]`
- `NextToken`: `str`


## ListRevisionAssetsResponseTypeDef

```python
from mypy_boto3_dataexchange.type_defs import ListRevisionAssetsResponseTypeDef
```




Optional fields:
- `Assets`: `List["AssetEntryTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_dataexchange.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`


## OriginDetailsTypeDef

```python
from mypy_boto3_dataexchange.type_defs import OriginDetailsTypeDef
```


Required fields:
- `ProductId`: `str`




## PaginatorConfigTypeDef

```python
from mypy_boto3_dataexchange.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## RequestDetailsTypeDef

```python
from mypy_boto3_dataexchange.type_defs import RequestDetailsTypeDef
```




Optional fields:
- `ExportAssetToSignedUrl`: `"ExportAssetToSignedUrlRequestDetailsTypeDef"`
- `ExportAssetsToS3`: `"ExportAssetsToS3RequestDetailsTypeDef"`
- `ExportRevisionsToS3`: `"ExportRevisionsToS3RequestDetailsTypeDef"`
- `ImportAssetFromSignedUrl`: `"ImportAssetFromSignedUrlRequestDetailsTypeDef"`
- `ImportAssetsFromS3`: `"ImportAssetsFromS3RequestDetailsTypeDef"`


## ResponseDetailsTypeDef

```python
from mypy_boto3_dataexchange.type_defs import ResponseDetailsTypeDef
```




Optional fields:
- `ExportAssetToSignedUrl`: `"ExportAssetToSignedUrlResponseDetailsTypeDef"`
- `ExportAssetsToS3`: `"ExportAssetsToS3ResponseDetailsTypeDef"`
- `ExportRevisionsToS3`: `"ExportRevisionsToS3ResponseDetailsTypeDef"`
- `ImportAssetFromSignedUrl`: `"ImportAssetFromSignedUrlResponseDetailsTypeDef"`
- `ImportAssetsFromS3`: `"ImportAssetsFromS3ResponseDetailsTypeDef"`


## RevisionDestinationEntryTypeDef

```python
from mypy_boto3_dataexchange.type_defs import RevisionDestinationEntryTypeDef
```


Required fields:
- `Bucket`: `str`
- `RevisionId`: `str`



Optional fields:
- `KeyPattern`: `str`


## RevisionEntryTypeDef

```python
from mypy_boto3_dataexchange.type_defs import RevisionEntryTypeDef
```


Required fields:
- `Arn`: `str`
- `CreatedAt`: `datetime`
- `DataSetId`: `str`
- `Id`: `str`
- `UpdatedAt`: `datetime`



Optional fields:
- `Comment`: `str`
- `Finalized`: `bool`
- `SourceId`: `str`


## S3SnapshotAssetTypeDef

```python
from mypy_boto3_dataexchange.type_defs import S3SnapshotAssetTypeDef
```


Required fields:
- `Size`: `float`




## UpdateAssetResponseTypeDef

```python
from mypy_boto3_dataexchange.type_defs import UpdateAssetResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `AssetDetails`: `"AssetDetailsTypeDef"`
- `AssetType`: `Literal['S3_SNAPSHOT']`
- `CreatedAt`: `datetime`
- `DataSetId`: `str`
- `Id`: `str`
- `Name`: `str`
- `RevisionId`: `str`
- `SourceId`: `str`
- `UpdatedAt`: `datetime`


## UpdateDataSetResponseTypeDef

```python
from mypy_boto3_dataexchange.type_defs import UpdateDataSetResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `AssetType`: `Literal['S3_SNAPSHOT']`
- `CreatedAt`: `datetime`
- `Description`: `str`
- `Id`: `str`
- `Name`: `str`
- `Origin`: `Origin`
- `OriginDetails`: `"OriginDetailsTypeDef"`
- `SourceId`: `str`
- `UpdatedAt`: `datetime`


## UpdateRevisionResponseTypeDef

```python
from mypy_boto3_dataexchange.type_defs import UpdateRevisionResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `Comment`: `str`
- `CreatedAt`: `datetime`
- `DataSetId`: `str`
- `Finalized`: `bool`
- `Id`: `str`
- `SourceId`: `str`
- `UpdatedAt`: `datetime`

