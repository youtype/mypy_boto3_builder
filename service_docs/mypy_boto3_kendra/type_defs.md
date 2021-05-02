# Structures for boto3 Kendra module

> [Index](../index.md) > [Kendra](./index.md) > Structures

Auto-generated documentation for [Kendra](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra)
type annotations stubs module [mypy_boto3_kendra](https://pypi.org/project/mypy-boto3-kendra/).

- [Structures for boto3 Kendra module](#structures-for-boto3-kendra-module)
  - [AccessControlListConfigurationTypeDef](#accesscontrollistconfigurationtypedef)
  - [AclConfigurationTypeDef](#aclconfigurationtypedef)
  - [AdditionalResultAttributeTypeDef](#additionalresultattributetypedef)
  - [AdditionalResultAttributeValueTypeDef](#additionalresultattributevaluetypedef)
  - [AttributeFilterTypeDef](#attributefiltertypedef)
  - [BatchDeleteDocumentResponseFailedDocumentTypeDef](#batchdeletedocumentresponsefaileddocumenttypedef)
  - [BatchDeleteDocumentResponseTypeDef](#batchdeletedocumentresponsetypedef)
  - [BatchPutDocumentResponseFailedDocumentTypeDef](#batchputdocumentresponsefaileddocumenttypedef)
  - [BatchPutDocumentResponseTypeDef](#batchputdocumentresponsetypedef)
  - [CapacityUnitsConfigurationTypeDef](#capacityunitsconfigurationtypedef)
  - [ClickFeedbackTypeDef](#clickfeedbacktypedef)
  - [ColumnConfigurationTypeDef](#columnconfigurationtypedef)
  - [ConfluenceAttachmentConfigurationTypeDef](#confluenceattachmentconfigurationtypedef)
  - [ConfluenceAttachmentToIndexFieldMappingTypeDef](#confluenceattachmenttoindexfieldmappingtypedef)
  - [ConfluenceBlogConfigurationTypeDef](#confluenceblogconfigurationtypedef)
  - [ConfluenceBlogToIndexFieldMappingTypeDef](#confluenceblogtoindexfieldmappingtypedef)
  - [ConfluenceConfigurationTypeDef](#confluenceconfigurationtypedef)
  - [ConfluencePageConfigurationTypeDef](#confluencepageconfigurationtypedef)
  - [ConfluencePageToIndexFieldMappingTypeDef](#confluencepagetoindexfieldmappingtypedef)
  - [ConfluenceSpaceConfigurationTypeDef](#confluencespaceconfigurationtypedef)
  - [ConfluenceSpaceToIndexFieldMappingTypeDef](#confluencespacetoindexfieldmappingtypedef)
  - [ConnectionConfigurationTypeDef](#connectionconfigurationtypedef)
  - [CreateDataSourceResponseTypeDef](#createdatasourceresponsetypedef)
  - [CreateFaqResponseTypeDef](#createfaqresponsetypedef)
  - [CreateIndexResponseTypeDef](#createindexresponsetypedef)
  - [CreateThesaurusResponseTypeDef](#createthesaurusresponsetypedef)
  - [DataSourceConfigurationTypeDef](#datasourceconfigurationtypedef)
  - [DataSourceSummaryTypeDef](#datasourcesummarytypedef)
  - [DataSourceSyncJobMetricTargetTypeDef](#datasourcesyncjobmetrictargettypedef)
  - [DataSourceSyncJobMetricsTypeDef](#datasourcesyncjobmetricstypedef)
  - [DataSourceSyncJobTypeDef](#datasourcesyncjobtypedef)
  - [DataSourceToIndexFieldMappingTypeDef](#datasourcetoindexfieldmappingtypedef)
  - [DataSourceVpcConfigurationTypeDef](#datasourcevpcconfigurationtypedef)
  - [DatabaseConfigurationTypeDef](#databaseconfigurationtypedef)
  - [DescribeDataSourceResponseTypeDef](#describedatasourceresponsetypedef)
  - [DescribeFaqResponseTypeDef](#describefaqresponsetypedef)
  - [DescribeIndexResponseTypeDef](#describeindexresponsetypedef)
  - [DescribeThesaurusResponseTypeDef](#describethesaurusresponsetypedef)
  - [DocumentAttributeTypeDef](#documentattributetypedef)
  - [DocumentAttributeValueCountPairTypeDef](#documentattributevaluecountpairtypedef)
  - [DocumentAttributeValueTypeDef](#documentattributevaluetypedef)
  - [DocumentMetadataConfigurationTypeDef](#documentmetadataconfigurationtypedef)
  - [DocumentRelevanceConfigurationTypeDef](#documentrelevanceconfigurationtypedef)
  - [DocumentTypeDef](#documenttypedef)
  - [DocumentsMetadataConfigurationTypeDef](#documentsmetadataconfigurationtypedef)
  - [FacetResultTypeDef](#facetresulttypedef)
  - [FacetTypeDef](#facettypedef)
  - [FaqStatisticsTypeDef](#faqstatisticstypedef)
  - [FaqSummaryTypeDef](#faqsummarytypedef)
  - [GoogleDriveConfigurationTypeDef](#googledriveconfigurationtypedef)
  - [HighlightTypeDef](#highlighttypedef)
  - [IndexConfigurationSummaryTypeDef](#indexconfigurationsummarytypedef)
  - [IndexStatisticsTypeDef](#indexstatisticstypedef)
  - [JsonTokenTypeConfigurationTypeDef](#jsontokentypeconfigurationtypedef)
  - [JwtTokenTypeConfigurationTypeDef](#jwttokentypeconfigurationtypedef)
  - [ListDataSourceSyncJobsResponseTypeDef](#listdatasourcesyncjobsresponsetypedef)
  - [ListDataSourcesResponseTypeDef](#listdatasourcesresponsetypedef)
  - [ListFaqsResponseTypeDef](#listfaqsresponsetypedef)
  - [ListIndicesResponseTypeDef](#listindicesresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListThesauriResponseTypeDef](#listthesauriresponsetypedef)
  - [OneDriveConfigurationTypeDef](#onedriveconfigurationtypedef)
  - [OneDriveUsersTypeDef](#onedriveuserstypedef)
  - [PrincipalTypeDef](#principaltypedef)
  - [QueryResultItemTypeDef](#queryresultitemtypedef)
  - [QueryResultTypeDef](#queryresulttypedef)
  - [RelevanceFeedbackTypeDef](#relevancefeedbacktypedef)
  - [RelevanceTypeDef](#relevancetypedef)
  - [S3DataSourceConfigurationTypeDef](#s3datasourceconfigurationtypedef)
  - [S3PathTypeDef](#s3pathtypedef)
  - [SalesforceChatterFeedConfigurationTypeDef](#salesforcechatterfeedconfigurationtypedef)
  - [SalesforceConfigurationTypeDef](#salesforceconfigurationtypedef)
  - [SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef](#salesforcecustomknowledgearticletypeconfigurationtypedef)
  - [SalesforceKnowledgeArticleConfigurationTypeDef](#salesforceknowledgearticleconfigurationtypedef)
  - [SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef](#salesforcestandardknowledgearticletypeconfigurationtypedef)
  - [SalesforceStandardObjectAttachmentConfigurationTypeDef](#salesforcestandardobjectattachmentconfigurationtypedef)
  - [SalesforceStandardObjectConfigurationTypeDef](#salesforcestandardobjectconfigurationtypedef)
  - [ScoreAttributesTypeDef](#scoreattributestypedef)
  - [SearchTypeDef](#searchtypedef)
  - [ServerSideEncryptionConfigurationTypeDef](#serversideencryptionconfigurationtypedef)
  - [ServiceNowConfigurationTypeDef](#servicenowconfigurationtypedef)
  - [ServiceNowKnowledgeArticleConfigurationTypeDef](#servicenowknowledgearticleconfigurationtypedef)
  - [ServiceNowServiceCatalogConfigurationTypeDef](#servicenowservicecatalogconfigurationtypedef)
  - [SharePointConfigurationTypeDef](#sharepointconfigurationtypedef)
  - [SortingConfigurationTypeDef](#sortingconfigurationtypedef)
  - [SqlConfigurationTypeDef](#sqlconfigurationtypedef)
  - [StartDataSourceSyncJobResponseTypeDef](#startdatasourcesyncjobresponsetypedef)
  - [TagTypeDef](#tagtypedef)
  - [TextDocumentStatisticsTypeDef](#textdocumentstatisticstypedef)
  - [TextWithHighlightsTypeDef](#textwithhighlightstypedef)
  - [ThesaurusSummaryTypeDef](#thesaurussummarytypedef)
  - [TimeRangeTypeDef](#timerangetypedef)
  - [UserContextTypeDef](#usercontexttypedef)
  - [UserTokenConfigurationTypeDef](#usertokenconfigurationtypedef)

## AccessControlListConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import AccessControlListConfigurationTypeDef
```




Optional fields:
- `KeyPath`: `str`


## AclConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import AclConfigurationTypeDef
```


Required fields:
- `AllowedGroupsColumnName`: `str`




## AdditionalResultAttributeTypeDef

```python
from mypy_boto3_kendra.type_defs import AdditionalResultAttributeTypeDef
```


Required fields:
- `Key`: `str`
- `ValueType`: `Literal['TEXT_WITH_HIGHLIGHTS_VALUE']`
- `Value`: `"AdditionalResultAttributeValueTypeDef"`




## AdditionalResultAttributeValueTypeDef

```python
from mypy_boto3_kendra.type_defs import AdditionalResultAttributeValueTypeDef
```




Optional fields:
- `TextWithHighlightsValue`: `"TextWithHighlightsTypeDef"`


## AttributeFilterTypeDef

```python
from mypy_boto3_kendra.type_defs import AttributeFilterTypeDef
```




Optional fields:
- `AndAllFilters`: `List[Dict[str, Any]]`
- `OrAllFilters`: `List[Dict[str, Any]]`
- `NotFilter`: `Dict[str, Any]`
- `EqualsTo`: `"DocumentAttributeTypeDef"`
- `ContainsAll`: `"DocumentAttributeTypeDef"`
- `ContainsAny`: `"DocumentAttributeTypeDef"`
- `GreaterThan`: `"DocumentAttributeTypeDef"`
- `GreaterThanOrEquals`: `"DocumentAttributeTypeDef"`
- `LessThan`: `"DocumentAttributeTypeDef"`
- `LessThanOrEquals`: `"DocumentAttributeTypeDef"`


## BatchDeleteDocumentResponseFailedDocumentTypeDef

```python
from mypy_boto3_kendra.type_defs import BatchDeleteDocumentResponseFailedDocumentTypeDef
```




Optional fields:
- `Id`: `str`
- `ErrorCode`: `ErrorCode`
- `ErrorMessage`: `str`


## BatchDeleteDocumentResponseTypeDef

```python
from mypy_boto3_kendra.type_defs import BatchDeleteDocumentResponseTypeDef
```




Optional fields:
- `FailedDocuments`: `List["BatchDeleteDocumentResponseFailedDocumentTypeDef"]`


## BatchPutDocumentResponseFailedDocumentTypeDef

```python
from mypy_boto3_kendra.type_defs import BatchPutDocumentResponseFailedDocumentTypeDef
```




Optional fields:
- `Id`: `str`
- `ErrorCode`: `ErrorCode`
- `ErrorMessage`: `str`


## BatchPutDocumentResponseTypeDef

```python
from mypy_boto3_kendra.type_defs import BatchPutDocumentResponseTypeDef
```




Optional fields:
- `FailedDocuments`: `List["BatchPutDocumentResponseFailedDocumentTypeDef"]`


## CapacityUnitsConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import CapacityUnitsConfigurationTypeDef
```


Required fields:
- `StorageCapacityUnits`: `int`
- `QueryCapacityUnits`: `int`




## ClickFeedbackTypeDef

```python
from mypy_boto3_kendra.type_defs import ClickFeedbackTypeDef
```


Required fields:
- `ResultId`: `str`
- `ClickTime`: `datetime`




## ColumnConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import ColumnConfigurationTypeDef
```


Required fields:
- `DocumentIdColumnName`: `str`
- `DocumentDataColumnName`: `str`
- `ChangeDetectingColumns`: `List[str]`



Optional fields:
- `DocumentTitleColumnName`: `str`
- `FieldMappings`: `List["DataSourceToIndexFieldMappingTypeDef"]`


## ConfluenceAttachmentConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import ConfluenceAttachmentConfigurationTypeDef
```




Optional fields:
- `CrawlAttachments`: `bool`
- `AttachmentFieldMappings`: `List["ConfluenceAttachmentToIndexFieldMappingTypeDef"]`


## ConfluenceAttachmentToIndexFieldMappingTypeDef

```python
from mypy_boto3_kendra.type_defs import ConfluenceAttachmentToIndexFieldMappingTypeDef
```




Optional fields:
- `DataSourceFieldName`: `ConfluenceAttachmentFieldName`
- `DateFieldFormat`: `str`
- `IndexFieldName`: `str`


## ConfluenceBlogConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import ConfluenceBlogConfigurationTypeDef
```




Optional fields:
- `BlogFieldMappings`: `List["ConfluenceBlogToIndexFieldMappingTypeDef"]`


## ConfluenceBlogToIndexFieldMappingTypeDef

```python
from mypy_boto3_kendra.type_defs import ConfluenceBlogToIndexFieldMappingTypeDef
```




Optional fields:
- `DataSourceFieldName`: `ConfluenceBlogFieldName`
- `DateFieldFormat`: `str`
- `IndexFieldName`: `str`


## ConfluenceConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import ConfluenceConfigurationTypeDef
```


Required fields:
- `ServerUrl`: `str`
- `SecretArn`: `str`
- `Version`: `ConfluenceVersion`



Optional fields:
- `SpaceConfiguration`: `"ConfluenceSpaceConfigurationTypeDef"`
- `PageConfiguration`: `"ConfluencePageConfigurationTypeDef"`
- `BlogConfiguration`: `"ConfluenceBlogConfigurationTypeDef"`
- `AttachmentConfiguration`: `"ConfluenceAttachmentConfigurationTypeDef"`
- `VpcConfiguration`: `"DataSourceVpcConfigurationTypeDef"`
- `InclusionPatterns`: `List[str]`
- `ExclusionPatterns`: `List[str]`


## ConfluencePageConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import ConfluencePageConfigurationTypeDef
```




Optional fields:
- `PageFieldMappings`: `List["ConfluencePageToIndexFieldMappingTypeDef"]`


## ConfluencePageToIndexFieldMappingTypeDef

```python
from mypy_boto3_kendra.type_defs import ConfluencePageToIndexFieldMappingTypeDef
```




Optional fields:
- `DataSourceFieldName`: `ConfluencePageFieldName`
- `DateFieldFormat`: `str`
- `IndexFieldName`: `str`


## ConfluenceSpaceConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import ConfluenceSpaceConfigurationTypeDef
```




Optional fields:
- `CrawlPersonalSpaces`: `bool`
- `CrawlArchivedSpaces`: `bool`
- `IncludeSpaces`: `List[str]`
- `ExcludeSpaces`: `List[str]`
- `SpaceFieldMappings`: `List["ConfluenceSpaceToIndexFieldMappingTypeDef"]`


## ConfluenceSpaceToIndexFieldMappingTypeDef

```python
from mypy_boto3_kendra.type_defs import ConfluenceSpaceToIndexFieldMappingTypeDef
```




Optional fields:
- `DataSourceFieldName`: `ConfluenceSpaceFieldName`
- `DateFieldFormat`: `str`
- `IndexFieldName`: `str`


## ConnectionConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import ConnectionConfigurationTypeDef
```


Required fields:
- `DatabaseHost`: `str`
- `DatabasePort`: `int`
- `DatabaseName`: `str`
- `TableName`: `str`
- `SecretArn`: `str`




## CreateDataSourceResponseTypeDef

```python
from mypy_boto3_kendra.type_defs import CreateDataSourceResponseTypeDef
```


Required fields:
- `Id`: `str`




## CreateFaqResponseTypeDef

```python
from mypy_boto3_kendra.type_defs import CreateFaqResponseTypeDef
```




Optional fields:
- `Id`: `str`


## CreateIndexResponseTypeDef

```python
from mypy_boto3_kendra.type_defs import CreateIndexResponseTypeDef
```




Optional fields:
- `Id`: `str`


## CreateThesaurusResponseTypeDef

```python
from mypy_boto3_kendra.type_defs import CreateThesaurusResponseTypeDef
```




Optional fields:
- `Id`: `str`


## DataSourceConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import DataSourceConfigurationTypeDef
```




Optional fields:
- `S3Configuration`: `"S3DataSourceConfigurationTypeDef"`
- `SharePointConfiguration`: `"SharePointConfigurationTypeDef"`
- `DatabaseConfiguration`: `"DatabaseConfigurationTypeDef"`
- `SalesforceConfiguration`: `"SalesforceConfigurationTypeDef"`
- `OneDriveConfiguration`: `"OneDriveConfigurationTypeDef"`
- `ServiceNowConfiguration`: `"ServiceNowConfigurationTypeDef"`
- `ConfluenceConfiguration`: `"ConfluenceConfigurationTypeDef"`
- `GoogleDriveConfiguration`: `"GoogleDriveConfigurationTypeDef"`


## DataSourceSummaryTypeDef

```python
from mypy_boto3_kendra.type_defs import DataSourceSummaryTypeDef
```




Optional fields:
- `Name`: `str`
- `Id`: `str`
- `Type`: `DataSourceType`
- `CreatedAt`: `datetime`
- `UpdatedAt`: `datetime`
- `Status`: `DataSourceStatus`


## DataSourceSyncJobMetricTargetTypeDef

```python
from mypy_boto3_kendra.type_defs import DataSourceSyncJobMetricTargetTypeDef
```


Required fields:
- `DataSourceId`: `str`
- `DataSourceSyncJobId`: `str`




## DataSourceSyncJobMetricsTypeDef

```python
from mypy_boto3_kendra.type_defs import DataSourceSyncJobMetricsTypeDef
```




Optional fields:
- `DocumentsAdded`: `str`
- `DocumentsModified`: `str`
- `DocumentsDeleted`: `str`
- `DocumentsFailed`: `str`
- `DocumentsScanned`: `str`


## DataSourceSyncJobTypeDef

```python
from mypy_boto3_kendra.type_defs import DataSourceSyncJobTypeDef
```




Optional fields:
- `ExecutionId`: `str`
- `StartTime`: `datetime`
- `EndTime`: `datetime`
- `Status`: `DataSourceSyncJobStatus`
- `ErrorMessage`: `str`
- `ErrorCode`: `ErrorCode`
- `DataSourceErrorCode`: `str`
- `Metrics`: `"DataSourceSyncJobMetricsTypeDef"`


## DataSourceToIndexFieldMappingTypeDef

```python
from mypy_boto3_kendra.type_defs import DataSourceToIndexFieldMappingTypeDef
```


Required fields:
- `DataSourceFieldName`: `str`
- `IndexFieldName`: `str`



Optional fields:
- `DateFieldFormat`: `str`


## DataSourceVpcConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import DataSourceVpcConfigurationTypeDef
```


Required fields:
- `SubnetIds`: `List[str]`
- `SecurityGroupIds`: `List[str]`




## DatabaseConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import DatabaseConfigurationTypeDef
```


Required fields:
- `DatabaseEngineType`: `DatabaseEngineType`
- `ConnectionConfiguration`: `"ConnectionConfigurationTypeDef"`
- `ColumnConfiguration`: `"ColumnConfigurationTypeDef"`



Optional fields:
- `VpcConfiguration`: `"DataSourceVpcConfigurationTypeDef"`
- `AclConfiguration`: `"AclConfigurationTypeDef"`
- `SqlConfiguration`: `"SqlConfigurationTypeDef"`


## DescribeDataSourceResponseTypeDef

```python
from mypy_boto3_kendra.type_defs import DescribeDataSourceResponseTypeDef
```




Optional fields:
- `Id`: `str`
- `IndexId`: `str`
- `Name`: `str`
- `Type`: `DataSourceType`
- `Configuration`: `"DataSourceConfigurationTypeDef"`
- `CreatedAt`: `datetime`
- `UpdatedAt`: `datetime`
- `Description`: `str`
- `Status`: `DataSourceStatus`
- `Schedule`: `str`
- `RoleArn`: `str`
- `ErrorMessage`: `str`


## DescribeFaqResponseTypeDef

```python
from mypy_boto3_kendra.type_defs import DescribeFaqResponseTypeDef
```




Optional fields:
- `Id`: `str`
- `IndexId`: `str`
- `Name`: `str`
- `Description`: `str`
- `CreatedAt`: `datetime`
- `UpdatedAt`: `datetime`
- `S3Path`: `"S3PathTypeDef"`
- `Status`: `FaqStatus`
- `RoleArn`: `str`
- `ErrorMessage`: `str`
- `FileFormat`: `FaqFileFormat`


## DescribeIndexResponseTypeDef

```python
from mypy_boto3_kendra.type_defs import DescribeIndexResponseTypeDef
```




Optional fields:
- `Name`: `str`
- `Id`: `str`
- `Edition`: `IndexEdition`
- `RoleArn`: `str`
- `ServerSideEncryptionConfiguration`: `"ServerSideEncryptionConfigurationTypeDef"`
- `Status`: `IndexStatus`
- `Description`: `str`
- `CreatedAt`: `datetime`
- `UpdatedAt`: `datetime`
- `DocumentMetadataConfigurations`: `List["DocumentMetadataConfigurationTypeDef"]`
- `IndexStatistics`: `"IndexStatisticsTypeDef"`
- `ErrorMessage`: `str`
- `CapacityUnits`: `"CapacityUnitsConfigurationTypeDef"`
- `UserTokenConfigurations`: `List["UserTokenConfigurationTypeDef"]`
- `UserContextPolicy`: `UserContextPolicy`


## DescribeThesaurusResponseTypeDef

```python
from mypy_boto3_kendra.type_defs import DescribeThesaurusResponseTypeDef
```




Optional fields:
- `Id`: `str`
- `IndexId`: `str`
- `Name`: `str`
- `Description`: `str`
- `Status`: `ThesaurusStatus`
- `ErrorMessage`: `str`
- `CreatedAt`: `datetime`
- `UpdatedAt`: `datetime`
- `RoleArn`: `str`
- `SourceS3Path`: `"S3PathTypeDef"`
- `FileSizeBytes`: `int`
- `TermCount`: `int`
- `SynonymRuleCount`: `int`


## DocumentAttributeTypeDef

```python
from mypy_boto3_kendra.type_defs import DocumentAttributeTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `"DocumentAttributeValueTypeDef"`




## DocumentAttributeValueCountPairTypeDef

```python
from mypy_boto3_kendra.type_defs import DocumentAttributeValueCountPairTypeDef
```




Optional fields:
- `DocumentAttributeValue`: `"DocumentAttributeValueTypeDef"`
- `Count`: `int`


## DocumentAttributeValueTypeDef

```python
from mypy_boto3_kendra.type_defs import DocumentAttributeValueTypeDef
```




Optional fields:
- `StringValue`: `str`
- `StringListValue`: `List[str]`
- `LongValue`: `int`
- `DateValue`: `datetime`


## DocumentMetadataConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import DocumentMetadataConfigurationTypeDef
```


Required fields:
- `Name`: `str`
- `Type`: `DocumentAttributeValueType`



Optional fields:
- `Relevance`: `"RelevanceTypeDef"`
- `Search`: `"SearchTypeDef"`


## DocumentRelevanceConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import DocumentRelevanceConfigurationTypeDef
```


Required fields:
- `Name`: `str`
- `Relevance`: `"RelevanceTypeDef"`




## DocumentTypeDef

```python
from mypy_boto3_kendra.type_defs import DocumentTypeDef
```


Required fields:
- `Id`: `str`



Optional fields:
- `Title`: `str`
- `Blob`: `Union[bytes, IO[bytes]]`
- `S3Path`: `"S3PathTypeDef"`
- `Attributes`: `List["DocumentAttributeTypeDef"]`
- `AccessControlList`: `List["PrincipalTypeDef"]`
- `ContentType`: `ContentType`


## DocumentsMetadataConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import DocumentsMetadataConfigurationTypeDef
```




Optional fields:
- `S3Prefix`: `str`


## FacetResultTypeDef

```python
from mypy_boto3_kendra.type_defs import FacetResultTypeDef
```




Optional fields:
- `DocumentAttributeKey`: `str`
- `DocumentAttributeValueType`: `DocumentAttributeValueType`
- `DocumentAttributeValueCountPairs`: `List["DocumentAttributeValueCountPairTypeDef"]`


## FacetTypeDef

```python
from mypy_boto3_kendra.type_defs import FacetTypeDef
```




Optional fields:
- `DocumentAttributeKey`: `str`


## FaqStatisticsTypeDef

```python
from mypy_boto3_kendra.type_defs import FaqStatisticsTypeDef
```


Required fields:
- `IndexedQuestionAnswersCount`: `int`




## FaqSummaryTypeDef

```python
from mypy_boto3_kendra.type_defs import FaqSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `Status`: `FaqStatus`
- `CreatedAt`: `datetime`
- `UpdatedAt`: `datetime`
- `FileFormat`: `FaqFileFormat`


## GoogleDriveConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import GoogleDriveConfigurationTypeDef
```


Required fields:
- `SecretArn`: `str`



Optional fields:
- `InclusionPatterns`: `List[str]`
- `ExclusionPatterns`: `List[str]`
- `FieldMappings`: `List["DataSourceToIndexFieldMappingTypeDef"]`
- `ExcludeMimeTypes`: `List[str]`
- `ExcludeUserAccounts`: `List[str]`
- `ExcludeSharedDrives`: `List[str]`


## HighlightTypeDef

```python
from mypy_boto3_kendra.type_defs import HighlightTypeDef
```


Required fields:
- `BeginOffset`: `int`
- `EndOffset`: `int`



Optional fields:
- `TopAnswer`: `bool`
- `Type`: `HighlightType`


## IndexConfigurationSummaryTypeDef

```python
from mypy_boto3_kendra.type_defs import IndexConfigurationSummaryTypeDef
```


Required fields:
- `CreatedAt`: `datetime`
- `UpdatedAt`: `datetime`
- `Status`: `IndexStatus`



Optional fields:
- `Name`: `str`
- `Id`: `str`
- `Edition`: `IndexEdition`


## IndexStatisticsTypeDef

```python
from mypy_boto3_kendra.type_defs import IndexStatisticsTypeDef
```


Required fields:
- `FaqStatistics`: `"FaqStatisticsTypeDef"`
- `TextDocumentStatistics`: `"TextDocumentStatisticsTypeDef"`




## JsonTokenTypeConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import JsonTokenTypeConfigurationTypeDef
```


Required fields:
- `UserNameAttributeField`: `str`
- `GroupAttributeField`: `str`




## JwtTokenTypeConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import JwtTokenTypeConfigurationTypeDef
```


Required fields:
- `KeyLocation`: `KeyLocation`



Optional fields:
- `URL`: `str`
- `SecretManagerArn`: `str`
- `UserNameAttributeField`: `str`
- `GroupAttributeField`: `str`
- `Issuer`: `str`
- `ClaimRegex`: `str`


## ListDataSourceSyncJobsResponseTypeDef

```python
from mypy_boto3_kendra.type_defs import ListDataSourceSyncJobsResponseTypeDef
```




Optional fields:
- `History`: `List["DataSourceSyncJobTypeDef"]`
- `NextToken`: `str`


## ListDataSourcesResponseTypeDef

```python
from mypy_boto3_kendra.type_defs import ListDataSourcesResponseTypeDef
```




Optional fields:
- `SummaryItems`: `List["DataSourceSummaryTypeDef"]`
- `NextToken`: `str`


## ListFaqsResponseTypeDef

```python
from mypy_boto3_kendra.type_defs import ListFaqsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `FaqSummaryItems`: `List["FaqSummaryTypeDef"]`


## ListIndicesResponseTypeDef

```python
from mypy_boto3_kendra.type_defs import ListIndicesResponseTypeDef
```




Optional fields:
- `IndexConfigurationSummaryItems`: `List["IndexConfigurationSummaryTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_kendra.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`


## ListThesauriResponseTypeDef

```python
from mypy_boto3_kendra.type_defs import ListThesauriResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `ThesaurusSummaryItems`: `List["ThesaurusSummaryTypeDef"]`


## OneDriveConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import OneDriveConfigurationTypeDef
```


Required fields:
- `TenantDomain`: `str`
- `SecretArn`: `str`
- `OneDriveUsers`: `"OneDriveUsersTypeDef"`



Optional fields:
- `InclusionPatterns`: `List[str]`
- `ExclusionPatterns`: `List[str]`
- `FieldMappings`: `List["DataSourceToIndexFieldMappingTypeDef"]`
- `DisableLocalGroups`: `bool`


## OneDriveUsersTypeDef

```python
from mypy_boto3_kendra.type_defs import OneDriveUsersTypeDef
```




Optional fields:
- `OneDriveUserList`: `List[str]`
- `OneDriveUserS3Path`: `"S3PathTypeDef"`


## PrincipalTypeDef

```python
from mypy_boto3_kendra.type_defs import PrincipalTypeDef
```


Required fields:
- `Name`: `str`
- `Type`: `PrincipalType`
- `Access`: `ReadAccessType`




## QueryResultItemTypeDef

```python
from mypy_boto3_kendra.type_defs import QueryResultItemTypeDef
```




Optional fields:
- `Id`: `str`
- `Type`: `QueryResultType`
- `AdditionalAttributes`: `List["AdditionalResultAttributeTypeDef"]`
- `DocumentId`: `str`
- `DocumentTitle`: `"TextWithHighlightsTypeDef"`
- `DocumentExcerpt`: `"TextWithHighlightsTypeDef"`
- `DocumentURI`: `str`
- `DocumentAttributes`: `List["DocumentAttributeTypeDef"]`
- `ScoreAttributes`: `"ScoreAttributesTypeDef"`
- `FeedbackToken`: `str`


## QueryResultTypeDef

```python
from mypy_boto3_kendra.type_defs import QueryResultTypeDef
```




Optional fields:
- `QueryId`: `str`
- `ResultItems`: `List["QueryResultItemTypeDef"]`
- `FacetResults`: `List["FacetResultTypeDef"]`
- `TotalNumberOfResults`: `int`


## RelevanceFeedbackTypeDef

```python
from mypy_boto3_kendra.type_defs import RelevanceFeedbackTypeDef
```


Required fields:
- `ResultId`: `str`
- `RelevanceValue`: `RelevanceType`




## RelevanceTypeDef

```python
from mypy_boto3_kendra.type_defs import RelevanceTypeDef
```




Optional fields:
- `Freshness`: `bool`
- `Importance`: `int`
- `Duration`: `str`
- `RankOrder`: `Order`
- `ValueImportanceMap`: `Dict[str, int]`


## S3DataSourceConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import S3DataSourceConfigurationTypeDef
```


Required fields:
- `BucketName`: `str`



Optional fields:
- `InclusionPrefixes`: `List[str]`
- `InclusionPatterns`: `List[str]`
- `ExclusionPatterns`: `List[str]`
- `DocumentsMetadataConfiguration`: `"DocumentsMetadataConfigurationTypeDef"`
- `AccessControlListConfiguration`: `"AccessControlListConfigurationTypeDef"`


## S3PathTypeDef

```python
from mypy_boto3_kendra.type_defs import S3PathTypeDef
```


Required fields:
- `Bucket`: `str`
- `Key`: `str`




## SalesforceChatterFeedConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import SalesforceChatterFeedConfigurationTypeDef
```


Required fields:
- `DocumentDataFieldName`: `str`



Optional fields:
- `DocumentTitleFieldName`: `str`
- `FieldMappings`: `List["DataSourceToIndexFieldMappingTypeDef"]`
- `IncludeFilterTypes`: `List[SalesforceChatterFeedIncludeFilterType]`


## SalesforceConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import SalesforceConfigurationTypeDef
```


Required fields:
- `ServerUrl`: `str`
- `SecretArn`: `str`



Optional fields:
- `StandardObjectConfigurations`: `List["SalesforceStandardObjectConfigurationTypeDef"]`
- `KnowledgeArticleConfiguration`: `"SalesforceKnowledgeArticleConfigurationTypeDef"`
- `ChatterFeedConfiguration`: `"SalesforceChatterFeedConfigurationTypeDef"`
- `CrawlAttachments`: `bool`
- `StandardObjectAttachmentConfiguration`: `"SalesforceStandardObjectAttachmentConfigurationTypeDef"`
- `IncludeAttachmentFilePatterns`: `List[str]`
- `ExcludeAttachmentFilePatterns`: `List[str]`


## SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef
```


Required fields:
- `Name`: `str`
- `DocumentDataFieldName`: `str`



Optional fields:
- `DocumentTitleFieldName`: `str`
- `FieldMappings`: `List["DataSourceToIndexFieldMappingTypeDef"]`


## SalesforceKnowledgeArticleConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import SalesforceKnowledgeArticleConfigurationTypeDef
```


Required fields:
- `IncludedStates`: `List[SalesforceKnowledgeArticleState]`



Optional fields:
- `StandardKnowledgeArticleTypeConfiguration`: `"SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef"`
- `CustomKnowledgeArticleTypeConfigurations`: `List["SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef"]`


## SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef
```


Required fields:
- `DocumentDataFieldName`: `str`



Optional fields:
- `DocumentTitleFieldName`: `str`
- `FieldMappings`: `List["DataSourceToIndexFieldMappingTypeDef"]`


## SalesforceStandardObjectAttachmentConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import SalesforceStandardObjectAttachmentConfigurationTypeDef
```




Optional fields:
- `DocumentTitleFieldName`: `str`
- `FieldMappings`: `List["DataSourceToIndexFieldMappingTypeDef"]`


## SalesforceStandardObjectConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import SalesforceStandardObjectConfigurationTypeDef
```


Required fields:
- `Name`: `SalesforceStandardObjectName`
- `DocumentDataFieldName`: `str`



Optional fields:
- `DocumentTitleFieldName`: `str`
- `FieldMappings`: `List["DataSourceToIndexFieldMappingTypeDef"]`


## ScoreAttributesTypeDef

```python
from mypy_boto3_kendra.type_defs import ScoreAttributesTypeDef
```




Optional fields:
- `ScoreConfidence`: `ScoreConfidence`


## SearchTypeDef

```python
from mypy_boto3_kendra.type_defs import SearchTypeDef
```




Optional fields:
- `Facetable`: `bool`
- `Searchable`: `bool`
- `Displayable`: `bool`
- `Sortable`: `bool`


## ServerSideEncryptionConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import ServerSideEncryptionConfigurationTypeDef
```




Optional fields:
- `KmsKeyId`: `str`


## ServiceNowConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import ServiceNowConfigurationTypeDef
```


Required fields:
- `HostUrl`: `str`
- `SecretArn`: `str`
- `ServiceNowBuildVersion`: `ServiceNowBuildVersionType`



Optional fields:
- `KnowledgeArticleConfiguration`: `"ServiceNowKnowledgeArticleConfigurationTypeDef"`
- `ServiceCatalogConfiguration`: `"ServiceNowServiceCatalogConfigurationTypeDef"`
- `AuthenticationType`: `ServiceNowAuthenticationType`


## ServiceNowKnowledgeArticleConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import ServiceNowKnowledgeArticleConfigurationTypeDef
```


Required fields:
- `DocumentDataFieldName`: `str`



Optional fields:
- `CrawlAttachments`: `bool`
- `IncludeAttachmentFilePatterns`: `List[str]`
- `ExcludeAttachmentFilePatterns`: `List[str]`
- `DocumentTitleFieldName`: `str`
- `FieldMappings`: `List["DataSourceToIndexFieldMappingTypeDef"]`
- `FilterQuery`: `str`


## ServiceNowServiceCatalogConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import ServiceNowServiceCatalogConfigurationTypeDef
```


Required fields:
- `DocumentDataFieldName`: `str`



Optional fields:
- `CrawlAttachments`: `bool`
- `IncludeAttachmentFilePatterns`: `List[str]`
- `ExcludeAttachmentFilePatterns`: `List[str]`
- `DocumentTitleFieldName`: `str`
- `FieldMappings`: `List["DataSourceToIndexFieldMappingTypeDef"]`


## SharePointConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import SharePointConfigurationTypeDef
```


Required fields:
- `SharePointVersion`: `Literal['SHAREPOINT_ONLINE']`
- `Urls`: `List[str]`
- `SecretArn`: `str`



Optional fields:
- `CrawlAttachments`: `bool`
- `UseChangeLog`: `bool`
- `InclusionPatterns`: `List[str]`
- `ExclusionPatterns`: `List[str]`
- `VpcConfiguration`: `"DataSourceVpcConfigurationTypeDef"`
- `FieldMappings`: `List["DataSourceToIndexFieldMappingTypeDef"]`
- `DocumentTitleFieldName`: `str`
- `DisableLocalGroups`: `bool`


## SortingConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import SortingConfigurationTypeDef
```


Required fields:
- `DocumentAttributeKey`: `str`
- `SortOrder`: `SortOrder`




## SqlConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import SqlConfigurationTypeDef
```




Optional fields:
- `QueryIdentifiersEnclosingOption`: `QueryIdentifiersEnclosingOption`


## StartDataSourceSyncJobResponseTypeDef

```python
from mypy_boto3_kendra.type_defs import StartDataSourceSyncJobResponseTypeDef
```




Optional fields:
- `ExecutionId`: `str`


## TagTypeDef

```python
from mypy_boto3_kendra.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## TextDocumentStatisticsTypeDef

```python
from mypy_boto3_kendra.type_defs import TextDocumentStatisticsTypeDef
```


Required fields:
- `IndexedTextDocumentsCount`: `int`
- `IndexedTextBytes`: `int`




## TextWithHighlightsTypeDef

```python
from mypy_boto3_kendra.type_defs import TextWithHighlightsTypeDef
```




Optional fields:
- `Text`: `str`
- `Highlights`: `List["HighlightTypeDef"]`


## ThesaurusSummaryTypeDef

```python
from mypy_boto3_kendra.type_defs import ThesaurusSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `Status`: `ThesaurusStatus`
- `CreatedAt`: `datetime`
- `UpdatedAt`: `datetime`


## TimeRangeTypeDef

```python
from mypy_boto3_kendra.type_defs import TimeRangeTypeDef
```




Optional fields:
- `StartTime`: `datetime`
- `EndTime`: `datetime`


## UserContextTypeDef

```python
from mypy_boto3_kendra.type_defs import UserContextTypeDef
```




Optional fields:
- `Token`: `str`


## UserTokenConfigurationTypeDef

```python
from mypy_boto3_kendra.type_defs import UserTokenConfigurationTypeDef
```




Optional fields:
- `JwtTokenTypeConfiguration`: `"JwtTokenTypeConfigurationTypeDef"`
- `JsonTokenTypeConfiguration`: `"JsonTokenTypeConfigurationTypeDef"`

