# SupportClient for boto3 Support module

> [Index](../index.md) > [Support](./index.md) > SupportClient

Auto-generated documentation for [Support](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support.html#Support)
type annotations stubs module [mypy_boto3_support](https://pypi.org/project/mypy-boto3-support/).

- [SupportClient for boto3 Support module](#supportclient-for-boto3-support-module)
  - [SupportClient](#supportclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_attachments_to_set](#add_attachments_to_set)
    - [add_communication_to_case](#add_communication_to_case)
    - [can_paginate](#can_paginate)
    - [create_case](#create_case)
    - [describe_attachment](#describe_attachment)
    - [describe_cases](#describe_cases)
    - [describe_communications](#describe_communications)
    - [describe_services](#describe_services)
    - [describe_severity_levels](#describe_severity_levels)
    - [describe_trusted_advisor_check_refresh_statuses](#describe_trusted_advisor_check_refresh_statuses)
    - [describe_trusted_advisor_check_result](#describe_trusted_advisor_check_result)
    - [describe_trusted_advisor_check_summaries](#describe_trusted_advisor_check_summaries)
    - [describe_trusted_advisor_checks](#describe_trusted_advisor_checks)
    - [generate_presigned_url](#generate_presigned_url)
    - [refresh_trusted_advisor_check](#refresh_trusted_advisor_check)
    - [resolve_case](#resolve_case)
    - [get_paginator](#get_paginator)

## SupportClient

Type annotations for `boto3.client("support")`

Can be used directly:

```python
from mypy_boto3_support.client import SupportClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_support.client import Exceptions

def handle_error(exc: Exceptions.AttachmentIdNotFound) -> None:
    ...
```


Exceptions:

- `Exceptions.AttachmentIdNotFound`
- `Exceptions.AttachmentLimitExceeded`
- `Exceptions.AttachmentSetExpired`
- `Exceptions.AttachmentSetIdNotFound`
- `Exceptions.AttachmentSetSizeLimitExceeded`
- `Exceptions.CaseCreationLimitExceeded`
- `Exceptions.CaseIdNotFound`
- `Exceptions.ClientError`
- `Exceptions.DescribeAttachmentLimitExceeded`
- `Exceptions.InternalServerError`


## Methods


### add_attachments_to_set

Type annotations for `boto3.client("support").add_attachments_to_set` method.

[Client.add_attachments_to_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support.html#Support.Client.add_attachments_to_set)

```python
def add_attachments_to_set(
    self,
    attachments: List["AttachmentTypeDef"],
    attachmentSetId: str = None
) -> AddAttachmentsToSetResponseTypeDef:
    pass
```

### add_communication_to_case

Type annotations for `boto3.client("support").add_communication_to_case` method.

[Client.add_communication_to_case documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support.html#Support.Client.add_communication_to_case)

```python
def add_communication_to_case(
    self,
    communicationBody: str,
    caseId: str = None,
    ccEmailAddresses: List[str] = None,
    attachmentSetId: str = None
) -> AddCommunicationToCaseResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("support").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support.html#Support.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_case

Type annotations for `boto3.client("support").create_case` method.

[Client.create_case documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support.html#Support.Client.create_case)

```python
def create_case(
    self,
    subject: str,
    communicationBody: str,
    serviceCode: str = None,
    severityCode: str = None,
    categoryCode: str = None,
    ccEmailAddresses: List[str] = None,
    language: str = None,
    issueType: str = None,
    attachmentSetId: str = None
) -> CreateCaseResponseTypeDef:
    pass
```

### describe_attachment

Type annotations for `boto3.client("support").describe_attachment` method.

[Client.describe_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support.html#Support.Client.describe_attachment)

```python
def describe_attachment(
    self,
    attachmentId: str
) -> DescribeAttachmentResponseTypeDef:
    pass
```

### describe_cases

Type annotations for `boto3.client("support").describe_cases` method.

[Client.describe_cases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support.html#Support.Client.describe_cases)

```python
def describe_cases(
    self,
    caseIdList: List[str] = None,
    displayId: str = None,
    afterTime: str = None,
    beforeTime: str = None,
    includeResolvedCases: bool = None,
    nextToken: str = None,
    maxResults: int = None,
    language: str = None,
    includeCommunications: bool = None
) -> DescribeCasesResponseTypeDef:
    pass
```

### describe_communications

Type annotations for `boto3.client("support").describe_communications` method.

[Client.describe_communications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support.html#Support.Client.describe_communications)

```python
def describe_communications(
    self,
    caseId: str,
    beforeTime: str = None,
    afterTime: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> DescribeCommunicationsResponseTypeDef:
    pass
```

### describe_services

Type annotations for `boto3.client("support").describe_services` method.

[Client.describe_services documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support.html#Support.Client.describe_services)

```python
def describe_services(
    self,
    serviceCodeList: List[str] = None,
    language: str = None
) -> DescribeServicesResponseTypeDef:
    pass
```

### describe_severity_levels

Type annotations for `boto3.client("support").describe_severity_levels` method.

[Client.describe_severity_levels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support.html#Support.Client.describe_severity_levels)

```python
def describe_severity_levels(
    self,
    language: str = None
) -> DescribeSeverityLevelsResponseTypeDef:
    pass
```

### describe_trusted_advisor_check_refresh_statuses

Type annotations for `boto3.client("support").describe_trusted_advisor_check_refresh_statuses` method.

[Client.describe_trusted_advisor_check_refresh_statuses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support.html#Support.Client.describe_trusted_advisor_check_refresh_statuses)

```python
def describe_trusted_advisor_check_refresh_statuses(
    self,
    checkIds: List[str]
) -> DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef:
    pass
```

### describe_trusted_advisor_check_result

Type annotations for `boto3.client("support").describe_trusted_advisor_check_result` method.

[Client.describe_trusted_advisor_check_result documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support.html#Support.Client.describe_trusted_advisor_check_result)

```python
def describe_trusted_advisor_check_result(
    self,
    checkId: str,
    language: str = None
) -> DescribeTrustedAdvisorCheckResultResponseTypeDef:
    pass
```

### describe_trusted_advisor_check_summaries

Type annotations for `boto3.client("support").describe_trusted_advisor_check_summaries` method.

[Client.describe_trusted_advisor_check_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support.html#Support.Client.describe_trusted_advisor_check_summaries)

```python
def describe_trusted_advisor_check_summaries(
    self,
    checkIds: List[str]
) -> DescribeTrustedAdvisorCheckSummariesResponseTypeDef:
    pass
```

### describe_trusted_advisor_checks

Type annotations for `boto3.client("support").describe_trusted_advisor_checks` method.

[Client.describe_trusted_advisor_checks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support.html#Support.Client.describe_trusted_advisor_checks)

```python
def describe_trusted_advisor_checks(
    self,
    language: str
) -> DescribeTrustedAdvisorChecksResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("support").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support.html#Support.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### refresh_trusted_advisor_check

Type annotations for `boto3.client("support").refresh_trusted_advisor_check` method.

[Client.refresh_trusted_advisor_check documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support.html#Support.Client.refresh_trusted_advisor_check)

```python
def refresh_trusted_advisor_check(
    self,
    checkId: str
) -> RefreshTrustedAdvisorCheckResponseTypeDef:
    pass
```

### resolve_case

Type annotations for `boto3.client("support").resolve_case` method.

[Client.resolve_case documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support.html#Support.Client.resolve_case)

```python
def resolve_case(
    self,
    caseId: str = None
) -> ResolveCaseResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("support").get_paginator` method with overloads.

- `client.get_paginator("describe_cases")` -> [DescribeCasesPaginator](./paginators.md#describecasespaginator)
- `client.get_paginator("describe_communications")` -> [DescribeCommunicationsPaginator](./paginators.md#describecommunicationspaginator)


