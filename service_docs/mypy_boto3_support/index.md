# Type annotations for boto3 Support module

> [Index](../index.md) > Support

Auto-generated documentation for [Support](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support.html#Support)
type annotations stubs module [mypy_boto3_support](https://pypi.org/project/mypy-boto3-support/).

```bash
pip install mypy-boto3-support
```

- [Type annotations for boto3 Support module](#type-annotations-for-boto3-support-module)
  - [SupportClient](#supportclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## SupportClient

Type annotations for  `boto3.client("support")` as [SupportClient](./client.md)

Can be used directly:

```python
from mypy_boto3_support.client import SupportClient
```


SupportClient [exceptions](./client.md#exceptions)



### Methods
- [add_attachments_to_set](./client.md#add-attachments-to-set)
- [add_communication_to_case](./client.md#add-communication-to-case)
- [can_paginate](./client.md#can-paginate)
- [create_case](./client.md#create-case)
- [describe_attachment](./client.md#describe-attachment)
- [describe_cases](./client.md#describe-cases)
- [describe_communications](./client.md#describe-communications)
- [describe_services](./client.md#describe-services)
- [describe_severity_levels](./client.md#describe-severity-levels)
- [describe_trusted_advisor_check_refresh_statuses](./client.md#describe-trusted-advisor-check-refresh-statuses)
- [describe_trusted_advisor_check_result](./client.md#describe-trusted-advisor-check-result)
- [describe_trusted_advisor_check_summaries](./client.md#describe-trusted-advisor-check-summaries)
- [describe_trusted_advisor_checks](./client.md#describe-trusted-advisor-checks)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [refresh_trusted_advisor_check](./client.md#refresh-trusted-advisor-check)
- [resolve_case](./client.md#resolve-case)




### Exceptions
- [AttachmentIdNotFound](./client.md#attachmentidnotfound)
- [AttachmentLimitExceeded](./client.md#attachmentlimitexceeded)
- [AttachmentSetExpired](./client.md#attachmentsetexpired)
- [AttachmentSetIdNotFound](./client.md#attachmentsetidnotfound)
- [AttachmentSetSizeLimitExceeded](./client.md#attachmentsetsizelimitexceeded)
- [CaseCreationLimitExceeded](./client.md#casecreationlimitexceeded)
- [CaseIdNotFound](./client.md#caseidnotfound)
- [ClientError](./client.md#clienterror)
- [DescribeAttachmentLimitExceeded](./client.md#describeattachmentlimitexceeded)
- [InternalServerError](./client.md#internalservererror)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("support").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_support.paginators import DescribeCasesPaginator, ...
```

- [DescribeCasesPaginator](./paginators.md#describecasespaginator)
- [DescribeCommunicationsPaginator](./paginators.md#describecommunicationspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_support.literals import DescribeCasesPaginatorName, ...
```

- [DescribeCasesPaginatorName](./literals.md#describecasespaginatorname)
- [DescribeCommunicationsPaginatorName](./literals.md#describecommunicationspaginatorname)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_support.type_defs import AddAttachmentsToSetResponseTypeDef, ...
```

- [AddAttachmentsToSetResponseTypeDef](./type_defs.md#addattachmentstosetresponsetypedef)
- [AddCommunicationToCaseResponseTypeDef](./type_defs.md#addcommunicationtocaseresponsetypedef)
- [AttachmentDetailsTypeDef](./type_defs.md#attachmentdetailstypedef)
- [AttachmentTypeDef](./type_defs.md#attachmenttypedef)
- [CaseDetailsTypeDef](./type_defs.md#casedetailstypedef)
- [CategoryTypeDef](./type_defs.md#categorytypedef)
- [CommunicationTypeDef](./type_defs.md#communicationtypedef)
- [CreateCaseResponseTypeDef](./type_defs.md#createcaseresponsetypedef)
- [DescribeAttachmentResponseTypeDef](./type_defs.md#describeattachmentresponsetypedef)
- [DescribeCasesResponseTypeDef](./type_defs.md#describecasesresponsetypedef)
- [DescribeCommunicationsResponseTypeDef](./type_defs.md#describecommunicationsresponsetypedef)
- [DescribeServicesResponseTypeDef](./type_defs.md#describeservicesresponsetypedef)
- [DescribeSeverityLevelsResponseTypeDef](./type_defs.md#describeseveritylevelsresponsetypedef)
- [DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef](./type_defs.md#describetrustedadvisorcheckrefreshstatusesresponsetypedef)
- [DescribeTrustedAdvisorCheckResultResponseTypeDef](./type_defs.md#describetrustedadvisorcheckresultresponsetypedef)
- [DescribeTrustedAdvisorCheckSummariesResponseTypeDef](./type_defs.md#describetrustedadvisorchecksummariesresponsetypedef)
- [DescribeTrustedAdvisorChecksResponseTypeDef](./type_defs.md#describetrustedadvisorchecksresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [RecentCaseCommunicationsTypeDef](./type_defs.md#recentcasecommunicationstypedef)
- [RefreshTrustedAdvisorCheckResponseTypeDef](./type_defs.md#refreshtrustedadvisorcheckresponsetypedef)
- [ResolveCaseResponseTypeDef](./type_defs.md#resolvecaseresponsetypedef)
- [ServiceTypeDef](./type_defs.md#servicetypedef)
- [SeverityLevelTypeDef](./type_defs.md#severityleveltypedef)
- [TrustedAdvisorCategorySpecificSummaryTypeDef](./type_defs.md#trustedadvisorcategoryspecificsummarytypedef)
- [TrustedAdvisorCheckDescriptionTypeDef](./type_defs.md#trustedadvisorcheckdescriptiontypedef)
- [TrustedAdvisorCheckRefreshStatusTypeDef](./type_defs.md#trustedadvisorcheckrefreshstatustypedef)
- [TrustedAdvisorCheckResultTypeDef](./type_defs.md#trustedadvisorcheckresulttypedef)
- [TrustedAdvisorCheckSummaryTypeDef](./type_defs.md#trustedadvisorchecksummarytypedef)
- [TrustedAdvisorCostOptimizingSummaryTypeDef](./type_defs.md#trustedadvisorcostoptimizingsummarytypedef)
- [TrustedAdvisorResourceDetailTypeDef](./type_defs.md#trustedadvisorresourcedetailtypedef)
- [TrustedAdvisorResourcesSummaryTypeDef](./type_defs.md#trustedadvisorresourcessummarytypedef)
