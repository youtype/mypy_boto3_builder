# Structures for boto3 Support module

> [Index](../index.md) > [Support](./index.md) > Structures

Auto-generated documentation for [Support](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support.html#Support)
type annotations stubs module [mypy_boto3_support](https://pypi.org/project/mypy-boto3-support/).

- [Structures for boto3 Support module](#structures-for-boto3-support-module)
  - [AddAttachmentsToSetResponseTypeDef](#addattachmentstosetresponsetypedef)
  - [AddCommunicationToCaseResponseTypeDef](#addcommunicationtocaseresponsetypedef)
  - [AttachmentDetailsTypeDef](#attachmentdetailstypedef)
  - [AttachmentTypeDef](#attachmenttypedef)
  - [CaseDetailsTypeDef](#casedetailstypedef)
  - [CategoryTypeDef](#categorytypedef)
  - [CommunicationTypeDef](#communicationtypedef)
  - [CreateCaseResponseTypeDef](#createcaseresponsetypedef)
  - [DescribeAttachmentResponseTypeDef](#describeattachmentresponsetypedef)
  - [DescribeCasesResponseTypeDef](#describecasesresponsetypedef)
  - [DescribeCommunicationsResponseTypeDef](#describecommunicationsresponsetypedef)
  - [DescribeServicesResponseTypeDef](#describeservicesresponsetypedef)
  - [DescribeSeverityLevelsResponseTypeDef](#describeseveritylevelsresponsetypedef)
  - [DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef](#describetrustedadvisorcheckrefreshstatusesresponsetypedef)
  - [DescribeTrustedAdvisorCheckResultResponseTypeDef](#describetrustedadvisorcheckresultresponsetypedef)
  - [DescribeTrustedAdvisorCheckSummariesResponseTypeDef](#describetrustedadvisorchecksummariesresponsetypedef)
  - [DescribeTrustedAdvisorChecksResponseTypeDef](#describetrustedadvisorchecksresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [RecentCaseCommunicationsTypeDef](#recentcasecommunicationstypedef)
  - [RefreshTrustedAdvisorCheckResponseTypeDef](#refreshtrustedadvisorcheckresponsetypedef)
  - [ResolveCaseResponseTypeDef](#resolvecaseresponsetypedef)
  - [ServiceTypeDef](#servicetypedef)
  - [SeverityLevelTypeDef](#severityleveltypedef)
  - [TrustedAdvisorCategorySpecificSummaryTypeDef](#trustedadvisorcategoryspecificsummarytypedef)
  - [TrustedAdvisorCheckDescriptionTypeDef](#trustedadvisorcheckdescriptiontypedef)
  - [TrustedAdvisorCheckRefreshStatusTypeDef](#trustedadvisorcheckrefreshstatustypedef)
  - [TrustedAdvisorCheckResultTypeDef](#trustedadvisorcheckresulttypedef)
  - [TrustedAdvisorCheckSummaryTypeDef](#trustedadvisorchecksummarytypedef)
  - [TrustedAdvisorCostOptimizingSummaryTypeDef](#trustedadvisorcostoptimizingsummarytypedef)
  - [TrustedAdvisorResourceDetailTypeDef](#trustedadvisorresourcedetailtypedef)
  - [TrustedAdvisorResourcesSummaryTypeDef](#trustedadvisorresourcessummarytypedef)

## AddAttachmentsToSetResponseTypeDef

```python
from mypy_boto3_support.type_defs import AddAttachmentsToSetResponseTypeDef
```




Optional fields:
- `attachmentSetId`: `str`
- `expiryTime`: `str`


## AddCommunicationToCaseResponseTypeDef

```python
from mypy_boto3_support.type_defs import AddCommunicationToCaseResponseTypeDef
```




Optional fields:
- `result`: `bool`


## AttachmentDetailsTypeDef

```python
from mypy_boto3_support.type_defs import AttachmentDetailsTypeDef
```




Optional fields:
- `attachmentId`: `str`
- `fileName`: `str`


## AttachmentTypeDef

```python
from mypy_boto3_support.type_defs import AttachmentTypeDef
```




Optional fields:
- `fileName`: `str`
- `data`: `Union[bytes, IO[bytes]]`


## CaseDetailsTypeDef

```python
from mypy_boto3_support.type_defs import CaseDetailsTypeDef
```




Optional fields:
- `caseId`: `str`
- `displayId`: `str`
- `subject`: `str`
- `status`: `str`
- `serviceCode`: `str`
- `categoryCode`: `str`
- `severityCode`: `str`
- `submittedBy`: `str`
- `timeCreated`: `str`
- `recentCommunications`: `"RecentCaseCommunicationsTypeDef"`
- `ccEmailAddresses`: `List[str]`
- `language`: `str`


## CategoryTypeDef

```python
from mypy_boto3_support.type_defs import CategoryTypeDef
```




Optional fields:
- `code`: `str`
- `name`: `str`


## CommunicationTypeDef

```python
from mypy_boto3_support.type_defs import CommunicationTypeDef
```




Optional fields:
- `caseId`: `str`
- `body`: `str`
- `submittedBy`: `str`
- `timeCreated`: `str`
- `attachmentSet`: `List["AttachmentDetailsTypeDef"]`


## CreateCaseResponseTypeDef

```python
from mypy_boto3_support.type_defs import CreateCaseResponseTypeDef
```




Optional fields:
- `caseId`: `str`


## DescribeAttachmentResponseTypeDef

```python
from mypy_boto3_support.type_defs import DescribeAttachmentResponseTypeDef
```




Optional fields:
- `attachment`: `"AttachmentTypeDef"`


## DescribeCasesResponseTypeDef

```python
from mypy_boto3_support.type_defs import DescribeCasesResponseTypeDef
```




Optional fields:
- `cases`: `List["CaseDetailsTypeDef"]`
- `nextToken`: `str`


## DescribeCommunicationsResponseTypeDef

```python
from mypy_boto3_support.type_defs import DescribeCommunicationsResponseTypeDef
```




Optional fields:
- `communications`: `List["CommunicationTypeDef"]`
- `nextToken`: `str`


## DescribeServicesResponseTypeDef

```python
from mypy_boto3_support.type_defs import DescribeServicesResponseTypeDef
```




Optional fields:
- `services`: `List["ServiceTypeDef"]`


## DescribeSeverityLevelsResponseTypeDef

```python
from mypy_boto3_support.type_defs import DescribeSeverityLevelsResponseTypeDef
```




Optional fields:
- `severityLevels`: `List["SeverityLevelTypeDef"]`


## DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef

```python
from mypy_boto3_support.type_defs import DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef
```


Required fields:
- `statuses`: `List["TrustedAdvisorCheckRefreshStatusTypeDef"]`




## DescribeTrustedAdvisorCheckResultResponseTypeDef

```python
from mypy_boto3_support.type_defs import DescribeTrustedAdvisorCheckResultResponseTypeDef
```




Optional fields:
- `result`: `"TrustedAdvisorCheckResultTypeDef"`


## DescribeTrustedAdvisorCheckSummariesResponseTypeDef

```python
from mypy_boto3_support.type_defs import DescribeTrustedAdvisorCheckSummariesResponseTypeDef
```


Required fields:
- `summaries`: `List["TrustedAdvisorCheckSummaryTypeDef"]`




## DescribeTrustedAdvisorChecksResponseTypeDef

```python
from mypy_boto3_support.type_defs import DescribeTrustedAdvisorChecksResponseTypeDef
```


Required fields:
- `checks`: `List["TrustedAdvisorCheckDescriptionTypeDef"]`




## PaginatorConfigTypeDef

```python
from mypy_boto3_support.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## RecentCaseCommunicationsTypeDef

```python
from mypy_boto3_support.type_defs import RecentCaseCommunicationsTypeDef
```




Optional fields:
- `communications`: `List["CommunicationTypeDef"]`
- `nextToken`: `str`


## RefreshTrustedAdvisorCheckResponseTypeDef

```python
from mypy_boto3_support.type_defs import RefreshTrustedAdvisorCheckResponseTypeDef
```


Required fields:
- `status`: `"TrustedAdvisorCheckRefreshStatusTypeDef"`




## ResolveCaseResponseTypeDef

```python
from mypy_boto3_support.type_defs import ResolveCaseResponseTypeDef
```




Optional fields:
- `initialCaseStatus`: `str`
- `finalCaseStatus`: `str`


## ServiceTypeDef

```python
from mypy_boto3_support.type_defs import ServiceTypeDef
```




Optional fields:
- `code`: `str`
- `name`: `str`
- `categories`: `List["CategoryTypeDef"]`


## SeverityLevelTypeDef

```python
from mypy_boto3_support.type_defs import SeverityLevelTypeDef
```




Optional fields:
- `code`: `str`
- `name`: `str`


## TrustedAdvisorCategorySpecificSummaryTypeDef

```python
from mypy_boto3_support.type_defs import TrustedAdvisorCategorySpecificSummaryTypeDef
```




Optional fields:
- `costOptimizing`: `"TrustedAdvisorCostOptimizingSummaryTypeDef"`


## TrustedAdvisorCheckDescriptionTypeDef

```python
from mypy_boto3_support.type_defs import TrustedAdvisorCheckDescriptionTypeDef
```


Required fields:
- `id`: `str`
- `name`: `str`
- `description`: `str`
- `category`: `str`
- `metadata`: `List[str]`




## TrustedAdvisorCheckRefreshStatusTypeDef

```python
from mypy_boto3_support.type_defs import TrustedAdvisorCheckRefreshStatusTypeDef
```


Required fields:
- `checkId`: `str`
- `status`: `str`
- `millisUntilNextRefreshable`: `int`




## TrustedAdvisorCheckResultTypeDef

```python
from mypy_boto3_support.type_defs import TrustedAdvisorCheckResultTypeDef
```


Required fields:
- `checkId`: `str`
- `timestamp`: `str`
- `status`: `str`
- `resourcesSummary`: `"TrustedAdvisorResourcesSummaryTypeDef"`
- `categorySpecificSummary`: `"TrustedAdvisorCategorySpecificSummaryTypeDef"`
- `flaggedResources`: `List["TrustedAdvisorResourceDetailTypeDef"]`




## TrustedAdvisorCheckSummaryTypeDef

```python
from mypy_boto3_support.type_defs import TrustedAdvisorCheckSummaryTypeDef
```


Required fields:
- `checkId`: `str`
- `timestamp`: `str`
- `status`: `str`
- `resourcesSummary`: `"TrustedAdvisorResourcesSummaryTypeDef"`
- `categorySpecificSummary`: `"TrustedAdvisorCategorySpecificSummaryTypeDef"`



Optional fields:
- `hasFlaggedResources`: `bool`


## TrustedAdvisorCostOptimizingSummaryTypeDef

```python
from mypy_boto3_support.type_defs import TrustedAdvisorCostOptimizingSummaryTypeDef
```


Required fields:
- `estimatedMonthlySavings`: `float`
- `estimatedPercentMonthlySavings`: `float`




## TrustedAdvisorResourceDetailTypeDef

```python
from mypy_boto3_support.type_defs import TrustedAdvisorResourceDetailTypeDef
```


Required fields:
- `status`: `str`
- `resourceId`: `str`
- `metadata`: `List[str]`



Optional fields:
- `region`: `str`
- `isSuppressed`: `bool`


## TrustedAdvisorResourcesSummaryTypeDef

```python
from mypy_boto3_support.type_defs import TrustedAdvisorResourcesSummaryTypeDef
```


Required fields:
- `resourcesProcessed`: `int`
- `resourcesFlagged`: `int`
- `resourcesIgnored`: `int`
- `resourcesSuppressed`: `int`



