# Type annotations for boto3 DataExchange module

> [Index](../index.md) > DataExchange

Auto-generated documentation for [DataExchange](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange)
type annotations stubs module [mypy_boto3_dataexchange](https://pypi.org/project/mypy-boto3-dataexchange/).

```bash
pip install mypy-boto3-dataexchange
```

- [Type annotations for boto3 DataExchange module](#type-annotations-for-boto3-dataexchange-module)
  - [DataExchangeClient](#dataexchangeclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## DataExchangeClient

Type annotations for  `boto3.client("dataexchange")` as [DataExchangeClient](./client.md)

Can be used directly:

```python
from mypy_boto3_dataexchange.client import DataExchangeClient
```


DataExchangeClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [cancel_job](./client.md#cancel-job)
- [create_data_set](./client.md#create-data-set)
- [create_job](./client.md#create-job)
- [create_revision](./client.md#create-revision)
- [delete_asset](./client.md#delete-asset)
- [delete_data_set](./client.md#delete-data-set)
- [delete_revision](./client.md#delete-revision)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_asset](./client.md#get-asset)
- [get_data_set](./client.md#get-data-set)
- [get_job](./client.md#get-job)
- [get_paginator](./client.md#get-paginator)
- [get_revision](./client.md#get-revision)
- [list_data_set_revisions](./client.md#list-data-set-revisions)
- [list_data_sets](./client.md#list-data-sets)
- [list_jobs](./client.md#list-jobs)
- [list_revision_assets](./client.md#list-revision-assets)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [start_job](./client.md#start-job)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_asset](./client.md#update-asset)
- [update_data_set](./client.md#update-data-set)
- [update_revision](./client.md#update-revision)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceLimitExceededException](./client.md#servicelimitexceededexception)
- [ThrottlingException](./client.md#throttlingexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("dataexchange").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_dataexchange.paginators import ListDataSetRevisionsPaginator, ...
```

- [ListDataSetRevisionsPaginator](./paginators.md#listdatasetrevisionspaginator)
- [ListDataSetsPaginator](./paginators.md#listdatasetspaginator)
- [ListJobsPaginator](./paginators.md#listjobspaginator)
- [ListRevisionAssetsPaginator](./paginators.md#listrevisionassetspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_dataexchange.literals import AssetType, ...
```

- [AssetType](./literals.md#assettype)
- [Code](./literals.md#code)
- [JobErrorLimitName](./literals.md#joberrorlimitname)
- [JobErrorResourceTypes](./literals.md#joberrorresourcetypes)
- [ListDataSetRevisionsPaginatorName](./literals.md#listdatasetrevisionspaginatorname)
- [ListDataSetsPaginatorName](./literals.md#listdatasetspaginatorname)
- [ListJobsPaginatorName](./literals.md#listjobspaginatorname)
- [ListRevisionAssetsPaginatorName](./literals.md#listrevisionassetspaginatorname)
- [Origin](./literals.md#origin)
- [ServerSideEncryptionTypes](./literals.md#serversideencryptiontypes)
- [State](./literals.md#state)
- [TypeType](./literals.md#typetype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_dataexchange.type_defs import AssetDestinationEntryTypeDef, ...
```

- [AssetDestinationEntryTypeDef](./type_defs.md#assetdestinationentrytypedef)
- [AssetDetailsTypeDef](./type_defs.md#assetdetailstypedef)
- [AssetEntryTypeDef](./type_defs.md#assetentrytypedef)
- [AssetSourceEntryTypeDef](./type_defs.md#assetsourceentrytypedef)
- [DataSetEntryTypeDef](./type_defs.md#datasetentrytypedef)
- [DetailsTypeDef](./type_defs.md#detailstypedef)
- [ExportAssetToSignedUrlRequestDetailsTypeDef](./type_defs.md#exportassettosignedurlrequestdetailstypedef)
- [ExportAssetToSignedUrlResponseDetailsTypeDef](./type_defs.md#exportassettosignedurlresponsedetailstypedef)
- [ExportAssetsToS3RequestDetailsTypeDef](./type_defs.md#exportassetstos3requestdetailstypedef)
- [ExportAssetsToS3ResponseDetailsTypeDef](./type_defs.md#exportassetstos3responsedetailstypedef)
- [ExportRevisionsToS3RequestDetailsTypeDef](./type_defs.md#exportrevisionstos3requestdetailstypedef)
- [ExportRevisionsToS3ResponseDetailsTypeDef](./type_defs.md#exportrevisionstos3responsedetailstypedef)
- [ExportServerSideEncryptionTypeDef](./type_defs.md#exportserversideencryptiontypedef)
- [ImportAssetFromSignedUrlJobErrorDetailsTypeDef](./type_defs.md#importassetfromsignedurljoberrordetailstypedef)
- [ImportAssetFromSignedUrlRequestDetailsTypeDef](./type_defs.md#importassetfromsignedurlrequestdetailstypedef)
- [ImportAssetFromSignedUrlResponseDetailsTypeDef](./type_defs.md#importassetfromsignedurlresponsedetailstypedef)
- [ImportAssetsFromS3RequestDetailsTypeDef](./type_defs.md#importassetsfroms3requestdetailstypedef)
- [ImportAssetsFromS3ResponseDetailsTypeDef](./type_defs.md#importassetsfroms3responsedetailstypedef)
- [JobEntryTypeDef](./type_defs.md#jobentrytypedef)
- [JobErrorTypeDef](./type_defs.md#joberrortypedef)
- [OriginDetailsTypeDef](./type_defs.md#origindetailstypedef)
- [ResponseDetailsTypeDef](./type_defs.md#responsedetailstypedef)
- [RevisionDestinationEntryTypeDef](./type_defs.md#revisiondestinationentrytypedef)
- [RevisionEntryTypeDef](./type_defs.md#revisionentrytypedef)
- [S3SnapshotAssetTypeDef](./type_defs.md#s3snapshotassettypedef)
- [CreateDataSetResponseTypeDef](./type_defs.md#createdatasetresponsetypedef)
- [CreateJobResponseTypeDef](./type_defs.md#createjobresponsetypedef)
- [CreateRevisionResponseTypeDef](./type_defs.md#createrevisionresponsetypedef)
- [GetAssetResponseTypeDef](./type_defs.md#getassetresponsetypedef)
- [GetDataSetResponseTypeDef](./type_defs.md#getdatasetresponsetypedef)
- [GetJobResponseTypeDef](./type_defs.md#getjobresponsetypedef)
- [GetRevisionResponseTypeDef](./type_defs.md#getrevisionresponsetypedef)
- [ListDataSetRevisionsResponseTypeDef](./type_defs.md#listdatasetrevisionsresponsetypedef)
- [ListDataSetsResponseTypeDef](./type_defs.md#listdatasetsresponsetypedef)
- [ListJobsResponseTypeDef](./type_defs.md#listjobsresponsetypedef)
- [ListRevisionAssetsResponseTypeDef](./type_defs.md#listrevisionassetsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [RequestDetailsTypeDef](./type_defs.md#requestdetailstypedef)
- [UpdateAssetResponseTypeDef](./type_defs.md#updateassetresponsetypedef)
- [UpdateDataSetResponseTypeDef](./type_defs.md#updatedatasetresponsetypedef)
- [UpdateRevisionResponseTypeDef](./type_defs.md#updaterevisionresponsetypedef)
