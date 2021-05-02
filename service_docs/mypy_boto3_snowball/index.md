# Type annotations for boto3 Snowball module

> [Index](../index.md) > Snowball

Auto-generated documentation for [Snowball](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball)
type annotations stubs module [mypy_boto3_snowball](https://pypi.org/project/mypy-boto3-snowball/).

```bash
pip install mypy-boto3-snowball
```

- [Type annotations for boto3 Snowball module](#type-annotations-for-boto3-snowball-module)
  - [SnowballClient](#snowballclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## SnowballClient

Type annotations for  `boto3.client("snowball")` as [SnowballClient](./client.md)

Can be used directly:

```python
from mypy_boto3_snowball.client import SnowballClient
```


SnowballClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [cancel_cluster](./client.md#cancel-cluster)
- [cancel_job](./client.md#cancel-job)
- [create_address](./client.md#create-address)
- [create_cluster](./client.md#create-cluster)
- [create_job](./client.md#create-job)
- [create_return_shipping_label](./client.md#create-return-shipping-label)
- [describe_address](./client.md#describe-address)
- [describe_addresses](./client.md#describe-addresses)
- [describe_cluster](./client.md#describe-cluster)
- [describe_job](./client.md#describe-job)
- [describe_return_shipping_label](./client.md#describe-return-shipping-label)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_job_manifest](./client.md#get-job-manifest)
- [get_job_unlock_code](./client.md#get-job-unlock-code)
- [get_paginator](./client.md#get-paginator)
- [get_snowball_usage](./client.md#get-snowball-usage)
- [get_software_updates](./client.md#get-software-updates)
- [list_cluster_jobs](./client.md#list-cluster-jobs)
- [list_clusters](./client.md#list-clusters)
- [list_compatible_images](./client.md#list-compatible-images)
- [list_jobs](./client.md#list-jobs)
- [update_cluster](./client.md#update-cluster)
- [update_job](./client.md#update-job)
- [update_job_shipment_state](./client.md#update-job-shipment-state)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ClusterLimitExceededException](./client.md#clusterlimitexceededexception)
- [ConflictException](./client.md#conflictexception)
- [Ec2RequestFailedException](./client.md#ec2requestfailedexception)
- [InvalidAddressException](./client.md#invalidaddressexception)
- [InvalidInputCombinationException](./client.md#invalidinputcombinationexception)
- [InvalidJobStateException](./client.md#invalidjobstateexception)
- [InvalidNextTokenException](./client.md#invalidnexttokenexception)
- [InvalidResourceException](./client.md#invalidresourceexception)
- [KMSRequestFailedException](./client.md#kmsrequestfailedexception)
- [ReturnShippingLabelAlreadyExistsException](./client.md#returnshippinglabelalreadyexistsexception)
- [UnsupportedAddressException](./client.md#unsupportedaddressexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("snowball").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_snowball.paginators import DescribeAddressesPaginator, ...
```

- [DescribeAddressesPaginator](./paginators.md#describeaddressespaginator)
- [ListClusterJobsPaginator](./paginators.md#listclusterjobspaginator)
- [ListClustersPaginator](./paginators.md#listclusterspaginator)
- [ListCompatibleImagesPaginator](./paginators.md#listcompatibleimagespaginator)
- [ListJobsPaginator](./paginators.md#listjobspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_snowball.literals import ClusterState, ...
```

- [ClusterState](./literals.md#clusterstate)
- [DescribeAddressesPaginatorName](./literals.md#describeaddressespaginatorname)
- [JobState](./literals.md#jobstate)
- [JobType](./literals.md#jobtype)
- [ListClusterJobsPaginatorName](./literals.md#listclusterjobspaginatorname)
- [ListClustersPaginatorName](./literals.md#listclusterspaginatorname)
- [ListCompatibleImagesPaginatorName](./literals.md#listcompatibleimagespaginatorname)
- [ListJobsPaginatorName](./literals.md#listjobspaginatorname)
- [ShipmentState](./literals.md#shipmentstate)
- [ShippingLabelStatus](./literals.md#shippinglabelstatus)
- [ShippingOption](./literals.md#shippingoption)
- [SnowballCapacity](./literals.md#snowballcapacity)
- [SnowballType](./literals.md#snowballtype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_snowball.type_defs import AddressTypeDef, ...
```

- [AddressTypeDef](./type_defs.md#addresstypedef)
- [ClusterListEntryTypeDef](./type_defs.md#clusterlistentrytypedef)
- [ClusterMetadataTypeDef](./type_defs.md#clustermetadatatypedef)
- [CompatibleImageTypeDef](./type_defs.md#compatibleimagetypedef)
- [CreateAddressResultTypeDef](./type_defs.md#createaddressresulttypedef)
- [CreateClusterResultTypeDef](./type_defs.md#createclusterresulttypedef)
- [CreateJobResultTypeDef](./type_defs.md#createjobresulttypedef)
- [CreateReturnShippingLabelResultTypeDef](./type_defs.md#createreturnshippinglabelresulttypedef)
- [DataTransferTypeDef](./type_defs.md#datatransfertypedef)
- [DescribeAddressResultTypeDef](./type_defs.md#describeaddressresulttypedef)
- [DescribeAddressesResultTypeDef](./type_defs.md#describeaddressesresulttypedef)
- [DescribeClusterResultTypeDef](./type_defs.md#describeclusterresulttypedef)
- [DescribeJobResultTypeDef](./type_defs.md#describejobresulttypedef)
- [DescribeReturnShippingLabelResultTypeDef](./type_defs.md#describereturnshippinglabelresulttypedef)
- [DeviceConfigurationTypeDef](./type_defs.md#deviceconfigurationtypedef)
- [Ec2AmiResourceTypeDef](./type_defs.md#ec2amiresourcetypedef)
- [EventTriggerDefinitionTypeDef](./type_defs.md#eventtriggerdefinitiontypedef)
- [GetJobManifestResultTypeDef](./type_defs.md#getjobmanifestresulttypedef)
- [GetJobUnlockCodeResultTypeDef](./type_defs.md#getjobunlockcoderesulttypedef)
- [GetSnowballUsageResultTypeDef](./type_defs.md#getsnowballusageresulttypedef)
- [GetSoftwareUpdatesResultTypeDef](./type_defs.md#getsoftwareupdatesresulttypedef)
- [INDTaxDocumentsTypeDef](./type_defs.md#indtaxdocumentstypedef)
- [JobListEntryTypeDef](./type_defs.md#joblistentrytypedef)
- [JobLogsTypeDef](./type_defs.md#joblogstypedef)
- [JobMetadataTypeDef](./type_defs.md#jobmetadatatypedef)
- [JobResourceTypeDef](./type_defs.md#jobresourcetypedef)
- [KeyRangeTypeDef](./type_defs.md#keyrangetypedef)
- [LambdaResourceTypeDef](./type_defs.md#lambdaresourcetypedef)
- [ListClusterJobsResultTypeDef](./type_defs.md#listclusterjobsresulttypedef)
- [ListClustersResultTypeDef](./type_defs.md#listclustersresulttypedef)
- [ListCompatibleImagesResultTypeDef](./type_defs.md#listcompatibleimagesresulttypedef)
- [ListJobsResultTypeDef](./type_defs.md#listjobsresulttypedef)
- [NotificationTypeDef](./type_defs.md#notificationtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [S3ResourceTypeDef](./type_defs.md#s3resourcetypedef)
- [ShipmentTypeDef](./type_defs.md#shipmenttypedef)
- [ShippingDetailsTypeDef](./type_defs.md#shippingdetailstypedef)
- [SnowconeDeviceConfigurationTypeDef](./type_defs.md#snowconedeviceconfigurationtypedef)
- [TaxDocumentsTypeDef](./type_defs.md#taxdocumentstypedef)
- [WirelessConnectionTypeDef](./type_defs.md#wirelessconnectiontypedef)
