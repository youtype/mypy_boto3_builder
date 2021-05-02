# Type annotations for boto3 MediaPackage module

> [Index](../index.md) > MediaPackage

Auto-generated documentation for [MediaPackage](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage)
type annotations stubs module [mypy_boto3_mediapackage](https://pypi.org/project/mypy-boto3-mediapackage/).

```bash
pip install mypy-boto3-mediapackage
```

- [Type annotations for boto3 MediaPackage module](#type-annotations-for-boto3-mediapackage-module)
  - [MediaPackageClient](#mediapackageclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## MediaPackageClient

Type annotations for  `boto3.client("mediapackage")` as [MediaPackageClient](./client.md)

Can be used directly:

```python
from mypy_boto3_mediapackage.client import MediaPackageClient
```


MediaPackageClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [configure_logs](./client.md#configure-logs)
- [create_channel](./client.md#create-channel)
- [create_harvest_job](./client.md#create-harvest-job)
- [create_origin_endpoint](./client.md#create-origin-endpoint)
- [delete_channel](./client.md#delete-channel)
- [delete_origin_endpoint](./client.md#delete-origin-endpoint)
- [describe_channel](./client.md#describe-channel)
- [describe_harvest_job](./client.md#describe-harvest-job)
- [describe_origin_endpoint](./client.md#describe-origin-endpoint)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [list_channels](./client.md#list-channels)
- [list_harvest_jobs](./client.md#list-harvest-jobs)
- [list_origin_endpoints](./client.md#list-origin-endpoints)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [rotate_channel_credentials](./client.md#rotate-channel-credentials)
- [rotate_ingest_endpoint_credentials](./client.md#rotate-ingest-endpoint-credentials)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_channel](./client.md#update-channel)
- [update_origin_endpoint](./client.md#update-origin-endpoint)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ForbiddenException](./client.md#forbiddenexception)
- [InternalServerErrorException](./client.md#internalservererrorexception)
- [NotFoundException](./client.md#notfoundexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)
- [UnprocessableEntityException](./client.md#unprocessableentityexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("mediapackage").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_mediapackage.paginators import ListChannelsPaginator, ...
```

- [ListChannelsPaginator](./paginators.md#listchannelspaginator)
- [ListHarvestJobsPaginator](./paginators.md#listharvestjobspaginator)
- [ListOriginEndpointsPaginator](./paginators.md#listoriginendpointspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_mediapackage.literals import AdMarkers, ...
```

- [AdMarkers](./literals.md#admarkers)
- [AdsOnDeliveryRestrictions](./literals.md#adsondeliveryrestrictions)
- [EncryptionMethod](./literals.md#encryptionmethod)
- [ListChannelsPaginatorName](./literals.md#listchannelspaginatorname)
- [ListHarvestJobsPaginatorName](./literals.md#listharvestjobspaginatorname)
- [ListOriginEndpointsPaginatorName](./literals.md#listoriginendpointspaginatorname)
- [ManifestLayout](./literals.md#manifestlayout)
- [Origination](./literals.md#origination)
- [PlaylistType](./literals.md#playlisttype)
- [PresetSpeke20Audio](./literals.md#presetspeke20audio)
- [PresetSpeke20Video](./literals.md#presetspeke20video)
- [Profile](./literals.md#profile)
- [SegmentTemplateFormat](./literals.md#segmenttemplateformat)
- [Status](./literals.md#status)
- [StreamOrder](./literals.md#streamorder)
- [UtcTiming](./literals.md#utctiming)
- [__AdTriggersElement](./literals.md#--adtriggerselement)
- [__PeriodTriggersElement](./literals.md#--periodtriggerselement)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_mediapackage.type_defs import AuthorizationTypeDef, ...
```

- [AuthorizationTypeDef](./type_defs.md#authorizationtypedef)
- [ChannelTypeDef](./type_defs.md#channeltypedef)
- [CmafEncryptionTypeDef](./type_defs.md#cmafencryptiontypedef)
- [CmafPackageTypeDef](./type_defs.md#cmafpackagetypedef)
- [DashEncryptionTypeDef](./type_defs.md#dashencryptiontypedef)
- [DashPackageTypeDef](./type_defs.md#dashpackagetypedef)
- [EgressAccessLogsTypeDef](./type_defs.md#egressaccesslogstypedef)
- [EncryptionContractConfigurationTypeDef](./type_defs.md#encryptioncontractconfigurationtypedef)
- [HarvestJobTypeDef](./type_defs.md#harvestjobtypedef)
- [HlsEncryptionTypeDef](./type_defs.md#hlsencryptiontypedef)
- [HlsIngestTypeDef](./type_defs.md#hlsingesttypedef)
- [HlsManifestCreateOrUpdateParametersTypeDef](./type_defs.md#hlsmanifestcreateorupdateparameterstypedef)
- [HlsManifestTypeDef](./type_defs.md#hlsmanifesttypedef)
- [HlsPackageTypeDef](./type_defs.md#hlspackagetypedef)
- [IngestEndpointTypeDef](./type_defs.md#ingestendpointtypedef)
- [IngressAccessLogsTypeDef](./type_defs.md#ingressaccesslogstypedef)
- [MssEncryptionTypeDef](./type_defs.md#mssencryptiontypedef)
- [MssPackageTypeDef](./type_defs.md#msspackagetypedef)
- [OriginEndpointTypeDef](./type_defs.md#originendpointtypedef)
- [S3DestinationTypeDef](./type_defs.md#s3destinationtypedef)
- [SpekeKeyProviderTypeDef](./type_defs.md#spekekeyprovidertypedef)
- [StreamSelectionTypeDef](./type_defs.md#streamselectiontypedef)
- [CmafPackageCreateOrUpdateParametersTypeDef](./type_defs.md#cmafpackagecreateorupdateparameterstypedef)
- [ConfigureLogsResponseTypeDef](./type_defs.md#configurelogsresponsetypedef)
- [CreateChannelResponseTypeDef](./type_defs.md#createchannelresponsetypedef)
- [CreateHarvestJobResponseTypeDef](./type_defs.md#createharvestjobresponsetypedef)
- [CreateOriginEndpointResponseTypeDef](./type_defs.md#createoriginendpointresponsetypedef)
- [DescribeChannelResponseTypeDef](./type_defs.md#describechannelresponsetypedef)
- [DescribeHarvestJobResponseTypeDef](./type_defs.md#describeharvestjobresponsetypedef)
- [DescribeOriginEndpointResponseTypeDef](./type_defs.md#describeoriginendpointresponsetypedef)
- [ListChannelsResponseTypeDef](./type_defs.md#listchannelsresponsetypedef)
- [ListHarvestJobsResponseTypeDef](./type_defs.md#listharvestjobsresponsetypedef)
- [ListOriginEndpointsResponseTypeDef](./type_defs.md#listoriginendpointsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [RotateChannelCredentialsResponseTypeDef](./type_defs.md#rotatechannelcredentialsresponsetypedef)
- [RotateIngestEndpointCredentialsResponseTypeDef](./type_defs.md#rotateingestendpointcredentialsresponsetypedef)
- [UpdateChannelResponseTypeDef](./type_defs.md#updatechannelresponsetypedef)
- [UpdateOriginEndpointResponseTypeDef](./type_defs.md#updateoriginendpointresponsetypedef)
