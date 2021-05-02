# Literals for boto3 Kendra module

> [Index](../index.md) > [Kendra](./index.md) > Literals

Auto-generated documentation for [Kendra](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra)
type annotations stubs module [mypy_boto3_kendra](https://pypi.org/project/mypy-boto3-kendra/).

- [Literals for boto3 Kendra module](#literals-for-boto3-kendra-module)
  - [AdditionalResultAttributeValueType](#additionalresultattributevaluetype)
  - [ConfluenceAttachmentFieldName](#confluenceattachmentfieldname)
  - [ConfluenceBlogFieldName](#confluenceblogfieldname)
  - [ConfluencePageFieldName](#confluencepagefieldname)
  - [ConfluenceSpaceFieldName](#confluencespacefieldname)
  - [ConfluenceVersion](#confluenceversion)
  - [ContentType](#contenttype)
  - [DataSourceStatus](#datasourcestatus)
  - [DataSourceSyncJobStatus](#datasourcesyncjobstatus)
  - [DataSourceType](#datasourcetype)
  - [DatabaseEngineType](#databaseenginetype)
  - [DocumentAttributeValueType](#documentattributevaluetype)
  - [ErrorCode](#errorcode)
  - [FaqFileFormat](#faqfileformat)
  - [FaqStatus](#faqstatus)
  - [HighlightType](#highlighttype)
  - [IndexEdition](#indexedition)
  - [IndexStatus](#indexstatus)
  - [KeyLocation](#keylocation)
  - [Order](#order)
  - [PrincipalType](#principaltype)
  - [QueryIdentifiersEnclosingOption](#queryidentifiersenclosingoption)
  - [QueryResultType](#queryresulttype)
  - [ReadAccessType](#readaccesstype)
  - [RelevanceType](#relevancetype)
  - [SalesforceChatterFeedIncludeFilterType](#salesforcechatterfeedincludefiltertype)
  - [SalesforceKnowledgeArticleState](#salesforceknowledgearticlestate)
  - [SalesforceStandardObjectName](#salesforcestandardobjectname)
  - [ScoreConfidence](#scoreconfidence)
  - [ServiceNowAuthenticationType](#servicenowauthenticationtype)
  - [ServiceNowBuildVersionType](#servicenowbuildversiontype)
  - [SharePointVersion](#sharepointversion)
  - [SortOrder](#sortorder)
  - [ThesaurusStatus](#thesaurusstatus)
  - [UserContextPolicy](#usercontextpolicy)

## AdditionalResultAttributeValueType

```python
from mypy_boto3_kendra.literals import AdditionalResultAttributeValueType
```

Values:

- `TEXT_WITH_HIGHLIGHTS_VALUE`

## ConfluenceAttachmentFieldName

```python
from mypy_boto3_kendra.literals import ConfluenceAttachmentFieldName
```

Values:

- `AUTHOR`
- `CONTENT_TYPE`
- `CREATED_DATE`
- `DISPLAY_URL`
- `FILE_SIZE`
- `ITEM_TYPE`
- `PARENT_ID`
- `SPACE_KEY`
- `SPACE_NAME`
- `URL`
- `VERSION`

## ConfluenceBlogFieldName

```python
from mypy_boto3_kendra.literals import ConfluenceBlogFieldName
```

Values:

- `AUTHOR`
- `DISPLAY_URL`
- `ITEM_TYPE`
- `LABELS`
- `PUBLISH_DATE`
- `SPACE_KEY`
- `SPACE_NAME`
- `URL`
- `VERSION`

## ConfluencePageFieldName

```python
from mypy_boto3_kendra.literals import ConfluencePageFieldName
```

Values:

- `AUTHOR`
- `CONTENT_STATUS`
- `CREATED_DATE`
- `DISPLAY_URL`
- `ITEM_TYPE`
- `LABELS`
- `MODIFIED_DATE`
- `PARENT_ID`
- `SPACE_KEY`
- `SPACE_NAME`
- `URL`
- `VERSION`

## ConfluenceSpaceFieldName

```python
from mypy_boto3_kendra.literals import ConfluenceSpaceFieldName
```

Values:

- `DISPLAY_URL`
- `ITEM_TYPE`
- `SPACE_KEY`
- `URL`

## ConfluenceVersion

```python
from mypy_boto3_kendra.literals import ConfluenceVersion
```

Values:

- `CLOUD`
- `SERVER`

## ContentType

```python
from mypy_boto3_kendra.literals import ContentType
```

Values:

- `HTML`
- `MS_WORD`
- `PDF`
- `PLAIN_TEXT`
- `PPT`

## DataSourceStatus

```python
from mypy_boto3_kendra.literals import DataSourceStatus
```

Values:

- `ACTIVE`
- `CREATING`
- `DELETING`
- `FAILED`
- `UPDATING`

## DataSourceSyncJobStatus

```python
from mypy_boto3_kendra.literals import DataSourceSyncJobStatus
```

Values:

- `ABORTED`
- `FAILED`
- `INCOMPLETE`
- `STOPPING`
- `SUCCEEDED`
- `SYNCING`
- `SYNCING_INDEXING`

## DataSourceType

```python
from mypy_boto3_kendra.literals import DataSourceType
```

Values:

- `CONFLUENCE`
- `CUSTOM`
- `DATABASE`
- `GOOGLEDRIVE`
- `ONEDRIVE`
- `S3`
- `SALESFORCE`
- `SERVICENOW`
- `SHAREPOINT`

## DatabaseEngineType

```python
from mypy_boto3_kendra.literals import DatabaseEngineType
```

Values:

- `RDS_AURORA_MYSQL`
- `RDS_AURORA_POSTGRESQL`
- `RDS_MYSQL`
- `RDS_POSTGRESQL`

## DocumentAttributeValueType

```python
from mypy_boto3_kendra.literals import DocumentAttributeValueType
```

Values:

- `DATE_VALUE`
- `LONG_VALUE`
- `STRING_LIST_VALUE`
- `STRING_VALUE`

## ErrorCode

```python
from mypy_boto3_kendra.literals import ErrorCode
```

Values:

- `InternalError`
- `InvalidRequest`

## FaqFileFormat

```python
from mypy_boto3_kendra.literals import FaqFileFormat
```

Values:

- `CSV`
- `CSV_WITH_HEADER`
- `JSON`

## FaqStatus

```python
from mypy_boto3_kendra.literals import FaqStatus
```

Values:

- `ACTIVE`
- `CREATING`
- `DELETING`
- `FAILED`
- `UPDATING`

## HighlightType

```python
from mypy_boto3_kendra.literals import HighlightType
```

Values:

- `STANDARD`
- `THESAURUS_SYNONYM`

## IndexEdition

```python
from mypy_boto3_kendra.literals import IndexEdition
```

Values:

- `DEVELOPER_EDITION`
- `ENTERPRISE_EDITION`

## IndexStatus

```python
from mypy_boto3_kendra.literals import IndexStatus
```

Values:

- `ACTIVE`
- `CREATING`
- `DELETING`
- `FAILED`
- `SYSTEM_UPDATING`
- `UPDATING`

## KeyLocation

```python
from mypy_boto3_kendra.literals import KeyLocation
```

Values:

- `SECRET_MANAGER`
- `URL`

## Order

```python
from mypy_boto3_kendra.literals import Order
```

Values:

- `ASCENDING`
- `DESCENDING`

## PrincipalType

```python
from mypy_boto3_kendra.literals import PrincipalType
```

Values:

- `GROUP`
- `USER`

## QueryIdentifiersEnclosingOption

```python
from mypy_boto3_kendra.literals import QueryIdentifiersEnclosingOption
```

Values:

- `DOUBLE_QUOTES`
- `NONE`

## QueryResultType

```python
from mypy_boto3_kendra.literals import QueryResultType
```

Values:

- `ANSWER`
- `DOCUMENT`
- `QUESTION_ANSWER`

## ReadAccessType

```python
from mypy_boto3_kendra.literals import ReadAccessType
```

Values:

- `ALLOW`
- `DENY`

## RelevanceType

```python
from mypy_boto3_kendra.literals import RelevanceType
```

Values:

- `NOT_RELEVANT`
- `RELEVANT`

## SalesforceChatterFeedIncludeFilterType

```python
from mypy_boto3_kendra.literals import SalesforceChatterFeedIncludeFilterType
```

Values:

- `ACTIVE_USER`
- `STANDARD_USER`

## SalesforceKnowledgeArticleState

```python
from mypy_boto3_kendra.literals import SalesforceKnowledgeArticleState
```

Values:

- `ARCHIVED`
- `DRAFT`
- `PUBLISHED`

## SalesforceStandardObjectName

```python
from mypy_boto3_kendra.literals import SalesforceStandardObjectName
```

Values:

- `ACCOUNT`
- `CAMPAIGN`
- `CASE`
- `CONTACT`
- `CONTRACT`
- `DOCUMENT`
- `GROUP`
- `IDEA`
- `LEAD`
- `OPPORTUNITY`
- `PARTNER`
- `PRICEBOOK`
- `PRODUCT`
- `PROFILE`
- `SOLUTION`
- `TASK`
- `USER`

## ScoreConfidence

```python
from mypy_boto3_kendra.literals import ScoreConfidence
```

Values:

- `HIGH`
- `LOW`
- `MEDIUM`
- `VERY_HIGH`

## ServiceNowAuthenticationType

```python
from mypy_boto3_kendra.literals import ServiceNowAuthenticationType
```

Values:

- `HTTP_BASIC`
- `OAUTH2`

## ServiceNowBuildVersionType

```python
from mypy_boto3_kendra.literals import ServiceNowBuildVersionType
```

Values:

- `LONDON`
- `OTHERS`

## SharePointVersion

```python
from mypy_boto3_kendra.literals import SharePointVersion
```

Values:

- `SHAREPOINT_ONLINE`

## SortOrder

```python
from mypy_boto3_kendra.literals import SortOrder
```

Values:

- `ASC`
- `DESC`

## ThesaurusStatus

```python
from mypy_boto3_kendra.literals import ThesaurusStatus
```

Values:

- `ACTIVE`
- `ACTIVE_BUT_UPDATE_FAILED`
- `CREATING`
- `DELETING`
- `FAILED`
- `UPDATING`

## UserContextPolicy

```python
from mypy_boto3_kendra.literals import UserContextPolicy
```

Values:

- `ATTRIBUTE_FILTER`
- `USER_TOKEN`
