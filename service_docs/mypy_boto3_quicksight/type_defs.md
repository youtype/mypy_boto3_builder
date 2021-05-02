# Structures for boto3 QuickSight module

> [Index](../index.md) > [QuickSight](./index.md) > Structures

Auto-generated documentation for [QuickSight](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight)
type annotations stubs module [mypy_boto3_quicksight](https://pypi.org/project/mypy-boto3-quicksight/).

- [Structures for boto3 QuickSight module](#structures-for-boto3-quicksight-module)
  - [AccountCustomizationTypeDef](#accountcustomizationtypedef)
  - [AccountSettingsTypeDef](#accountsettingstypedef)
  - [ActiveIAMPolicyAssignmentTypeDef](#activeiampolicyassignmenttypedef)
  - [AdHocFilteringOptionTypeDef](#adhocfilteringoptiontypedef)
  - [AmazonElasticsearchParametersTypeDef](#amazonelasticsearchparameterstypedef)
  - [AnalysisErrorTypeDef](#analysiserrortypedef)
  - [AnalysisSourceTemplateTypeDef](#analysissourcetemplatetypedef)
  - [AnalysisSummaryTypeDef](#analysissummarytypedef)
  - [AnalysisTypeDef](#analysistypedef)
  - [AthenaParametersTypeDef](#athenaparameterstypedef)
  - [AuroraParametersTypeDef](#auroraparameterstypedef)
  - [AuroraPostgreSqlParametersTypeDef](#aurorapostgresqlparameterstypedef)
  - [AwsIotAnalyticsParametersTypeDef](#awsiotanalyticsparameterstypedef)
  - [BorderStyleTypeDef](#borderstyletypedef)
  - [CalculatedColumnTypeDef](#calculatedcolumntypedef)
  - [CastColumnTypeOperationTypeDef](#castcolumntypeoperationtypedef)
  - [ColumnDescriptionTypeDef](#columndescriptiontypedef)
  - [ColumnGroupColumnSchemaTypeDef](#columngroupcolumnschematypedef)
  - [ColumnGroupSchemaTypeDef](#columngroupschematypedef)
  - [ColumnGroupTypeDef](#columngrouptypedef)
  - [ColumnLevelPermissionRuleTypeDef](#columnlevelpermissionruletypedef)
  - [ColumnSchemaTypeDef](#columnschematypedef)
  - [ColumnTagTypeDef](#columntagtypedef)
  - [CreateColumnsOperationTypeDef](#createcolumnsoperationtypedef)
  - [CredentialPairTypeDef](#credentialpairtypedef)
  - [CustomSqlTypeDef](#customsqltypedef)
  - [DashboardErrorTypeDef](#dashboarderrortypedef)
  - [DashboardSourceTemplateTypeDef](#dashboardsourcetemplatetypedef)
  - [DashboardSummaryTypeDef](#dashboardsummarytypedef)
  - [DashboardTypeDef](#dashboardtypedef)
  - [DashboardVersionSummaryTypeDef](#dashboardversionsummarytypedef)
  - [DashboardVersionTypeDef](#dashboardversiontypedef)
  - [DataColorPaletteTypeDef](#datacolorpalettetypedef)
  - [DataSetConfigurationTypeDef](#datasetconfigurationtypedef)
  - [DataSetReferenceTypeDef](#datasetreferencetypedef)
  - [DataSetSchemaTypeDef](#datasetschematypedef)
  - [DataSetSummaryTypeDef](#datasetsummarytypedef)
  - [DataSetTypeDef](#datasettypedef)
  - [DataSourceErrorInfoTypeDef](#datasourceerrorinfotypedef)
  - [DataSourceParametersTypeDef](#datasourceparameterstypedef)
  - [DataSourceTypeDef](#datasourcetypedef)
  - [DateTimeParameterTypeDef](#datetimeparametertypedef)
  - [DecimalParameterTypeDef](#decimalparametertypedef)
  - [ErrorInfoTypeDef](#errorinfotypedef)
  - [ExportToCSVOptionTypeDef](#exporttocsvoptiontypedef)
  - [FieldFolderTypeDef](#fieldfoldertypedef)
  - [FilterOperationTypeDef](#filteroperationtypedef)
  - [GeoSpatialColumnGroupTypeDef](#geospatialcolumngrouptypedef)
  - [GroupMemberTypeDef](#groupmembertypedef)
  - [GroupTypeDef](#grouptypedef)
  - [GutterStyleTypeDef](#gutterstyletypedef)
  - [IAMPolicyAssignmentSummaryTypeDef](#iampolicyassignmentsummarytypedef)
  - [IAMPolicyAssignmentTypeDef](#iampolicyassignmenttypedef)
  - [IngestionTypeDef](#ingestiontypedef)
  - [InputColumnTypeDef](#inputcolumntypedef)
  - [IntegerParameterTypeDef](#integerparametertypedef)
  - [JiraParametersTypeDef](#jiraparameterstypedef)
  - [JoinInstructionTypeDef](#joininstructiontypedef)
  - [JoinKeyPropertiesTypeDef](#joinkeypropertiestypedef)
  - [LogicalTableSourceTypeDef](#logicaltablesourcetypedef)
  - [LogicalTableTypeDef](#logicaltabletypedef)
  - [ManifestFileLocationTypeDef](#manifestfilelocationtypedef)
  - [MarginStyleTypeDef](#marginstyletypedef)
  - [MariaDbParametersTypeDef](#mariadbparameterstypedef)
  - [MySqlParametersTypeDef](#mysqlparameterstypedef)
  - [NamespaceErrorTypeDef](#namespaceerrortypedef)
  - [NamespaceInfoV2TypeDef](#namespaceinfov2typedef)
  - [OracleParametersTypeDef](#oracleparameterstypedef)
  - [OutputColumnTypeDef](#outputcolumntypedef)
  - [PhysicalTableTypeDef](#physicaltabletypedef)
  - [PostgreSqlParametersTypeDef](#postgresqlparameterstypedef)
  - [PrestoParametersTypeDef](#prestoparameterstypedef)
  - [ProjectOperationTypeDef](#projectoperationtypedef)
  - [QueueInfoTypeDef](#queueinfotypedef)
  - [RdsParametersTypeDef](#rdsparameterstypedef)
  - [RedshiftParametersTypeDef](#redshiftparameterstypedef)
  - [RelationalTableTypeDef](#relationaltabletypedef)
  - [RenameColumnOperationTypeDef](#renamecolumnoperationtypedef)
  - [ResourcePermissionTypeDef](#resourcepermissiontypedef)
  - [RowInfoTypeDef](#rowinfotypedef)
  - [RowLevelPermissionDataSetTypeDef](#rowlevelpermissiondatasettypedef)
  - [S3ParametersTypeDef](#s3parameterstypedef)
  - [S3SourceTypeDef](#s3sourcetypedef)
  - [ServiceNowParametersTypeDef](#servicenowparameterstypedef)
  - [SheetControlsOptionTypeDef](#sheetcontrolsoptiontypedef)
  - [SheetStyleTypeDef](#sheetstyletypedef)
  - [SheetTypeDef](#sheettypedef)
  - [SnowflakeParametersTypeDef](#snowflakeparameterstypedef)
  - [SparkParametersTypeDef](#sparkparameterstypedef)
  - [SqlServerParametersTypeDef](#sqlserverparameterstypedef)
  - [SslPropertiesTypeDef](#sslpropertiestypedef)
  - [StringParameterTypeDef](#stringparametertypedef)
  - [TagColumnOperationTypeDef](#tagcolumnoperationtypedef)
  - [TagTypeDef](#tagtypedef)
  - [TemplateAliasTypeDef](#templatealiastypedef)
  - [TemplateErrorTypeDef](#templateerrortypedef)
  - [TemplateSourceAnalysisTypeDef](#templatesourceanalysistypedef)
  - [TemplateSourceTemplateTypeDef](#templatesourcetemplatetypedef)
  - [TemplateSummaryTypeDef](#templatesummarytypedef)
  - [TemplateTypeDef](#templatetypedef)
  - [TemplateVersionSummaryTypeDef](#templateversionsummarytypedef)
  - [TemplateVersionTypeDef](#templateversiontypedef)
  - [TeradataParametersTypeDef](#teradataparameterstypedef)
  - [ThemeAliasTypeDef](#themealiastypedef)
  - [ThemeConfigurationTypeDef](#themeconfigurationtypedef)
  - [ThemeErrorTypeDef](#themeerrortypedef)
  - [ThemeSummaryTypeDef](#themesummarytypedef)
  - [ThemeTypeDef](#themetypedef)
  - [ThemeVersionSummaryTypeDef](#themeversionsummarytypedef)
  - [ThemeVersionTypeDef](#themeversiontypedef)
  - [TileLayoutStyleTypeDef](#tilelayoutstyletypedef)
  - [TileStyleTypeDef](#tilestyletypedef)
  - [TransformOperationTypeDef](#transformoperationtypedef)
  - [TwitterParametersTypeDef](#twitterparameterstypedef)
  - [UIColorPaletteTypeDef](#uicolorpalettetypedef)
  - [UploadSettingsTypeDef](#uploadsettingstypedef)
  - [UserTypeDef](#usertypedef)
  - [VpcConnectionPropertiesTypeDef](#vpcconnectionpropertiestypedef)
  - [AnalysisSearchFilterTypeDef](#analysissearchfiltertypedef)
  - [AnalysisSourceEntityTypeDef](#analysissourceentitytypedef)
  - [CancelIngestionResponseTypeDef](#cancelingestionresponsetypedef)
  - [CreateAccountCustomizationResponseTypeDef](#createaccountcustomizationresponsetypedef)
  - [CreateAnalysisResponseTypeDef](#createanalysisresponsetypedef)
  - [CreateDashboardResponseTypeDef](#createdashboardresponsetypedef)
  - [CreateDataSetResponseTypeDef](#createdatasetresponsetypedef)
  - [CreateDataSourceResponseTypeDef](#createdatasourceresponsetypedef)
  - [CreateGroupMembershipResponseTypeDef](#creategroupmembershipresponsetypedef)
  - [CreateGroupResponseTypeDef](#creategroupresponsetypedef)
  - [CreateIAMPolicyAssignmentResponseTypeDef](#createiampolicyassignmentresponsetypedef)
  - [CreateIngestionResponseTypeDef](#createingestionresponsetypedef)
  - [CreateNamespaceResponseTypeDef](#createnamespaceresponsetypedef)
  - [CreateTemplateAliasResponseTypeDef](#createtemplatealiasresponsetypedef)
  - [CreateTemplateResponseTypeDef](#createtemplateresponsetypedef)
  - [CreateThemeAliasResponseTypeDef](#createthemealiasresponsetypedef)
  - [CreateThemeResponseTypeDef](#createthemeresponsetypedef)
  - [DashboardPublishOptionsTypeDef](#dashboardpublishoptionstypedef)
  - [DashboardSearchFilterTypeDef](#dashboardsearchfiltertypedef)
  - [DashboardSourceEntityTypeDef](#dashboardsourceentitytypedef)
  - [DataSourceCredentialsTypeDef](#datasourcecredentialstypedef)
  - [DeleteAccountCustomizationResponseTypeDef](#deleteaccountcustomizationresponsetypedef)
  - [DeleteAnalysisResponseTypeDef](#deleteanalysisresponsetypedef)
  - [DeleteDashboardResponseTypeDef](#deletedashboardresponsetypedef)
  - [DeleteDataSetResponseTypeDef](#deletedatasetresponsetypedef)
  - [DeleteDataSourceResponseTypeDef](#deletedatasourceresponsetypedef)
  - [DeleteGroupMembershipResponseTypeDef](#deletegroupmembershipresponsetypedef)
  - [DeleteGroupResponseTypeDef](#deletegroupresponsetypedef)
  - [DeleteIAMPolicyAssignmentResponseTypeDef](#deleteiampolicyassignmentresponsetypedef)
  - [DeleteNamespaceResponseTypeDef](#deletenamespaceresponsetypedef)
  - [DeleteTemplateAliasResponseTypeDef](#deletetemplatealiasresponsetypedef)
  - [DeleteTemplateResponseTypeDef](#deletetemplateresponsetypedef)
  - [DeleteThemeAliasResponseTypeDef](#deletethemealiasresponsetypedef)
  - [DeleteThemeResponseTypeDef](#deletethemeresponsetypedef)
  - [DeleteUserByPrincipalIdResponseTypeDef](#deleteuserbyprincipalidresponsetypedef)
  - [DeleteUserResponseTypeDef](#deleteuserresponsetypedef)
  - [DescribeAccountCustomizationResponseTypeDef](#describeaccountcustomizationresponsetypedef)
  - [DescribeAccountSettingsResponseTypeDef](#describeaccountsettingsresponsetypedef)
  - [DescribeAnalysisPermissionsResponseTypeDef](#describeanalysispermissionsresponsetypedef)
  - [DescribeAnalysisResponseTypeDef](#describeanalysisresponsetypedef)
  - [DescribeDashboardPermissionsResponseTypeDef](#describedashboardpermissionsresponsetypedef)
  - [DescribeDashboardResponseTypeDef](#describedashboardresponsetypedef)
  - [DescribeDataSetPermissionsResponseTypeDef](#describedatasetpermissionsresponsetypedef)
  - [DescribeDataSetResponseTypeDef](#describedatasetresponsetypedef)
  - [DescribeDataSourcePermissionsResponseTypeDef](#describedatasourcepermissionsresponsetypedef)
  - [DescribeDataSourceResponseTypeDef](#describedatasourceresponsetypedef)
  - [DescribeGroupResponseTypeDef](#describegroupresponsetypedef)
  - [DescribeIAMPolicyAssignmentResponseTypeDef](#describeiampolicyassignmentresponsetypedef)
  - [DescribeIngestionResponseTypeDef](#describeingestionresponsetypedef)
  - [DescribeNamespaceResponseTypeDef](#describenamespaceresponsetypedef)
  - [DescribeTemplateAliasResponseTypeDef](#describetemplatealiasresponsetypedef)
  - [DescribeTemplatePermissionsResponseTypeDef](#describetemplatepermissionsresponsetypedef)
  - [DescribeTemplateResponseTypeDef](#describetemplateresponsetypedef)
  - [DescribeThemeAliasResponseTypeDef](#describethemealiasresponsetypedef)
  - [DescribeThemePermissionsResponseTypeDef](#describethemepermissionsresponsetypedef)
  - [DescribeThemeResponseTypeDef](#describethemeresponsetypedef)
  - [DescribeUserResponseTypeDef](#describeuserresponsetypedef)
  - [GetDashboardEmbedUrlResponseTypeDef](#getdashboardembedurlresponsetypedef)
  - [GetSessionEmbedUrlResponseTypeDef](#getsessionembedurlresponsetypedef)
  - [ListAnalysesResponseTypeDef](#listanalysesresponsetypedef)
  - [ListDashboardVersionsResponseTypeDef](#listdashboardversionsresponsetypedef)
  - [ListDashboardsResponseTypeDef](#listdashboardsresponsetypedef)
  - [ListDataSetsResponseTypeDef](#listdatasetsresponsetypedef)
  - [ListDataSourcesResponseTypeDef](#listdatasourcesresponsetypedef)
  - [ListGroupMembershipsResponseTypeDef](#listgroupmembershipsresponsetypedef)
  - [ListGroupsResponseTypeDef](#listgroupsresponsetypedef)
  - [ListIAMPolicyAssignmentsForUserResponseTypeDef](#listiampolicyassignmentsforuserresponsetypedef)
  - [ListIAMPolicyAssignmentsResponseTypeDef](#listiampolicyassignmentsresponsetypedef)
  - [ListIngestionsResponseTypeDef](#listingestionsresponsetypedef)
  - [ListNamespacesResponseTypeDef](#listnamespacesresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListTemplateAliasesResponseTypeDef](#listtemplatealiasesresponsetypedef)
  - [ListTemplateVersionsResponseTypeDef](#listtemplateversionsresponsetypedef)
  - [ListTemplatesResponseTypeDef](#listtemplatesresponsetypedef)
  - [ListThemeAliasesResponseTypeDef](#listthemealiasesresponsetypedef)
  - [ListThemeVersionsResponseTypeDef](#listthemeversionsresponsetypedef)
  - [ListThemesResponseTypeDef](#listthemesresponsetypedef)
  - [ListUserGroupsResponseTypeDef](#listusergroupsresponsetypedef)
  - [ListUsersResponseTypeDef](#listusersresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ParametersTypeDef](#parameterstypedef)
  - [RegisterUserResponseTypeDef](#registeruserresponsetypedef)
  - [RestoreAnalysisResponseTypeDef](#restoreanalysisresponsetypedef)
  - [SearchAnalysesResponseTypeDef](#searchanalysesresponsetypedef)
  - [SearchDashboardsResponseTypeDef](#searchdashboardsresponsetypedef)
  - [TagResourceResponseTypeDef](#tagresourceresponsetypedef)
  - [TemplateSourceEntityTypeDef](#templatesourceentitytypedef)
  - [UntagResourceResponseTypeDef](#untagresourceresponsetypedef)
  - [UpdateAccountCustomizationResponseTypeDef](#updateaccountcustomizationresponsetypedef)
  - [UpdateAccountSettingsResponseTypeDef](#updateaccountsettingsresponsetypedef)
  - [UpdateAnalysisPermissionsResponseTypeDef](#updateanalysispermissionsresponsetypedef)
  - [UpdateAnalysisResponseTypeDef](#updateanalysisresponsetypedef)
  - [UpdateDashboardPermissionsResponseTypeDef](#updatedashboardpermissionsresponsetypedef)
  - [UpdateDashboardPublishedVersionResponseTypeDef](#updatedashboardpublishedversionresponsetypedef)
  - [UpdateDashboardResponseTypeDef](#updatedashboardresponsetypedef)
  - [UpdateDataSetPermissionsResponseTypeDef](#updatedatasetpermissionsresponsetypedef)
  - [UpdateDataSetResponseTypeDef](#updatedatasetresponsetypedef)
  - [UpdateDataSourcePermissionsResponseTypeDef](#updatedatasourcepermissionsresponsetypedef)
  - [UpdateDataSourceResponseTypeDef](#updatedatasourceresponsetypedef)
  - [UpdateGroupResponseTypeDef](#updategroupresponsetypedef)
  - [UpdateIAMPolicyAssignmentResponseTypeDef](#updateiampolicyassignmentresponsetypedef)
  - [UpdateTemplateAliasResponseTypeDef](#updatetemplatealiasresponsetypedef)
  - [UpdateTemplatePermissionsResponseTypeDef](#updatetemplatepermissionsresponsetypedef)
  - [UpdateTemplateResponseTypeDef](#updatetemplateresponsetypedef)
  - [UpdateThemeAliasResponseTypeDef](#updatethemealiasresponsetypedef)
  - [UpdateThemePermissionsResponseTypeDef](#updatethemepermissionsresponsetypedef)
  - [UpdateThemeResponseTypeDef](#updatethemeresponsetypedef)
  - [UpdateUserResponseTypeDef](#updateuserresponsetypedef)

## AccountCustomizationTypeDef

```python
from mypy_boto3_quicksight.type_defs import AccountCustomizationTypeDef
```




Optional fields:
- `DefaultTheme`: `str`


## AccountSettingsTypeDef

```python
from mypy_boto3_quicksight.type_defs import AccountSettingsTypeDef
```




Optional fields:
- `AccountName`: `str`
- `Edition`: `Edition`
- `DefaultNamespace`: `str`
- `NotificationEmail`: `str`


## ActiveIAMPolicyAssignmentTypeDef

```python
from mypy_boto3_quicksight.type_defs import ActiveIAMPolicyAssignmentTypeDef
```




Optional fields:
- `AssignmentName`: `str`
- `PolicyArn`: `str`


## AdHocFilteringOptionTypeDef

```python
from mypy_boto3_quicksight.type_defs import AdHocFilteringOptionTypeDef
```




Optional fields:
- `AvailabilityStatus`: `DashboardBehavior`


## AmazonElasticsearchParametersTypeDef

```python
from mypy_boto3_quicksight.type_defs import AmazonElasticsearchParametersTypeDef
```


Required fields:
- `Domain`: `str`




## AnalysisErrorTypeDef

```python
from mypy_boto3_quicksight.type_defs import AnalysisErrorTypeDef
```




Optional fields:
- `Type`: `AnalysisErrorType`
- `Message`: `str`


## AnalysisSourceTemplateTypeDef

```python
from mypy_boto3_quicksight.type_defs import AnalysisSourceTemplateTypeDef
```


Required fields:
- `DataSetReferences`: `List["DataSetReferenceTypeDef"]`
- `Arn`: `str`




## AnalysisSummaryTypeDef

```python
from mypy_boto3_quicksight.type_defs import AnalysisSummaryTypeDef
```




Optional fields:
- `Arn`: `str`
- `AnalysisId`: `str`
- `Name`: `str`
- `Status`: `ResourceStatus`
- `CreatedTime`: `datetime`
- `LastUpdatedTime`: `datetime`


## AnalysisTypeDef

```python
from mypy_boto3_quicksight.type_defs import AnalysisTypeDef
```




Optional fields:
- `AnalysisId`: `str`
- `Arn`: `str`
- `Name`: `str`
- `Status`: `ResourceStatus`
- `Errors`: `List["AnalysisErrorTypeDef"]`
- `DataSetArns`: `List[str]`
- `ThemeArn`: `str`
- `CreatedTime`: `datetime`
- `LastUpdatedTime`: `datetime`
- `Sheets`: `List["SheetTypeDef"]`


## AthenaParametersTypeDef

```python
from mypy_boto3_quicksight.type_defs import AthenaParametersTypeDef
```




Optional fields:
- `WorkGroup`: `str`


## AuroraParametersTypeDef

```python
from mypy_boto3_quicksight.type_defs import AuroraParametersTypeDef
```


Required fields:
- `Host`: `str`
- `Port`: `int`
- `Database`: `str`




## AuroraPostgreSqlParametersTypeDef

```python
from mypy_boto3_quicksight.type_defs import AuroraPostgreSqlParametersTypeDef
```


Required fields:
- `Host`: `str`
- `Port`: `int`
- `Database`: `str`




## AwsIotAnalyticsParametersTypeDef

```python
from mypy_boto3_quicksight.type_defs import AwsIotAnalyticsParametersTypeDef
```


Required fields:
- `DataSetName`: `str`




## BorderStyleTypeDef

```python
from mypy_boto3_quicksight.type_defs import BorderStyleTypeDef
```




Optional fields:
- `Show`: `bool`


## CalculatedColumnTypeDef

```python
from mypy_boto3_quicksight.type_defs import CalculatedColumnTypeDef
```


Required fields:
- `ColumnName`: `str`
- `ColumnId`: `str`
- `Expression`: `str`




## CastColumnTypeOperationTypeDef

```python
from mypy_boto3_quicksight.type_defs import CastColumnTypeOperationTypeDef
```


Required fields:
- `ColumnName`: `str`
- `NewColumnType`: `ColumnDataType`



Optional fields:
- `Format`: `str`


## ColumnDescriptionTypeDef

```python
from mypy_boto3_quicksight.type_defs import ColumnDescriptionTypeDef
```




Optional fields:
- `Text`: `str`


## ColumnGroupColumnSchemaTypeDef

```python
from mypy_boto3_quicksight.type_defs import ColumnGroupColumnSchemaTypeDef
```




Optional fields:
- `Name`: `str`


## ColumnGroupSchemaTypeDef

```python
from mypy_boto3_quicksight.type_defs import ColumnGroupSchemaTypeDef
```




Optional fields:
- `Name`: `str`
- `ColumnGroupColumnSchemaList`: `List["ColumnGroupColumnSchemaTypeDef"]`


## ColumnGroupTypeDef

```python
from mypy_boto3_quicksight.type_defs import ColumnGroupTypeDef
```




Optional fields:
- `GeoSpatialColumnGroup`: `"GeoSpatialColumnGroupTypeDef"`


## ColumnLevelPermissionRuleTypeDef

```python
from mypy_boto3_quicksight.type_defs import ColumnLevelPermissionRuleTypeDef
```




Optional fields:
- `Principals`: `List[str]`
- `ColumnNames`: `List[str]`


## ColumnSchemaTypeDef

```python
from mypy_boto3_quicksight.type_defs import ColumnSchemaTypeDef
```




Optional fields:
- `Name`: `str`
- `DataType`: `str`
- `GeographicRole`: `str`


## ColumnTagTypeDef

```python
from mypy_boto3_quicksight.type_defs import ColumnTagTypeDef
```




Optional fields:
- `ColumnGeographicRole`: `GeoSpatialDataRole`
- `ColumnDescription`: `"ColumnDescriptionTypeDef"`


## CreateColumnsOperationTypeDef

```python
from mypy_boto3_quicksight.type_defs import CreateColumnsOperationTypeDef
```


Required fields:
- `Columns`: `List["CalculatedColumnTypeDef"]`




## CredentialPairTypeDef

```python
from mypy_boto3_quicksight.type_defs import CredentialPairTypeDef
```


Required fields:
- `Username`: `str`
- `Password`: `str`



Optional fields:
- `AlternateDataSourceParameters`: `List["DataSourceParametersTypeDef"]`


## CustomSqlTypeDef

```python
from mypy_boto3_quicksight.type_defs import CustomSqlTypeDef
```


Required fields:
- `DataSourceArn`: `str`
- `Name`: `str`
- `SqlQuery`: `str`



Optional fields:
- `Columns`: `List["InputColumnTypeDef"]`


## DashboardErrorTypeDef

```python
from mypy_boto3_quicksight.type_defs import DashboardErrorTypeDef
```




Optional fields:
- `Type`: `DashboardErrorType`
- `Message`: `str`


## DashboardSourceTemplateTypeDef

```python
from mypy_boto3_quicksight.type_defs import DashboardSourceTemplateTypeDef
```


Required fields:
- `DataSetReferences`: `List["DataSetReferenceTypeDef"]`
- `Arn`: `str`




## DashboardSummaryTypeDef

```python
from mypy_boto3_quicksight.type_defs import DashboardSummaryTypeDef
```




Optional fields:
- `Arn`: `str`
- `DashboardId`: `str`
- `Name`: `str`
- `CreatedTime`: `datetime`
- `LastUpdatedTime`: `datetime`
- `PublishedVersionNumber`: `int`
- `LastPublishedTime`: `datetime`


## DashboardTypeDef

```python
from mypy_boto3_quicksight.type_defs import DashboardTypeDef
```




Optional fields:
- `DashboardId`: `str`
- `Arn`: `str`
- `Name`: `str`
- `Version`: `"DashboardVersionTypeDef"`
- `CreatedTime`: `datetime`
- `LastPublishedTime`: `datetime`
- `LastUpdatedTime`: `datetime`


## DashboardVersionSummaryTypeDef

```python
from mypy_boto3_quicksight.type_defs import DashboardVersionSummaryTypeDef
```




Optional fields:
- `Arn`: `str`
- `CreatedTime`: `datetime`
- `VersionNumber`: `int`
- `Status`: `ResourceStatus`
- `SourceEntityArn`: `str`
- `Description`: `str`


## DashboardVersionTypeDef

```python
from mypy_boto3_quicksight.type_defs import DashboardVersionTypeDef
```




Optional fields:
- `CreatedTime`: `datetime`
- `Errors`: `List["DashboardErrorTypeDef"]`
- `VersionNumber`: `int`
- `Status`: `ResourceStatus`
- `Arn`: `str`
- `SourceEntityArn`: `str`
- `DataSetArns`: `List[str]`
- `Description`: `str`
- `ThemeArn`: `str`
- `Sheets`: `List["SheetTypeDef"]`


## DataColorPaletteTypeDef

```python
from mypy_boto3_quicksight.type_defs import DataColorPaletteTypeDef
```




Optional fields:
- `Colors`: `List[str]`
- `MinMaxGradient`: `List[str]`
- `EmptyFillColor`: `str`


## DataSetConfigurationTypeDef

```python
from mypy_boto3_quicksight.type_defs import DataSetConfigurationTypeDef
```




Optional fields:
- `Placeholder`: `str`
- `DataSetSchema`: `"DataSetSchemaTypeDef"`
- `ColumnGroupSchemaList`: `List["ColumnGroupSchemaTypeDef"]`


## DataSetReferenceTypeDef

```python
from mypy_boto3_quicksight.type_defs import DataSetReferenceTypeDef
```


Required fields:
- `DataSetPlaceholder`: `str`
- `DataSetArn`: `str`




## DataSetSchemaTypeDef

```python
from mypy_boto3_quicksight.type_defs import DataSetSchemaTypeDef
```




Optional fields:
- `ColumnSchemaList`: `List["ColumnSchemaTypeDef"]`


## DataSetSummaryTypeDef

```python
from mypy_boto3_quicksight.type_defs import DataSetSummaryTypeDef
```




Optional fields:
- `Arn`: `str`
- `DataSetId`: `str`
- `Name`: `str`
- `CreatedTime`: `datetime`
- `LastUpdatedTime`: `datetime`
- `ImportMode`: `DataSetImportMode`
- `RowLevelPermissionDataSet`: `"RowLevelPermissionDataSetTypeDef"`
- `ColumnLevelPermissionRulesApplied`: `bool`


## DataSetTypeDef

```python
from mypy_boto3_quicksight.type_defs import DataSetTypeDef
```




Optional fields:
- `Arn`: `str`
- `DataSetId`: `str`
- `Name`: `str`
- `CreatedTime`: `datetime`
- `LastUpdatedTime`: `datetime`
- `PhysicalTableMap`: `Dict[str, "PhysicalTableTypeDef"]`
- `LogicalTableMap`: `Dict[str, "LogicalTableTypeDef"]`
- `OutputColumns`: `List["OutputColumnTypeDef"]`
- `ImportMode`: `DataSetImportMode`
- `ConsumedSpiceCapacityInBytes`: `int`
- `ColumnGroups`: `List["ColumnGroupTypeDef"]`
- `FieldFolders`: `Dict[str, "FieldFolderTypeDef"]`
- `RowLevelPermissionDataSet`: `"RowLevelPermissionDataSetTypeDef"`
- `ColumnLevelPermissionRules`: `List["ColumnLevelPermissionRuleTypeDef"]`


## DataSourceErrorInfoTypeDef

```python
from mypy_boto3_quicksight.type_defs import DataSourceErrorInfoTypeDef
```




Optional fields:
- `Type`: `DataSourceErrorInfoType`
- `Message`: `str`


## DataSourceParametersTypeDef

```python
from mypy_boto3_quicksight.type_defs import DataSourceParametersTypeDef
```




Optional fields:
- `AmazonElasticsearchParameters`: `"AmazonElasticsearchParametersTypeDef"`
- `AthenaParameters`: `"AthenaParametersTypeDef"`
- `AuroraParameters`: `"AuroraParametersTypeDef"`
- `AuroraPostgreSqlParameters`: `"AuroraPostgreSqlParametersTypeDef"`
- `AwsIotAnalyticsParameters`: `"AwsIotAnalyticsParametersTypeDef"`
- `JiraParameters`: `"JiraParametersTypeDef"`
- `MariaDbParameters`: `"MariaDbParametersTypeDef"`
- `MySqlParameters`: `"MySqlParametersTypeDef"`
- `OracleParameters`: `"OracleParametersTypeDef"`
- `PostgreSqlParameters`: `"PostgreSqlParametersTypeDef"`
- `PrestoParameters`: `"PrestoParametersTypeDef"`
- `RdsParameters`: `"RdsParametersTypeDef"`
- `RedshiftParameters`: `"RedshiftParametersTypeDef"`
- `S3Parameters`: `"S3ParametersTypeDef"`
- `ServiceNowParameters`: `"ServiceNowParametersTypeDef"`
- `SnowflakeParameters`: `"SnowflakeParametersTypeDef"`
- `SparkParameters`: `"SparkParametersTypeDef"`
- `SqlServerParameters`: `"SqlServerParametersTypeDef"`
- `TeradataParameters`: `"TeradataParametersTypeDef"`
- `TwitterParameters`: `"TwitterParametersTypeDef"`


## DataSourceTypeDef

```python
from mypy_boto3_quicksight.type_defs import DataSourceTypeDef
```




Optional fields:
- `Arn`: `str`
- `DataSourceId`: `str`
- `Name`: `str`
- `Type`: `DataSourceType`
- `Status`: `ResourceStatus`
- `CreatedTime`: `datetime`
- `LastUpdatedTime`: `datetime`
- `DataSourceParameters`: `"DataSourceParametersTypeDef"`
- `AlternateDataSourceParameters`: `List["DataSourceParametersTypeDef"]`
- `VpcConnectionProperties`: `"VpcConnectionPropertiesTypeDef"`
- `SslProperties`: `"SslPropertiesTypeDef"`
- `ErrorInfo`: `"DataSourceErrorInfoTypeDef"`


## DateTimeParameterTypeDef

```python
from mypy_boto3_quicksight.type_defs import DateTimeParameterTypeDef
```


Required fields:
- `Name`: `str`
- `Values`: `List[datetime]`




## DecimalParameterTypeDef

```python
from mypy_boto3_quicksight.type_defs import DecimalParameterTypeDef
```


Required fields:
- `Name`: `str`
- `Values`: `List[float]`




## ErrorInfoTypeDef

```python
from mypy_boto3_quicksight.type_defs import ErrorInfoTypeDef
```




Optional fields:
- `Type`: `IngestionErrorType`
- `Message`: `str`


## ExportToCSVOptionTypeDef

```python
from mypy_boto3_quicksight.type_defs import ExportToCSVOptionTypeDef
```




Optional fields:
- `AvailabilityStatus`: `DashboardBehavior`


## FieldFolderTypeDef

```python
from mypy_boto3_quicksight.type_defs import FieldFolderTypeDef
```




Optional fields:
- `description`: `str`
- `columns`: `List[str]`


## FilterOperationTypeDef

```python
from mypy_boto3_quicksight.type_defs import FilterOperationTypeDef
```


Required fields:
- `ConditionExpression`: `str`




## GeoSpatialColumnGroupTypeDef

```python
from mypy_boto3_quicksight.type_defs import GeoSpatialColumnGroupTypeDef
```


Required fields:
- `Name`: `str`
- `CountryCode`: `GeoSpatialCountryCode`
- `Columns`: `List[str]`




## GroupMemberTypeDef

```python
from mypy_boto3_quicksight.type_defs import GroupMemberTypeDef
```




Optional fields:
- `Arn`: `str`
- `MemberName`: `str`


## GroupTypeDef

```python
from mypy_boto3_quicksight.type_defs import GroupTypeDef
```




Optional fields:
- `Arn`: `str`
- `GroupName`: `str`
- `Description`: `str`
- `PrincipalId`: `str`


## GutterStyleTypeDef

```python
from mypy_boto3_quicksight.type_defs import GutterStyleTypeDef
```




Optional fields:
- `Show`: `bool`


## IAMPolicyAssignmentSummaryTypeDef

```python
from mypy_boto3_quicksight.type_defs import IAMPolicyAssignmentSummaryTypeDef
```




Optional fields:
- `AssignmentName`: `str`
- `AssignmentStatus`: `AssignmentStatus`


## IAMPolicyAssignmentTypeDef

```python
from mypy_boto3_quicksight.type_defs import IAMPolicyAssignmentTypeDef
```




Optional fields:
- `AwsAccountId`: `str`
- `AssignmentId`: `str`
- `AssignmentName`: `str`
- `PolicyArn`: `str`
- `Identities`: `Dict[str, List[str]]`
- `AssignmentStatus`: `AssignmentStatus`


## IngestionTypeDef

```python
from mypy_boto3_quicksight.type_defs import IngestionTypeDef
```


Required fields:
- `Arn`: `str`
- `IngestionStatus`: `IngestionStatus`
- `CreatedTime`: `datetime`



Optional fields:
- `IngestionId`: `str`
- `ErrorInfo`: `"ErrorInfoTypeDef"`
- `RowInfo`: `"RowInfoTypeDef"`
- `QueueInfo`: `"QueueInfoTypeDef"`
- `IngestionTimeInSeconds`: `int`
- `IngestionSizeInBytes`: `int`
- `RequestSource`: `IngestionRequestSource`
- `RequestType`: `IngestionRequestType`


## InputColumnTypeDef

```python
from mypy_boto3_quicksight.type_defs import InputColumnTypeDef
```


Required fields:
- `Name`: `str`
- `Type`: `InputColumnDataType`




## IntegerParameterTypeDef

```python
from mypy_boto3_quicksight.type_defs import IntegerParameterTypeDef
```


Required fields:
- `Name`: `str`
- `Values`: `List[int]`




## JiraParametersTypeDef

```python
from mypy_boto3_quicksight.type_defs import JiraParametersTypeDef
```


Required fields:
- `SiteBaseUrl`: `str`




## JoinInstructionTypeDef

```python
from mypy_boto3_quicksight.type_defs import JoinInstructionTypeDef
```


Required fields:
- `LeftOperand`: `str`
- `RightOperand`: `str`
- `Type`: `JoinType`
- `OnClause`: `str`



Optional fields:
- `LeftJoinKeyProperties`: `"JoinKeyPropertiesTypeDef"`
- `RightJoinKeyProperties`: `"JoinKeyPropertiesTypeDef"`


## JoinKeyPropertiesTypeDef

```python
from mypy_boto3_quicksight.type_defs import JoinKeyPropertiesTypeDef
```




Optional fields:
- `UniqueKey`: `bool`


## LogicalTableSourceTypeDef

```python
from mypy_boto3_quicksight.type_defs import LogicalTableSourceTypeDef
```




Optional fields:
- `JoinInstruction`: `"JoinInstructionTypeDef"`
- `PhysicalTableId`: `str`


## LogicalTableTypeDef

```python
from mypy_boto3_quicksight.type_defs import LogicalTableTypeDef
```


Required fields:
- `Alias`: `str`
- `Source`: `"LogicalTableSourceTypeDef"`



Optional fields:
- `DataTransforms`: `List["TransformOperationTypeDef"]`


## ManifestFileLocationTypeDef

```python
from mypy_boto3_quicksight.type_defs import ManifestFileLocationTypeDef
```


Required fields:
- `Bucket`: `str`
- `Key`: `str`




## MarginStyleTypeDef

```python
from mypy_boto3_quicksight.type_defs import MarginStyleTypeDef
```




Optional fields:
- `Show`: `bool`


## MariaDbParametersTypeDef

```python
from mypy_boto3_quicksight.type_defs import MariaDbParametersTypeDef
```


Required fields:
- `Host`: `str`
- `Port`: `int`
- `Database`: `str`




## MySqlParametersTypeDef

```python
from mypy_boto3_quicksight.type_defs import MySqlParametersTypeDef
```


Required fields:
- `Host`: `str`
- `Port`: `int`
- `Database`: `str`




## NamespaceErrorTypeDef

```python
from mypy_boto3_quicksight.type_defs import NamespaceErrorTypeDef
```




Optional fields:
- `Type`: `NamespaceErrorType`
- `Message`: `str`


## NamespaceInfoV2TypeDef

```python
from mypy_boto3_quicksight.type_defs import NamespaceInfoV2TypeDef
```




Optional fields:
- `Name`: `str`
- `Arn`: `str`
- `CapacityRegion`: `str`
- `CreationStatus`: `NamespaceStatus`
- `IdentityStore`: `IdentityStore`
- `NamespaceError`: `"NamespaceErrorTypeDef"`


## OracleParametersTypeDef

```python
from mypy_boto3_quicksight.type_defs import OracleParametersTypeDef
```


Required fields:
- `Host`: `str`
- `Port`: `int`
- `Database`: `str`




## OutputColumnTypeDef

```python
from mypy_boto3_quicksight.type_defs import OutputColumnTypeDef
```




Optional fields:
- `Name`: `str`
- `Description`: `str`
- `Type`: `ColumnDataType`


## PhysicalTableTypeDef

```python
from mypy_boto3_quicksight.type_defs import PhysicalTableTypeDef
```




Optional fields:
- `RelationalTable`: `"RelationalTableTypeDef"`
- `CustomSql`: `"CustomSqlTypeDef"`
- `S3Source`: `"S3SourceTypeDef"`


## PostgreSqlParametersTypeDef

```python
from mypy_boto3_quicksight.type_defs import PostgreSqlParametersTypeDef
```


Required fields:
- `Host`: `str`
- `Port`: `int`
- `Database`: `str`




## PrestoParametersTypeDef

```python
from mypy_boto3_quicksight.type_defs import PrestoParametersTypeDef
```


Required fields:
- `Host`: `str`
- `Port`: `int`
- `Catalog`: `str`




## ProjectOperationTypeDef

```python
from mypy_boto3_quicksight.type_defs import ProjectOperationTypeDef
```


Required fields:
- `ProjectedColumns`: `List[str]`




## QueueInfoTypeDef

```python
from mypy_boto3_quicksight.type_defs import QueueInfoTypeDef
```


Required fields:
- `WaitingOnIngestion`: `str`
- `QueuedIngestion`: `str`




## RdsParametersTypeDef

```python
from mypy_boto3_quicksight.type_defs import RdsParametersTypeDef
```


Required fields:
- `InstanceId`: `str`
- `Database`: `str`




## RedshiftParametersTypeDef

```python
from mypy_boto3_quicksight.type_defs import RedshiftParametersTypeDef
```


Required fields:
- `Database`: `str`



Optional fields:
- `Host`: `str`
- `Port`: `int`
- `ClusterId`: `str`


## RelationalTableTypeDef

```python
from mypy_boto3_quicksight.type_defs import RelationalTableTypeDef
```


Required fields:
- `DataSourceArn`: `str`
- `Name`: `str`
- `InputColumns`: `List["InputColumnTypeDef"]`



Optional fields:
- `Catalog`: `str`
- `Schema`: `str`


## RenameColumnOperationTypeDef

```python
from mypy_boto3_quicksight.type_defs import RenameColumnOperationTypeDef
```


Required fields:
- `ColumnName`: `str`
- `NewColumnName`: `str`




## ResourcePermissionTypeDef

```python
from mypy_boto3_quicksight.type_defs import ResourcePermissionTypeDef
```


Required fields:
- `Principal`: `str`
- `Actions`: `List[str]`




## RowInfoTypeDef

```python
from mypy_boto3_quicksight.type_defs import RowInfoTypeDef
```




Optional fields:
- `RowsIngested`: `int`
- `RowsDropped`: `int`


## RowLevelPermissionDataSetTypeDef

```python
from mypy_boto3_quicksight.type_defs import RowLevelPermissionDataSetTypeDef
```


Required fields:
- `Arn`: `str`
- `PermissionPolicy`: `RowLevelPermissionPolicy`



Optional fields:
- `Namespace`: `str`


## S3ParametersTypeDef

```python
from mypy_boto3_quicksight.type_defs import S3ParametersTypeDef
```


Required fields:
- `ManifestFileLocation`: `"ManifestFileLocationTypeDef"`




## S3SourceTypeDef

```python
from mypy_boto3_quicksight.type_defs import S3SourceTypeDef
```


Required fields:
- `DataSourceArn`: `str`
- `InputColumns`: `List["InputColumnTypeDef"]`



Optional fields:
- `UploadSettings`: `"UploadSettingsTypeDef"`


## ServiceNowParametersTypeDef

```python
from mypy_boto3_quicksight.type_defs import ServiceNowParametersTypeDef
```


Required fields:
- `SiteBaseUrl`: `str`




## SheetControlsOptionTypeDef

```python
from mypy_boto3_quicksight.type_defs import SheetControlsOptionTypeDef
```




Optional fields:
- `VisibilityState`: `DashboardUIState`


## SheetStyleTypeDef

```python
from mypy_boto3_quicksight.type_defs import SheetStyleTypeDef
```




Optional fields:
- `Tile`: `"TileStyleTypeDef"`
- `TileLayout`: `"TileLayoutStyleTypeDef"`


## SheetTypeDef

```python
from mypy_boto3_quicksight.type_defs import SheetTypeDef
```




Optional fields:
- `SheetId`: `str`
- `Name`: `str`


## SnowflakeParametersTypeDef

```python
from mypy_boto3_quicksight.type_defs import SnowflakeParametersTypeDef
```


Required fields:
- `Host`: `str`
- `Database`: `str`
- `Warehouse`: `str`




## SparkParametersTypeDef

```python
from mypy_boto3_quicksight.type_defs import SparkParametersTypeDef
```


Required fields:
- `Host`: `str`
- `Port`: `int`




## SqlServerParametersTypeDef

```python
from mypy_boto3_quicksight.type_defs import SqlServerParametersTypeDef
```


Required fields:
- `Host`: `str`
- `Port`: `int`
- `Database`: `str`




## SslPropertiesTypeDef

```python
from mypy_boto3_quicksight.type_defs import SslPropertiesTypeDef
```




Optional fields:
- `DisableSsl`: `bool`


## StringParameterTypeDef

```python
from mypy_boto3_quicksight.type_defs import StringParameterTypeDef
```


Required fields:
- `Name`: `str`
- `Values`: `List[str]`




## TagColumnOperationTypeDef

```python
from mypy_boto3_quicksight.type_defs import TagColumnOperationTypeDef
```


Required fields:
- `ColumnName`: `str`
- `Tags`: `List["ColumnTagTypeDef"]`




## TagTypeDef

```python
from mypy_boto3_quicksight.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## TemplateAliasTypeDef

```python
from mypy_boto3_quicksight.type_defs import TemplateAliasTypeDef
```




Optional fields:
- `AliasName`: `str`
- `Arn`: `str`
- `TemplateVersionNumber`: `int`


## TemplateErrorTypeDef

```python
from mypy_boto3_quicksight.type_defs import TemplateErrorTypeDef
```




Optional fields:
- `Type`: `TemplateErrorType`
- `Message`: `str`


## TemplateSourceAnalysisTypeDef

```python
from mypy_boto3_quicksight.type_defs import TemplateSourceAnalysisTypeDef
```


Required fields:
- `Arn`: `str`
- `DataSetReferences`: `List["DataSetReferenceTypeDef"]`




## TemplateSourceTemplateTypeDef

```python
from mypy_boto3_quicksight.type_defs import TemplateSourceTemplateTypeDef
```


Required fields:
- `Arn`: `str`




## TemplateSummaryTypeDef

```python
from mypy_boto3_quicksight.type_defs import TemplateSummaryTypeDef
```




Optional fields:
- `Arn`: `str`
- `TemplateId`: `str`
- `Name`: `str`
- `LatestVersionNumber`: `int`
- `CreatedTime`: `datetime`
- `LastUpdatedTime`: `datetime`


## TemplateTypeDef

```python
from mypy_boto3_quicksight.type_defs import TemplateTypeDef
```




Optional fields:
- `Arn`: `str`
- `Name`: `str`
- `Version`: `"TemplateVersionTypeDef"`
- `TemplateId`: `str`
- `LastUpdatedTime`: `datetime`
- `CreatedTime`: `datetime`


## TemplateVersionSummaryTypeDef

```python
from mypy_boto3_quicksight.type_defs import TemplateVersionSummaryTypeDef
```




Optional fields:
- `Arn`: `str`
- `VersionNumber`: `int`
- `CreatedTime`: `datetime`
- `Status`: `ResourceStatus`
- `Description`: `str`


## TemplateVersionTypeDef

```python
from mypy_boto3_quicksight.type_defs import TemplateVersionTypeDef
```




Optional fields:
- `CreatedTime`: `datetime`
- `Errors`: `List["TemplateErrorTypeDef"]`
- `VersionNumber`: `int`
- `Status`: `ResourceStatus`
- `DataSetConfigurations`: `List["DataSetConfigurationTypeDef"]`
- `Description`: `str`
- `SourceEntityArn`: `str`
- `ThemeArn`: `str`
- `Sheets`: `List["SheetTypeDef"]`


## TeradataParametersTypeDef

```python
from mypy_boto3_quicksight.type_defs import TeradataParametersTypeDef
```


Required fields:
- `Host`: `str`
- `Port`: `int`
- `Database`: `str`




## ThemeAliasTypeDef

```python
from mypy_boto3_quicksight.type_defs import ThemeAliasTypeDef
```




Optional fields:
- `Arn`: `str`
- `AliasName`: `str`
- `ThemeVersionNumber`: `int`


## ThemeConfigurationTypeDef

```python
from mypy_boto3_quicksight.type_defs import ThemeConfigurationTypeDef
```




Optional fields:
- `DataColorPalette`: `"DataColorPaletteTypeDef"`
- `UIColorPalette`: `"UIColorPaletteTypeDef"`
- `Sheet`: `"SheetStyleTypeDef"`


## ThemeErrorTypeDef

```python
from mypy_boto3_quicksight.type_defs import ThemeErrorTypeDef
```




Optional fields:
- `Type`: `ThemeErrorType`
- `Message`: `str`


## ThemeSummaryTypeDef

```python
from mypy_boto3_quicksight.type_defs import ThemeSummaryTypeDef
```




Optional fields:
- `Arn`: `str`
- `Name`: `str`
- `ThemeId`: `str`
- `LatestVersionNumber`: `int`
- `CreatedTime`: `datetime`
- `LastUpdatedTime`: `datetime`


## ThemeTypeDef

```python
from mypy_boto3_quicksight.type_defs import ThemeTypeDef
```




Optional fields:
- `Arn`: `str`
- `Name`: `str`
- `ThemeId`: `str`
- `Version`: `"ThemeVersionTypeDef"`
- `CreatedTime`: `datetime`
- `LastUpdatedTime`: `datetime`
- `Type`: `ThemeType`


## ThemeVersionSummaryTypeDef

```python
from mypy_boto3_quicksight.type_defs import ThemeVersionSummaryTypeDef
```




Optional fields:
- `VersionNumber`: `int`
- `Arn`: `str`
- `Description`: `str`
- `CreatedTime`: `datetime`
- `Status`: `ResourceStatus`


## ThemeVersionTypeDef

```python
from mypy_boto3_quicksight.type_defs import ThemeVersionTypeDef
```




Optional fields:
- `VersionNumber`: `int`
- `Arn`: `str`
- `Description`: `str`
- `BaseThemeId`: `str`
- `CreatedTime`: `datetime`
- `Configuration`: `"ThemeConfigurationTypeDef"`
- `Errors`: `List["ThemeErrorTypeDef"]`
- `Status`: `ResourceStatus`


## TileLayoutStyleTypeDef

```python
from mypy_boto3_quicksight.type_defs import TileLayoutStyleTypeDef
```




Optional fields:
- `Gutter`: `"GutterStyleTypeDef"`
- `Margin`: `"MarginStyleTypeDef"`


## TileStyleTypeDef

```python
from mypy_boto3_quicksight.type_defs import TileStyleTypeDef
```




Optional fields:
- `Border`: `"BorderStyleTypeDef"`


## TransformOperationTypeDef

```python
from mypy_boto3_quicksight.type_defs import TransformOperationTypeDef
```




Optional fields:
- `ProjectOperation`: `"ProjectOperationTypeDef"`
- `FilterOperation`: `"FilterOperationTypeDef"`
- `CreateColumnsOperation`: `"CreateColumnsOperationTypeDef"`
- `RenameColumnOperation`: `"RenameColumnOperationTypeDef"`
- `CastColumnTypeOperation`: `"CastColumnTypeOperationTypeDef"`
- `TagColumnOperation`: `"TagColumnOperationTypeDef"`


## TwitterParametersTypeDef

```python
from mypy_boto3_quicksight.type_defs import TwitterParametersTypeDef
```


Required fields:
- `Query`: `str`
- `MaxRows`: `int`




## UIColorPaletteTypeDef

```python
from mypy_boto3_quicksight.type_defs import UIColorPaletteTypeDef
```




Optional fields:
- `PrimaryForeground`: `str`
- `PrimaryBackground`: `str`
- `SecondaryForeground`: `str`
- `SecondaryBackground`: `str`
- `Accent`: `str`
- `AccentForeground`: `str`
- `Danger`: `str`
- `DangerForeground`: `str`
- `Warning`: `str`
- `WarningForeground`: `str`
- `Success`: `str`
- `SuccessForeground`: `str`
- `Dimension`: `str`
- `DimensionForeground`: `str`
- `Measure`: `str`
- `MeasureForeground`: `str`


## UploadSettingsTypeDef

```python
from mypy_boto3_quicksight.type_defs import UploadSettingsTypeDef
```




Optional fields:
- `Format`: `FileFormat`
- `StartFromRow`: `int`
- `ContainsHeader`: `bool`
- `TextQualifier`: `TextQualifier`
- `Delimiter`: `str`


## UserTypeDef

```python
from mypy_boto3_quicksight.type_defs import UserTypeDef
```




Optional fields:
- `Arn`: `str`
- `UserName`: `str`
- `Email`: `str`
- `Role`: `UserRole`
- `IdentityType`: `IdentityType`
- `Active`: `bool`
- `PrincipalId`: `str`
- `CustomPermissionsName`: `str`


## VpcConnectionPropertiesTypeDef

```python
from mypy_boto3_quicksight.type_defs import VpcConnectionPropertiesTypeDef
```


Required fields:
- `VpcConnectionArn`: `str`




## AnalysisSearchFilterTypeDef

```python
from mypy_boto3_quicksight.type_defs import AnalysisSearchFilterTypeDef
```




Optional fields:
- `Operator`: `FilterOperator`
- `Name`: `AnalysisFilterAttribute`
- `Value`: `str`


## AnalysisSourceEntityTypeDef

```python
from mypy_boto3_quicksight.type_defs import AnalysisSourceEntityTypeDef
```




Optional fields:
- `SourceTemplate`: `"AnalysisSourceTemplateTypeDef"`


## CancelIngestionResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import CancelIngestionResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `IngestionId`: `str`
- `RequestId`: `str`
- `Status`: `int`


## CreateAccountCustomizationResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import CreateAccountCustomizationResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `AwsAccountId`: `str`
- `Namespace`: `str`
- `AccountCustomization`: `"AccountCustomizationTypeDef"`
- `RequestId`: `str`
- `Status`: `int`


## CreateAnalysisResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import CreateAnalysisResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `AnalysisId`: `str`
- `CreationStatus`: `ResourceStatus`
- `Status`: `int`
- `RequestId`: `str`


## CreateDashboardResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import CreateDashboardResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `VersionArn`: `str`
- `DashboardId`: `str`
- `CreationStatus`: `ResourceStatus`
- `Status`: `int`
- `RequestId`: `str`


## CreateDataSetResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import CreateDataSetResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `DataSetId`: `str`
- `IngestionArn`: `str`
- `IngestionId`: `str`
- `RequestId`: `str`
- `Status`: `int`


## CreateDataSourceResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import CreateDataSourceResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `DataSourceId`: `str`
- `CreationStatus`: `ResourceStatus`
- `RequestId`: `str`
- `Status`: `int`


## CreateGroupMembershipResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import CreateGroupMembershipResponseTypeDef
```




Optional fields:
- `GroupMember`: `"GroupMemberTypeDef"`
- `RequestId`: `str`
- `Status`: `int`


## CreateGroupResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import CreateGroupResponseTypeDef
```




Optional fields:
- `Group`: `"GroupTypeDef"`
- `RequestId`: `str`
- `Status`: `int`


## CreateIAMPolicyAssignmentResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import CreateIAMPolicyAssignmentResponseTypeDef
```




Optional fields:
- `AssignmentName`: `str`
- `AssignmentId`: `str`
- `AssignmentStatus`: `AssignmentStatus`
- `PolicyArn`: `str`
- `Identities`: `Dict[str, List[str]]`
- `RequestId`: `str`
- `Status`: `int`


## CreateIngestionResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import CreateIngestionResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `IngestionId`: `str`
- `IngestionStatus`: `IngestionStatus`
- `RequestId`: `str`
- `Status`: `int`


## CreateNamespaceResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import CreateNamespaceResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `Name`: `str`
- `CapacityRegion`: `str`
- `CreationStatus`: `NamespaceStatus`
- `IdentityStore`: `IdentityStore`
- `RequestId`: `str`
- `Status`: `int`


## CreateTemplateAliasResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import CreateTemplateAliasResponseTypeDef
```




Optional fields:
- `TemplateAlias`: `"TemplateAliasTypeDef"`
- `Status`: `int`
- `RequestId`: `str`


## CreateTemplateResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import CreateTemplateResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `VersionArn`: `str`
- `TemplateId`: `str`
- `CreationStatus`: `ResourceStatus`
- `Status`: `int`
- `RequestId`: `str`


## CreateThemeAliasResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import CreateThemeAliasResponseTypeDef
```




Optional fields:
- `ThemeAlias`: `"ThemeAliasTypeDef"`
- `Status`: `int`
- `RequestId`: `str`


## CreateThemeResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import CreateThemeResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `VersionArn`: `str`
- `ThemeId`: `str`
- `CreationStatus`: `ResourceStatus`
- `Status`: `int`
- `RequestId`: `str`


## DashboardPublishOptionsTypeDef

```python
from mypy_boto3_quicksight.type_defs import DashboardPublishOptionsTypeDef
```




Optional fields:
- `AdHocFilteringOption`: `"AdHocFilteringOptionTypeDef"`
- `ExportToCSVOption`: `"ExportToCSVOptionTypeDef"`
- `SheetControlsOption`: `"SheetControlsOptionTypeDef"`


## DashboardSearchFilterTypeDef

```python
from mypy_boto3_quicksight.type_defs import DashboardSearchFilterTypeDef
```


Required fields:
- `Operator`: `FilterOperator`



Optional fields:
- `Name`: `DashboardFilterAttribute`
- `Value`: `str`


## DashboardSourceEntityTypeDef

```python
from mypy_boto3_quicksight.type_defs import DashboardSourceEntityTypeDef
```




Optional fields:
- `SourceTemplate`: `"DashboardSourceTemplateTypeDef"`


## DataSourceCredentialsTypeDef

```python
from mypy_boto3_quicksight.type_defs import DataSourceCredentialsTypeDef
```




Optional fields:
- `CredentialPair`: `"CredentialPairTypeDef"`
- `CopySourceArn`: `str`


## DeleteAccountCustomizationResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DeleteAccountCustomizationResponseTypeDef
```




Optional fields:
- `RequestId`: `str`
- `Status`: `int`


## DeleteAnalysisResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DeleteAnalysisResponseTypeDef
```




Optional fields:
- `Status`: `int`
- `Arn`: `str`
- `AnalysisId`: `str`
- `DeletionTime`: `datetime`
- `RequestId`: `str`


## DeleteDashboardResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DeleteDashboardResponseTypeDef
```




Optional fields:
- `Status`: `int`
- `Arn`: `str`
- `DashboardId`: `str`
- `RequestId`: `str`


## DeleteDataSetResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DeleteDataSetResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `DataSetId`: `str`
- `RequestId`: `str`
- `Status`: `int`


## DeleteDataSourceResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DeleteDataSourceResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `DataSourceId`: `str`
- `RequestId`: `str`
- `Status`: `int`


## DeleteGroupMembershipResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DeleteGroupMembershipResponseTypeDef
```




Optional fields:
- `RequestId`: `str`
- `Status`: `int`


## DeleteGroupResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DeleteGroupResponseTypeDef
```




Optional fields:
- `RequestId`: `str`
- `Status`: `int`


## DeleteIAMPolicyAssignmentResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DeleteIAMPolicyAssignmentResponseTypeDef
```




Optional fields:
- `AssignmentName`: `str`
- `RequestId`: `str`
- `Status`: `int`


## DeleteNamespaceResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DeleteNamespaceResponseTypeDef
```




Optional fields:
- `RequestId`: `str`
- `Status`: `int`


## DeleteTemplateAliasResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DeleteTemplateAliasResponseTypeDef
```




Optional fields:
- `Status`: `int`
- `TemplateId`: `str`
- `AliasName`: `str`
- `Arn`: `str`
- `RequestId`: `str`


## DeleteTemplateResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DeleteTemplateResponseTypeDef
```




Optional fields:
- `RequestId`: `str`
- `Arn`: `str`
- `TemplateId`: `str`
- `Status`: `int`


## DeleteThemeAliasResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DeleteThemeAliasResponseTypeDef
```




Optional fields:
- `AliasName`: `str`
- `Arn`: `str`
- `RequestId`: `str`
- `Status`: `int`
- `ThemeId`: `str`


## DeleteThemeResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DeleteThemeResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `RequestId`: `str`
- `Status`: `int`
- `ThemeId`: `str`


## DeleteUserByPrincipalIdResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DeleteUserByPrincipalIdResponseTypeDef
```




Optional fields:
- `RequestId`: `str`
- `Status`: `int`


## DeleteUserResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DeleteUserResponseTypeDef
```




Optional fields:
- `RequestId`: `str`
- `Status`: `int`


## DescribeAccountCustomizationResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DescribeAccountCustomizationResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `AwsAccountId`: `str`
- `Namespace`: `str`
- `AccountCustomization`: `"AccountCustomizationTypeDef"`
- `RequestId`: `str`
- `Status`: `int`


## DescribeAccountSettingsResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DescribeAccountSettingsResponseTypeDef
```




Optional fields:
- `AccountSettings`: `"AccountSettingsTypeDef"`
- `RequestId`: `str`
- `Status`: `int`


## DescribeAnalysisPermissionsResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DescribeAnalysisPermissionsResponseTypeDef
```




Optional fields:
- `AnalysisId`: `str`
- `AnalysisArn`: `str`
- `Permissions`: `List["ResourcePermissionTypeDef"]`
- `Status`: `int`
- `RequestId`: `str`


## DescribeAnalysisResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DescribeAnalysisResponseTypeDef
```




Optional fields:
- `Analysis`: `"AnalysisTypeDef"`
- `Status`: `int`
- `RequestId`: `str`


## DescribeDashboardPermissionsResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DescribeDashboardPermissionsResponseTypeDef
```




Optional fields:
- `DashboardId`: `str`
- `DashboardArn`: `str`
- `Permissions`: `List["ResourcePermissionTypeDef"]`
- `Status`: `int`
- `RequestId`: `str`


## DescribeDashboardResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DescribeDashboardResponseTypeDef
```




Optional fields:
- `Dashboard`: `"DashboardTypeDef"`
- `Status`: `int`
- `RequestId`: `str`


## DescribeDataSetPermissionsResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DescribeDataSetPermissionsResponseTypeDef
```




Optional fields:
- `DataSetArn`: `str`
- `DataSetId`: `str`
- `Permissions`: `List["ResourcePermissionTypeDef"]`
- `RequestId`: `str`
- `Status`: `int`


## DescribeDataSetResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DescribeDataSetResponseTypeDef
```




Optional fields:
- `DataSet`: `"DataSetTypeDef"`
- `RequestId`: `str`
- `Status`: `int`


## DescribeDataSourcePermissionsResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DescribeDataSourcePermissionsResponseTypeDef
```




Optional fields:
- `DataSourceArn`: `str`
- `DataSourceId`: `str`
- `Permissions`: `List["ResourcePermissionTypeDef"]`
- `RequestId`: `str`
- `Status`: `int`


## DescribeDataSourceResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DescribeDataSourceResponseTypeDef
```




Optional fields:
- `DataSource`: `"DataSourceTypeDef"`
- `RequestId`: `str`
- `Status`: `int`


## DescribeGroupResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DescribeGroupResponseTypeDef
```




Optional fields:
- `Group`: `"GroupTypeDef"`
- `RequestId`: `str`
- `Status`: `int`


## DescribeIAMPolicyAssignmentResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DescribeIAMPolicyAssignmentResponseTypeDef
```




Optional fields:
- `IAMPolicyAssignment`: `"IAMPolicyAssignmentTypeDef"`
- `RequestId`: `str`
- `Status`: `int`


## DescribeIngestionResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DescribeIngestionResponseTypeDef
```




Optional fields:
- `Ingestion`: `"IngestionTypeDef"`
- `RequestId`: `str`
- `Status`: `int`


## DescribeNamespaceResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DescribeNamespaceResponseTypeDef
```




Optional fields:
- `Namespace`: `"NamespaceInfoV2TypeDef"`
- `RequestId`: `str`
- `Status`: `int`


## DescribeTemplateAliasResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DescribeTemplateAliasResponseTypeDef
```




Optional fields:
- `TemplateAlias`: `"TemplateAliasTypeDef"`
- `Status`: `int`
- `RequestId`: `str`


## DescribeTemplatePermissionsResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DescribeTemplatePermissionsResponseTypeDef
```




Optional fields:
- `TemplateId`: `str`
- `TemplateArn`: `str`
- `Permissions`: `List["ResourcePermissionTypeDef"]`
- `RequestId`: `str`
- `Status`: `int`


## DescribeTemplateResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DescribeTemplateResponseTypeDef
```




Optional fields:
- `Template`: `"TemplateTypeDef"`
- `Status`: `int`
- `RequestId`: `str`


## DescribeThemeAliasResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DescribeThemeAliasResponseTypeDef
```




Optional fields:
- `ThemeAlias`: `"ThemeAliasTypeDef"`
- `Status`: `int`
- `RequestId`: `str`


## DescribeThemePermissionsResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DescribeThemePermissionsResponseTypeDef
```




Optional fields:
- `ThemeId`: `str`
- `ThemeArn`: `str`
- `Permissions`: `List["ResourcePermissionTypeDef"]`
- `RequestId`: `str`
- `Status`: `int`


## DescribeThemeResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DescribeThemeResponseTypeDef
```




Optional fields:
- `Theme`: `"ThemeTypeDef"`
- `Status`: `int`
- `RequestId`: `str`


## DescribeUserResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import DescribeUserResponseTypeDef
```




Optional fields:
- `User`: `"UserTypeDef"`
- `RequestId`: `str`
- `Status`: `int`


## GetDashboardEmbedUrlResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import GetDashboardEmbedUrlResponseTypeDef
```




Optional fields:
- `EmbedUrl`: `str`
- `Status`: `int`
- `RequestId`: `str`


## GetSessionEmbedUrlResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import GetSessionEmbedUrlResponseTypeDef
```




Optional fields:
- `EmbedUrl`: `str`
- `Status`: `int`
- `RequestId`: `str`


## ListAnalysesResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import ListAnalysesResponseTypeDef
```




Optional fields:
- `AnalysisSummaryList`: `List["AnalysisSummaryTypeDef"]`
- `NextToken`: `str`
- `Status`: `int`
- `RequestId`: `str`


## ListDashboardVersionsResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import ListDashboardVersionsResponseTypeDef
```




Optional fields:
- `DashboardVersionSummaryList`: `List["DashboardVersionSummaryTypeDef"]`
- `NextToken`: `str`
- `Status`: `int`
- `RequestId`: `str`


## ListDashboardsResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import ListDashboardsResponseTypeDef
```




Optional fields:
- `DashboardSummaryList`: `List["DashboardSummaryTypeDef"]`
- `NextToken`: `str`
- `Status`: `int`
- `RequestId`: `str`


## ListDataSetsResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import ListDataSetsResponseTypeDef
```




Optional fields:
- `DataSetSummaries`: `List["DataSetSummaryTypeDef"]`
- `NextToken`: `str`
- `RequestId`: `str`
- `Status`: `int`


## ListDataSourcesResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import ListDataSourcesResponseTypeDef
```




Optional fields:
- `DataSources`: `List["DataSourceTypeDef"]`
- `NextToken`: `str`
- `RequestId`: `str`
- `Status`: `int`


## ListGroupMembershipsResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import ListGroupMembershipsResponseTypeDef
```




Optional fields:
- `GroupMemberList`: `List["GroupMemberTypeDef"]`
- `NextToken`: `str`
- `RequestId`: `str`
- `Status`: `int`


## ListGroupsResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import ListGroupsResponseTypeDef
```




Optional fields:
- `GroupList`: `List["GroupTypeDef"]`
- `NextToken`: `str`
- `RequestId`: `str`
- `Status`: `int`


## ListIAMPolicyAssignmentsForUserResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import ListIAMPolicyAssignmentsForUserResponseTypeDef
```




Optional fields:
- `ActiveAssignments`: `List["ActiveIAMPolicyAssignmentTypeDef"]`
- `RequestId`: `str`
- `NextToken`: `str`
- `Status`: `int`


## ListIAMPolicyAssignmentsResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import ListIAMPolicyAssignmentsResponseTypeDef
```




Optional fields:
- `IAMPolicyAssignments`: `List["IAMPolicyAssignmentSummaryTypeDef"]`
- `NextToken`: `str`
- `RequestId`: `str`
- `Status`: `int`


## ListIngestionsResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import ListIngestionsResponseTypeDef
```




Optional fields:
- `Ingestions`: `List["IngestionTypeDef"]`
- `NextToken`: `str`
- `RequestId`: `str`
- `Status`: `int`


## ListNamespacesResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import ListNamespacesResponseTypeDef
```




Optional fields:
- `Namespaces`: `List["NamespaceInfoV2TypeDef"]`
- `NextToken`: `str`
- `RequestId`: `str`
- `Status`: `int`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`
- `RequestId`: `str`
- `Status`: `int`


## ListTemplateAliasesResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import ListTemplateAliasesResponseTypeDef
```




Optional fields:
- `TemplateAliasList`: `List["TemplateAliasTypeDef"]`
- `Status`: `int`
- `RequestId`: `str`
- `NextToken`: `str`


## ListTemplateVersionsResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import ListTemplateVersionsResponseTypeDef
```




Optional fields:
- `TemplateVersionSummaryList`: `List["TemplateVersionSummaryTypeDef"]`
- `NextToken`: `str`
- `Status`: `int`
- `RequestId`: `str`


## ListTemplatesResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import ListTemplatesResponseTypeDef
```




Optional fields:
- `TemplateSummaryList`: `List["TemplateSummaryTypeDef"]`
- `NextToken`: `str`
- `Status`: `int`
- `RequestId`: `str`


## ListThemeAliasesResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import ListThemeAliasesResponseTypeDef
```




Optional fields:
- `ThemeAliasList`: `List["ThemeAliasTypeDef"]`
- `Status`: `int`
- `RequestId`: `str`
- `NextToken`: `str`


## ListThemeVersionsResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import ListThemeVersionsResponseTypeDef
```




Optional fields:
- `ThemeVersionSummaryList`: `List["ThemeVersionSummaryTypeDef"]`
- `NextToken`: `str`
- `Status`: `int`
- `RequestId`: `str`


## ListThemesResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import ListThemesResponseTypeDef
```




Optional fields:
- `ThemeSummaryList`: `List["ThemeSummaryTypeDef"]`
- `NextToken`: `str`
- `Status`: `int`
- `RequestId`: `str`


## ListUserGroupsResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import ListUserGroupsResponseTypeDef
```




Optional fields:
- `GroupList`: `List["GroupTypeDef"]`
- `NextToken`: `str`
- `RequestId`: `str`
- `Status`: `int`


## ListUsersResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import ListUsersResponseTypeDef
```




Optional fields:
- `UserList`: `List["UserTypeDef"]`
- `NextToken`: `str`
- `RequestId`: `str`
- `Status`: `int`


## PaginatorConfigTypeDef

```python
from mypy_boto3_quicksight.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ParametersTypeDef

```python
from mypy_boto3_quicksight.type_defs import ParametersTypeDef
```




Optional fields:
- `StringParameters`: `List["StringParameterTypeDef"]`
- `IntegerParameters`: `List["IntegerParameterTypeDef"]`
- `DecimalParameters`: `List["DecimalParameterTypeDef"]`
- `DateTimeParameters`: `List["DateTimeParameterTypeDef"]`


## RegisterUserResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import RegisterUserResponseTypeDef
```




Optional fields:
- `User`: `"UserTypeDef"`
- `UserInvitationUrl`: `str`
- `RequestId`: `str`
- `Status`: `int`


## RestoreAnalysisResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import RestoreAnalysisResponseTypeDef
```




Optional fields:
- `Status`: `int`
- `Arn`: `str`
- `AnalysisId`: `str`
- `RequestId`: `str`


## SearchAnalysesResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import SearchAnalysesResponseTypeDef
```




Optional fields:
- `AnalysisSummaryList`: `List["AnalysisSummaryTypeDef"]`
- `NextToken`: `str`
- `Status`: `int`
- `RequestId`: `str`


## SearchDashboardsResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import SearchDashboardsResponseTypeDef
```




Optional fields:
- `DashboardSummaryList`: `List["DashboardSummaryTypeDef"]`
- `NextToken`: `str`
- `Status`: `int`
- `RequestId`: `str`


## TagResourceResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import TagResourceResponseTypeDef
```




Optional fields:
- `RequestId`: `str`
- `Status`: `int`


## TemplateSourceEntityTypeDef

```python
from mypy_boto3_quicksight.type_defs import TemplateSourceEntityTypeDef
```




Optional fields:
- `SourceAnalysis`: `"TemplateSourceAnalysisTypeDef"`
- `SourceTemplate`: `"TemplateSourceTemplateTypeDef"`


## UntagResourceResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import UntagResourceResponseTypeDef
```




Optional fields:
- `RequestId`: `str`
- `Status`: `int`


## UpdateAccountCustomizationResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import UpdateAccountCustomizationResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `AwsAccountId`: `str`
- `Namespace`: `str`
- `AccountCustomization`: `"AccountCustomizationTypeDef"`
- `RequestId`: `str`
- `Status`: `int`


## UpdateAccountSettingsResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import UpdateAccountSettingsResponseTypeDef
```




Optional fields:
- `RequestId`: `str`
- `Status`: `int`


## UpdateAnalysisPermissionsResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import UpdateAnalysisPermissionsResponseTypeDef
```




Optional fields:
- `AnalysisArn`: `str`
- `AnalysisId`: `str`
- `Permissions`: `List["ResourcePermissionTypeDef"]`
- `RequestId`: `str`
- `Status`: `int`


## UpdateAnalysisResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import UpdateAnalysisResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `AnalysisId`: `str`
- `UpdateStatus`: `ResourceStatus`
- `Status`: `int`
- `RequestId`: `str`


## UpdateDashboardPermissionsResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import UpdateDashboardPermissionsResponseTypeDef
```




Optional fields:
- `DashboardArn`: `str`
- `DashboardId`: `str`
- `Permissions`: `List["ResourcePermissionTypeDef"]`
- `RequestId`: `str`
- `Status`: `int`


## UpdateDashboardPublishedVersionResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import UpdateDashboardPublishedVersionResponseTypeDef
```




Optional fields:
- `DashboardId`: `str`
- `DashboardArn`: `str`
- `Status`: `int`
- `RequestId`: `str`


## UpdateDashboardResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import UpdateDashboardResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `VersionArn`: `str`
- `DashboardId`: `str`
- `CreationStatus`: `ResourceStatus`
- `Status`: `int`
- `RequestId`: `str`


## UpdateDataSetPermissionsResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import UpdateDataSetPermissionsResponseTypeDef
```




Optional fields:
- `DataSetArn`: `str`
- `DataSetId`: `str`
- `RequestId`: `str`
- `Status`: `int`


## UpdateDataSetResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import UpdateDataSetResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `DataSetId`: `str`
- `IngestionArn`: `str`
- `IngestionId`: `str`
- `RequestId`: `str`
- `Status`: `int`


## UpdateDataSourcePermissionsResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import UpdateDataSourcePermissionsResponseTypeDef
```




Optional fields:
- `DataSourceArn`: `str`
- `DataSourceId`: `str`
- `RequestId`: `str`
- `Status`: `int`


## UpdateDataSourceResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import UpdateDataSourceResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `DataSourceId`: `str`
- `UpdateStatus`: `ResourceStatus`
- `RequestId`: `str`
- `Status`: `int`


## UpdateGroupResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import UpdateGroupResponseTypeDef
```




Optional fields:
- `Group`: `"GroupTypeDef"`
- `RequestId`: `str`
- `Status`: `int`


## UpdateIAMPolicyAssignmentResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import UpdateIAMPolicyAssignmentResponseTypeDef
```




Optional fields:
- `AssignmentName`: `str`
- `AssignmentId`: `str`
- `PolicyArn`: `str`
- `Identities`: `Dict[str, List[str]]`
- `AssignmentStatus`: `AssignmentStatus`
- `RequestId`: `str`
- `Status`: `int`


## UpdateTemplateAliasResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import UpdateTemplateAliasResponseTypeDef
```




Optional fields:
- `TemplateAlias`: `"TemplateAliasTypeDef"`
- `Status`: `int`
- `RequestId`: `str`


## UpdateTemplatePermissionsResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import UpdateTemplatePermissionsResponseTypeDef
```




Optional fields:
- `TemplateId`: `str`
- `TemplateArn`: `str`
- `Permissions`: `List["ResourcePermissionTypeDef"]`
- `RequestId`: `str`
- `Status`: `int`


## UpdateTemplateResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import UpdateTemplateResponseTypeDef
```




Optional fields:
- `TemplateId`: `str`
- `Arn`: `str`
- `VersionArn`: `str`
- `CreationStatus`: `ResourceStatus`
- `Status`: `int`
- `RequestId`: `str`


## UpdateThemeAliasResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import UpdateThemeAliasResponseTypeDef
```




Optional fields:
- `ThemeAlias`: `"ThemeAliasTypeDef"`
- `Status`: `int`
- `RequestId`: `str`


## UpdateThemePermissionsResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import UpdateThemePermissionsResponseTypeDef
```




Optional fields:
- `ThemeId`: `str`
- `ThemeArn`: `str`
- `Permissions`: `List["ResourcePermissionTypeDef"]`
- `RequestId`: `str`
- `Status`: `int`


## UpdateThemeResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import UpdateThemeResponseTypeDef
```




Optional fields:
- `ThemeId`: `str`
- `Arn`: `str`
- `VersionArn`: `str`
- `CreationStatus`: `ResourceStatus`
- `Status`: `int`
- `RequestId`: `str`


## UpdateUserResponseTypeDef

```python
from mypy_boto3_quicksight.type_defs import UpdateUserResponseTypeDef
```




Optional fields:
- `User`: `"UserTypeDef"`
- `RequestId`: `str`
- `Status`: `int`

