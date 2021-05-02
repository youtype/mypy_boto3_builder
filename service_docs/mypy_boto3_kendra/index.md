# Type annotations for boto3 Kendra module

> [Index](../index.md) > Kendra

Auto-generated documentation for [Kendra](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra)
type annotations stubs module [mypy_boto3_kendra](https://pypi.org/project/mypy-boto3-kendra/).

```bash
pip install mypy-boto3-kendra
```

- [Type annotations for boto3 Kendra module](#type-annotations-for-boto3-kendra-module)
  - [KendraClient](#kendraclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## KendraClient

Type annotations for  `boto3.client("kendra")` as [KendraClient](./client.md)

Can be used directly:

```python
from mypy_boto3_kendra.client import KendraClient
```


KendraClient [exceptions](./client.md#exceptions)



### Methods
- [batch_delete_document](./client.md#batch-delete-document)
- [batch_put_document](./client.md#batch-put-document)
- [can_paginate](./client.md#can-paginate)
- [create_data_source](./client.md#create-data-source)
- [create_faq](./client.md#create-faq)
- [create_index](./client.md#create-index)
- [create_thesaurus](./client.md#create-thesaurus)
- [delete_data_source](./client.md#delete-data-source)
- [delete_faq](./client.md#delete-faq)
- [delete_index](./client.md#delete-index)
- [delete_thesaurus](./client.md#delete-thesaurus)
- [describe_data_source](./client.md#describe-data-source)
- [describe_faq](./client.md#describe-faq)
- [describe_index](./client.md#describe-index)
- [describe_thesaurus](./client.md#describe-thesaurus)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [list_data_source_sync_jobs](./client.md#list-data-source-sync-jobs)
- [list_data_sources](./client.md#list-data-sources)
- [list_faqs](./client.md#list-faqs)
- [list_indices](./client.md#list-indices)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_thesauri](./client.md#list-thesauri)
- [query](./client.md#query)
- [start_data_source_sync_job](./client.md#start-data-source-sync-job)
- [stop_data_source_sync_job](./client.md#stop-data-source-sync-job)
- [submit_feedback](./client.md#submit-feedback)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_data_source](./client.md#update-data-source)
- [update_index](./client.md#update-index)
- [update_thesaurus](./client.md#update-thesaurus)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceAlreadyExistException](./client.md#resourcealreadyexistexception)
- [ResourceInUseException](./client.md#resourceinuseexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ResourceUnavailableException](./client.md#resourceunavailableexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [ThrottlingException](./client.md#throttlingexception)
- [ValidationException](./client.md#validationexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_kendra.literals import AdditionalResultAttributeValueType, ...
```

- [AdditionalResultAttributeValueType](./literals.md#additionalresultattributevaluetype)
- [ConfluenceAttachmentFieldName](./literals.md#confluenceattachmentfieldname)
- [ConfluenceBlogFieldName](./literals.md#confluenceblogfieldname)
- [ConfluencePageFieldName](./literals.md#confluencepagefieldname)
- [ConfluenceSpaceFieldName](./literals.md#confluencespacefieldname)
- [ConfluenceVersion](./literals.md#confluenceversion)
- [ContentType](./literals.md#contenttype)
- [DataSourceStatus](./literals.md#datasourcestatus)
- [DataSourceSyncJobStatus](./literals.md#datasourcesyncjobstatus)
- [DataSourceType](./literals.md#datasourcetype)
- [DatabaseEngineType](./literals.md#databaseenginetype)
- [DocumentAttributeValueType](./literals.md#documentattributevaluetype)
- [ErrorCode](./literals.md#errorcode)
- [FaqFileFormat](./literals.md#faqfileformat)
- [FaqStatus](./literals.md#faqstatus)
- [HighlightType](./literals.md#highlighttype)
- [IndexEdition](./literals.md#indexedition)
- [IndexStatus](./literals.md#indexstatus)
- [KeyLocation](./literals.md#keylocation)
- [Order](./literals.md#order)
- [PrincipalType](./literals.md#principaltype)
- [QueryIdentifiersEnclosingOption](./literals.md#queryidentifiersenclosingoption)
- [QueryResultType](./literals.md#queryresulttype)
- [ReadAccessType](./literals.md#readaccesstype)
- [RelevanceType](./literals.md#relevancetype)
- [SalesforceChatterFeedIncludeFilterType](./literals.md#salesforcechatterfeedincludefiltertype)
- [SalesforceKnowledgeArticleState](./literals.md#salesforceknowledgearticlestate)
- [SalesforceStandardObjectName](./literals.md#salesforcestandardobjectname)
- [ScoreConfidence](./literals.md#scoreconfidence)
- [ServiceNowAuthenticationType](./literals.md#servicenowauthenticationtype)
- [ServiceNowBuildVersionType](./literals.md#servicenowbuildversiontype)
- [SharePointVersion](./literals.md#sharepointversion)
- [SortOrder](./literals.md#sortorder)
- [ThesaurusStatus](./literals.md#thesaurusstatus)
- [UserContextPolicy](./literals.md#usercontextpolicy)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_kendra.type_defs import AccessControlListConfigurationTypeDef, ...
```

- [AccessControlListConfigurationTypeDef](./type_defs.md#accesscontrollistconfigurationtypedef)
- [AclConfigurationTypeDef](./type_defs.md#aclconfigurationtypedef)
- [AdditionalResultAttributeTypeDef](./type_defs.md#additionalresultattributetypedef)
- [AdditionalResultAttributeValueTypeDef](./type_defs.md#additionalresultattributevaluetypedef)
- [BatchDeleteDocumentResponseFailedDocumentTypeDef](./type_defs.md#batchdeletedocumentresponsefaileddocumenttypedef)
- [BatchPutDocumentResponseFailedDocumentTypeDef](./type_defs.md#batchputdocumentresponsefaileddocumenttypedef)
- [CapacityUnitsConfigurationTypeDef](./type_defs.md#capacityunitsconfigurationtypedef)
- [ColumnConfigurationTypeDef](./type_defs.md#columnconfigurationtypedef)
- [ConfluenceAttachmentConfigurationTypeDef](./type_defs.md#confluenceattachmentconfigurationtypedef)
- [ConfluenceAttachmentToIndexFieldMappingTypeDef](./type_defs.md#confluenceattachmenttoindexfieldmappingtypedef)
- [ConfluenceBlogConfigurationTypeDef](./type_defs.md#confluenceblogconfigurationtypedef)
- [ConfluenceBlogToIndexFieldMappingTypeDef](./type_defs.md#confluenceblogtoindexfieldmappingtypedef)
- [ConfluenceConfigurationTypeDef](./type_defs.md#confluenceconfigurationtypedef)
- [ConfluencePageConfigurationTypeDef](./type_defs.md#confluencepageconfigurationtypedef)
- [ConfluencePageToIndexFieldMappingTypeDef](./type_defs.md#confluencepagetoindexfieldmappingtypedef)
- [ConfluenceSpaceConfigurationTypeDef](./type_defs.md#confluencespaceconfigurationtypedef)
- [ConfluenceSpaceToIndexFieldMappingTypeDef](./type_defs.md#confluencespacetoindexfieldmappingtypedef)
- [ConnectionConfigurationTypeDef](./type_defs.md#connectionconfigurationtypedef)
- [DataSourceConfigurationTypeDef](./type_defs.md#datasourceconfigurationtypedef)
- [DataSourceSummaryTypeDef](./type_defs.md#datasourcesummarytypedef)
- [DataSourceSyncJobMetricsTypeDef](./type_defs.md#datasourcesyncjobmetricstypedef)
- [DataSourceSyncJobTypeDef](./type_defs.md#datasourcesyncjobtypedef)
- [DataSourceToIndexFieldMappingTypeDef](./type_defs.md#datasourcetoindexfieldmappingtypedef)
- [DataSourceVpcConfigurationTypeDef](./type_defs.md#datasourcevpcconfigurationtypedef)
- [DatabaseConfigurationTypeDef](./type_defs.md#databaseconfigurationtypedef)
- [DocumentAttributeTypeDef](./type_defs.md#documentattributetypedef)
- [DocumentAttributeValueCountPairTypeDef](./type_defs.md#documentattributevaluecountpairtypedef)
- [DocumentAttributeValueTypeDef](./type_defs.md#documentattributevaluetypedef)
- [DocumentMetadataConfigurationTypeDef](./type_defs.md#documentmetadataconfigurationtypedef)
- [DocumentsMetadataConfigurationTypeDef](./type_defs.md#documentsmetadataconfigurationtypedef)
- [FacetResultTypeDef](./type_defs.md#facetresulttypedef)
- [FaqStatisticsTypeDef](./type_defs.md#faqstatisticstypedef)
- [FaqSummaryTypeDef](./type_defs.md#faqsummarytypedef)
- [GoogleDriveConfigurationTypeDef](./type_defs.md#googledriveconfigurationtypedef)
- [HighlightTypeDef](./type_defs.md#highlighttypedef)
- [IndexConfigurationSummaryTypeDef](./type_defs.md#indexconfigurationsummarytypedef)
- [IndexStatisticsTypeDef](./type_defs.md#indexstatisticstypedef)
- [JsonTokenTypeConfigurationTypeDef](./type_defs.md#jsontokentypeconfigurationtypedef)
- [JwtTokenTypeConfigurationTypeDef](./type_defs.md#jwttokentypeconfigurationtypedef)
- [OneDriveConfigurationTypeDef](./type_defs.md#onedriveconfigurationtypedef)
- [OneDriveUsersTypeDef](./type_defs.md#onedriveuserstypedef)
- [PrincipalTypeDef](./type_defs.md#principaltypedef)
- [QueryResultItemTypeDef](./type_defs.md#queryresultitemtypedef)
- [RelevanceTypeDef](./type_defs.md#relevancetypedef)
- [S3DataSourceConfigurationTypeDef](./type_defs.md#s3datasourceconfigurationtypedef)
- [S3PathTypeDef](./type_defs.md#s3pathtypedef)
- [SalesforceChatterFeedConfigurationTypeDef](./type_defs.md#salesforcechatterfeedconfigurationtypedef)
- [SalesforceConfigurationTypeDef](./type_defs.md#salesforceconfigurationtypedef)
- [SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef](./type_defs.md#salesforcecustomknowledgearticletypeconfigurationtypedef)
- [SalesforceKnowledgeArticleConfigurationTypeDef](./type_defs.md#salesforceknowledgearticleconfigurationtypedef)
- [SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef](./type_defs.md#salesforcestandardknowledgearticletypeconfigurationtypedef)
- [SalesforceStandardObjectAttachmentConfigurationTypeDef](./type_defs.md#salesforcestandardobjectattachmentconfigurationtypedef)
- [SalesforceStandardObjectConfigurationTypeDef](./type_defs.md#salesforcestandardobjectconfigurationtypedef)
- [ScoreAttributesTypeDef](./type_defs.md#scoreattributestypedef)
- [SearchTypeDef](./type_defs.md#searchtypedef)
- [ServerSideEncryptionConfigurationTypeDef](./type_defs.md#serversideencryptionconfigurationtypedef)
- [ServiceNowConfigurationTypeDef](./type_defs.md#servicenowconfigurationtypedef)
- [ServiceNowKnowledgeArticleConfigurationTypeDef](./type_defs.md#servicenowknowledgearticleconfigurationtypedef)
- [ServiceNowServiceCatalogConfigurationTypeDef](./type_defs.md#servicenowservicecatalogconfigurationtypedef)
- [SharePointConfigurationTypeDef](./type_defs.md#sharepointconfigurationtypedef)
- [SqlConfigurationTypeDef](./type_defs.md#sqlconfigurationtypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TextDocumentStatisticsTypeDef](./type_defs.md#textdocumentstatisticstypedef)
- [TextWithHighlightsTypeDef](./type_defs.md#textwithhighlightstypedef)
- [ThesaurusSummaryTypeDef](./type_defs.md#thesaurussummarytypedef)
- [UserTokenConfigurationTypeDef](./type_defs.md#usertokenconfigurationtypedef)
- [BatchDeleteDocumentResponseTypeDef](./type_defs.md#batchdeletedocumentresponsetypedef)
- [BatchPutDocumentResponseTypeDef](./type_defs.md#batchputdocumentresponsetypedef)
- [ClickFeedbackTypeDef](./type_defs.md#clickfeedbacktypedef)
- [CreateDataSourceResponseTypeDef](./type_defs.md#createdatasourceresponsetypedef)
- [CreateFaqResponseTypeDef](./type_defs.md#createfaqresponsetypedef)
- [CreateIndexResponseTypeDef](./type_defs.md#createindexresponsetypedef)
- [CreateThesaurusResponseTypeDef](./type_defs.md#createthesaurusresponsetypedef)
- [DataSourceSyncJobMetricTargetTypeDef](./type_defs.md#datasourcesyncjobmetrictargettypedef)
- [DescribeDataSourceResponseTypeDef](./type_defs.md#describedatasourceresponsetypedef)
- [DescribeFaqResponseTypeDef](./type_defs.md#describefaqresponsetypedef)
- [DescribeIndexResponseTypeDef](./type_defs.md#describeindexresponsetypedef)
- [DescribeThesaurusResponseTypeDef](./type_defs.md#describethesaurusresponsetypedef)
- [AttributeFilterTypeDef](./type_defs.md#attributefiltertypedef)
- [DocumentRelevanceConfigurationTypeDef](./type_defs.md#documentrelevanceconfigurationtypedef)
- [DocumentTypeDef](./type_defs.md#documenttypedef)
- [FacetTypeDef](./type_defs.md#facettypedef)
- [ListDataSourceSyncJobsResponseTypeDef](./type_defs.md#listdatasourcesyncjobsresponsetypedef)
- [ListDataSourcesResponseTypeDef](./type_defs.md#listdatasourcesresponsetypedef)
- [ListFaqsResponseTypeDef](./type_defs.md#listfaqsresponsetypedef)
- [ListIndicesResponseTypeDef](./type_defs.md#listindicesresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ListThesauriResponseTypeDef](./type_defs.md#listthesauriresponsetypedef)
- [QueryResultTypeDef](./type_defs.md#queryresulttypedef)
- [RelevanceFeedbackTypeDef](./type_defs.md#relevancefeedbacktypedef)
- [SortingConfigurationTypeDef](./type_defs.md#sortingconfigurationtypedef)
- [StartDataSourceSyncJobResponseTypeDef](./type_defs.md#startdatasourcesyncjobresponsetypedef)
- [TimeRangeTypeDef](./type_defs.md#timerangetypedef)
- [UserContextTypeDef](./type_defs.md#usercontexttypedef)
