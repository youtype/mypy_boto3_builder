# Literals for boto3 QuickSight module

> [Index](../index.md) > [QuickSight](./index.md) > Literals

Auto-generated documentation for [QuickSight](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight)
type annotations stubs module [mypy_boto3_quicksight](https://pypi.org/project/mypy-boto3-quicksight/).

- [Literals for boto3 QuickSight module](#literals-for-boto3-quicksight-module)
  - [AnalysisErrorType](#analysiserrortype)
  - [AnalysisFilterAttribute](#analysisfilterattribute)
  - [AssignmentStatus](#assignmentstatus)
  - [ColumnDataType](#columndatatype)
  - [DashboardBehavior](#dashboardbehavior)
  - [DashboardErrorType](#dashboarderrortype)
  - [DashboardFilterAttribute](#dashboardfilterattribute)
  - [DashboardUIState](#dashboarduistate)
  - [DataSetImportMode](#datasetimportmode)
  - [DataSourceErrorInfoType](#datasourceerrorinfotype)
  - [DataSourceType](#datasourcetype)
  - [Edition](#edition)
  - [EmbeddingIdentityType](#embeddingidentitytype)
  - [FileFormat](#fileformat)
  - [FilterOperator](#filteroperator)
  - [GeoSpatialCountryCode](#geospatialcountrycode)
  - [GeoSpatialDataRole](#geospatialdatarole)
  - [IdentityStore](#identitystore)
  - [IdentityType](#identitytype)
  - [IngestionErrorType](#ingestionerrortype)
  - [IngestionRequestSource](#ingestionrequestsource)
  - [IngestionRequestType](#ingestionrequesttype)
  - [IngestionStatus](#ingestionstatus)
  - [InputColumnDataType](#inputcolumndatatype)
  - [JoinType](#jointype)
  - [ListAnalysesPaginatorName](#listanalysespaginatorname)
  - [ListDashboardVersionsPaginatorName](#listdashboardversionspaginatorname)
  - [ListDashboardsPaginatorName](#listdashboardspaginatorname)
  - [ListDataSetsPaginatorName](#listdatasetspaginatorname)
  - [ListDataSourcesPaginatorName](#listdatasourcespaginatorname)
  - [ListIngestionsPaginatorName](#listingestionspaginatorname)
  - [ListNamespacesPaginatorName](#listnamespacespaginatorname)
  - [ListTemplateAliasesPaginatorName](#listtemplatealiasespaginatorname)
  - [ListTemplateVersionsPaginatorName](#listtemplateversionspaginatorname)
  - [ListTemplatesPaginatorName](#listtemplatespaginatorname)
  - [ListThemeVersionsPaginatorName](#listthemeversionspaginatorname)
  - [ListThemesPaginatorName](#listthemespaginatorname)
  - [NamespaceErrorType](#namespaceerrortype)
  - [NamespaceStatus](#namespacestatus)
  - [ResourceStatus](#resourcestatus)
  - [RowLevelPermissionPolicy](#rowlevelpermissionpolicy)
  - [SearchAnalysesPaginatorName](#searchanalysespaginatorname)
  - [SearchDashboardsPaginatorName](#searchdashboardspaginatorname)
  - [TemplateErrorType](#templateerrortype)
  - [TextQualifier](#textqualifier)
  - [ThemeErrorType](#themeerrortype)
  - [ThemeType](#themetype)
  - [UserRole](#userrole)

## AnalysisErrorType

```python
from mypy_boto3_quicksight.literals import AnalysisErrorType
```

Values:

- `ACCESS_DENIED`
- `COLUMN_GEOGRAPHIC_ROLE_MISMATCH`
- `COLUMN_REPLACEMENT_MISSING`
- `COLUMN_TYPE_MISMATCH`
- `DATA_SET_NOT_FOUND`
- `INTERNAL_FAILURE`
- `PARAMETER_NOT_FOUND`
- `PARAMETER_TYPE_INVALID`
- `PARAMETER_VALUE_INCOMPATIBLE`
- `SOURCE_NOT_FOUND`

## AnalysisFilterAttribute

```python
from mypy_boto3_quicksight.literals import AnalysisFilterAttribute
```

Values:

- `QUICKSIGHT_USER`

## AssignmentStatus

```python
from mypy_boto3_quicksight.literals import AssignmentStatus
```

Values:

- `DISABLED`
- `DRAFT`
- `ENABLED`

## ColumnDataType

```python
from mypy_boto3_quicksight.literals import ColumnDataType
```

Values:

- `DATETIME`
- `DECIMAL`
- `INTEGER`
- `STRING`

## DashboardBehavior

```python
from mypy_boto3_quicksight.literals import DashboardBehavior
```

Values:

- `DISABLED`
- `ENABLED`

## DashboardErrorType

```python
from mypy_boto3_quicksight.literals import DashboardErrorType
```

Values:

- `ACCESS_DENIED`
- `COLUMN_GEOGRAPHIC_ROLE_MISMATCH`
- `COLUMN_REPLACEMENT_MISSING`
- `COLUMN_TYPE_MISMATCH`
- `DATA_SET_NOT_FOUND`
- `INTERNAL_FAILURE`
- `PARAMETER_NOT_FOUND`
- `PARAMETER_TYPE_INVALID`
- `PARAMETER_VALUE_INCOMPATIBLE`
- `SOURCE_NOT_FOUND`

## DashboardFilterAttribute

```python
from mypy_boto3_quicksight.literals import DashboardFilterAttribute
```

Values:

- `QUICKSIGHT_USER`

## DashboardUIState

```python
from mypy_boto3_quicksight.literals import DashboardUIState
```

Values:

- `COLLAPSED`
- `EXPANDED`

## DataSetImportMode

```python
from mypy_boto3_quicksight.literals import DataSetImportMode
```

Values:

- `DIRECT_QUERY`
- `SPICE`

## DataSourceErrorInfoType

```python
from mypy_boto3_quicksight.literals import DataSourceErrorInfoType
```

Values:

- `ACCESS_DENIED`
- `CONFLICT`
- `COPY_SOURCE_NOT_FOUND`
- `ENGINE_VERSION_NOT_SUPPORTED`
- `GENERIC_SQL_FAILURE`
- `TIMEOUT`
- `UNKNOWN`
- `UNKNOWN_HOST`

## DataSourceType

```python
from mypy_boto3_quicksight.literals import DataSourceType
```

Values:

- `ADOBE_ANALYTICS`
- `AMAZON_ELASTICSEARCH`
- `ATHENA`
- `AURORA`
- `AURORA_POSTGRESQL`
- `AWS_IOT_ANALYTICS`
- `GITHUB`
- `JIRA`
- `MARIADB`
- `MYSQL`
- `ORACLE`
- `POSTGRESQL`
- `PRESTO`
- `REDSHIFT`
- `S3`
- `SALESFORCE`
- `SERVICENOW`
- `SNOWFLAKE`
- `SPARK`
- `SQLSERVER`
- `TERADATA`
- `TIMESTREAM`
- `TWITTER`

## Edition

```python
from mypy_boto3_quicksight.literals import Edition
```

Values:

- `ENTERPRISE`
- `STANDARD`

## EmbeddingIdentityType

```python
from mypy_boto3_quicksight.literals import EmbeddingIdentityType
```

Values:

- `ANONYMOUS`
- `IAM`
- `QUICKSIGHT`

## FileFormat

```python
from mypy_boto3_quicksight.literals import FileFormat
```

Values:

- `CLF`
- `CSV`
- `ELF`
- `JSON`
- `TSV`
- `XLSX`

## FilterOperator

```python
from mypy_boto3_quicksight.literals import FilterOperator
```

Values:

- `StringEquals`

## GeoSpatialCountryCode

```python
from mypy_boto3_quicksight.literals import GeoSpatialCountryCode
```

Values:

- `US`

## GeoSpatialDataRole

```python
from mypy_boto3_quicksight.literals import GeoSpatialDataRole
```

Values:

- `CITY`
- `COUNTRY`
- `COUNTY`
- `LATITUDE`
- `LONGITUDE`
- `POSTCODE`
- `STATE`

## IdentityStore

```python
from mypy_boto3_quicksight.literals import IdentityStore
```

Values:

- `QUICKSIGHT`

## IdentityType

```python
from mypy_boto3_quicksight.literals import IdentityType
```

Values:

- `IAM`
- `QUICKSIGHT`

## IngestionErrorType

```python
from mypy_boto3_quicksight.literals import IngestionErrorType
```

Values:

- `ACCOUNT_CAPACITY_LIMIT_EXCEEDED`
- `CONNECTION_FAILURE`
- `CUSTOMER_ERROR`
- `DATA_SET_DELETED`
- `DATA_SET_NOT_SPICE`
- `DATA_SET_SIZE_LIMIT_EXCEEDED`
- `DATA_SOURCE_AUTH_FAILED`
- `DATA_SOURCE_CONNECTION_FAILED`
- `DATA_SOURCE_NOT_FOUND`
- `DATA_TOLERANCE_EXCEPTION`
- `FAILURE_TO_ASSUME_ROLE`
- `FAILURE_TO_PROCESS_JSON_FILE`
- `IAM_ROLE_NOT_AVAILABLE`
- `INGESTION_CANCELED`
- `INGESTION_SUPERSEDED`
- `INTERNAL_SERVICE_ERROR`
- `INVALID_DATA_SOURCE_CONFIG`
- `INVALID_DATAPREP_SYNTAX`
- `INVALID_DATE_FORMAT`
- `IOT_DATA_SET_FILE_EMPTY`
- `IOT_FILE_NOT_FOUND`
- `OAUTH_TOKEN_FAILURE`
- `PASSWORD_AUTHENTICATION_FAILURE`
- `PERMISSION_DENIED`
- `QUERY_TIMEOUT`
- `ROW_SIZE_LIMIT_EXCEEDED`
- `S3_FILE_INACCESSIBLE`
- `S3_MANIFEST_ERROR`
- `S3_UPLOADED_FILE_DELETED`
- `SOURCE_API_LIMIT_EXCEEDED_FAILURE`
- `SOURCE_RESOURCE_LIMIT_EXCEEDED`
- `SPICE_TABLE_NOT_FOUND`
- `SQL_EXCEPTION`
- `SQL_INVALID_PARAMETER_VALUE`
- `SQL_NUMERIC_OVERFLOW`
- `SQL_SCHEMA_MISMATCH_ERROR`
- `SQL_TABLE_NOT_FOUND`
- `SSL_CERTIFICATE_VALIDATION_FAILURE`
- `UNRESOLVABLE_HOST`
- `UNROUTABLE_HOST`

## IngestionRequestSource

```python
from mypy_boto3_quicksight.literals import IngestionRequestSource
```

Values:

- `MANUAL`
- `SCHEDULED`

## IngestionRequestType

```python
from mypy_boto3_quicksight.literals import IngestionRequestType
```

Values:

- `EDIT`
- `FULL_REFRESH`
- `INCREMENTAL_REFRESH`
- `INITIAL_INGESTION`

## IngestionStatus

```python
from mypy_boto3_quicksight.literals import IngestionStatus
```

Values:

- `CANCELLED`
- `COMPLETED`
- `FAILED`
- `INITIALIZED`
- `QUEUED`
- `RUNNING`

## InputColumnDataType

```python
from mypy_boto3_quicksight.literals import InputColumnDataType
```

Values:

- `BIT`
- `BOOLEAN`
- `DATETIME`
- `DECIMAL`
- `INTEGER`
- `JSON`
- `STRING`

## JoinType

```python
from mypy_boto3_quicksight.literals import JoinType
```

Values:

- `INNER`
- `LEFT`
- `OUTER`
- `RIGHT`

## ListAnalysesPaginatorName

```python
from mypy_boto3_quicksight.literals import ListAnalysesPaginatorName
```

Values:

- `list_analyses`

## ListDashboardVersionsPaginatorName

```python
from mypy_boto3_quicksight.literals import ListDashboardVersionsPaginatorName
```

Values:

- `list_dashboard_versions`

## ListDashboardsPaginatorName

```python
from mypy_boto3_quicksight.literals import ListDashboardsPaginatorName
```

Values:

- `list_dashboards`

## ListDataSetsPaginatorName

```python
from mypy_boto3_quicksight.literals import ListDataSetsPaginatorName
```

Values:

- `list_data_sets`

## ListDataSourcesPaginatorName

```python
from mypy_boto3_quicksight.literals import ListDataSourcesPaginatorName
```

Values:

- `list_data_sources`

## ListIngestionsPaginatorName

```python
from mypy_boto3_quicksight.literals import ListIngestionsPaginatorName
```

Values:

- `list_ingestions`

## ListNamespacesPaginatorName

```python
from mypy_boto3_quicksight.literals import ListNamespacesPaginatorName
```

Values:

- `list_namespaces`

## ListTemplateAliasesPaginatorName

```python
from mypy_boto3_quicksight.literals import ListTemplateAliasesPaginatorName
```

Values:

- `list_template_aliases`

## ListTemplateVersionsPaginatorName

```python
from mypy_boto3_quicksight.literals import ListTemplateVersionsPaginatorName
```

Values:

- `list_template_versions`

## ListTemplatesPaginatorName

```python
from mypy_boto3_quicksight.literals import ListTemplatesPaginatorName
```

Values:

- `list_templates`

## ListThemeVersionsPaginatorName

```python
from mypy_boto3_quicksight.literals import ListThemeVersionsPaginatorName
```

Values:

- `list_theme_versions`

## ListThemesPaginatorName

```python
from mypy_boto3_quicksight.literals import ListThemesPaginatorName
```

Values:

- `list_themes`

## NamespaceErrorType

```python
from mypy_boto3_quicksight.literals import NamespaceErrorType
```

Values:

- `INTERNAL_SERVICE_ERROR`
- `PERMISSION_DENIED`

## NamespaceStatus

```python
from mypy_boto3_quicksight.literals import NamespaceStatus
```

Values:

- `CREATED`
- `CREATING`
- `DELETING`
- `NON_RETRYABLE_FAILURE`
- `RETRYABLE_FAILURE`

## ResourceStatus

```python
from mypy_boto3_quicksight.literals import ResourceStatus
```

Values:

- `CREATION_FAILED`
- `CREATION_IN_PROGRESS`
- `CREATION_SUCCESSFUL`
- `DELETED`
- `UPDATE_FAILED`
- `UPDATE_IN_PROGRESS`
- `UPDATE_SUCCESSFUL`

## RowLevelPermissionPolicy

```python
from mypy_boto3_quicksight.literals import RowLevelPermissionPolicy
```

Values:

- `DENY_ACCESS`
- `GRANT_ACCESS`

## SearchAnalysesPaginatorName

```python
from mypy_boto3_quicksight.literals import SearchAnalysesPaginatorName
```

Values:

- `search_analyses`

## SearchDashboardsPaginatorName

```python
from mypy_boto3_quicksight.literals import SearchDashboardsPaginatorName
```

Values:

- `search_dashboards`

## TemplateErrorType

```python
from mypy_boto3_quicksight.literals import TemplateErrorType
```

Values:

- `ACCESS_DENIED`
- `DATA_SET_NOT_FOUND`
- `INTERNAL_FAILURE`
- `SOURCE_NOT_FOUND`

## TextQualifier

```python
from mypy_boto3_quicksight.literals import TextQualifier
```

Values:

- `DOUBLE_QUOTE`
- `SINGLE_QUOTE`

## ThemeErrorType

```python
from mypy_boto3_quicksight.literals import ThemeErrorType
```

Values:

- `INTERNAL_FAILURE`

## ThemeType

```python
from mypy_boto3_quicksight.literals import ThemeType
```

Values:

- `ALL`
- `CUSTOM`
- `QUICKSIGHT`

## UserRole

```python
from mypy_boto3_quicksight.literals import UserRole
```

Values:

- `ADMIN`
- `AUTHOR`
- `READER`
- `RESTRICTED_AUTHOR`
- `RESTRICTED_READER`
