# Type annotations for boto3 ResourceGroupsTaggingAPI module

> [Index](../index.md) > ResourceGroupsTaggingAPI

Auto-generated documentation for [ResourceGroupsTaggingAPI](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI)
type annotations stubs module [mypy_boto3_resourcegroupstaggingapi](https://pypi.org/project/mypy-boto3-resourcegroupstaggingapi/).

```bash
pip install mypy-boto3-resourcegroupstaggingapi
```

- [Type annotations for boto3 ResourceGroupsTaggingAPI module](#type-annotations-for-boto3-resourcegroupstaggingapi-module)
  - [ResourceGroupsTaggingAPIClient](#resourcegroupstaggingapiclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## ResourceGroupsTaggingAPIClient

Type annotations for  `boto3.client("resourcegroupstaggingapi")` as [ResourceGroupsTaggingAPIClient](./client.md)

Can be used directly:

```python
from mypy_boto3_resourcegroupstaggingapi.client import ResourceGroupsTaggingAPIClient
```


ResourceGroupsTaggingAPIClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [describe_report_creation](./client.md#describe-report-creation)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_compliance_summary](./client.md#get-compliance-summary)
- [get_paginator](./client.md#get-paginator)
- [get_resources](./client.md#get-resources)
- [get_tag_keys](./client.md#get-tag-keys)
- [get_tag_values](./client.md#get-tag-values)
- [start_report_creation](./client.md#start-report-creation)
- [tag_resources](./client.md#tag-resources)
- [untag_resources](./client.md#untag-resources)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ConcurrentModificationException](./client.md#concurrentmodificationexception)
- [ConstraintViolationException](./client.md#constraintviolationexception)
- [InternalServiceException](./client.md#internalserviceexception)
- [InvalidParameterException](./client.md#invalidparameterexception)
- [PaginationTokenExpiredException](./client.md#paginationtokenexpiredexception)
- [ThrottledException](./client.md#throttledexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("resourcegroupstaggingapi").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_resourcegroupstaggingapi.paginators import GetComplianceSummaryPaginator, ...
```

- [GetComplianceSummaryPaginator](./paginators.md#getcompliancesummarypaginator)
- [GetResourcesPaginator](./paginators.md#getresourcespaginator)
- [GetTagKeysPaginator](./paginators.md#gettagkeyspaginator)
- [GetTagValuesPaginator](./paginators.md#gettagvaluespaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_resourcegroupstaggingapi.literals import ErrorCode, ...
```

- [ErrorCode](./literals.md#errorcode)
- [GetComplianceSummaryPaginatorName](./literals.md#getcompliancesummarypaginatorname)
- [GetResourcesPaginatorName](./literals.md#getresourcespaginatorname)
- [GetTagKeysPaginatorName](./literals.md#gettagkeyspaginatorname)
- [GetTagValuesPaginatorName](./literals.md#gettagvaluespaginatorname)
- [GroupByAttribute](./literals.md#groupbyattribute)
- [TargetIdType](./literals.md#targetidtype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_resourcegroupstaggingapi.type_defs import ComplianceDetailsTypeDef, ...
```

- [ComplianceDetailsTypeDef](./type_defs.md#compliancedetailstypedef)
- [FailureInfoTypeDef](./type_defs.md#failureinfotypedef)
- [ResourceTagMappingTypeDef](./type_defs.md#resourcetagmappingtypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [SummaryTypeDef](./type_defs.md#summarytypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [DescribeReportCreationOutputTypeDef](./type_defs.md#describereportcreationoutputtypedef)
- [GetComplianceSummaryOutputTypeDef](./type_defs.md#getcompliancesummaryoutputtypedef)
- [GetResourcesOutputTypeDef](./type_defs.md#getresourcesoutputtypedef)
- [GetTagKeysOutputTypeDef](./type_defs.md#gettagkeysoutputtypedef)
- [GetTagValuesOutputTypeDef](./type_defs.md#gettagvaluesoutputtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [TagFilterTypeDef](./type_defs.md#tagfiltertypedef)
- [TagResourcesOutputTypeDef](./type_defs.md#tagresourcesoutputtypedef)
- [UntagResourcesOutputTypeDef](./type_defs.md#untagresourcesoutputtypedef)
