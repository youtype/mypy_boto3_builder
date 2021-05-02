# QuickSightClient for boto3 QuickSight module

> [Index](../index.md) > [QuickSight](./index.md) > QuickSightClient

Auto-generated documentation for [QuickSight](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight)
type annotations stubs module [mypy_boto3_quicksight](https://pypi.org/project/mypy-boto3-quicksight/).

- [QuickSightClient for boto3 QuickSight module](#quicksightclient-for-boto3-quicksight-module)
  - [QuickSightClient](#quicksightclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [cancel_ingestion](#cancel_ingestion)
    - [create_account_customization](#create_account_customization)
    - [create_analysis](#create_analysis)
    - [create_dashboard](#create_dashboard)
    - [create_data_set](#create_data_set)
    - [create_data_source](#create_data_source)
    - [create_group](#create_group)
    - [create_group_membership](#create_group_membership)
    - [create_iam_policy_assignment](#create_iam_policy_assignment)
    - [create_ingestion](#create_ingestion)
    - [create_namespace](#create_namespace)
    - [create_template](#create_template)
    - [create_template_alias](#create_template_alias)
    - [create_theme](#create_theme)
    - [create_theme_alias](#create_theme_alias)
    - [delete_account_customization](#delete_account_customization)
    - [delete_analysis](#delete_analysis)
    - [delete_dashboard](#delete_dashboard)
    - [delete_data_set](#delete_data_set)
    - [delete_data_source](#delete_data_source)
    - [delete_group](#delete_group)
    - [delete_group_membership](#delete_group_membership)
    - [delete_iam_policy_assignment](#delete_iam_policy_assignment)
    - [delete_namespace](#delete_namespace)
    - [delete_template](#delete_template)
    - [delete_template_alias](#delete_template_alias)
    - [delete_theme](#delete_theme)
    - [delete_theme_alias](#delete_theme_alias)
    - [delete_user](#delete_user)
    - [delete_user_by_principal_id](#delete_user_by_principal_id)
    - [describe_account_customization](#describe_account_customization)
    - [describe_account_settings](#describe_account_settings)
    - [describe_analysis](#describe_analysis)
    - [describe_analysis_permissions](#describe_analysis_permissions)
    - [describe_dashboard](#describe_dashboard)
    - [describe_dashboard_permissions](#describe_dashboard_permissions)
    - [describe_data_set](#describe_data_set)
    - [describe_data_set_permissions](#describe_data_set_permissions)
    - [describe_data_source](#describe_data_source)
    - [describe_data_source_permissions](#describe_data_source_permissions)
    - [describe_group](#describe_group)
    - [describe_iam_policy_assignment](#describe_iam_policy_assignment)
    - [describe_ingestion](#describe_ingestion)
    - [describe_namespace](#describe_namespace)
    - [describe_template](#describe_template)
    - [describe_template_alias](#describe_template_alias)
    - [describe_template_permissions](#describe_template_permissions)
    - [describe_theme](#describe_theme)
    - [describe_theme_alias](#describe_theme_alias)
    - [describe_theme_permissions](#describe_theme_permissions)
    - [describe_user](#describe_user)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_dashboard_embed_url](#get_dashboard_embed_url)
    - [get_session_embed_url](#get_session_embed_url)
    - [list_analyses](#list_analyses)
    - [list_dashboard_versions](#list_dashboard_versions)
    - [list_dashboards](#list_dashboards)
    - [list_data_sets](#list_data_sets)
    - [list_data_sources](#list_data_sources)
    - [list_group_memberships](#list_group_memberships)
    - [list_groups](#list_groups)
    - [list_iam_policy_assignments](#list_iam_policy_assignments)
    - [list_iam_policy_assignments_for_user](#list_iam_policy_assignments_for_user)
    - [list_ingestions](#list_ingestions)
    - [list_namespaces](#list_namespaces)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_template_aliases](#list_template_aliases)
    - [list_template_versions](#list_template_versions)
    - [list_templates](#list_templates)
    - [list_theme_aliases](#list_theme_aliases)
    - [list_theme_versions](#list_theme_versions)
    - [list_themes](#list_themes)
    - [list_user_groups](#list_user_groups)
    - [list_users](#list_users)
    - [register_user](#register_user)
    - [restore_analysis](#restore_analysis)
    - [search_analyses](#search_analyses)
    - [search_dashboards](#search_dashboards)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_account_customization](#update_account_customization)
    - [update_account_settings](#update_account_settings)
    - [update_analysis](#update_analysis)
    - [update_analysis_permissions](#update_analysis_permissions)
    - [update_dashboard](#update_dashboard)
    - [update_dashboard_permissions](#update_dashboard_permissions)
    - [update_dashboard_published_version](#update_dashboard_published_version)
    - [update_data_set](#update_data_set)
    - [update_data_set_permissions](#update_data_set_permissions)
    - [update_data_source](#update_data_source)
    - [update_data_source_permissions](#update_data_source_permissions)
    - [update_group](#update_group)
    - [update_iam_policy_assignment](#update_iam_policy_assignment)
    - [update_template](#update_template)
    - [update_template_alias](#update_template_alias)
    - [update_template_permissions](#update_template_permissions)
    - [update_theme](#update_theme)
    - [update_theme_alias](#update_theme_alias)
    - [update_theme_permissions](#update_theme_permissions)
    - [update_user](#update_user)
    - [get_paginator](#get_paginator)

## QuickSightClient

Type annotations for `boto3.client("quicksight")`

Can be used directly:

```python
from mypy_boto3_quicksight.client import QuickSightClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_quicksight.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConcurrentUpdatingException`
- `Exceptions.ConflictException`
- `Exceptions.DomainNotWhitelistedException`
- `Exceptions.IdentityTypeNotSupportedException`
- `Exceptions.InternalFailureException`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.InvalidParameterValueException`
- `Exceptions.LimitExceededException`
- `Exceptions.PreconditionNotMetException`
- `Exceptions.QuickSightUserNotFoundException`
- `Exceptions.ResourceExistsException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ResourceUnavailableException`
- `Exceptions.SessionLifetimeInMinutesInvalidException`
- `Exceptions.ThrottlingException`
- `Exceptions.UnsupportedPricingPlanException`
- `Exceptions.UnsupportedUserEditionException`


## Methods


### can_paginate

Type annotations for `boto3.client("quicksight").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_ingestion

Type annotations for `boto3.client("quicksight").cancel_ingestion` method.

[Client.cancel_ingestion documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.cancel_ingestion)

```python
def cancel_ingestion(
    self,
    AwsAccountId: str,
    DataSetId: str,
    IngestionId: str
) -> CancelIngestionResponseTypeDef:
    pass
```

### create_account_customization

Type annotations for `boto3.client("quicksight").create_account_customization` method.

[Client.create_account_customization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_account_customization)

```python
def create_account_customization(
    self,
    AwsAccountId: str,
    AccountCustomization: "AccountCustomizationTypeDef",
    Namespace: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateAccountCustomizationResponseTypeDef:
    pass
```

### create_analysis

Type annotations for `boto3.client("quicksight").create_analysis` method.

[Client.create_analysis documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_analysis)

```python
def create_analysis(
    self,
    AwsAccountId: str,
    AnalysisId: str,
    Name: str,
    SourceEntity: AnalysisSourceEntityTypeDef,
    Parameters: ParametersTypeDef = None,
    Permissions: List["ResourcePermissionTypeDef"] = None,
    ThemeArn: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateAnalysisResponseTypeDef:
    pass
```

### create_dashboard

Type annotations for `boto3.client("quicksight").create_dashboard` method.

[Client.create_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_dashboard)

```python
def create_dashboard(
    self,
    AwsAccountId: str,
    DashboardId: str,
    Name: str,
    SourceEntity: DashboardSourceEntityTypeDef,
    Parameters: ParametersTypeDef = None,
    Permissions: List["ResourcePermissionTypeDef"] = None,
    Tags: List["TagTypeDef"] = None,
    VersionDescription: str = None,
    DashboardPublishOptions: DashboardPublishOptionsTypeDef = None,
    ThemeArn: str = None
) -> CreateDashboardResponseTypeDef:
    pass
```

### create_data_set

Type annotations for `boto3.client("quicksight").create_data_set` method.

[Client.create_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_data_set)

```python
def create_data_set(
    self,
    AwsAccountId: str,
    DataSetId: str,
    Name: str,
    PhysicalTableMap: Dict[str, "PhysicalTableTypeDef"],
    ImportMode: DataSetImportMode,
    LogicalTableMap: Dict[str, "LogicalTableTypeDef"] = None,
    ColumnGroups: List["ColumnGroupTypeDef"] = None,
    FieldFolders: Dict[str, "FieldFolderTypeDef"] = None,
    Permissions: List["ResourcePermissionTypeDef"] = None,
    RowLevelPermissionDataSet: "RowLevelPermissionDataSetTypeDef" = None,
    ColumnLevelPermissionRules: List["ColumnLevelPermissionRuleTypeDef"] = None,
    Tags: List["TagTypeDef"] = None
) -> CreateDataSetResponseTypeDef:
    pass
```

### create_data_source

Type annotations for `boto3.client("quicksight").create_data_source` method.

[Client.create_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_data_source)

```python
def create_data_source(
    self,
    AwsAccountId: str,
    DataSourceId: str,
    Name: str,
    Type: DataSourceType,
    DataSourceParameters: "DataSourceParametersTypeDef" = None,
    Credentials: DataSourceCredentialsTypeDef = None,
    Permissions: List["ResourcePermissionTypeDef"] = None,
    VpcConnectionProperties: "VpcConnectionPropertiesTypeDef" = None,
    SslProperties: "SslPropertiesTypeDef" = None,
    Tags: List["TagTypeDef"] = None
) -> CreateDataSourceResponseTypeDef:
    pass
```

### create_group

Type annotations for `boto3.client("quicksight").create_group` method.

[Client.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_group)

```python
def create_group(
    self,
    GroupName: str,
    AwsAccountId: str,
    Namespace: str,
    Description: str = None
) -> CreateGroupResponseTypeDef:
    pass
```

### create_group_membership

Type annotations for `boto3.client("quicksight").create_group_membership` method.

[Client.create_group_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_group_membership)

```python
def create_group_membership(
    self,
    MemberName: str,
    GroupName: str,
    AwsAccountId: str,
    Namespace: str
) -> CreateGroupMembershipResponseTypeDef:
    pass
```

### create_iam_policy_assignment

Type annotations for `boto3.client("quicksight").create_iam_policy_assignment` method.

[Client.create_iam_policy_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_iam_policy_assignment)

```python
def create_iam_policy_assignment(
    self,
    AwsAccountId: str,
    AssignmentName: str,
    AssignmentStatus: AssignmentStatus,
    Namespace: str,
    PolicyArn: str = None,
    Identities: Dict[str, List[str]] = None
) -> CreateIAMPolicyAssignmentResponseTypeDef:
    pass
```

### create_ingestion

Type annotations for `boto3.client("quicksight").create_ingestion` method.

[Client.create_ingestion documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_ingestion)

```python
def create_ingestion(
    self,
    DataSetId: str,
    IngestionId: str,
    AwsAccountId: str
) -> CreateIngestionResponseTypeDef:
    pass
```

### create_namespace

Type annotations for `boto3.client("quicksight").create_namespace` method.

[Client.create_namespace documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_namespace)

```python
def create_namespace(
    self,
    AwsAccountId: str,
    Namespace: str,
    IdentityStore: Literal['QUICKSIGHT'],
    Tags: List["TagTypeDef"] = None
) -> CreateNamespaceResponseTypeDef:
    pass
```

### create_template

Type annotations for `boto3.client("quicksight").create_template` method.

[Client.create_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_template)

```python
def create_template(
    self,
    AwsAccountId: str,
    TemplateId: str,
    SourceEntity: TemplateSourceEntityTypeDef,
    Name: str = None,
    Permissions: List["ResourcePermissionTypeDef"] = None,
    Tags: List["TagTypeDef"] = None,
    VersionDescription: str = None
) -> CreateTemplateResponseTypeDef:
    pass
```

### create_template_alias

Type annotations for `boto3.client("quicksight").create_template_alias` method.

[Client.create_template_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_template_alias)

```python
def create_template_alias(
    self,
    AwsAccountId: str,
    TemplateId: str,
    AliasName: str,
    TemplateVersionNumber: int
) -> CreateTemplateAliasResponseTypeDef:
    pass
```

### create_theme

Type annotations for `boto3.client("quicksight").create_theme` method.

[Client.create_theme documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_theme)

```python
def create_theme(
    self,
    AwsAccountId: str,
    ThemeId: str,
    Name: str,
    BaseThemeId: str,
    Configuration: "ThemeConfigurationTypeDef",
    VersionDescription: str = None,
    Permissions: List["ResourcePermissionTypeDef"] = None,
    Tags: List["TagTypeDef"] = None
) -> CreateThemeResponseTypeDef:
    pass
```

### create_theme_alias

Type annotations for `boto3.client("quicksight").create_theme_alias` method.

[Client.create_theme_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_theme_alias)

```python
def create_theme_alias(
    self,
    AwsAccountId: str,
    ThemeId: str,
    AliasName: str,
    ThemeVersionNumber: int
) -> CreateThemeAliasResponseTypeDef:
    pass
```

### delete_account_customization

Type annotations for `boto3.client("quicksight").delete_account_customization` method.

[Client.delete_account_customization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_account_customization)

```python
def delete_account_customization(
    self,
    AwsAccountId: str,
    Namespace: str = None
) -> DeleteAccountCustomizationResponseTypeDef:
    pass
```

### delete_analysis

Type annotations for `boto3.client("quicksight").delete_analysis` method.

[Client.delete_analysis documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_analysis)

```python
def delete_analysis(
    self,
    AwsAccountId: str,
    AnalysisId: str,
    RecoveryWindowInDays: int = None,
    ForceDeleteWithoutRecovery: bool = None
) -> DeleteAnalysisResponseTypeDef:
    pass
```

### delete_dashboard

Type annotations for `boto3.client("quicksight").delete_dashboard` method.

[Client.delete_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_dashboard)

```python
def delete_dashboard(
    self,
    AwsAccountId: str,
    DashboardId: str,
    VersionNumber: int = None
) -> DeleteDashboardResponseTypeDef:
    pass
```

### delete_data_set

Type annotations for `boto3.client("quicksight").delete_data_set` method.

[Client.delete_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_data_set)

```python
def delete_data_set(
    self,
    AwsAccountId: str,
    DataSetId: str
) -> DeleteDataSetResponseTypeDef:
    pass
```

### delete_data_source

Type annotations for `boto3.client("quicksight").delete_data_source` method.

[Client.delete_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_data_source)

```python
def delete_data_source(
    self,
    AwsAccountId: str,
    DataSourceId: str
) -> DeleteDataSourceResponseTypeDef:
    pass
```

### delete_group

Type annotations for `boto3.client("quicksight").delete_group` method.

[Client.delete_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_group)

```python
def delete_group(
    self,
    GroupName: str,
    AwsAccountId: str,
    Namespace: str
) -> DeleteGroupResponseTypeDef:
    pass
```

### delete_group_membership

Type annotations for `boto3.client("quicksight").delete_group_membership` method.

[Client.delete_group_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_group_membership)

```python
def delete_group_membership(
    self,
    MemberName: str,
    GroupName: str,
    AwsAccountId: str,
    Namespace: str
) -> DeleteGroupMembershipResponseTypeDef:
    pass
```

### delete_iam_policy_assignment

Type annotations for `boto3.client("quicksight").delete_iam_policy_assignment` method.

[Client.delete_iam_policy_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_iam_policy_assignment)

```python
def delete_iam_policy_assignment(
    self,
    AwsAccountId: str,
    AssignmentName: str,
    Namespace: str
) -> DeleteIAMPolicyAssignmentResponseTypeDef:
    pass
```

### delete_namespace

Type annotations for `boto3.client("quicksight").delete_namespace` method.

[Client.delete_namespace documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_namespace)

```python
def delete_namespace(
    self,
    AwsAccountId: str,
    Namespace: str
) -> DeleteNamespaceResponseTypeDef:
    pass
```

### delete_template

Type annotations for `boto3.client("quicksight").delete_template` method.

[Client.delete_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_template)

```python
def delete_template(
    self,
    AwsAccountId: str,
    TemplateId: str,
    VersionNumber: int = None
) -> DeleteTemplateResponseTypeDef:
    pass
```

### delete_template_alias

Type annotations for `boto3.client("quicksight").delete_template_alias` method.

[Client.delete_template_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_template_alias)

```python
def delete_template_alias(
    self,
    AwsAccountId: str,
    TemplateId: str,
    AliasName: str
) -> DeleteTemplateAliasResponseTypeDef:
    pass
```

### delete_theme

Type annotations for `boto3.client("quicksight").delete_theme` method.

[Client.delete_theme documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_theme)

```python
def delete_theme(
    self,
    AwsAccountId: str,
    ThemeId: str,
    VersionNumber: int = None
) -> DeleteThemeResponseTypeDef:
    pass
```

### delete_theme_alias

Type annotations for `boto3.client("quicksight").delete_theme_alias` method.

[Client.delete_theme_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_theme_alias)

```python
def delete_theme_alias(
    self,
    AwsAccountId: str,
    ThemeId: str,
    AliasName: str
) -> DeleteThemeAliasResponseTypeDef:
    pass
```

### delete_user

Type annotations for `boto3.client("quicksight").delete_user` method.

[Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_user)

```python
def delete_user(
    self,
    UserName: str,
    AwsAccountId: str,
    Namespace: str
) -> DeleteUserResponseTypeDef:
    pass
```

### delete_user_by_principal_id

Type annotations for `boto3.client("quicksight").delete_user_by_principal_id` method.

[Client.delete_user_by_principal_id documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_user_by_principal_id)

```python
def delete_user_by_principal_id(
    self,
    PrincipalId: str,
    AwsAccountId: str,
    Namespace: str
) -> DeleteUserByPrincipalIdResponseTypeDef:
    pass
```

### describe_account_customization

Type annotations for `boto3.client("quicksight").describe_account_customization` method.

[Client.describe_account_customization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_account_customization)

```python
def describe_account_customization(
    self,
    AwsAccountId: str,
    Namespace: str = None,
    Resolved: bool = None
) -> DescribeAccountCustomizationResponseTypeDef:
    pass
```

### describe_account_settings

Type annotations for `boto3.client("quicksight").describe_account_settings` method.

[Client.describe_account_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_account_settings)

```python
def describe_account_settings(
    self,
    AwsAccountId: str
) -> DescribeAccountSettingsResponseTypeDef:
    pass
```

### describe_analysis

Type annotations for `boto3.client("quicksight").describe_analysis` method.

[Client.describe_analysis documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_analysis)

```python
def describe_analysis(
    self,
    AwsAccountId: str,
    AnalysisId: str
) -> DescribeAnalysisResponseTypeDef:
    pass
```

### describe_analysis_permissions

Type annotations for `boto3.client("quicksight").describe_analysis_permissions` method.

[Client.describe_analysis_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_analysis_permissions)

```python
def describe_analysis_permissions(
    self,
    AwsAccountId: str,
    AnalysisId: str
) -> DescribeAnalysisPermissionsResponseTypeDef:
    pass
```

### describe_dashboard

Type annotations for `boto3.client("quicksight").describe_dashboard` method.

[Client.describe_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_dashboard)

```python
def describe_dashboard(
    self,
    AwsAccountId: str,
    DashboardId: str,
    VersionNumber: int = None,
    AliasName: str = None
) -> DescribeDashboardResponseTypeDef:
    pass
```

### describe_dashboard_permissions

Type annotations for `boto3.client("quicksight").describe_dashboard_permissions` method.

[Client.describe_dashboard_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_dashboard_permissions)

```python
def describe_dashboard_permissions(
    self,
    AwsAccountId: str,
    DashboardId: str
) -> DescribeDashboardPermissionsResponseTypeDef:
    pass
```

### describe_data_set

Type annotations for `boto3.client("quicksight").describe_data_set` method.

[Client.describe_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_data_set)

```python
def describe_data_set(
    self,
    AwsAccountId: str,
    DataSetId: str
) -> DescribeDataSetResponseTypeDef:
    pass
```

### describe_data_set_permissions

Type annotations for `boto3.client("quicksight").describe_data_set_permissions` method.

[Client.describe_data_set_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_data_set_permissions)

```python
def describe_data_set_permissions(
    self,
    AwsAccountId: str,
    DataSetId: str
) -> DescribeDataSetPermissionsResponseTypeDef:
    pass
```

### describe_data_source

Type annotations for `boto3.client("quicksight").describe_data_source` method.

[Client.describe_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_data_source)

```python
def describe_data_source(
    self,
    AwsAccountId: str,
    DataSourceId: str
) -> DescribeDataSourceResponseTypeDef:
    pass
```

### describe_data_source_permissions

Type annotations for `boto3.client("quicksight").describe_data_source_permissions` method.

[Client.describe_data_source_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_data_source_permissions)

```python
def describe_data_source_permissions(
    self,
    AwsAccountId: str,
    DataSourceId: str
) -> DescribeDataSourcePermissionsResponseTypeDef:
    pass
```

### describe_group

Type annotations for `boto3.client("quicksight").describe_group` method.

[Client.describe_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_group)

```python
def describe_group(
    self,
    GroupName: str,
    AwsAccountId: str,
    Namespace: str
) -> DescribeGroupResponseTypeDef:
    pass
```

### describe_iam_policy_assignment

Type annotations for `boto3.client("quicksight").describe_iam_policy_assignment` method.

[Client.describe_iam_policy_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_iam_policy_assignment)

```python
def describe_iam_policy_assignment(
    self,
    AwsAccountId: str,
    AssignmentName: str,
    Namespace: str
) -> DescribeIAMPolicyAssignmentResponseTypeDef:
    pass
```

### describe_ingestion

Type annotations for `boto3.client("quicksight").describe_ingestion` method.

[Client.describe_ingestion documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_ingestion)

```python
def describe_ingestion(
    self,
    AwsAccountId: str,
    DataSetId: str,
    IngestionId: str
) -> DescribeIngestionResponseTypeDef:
    pass
```

### describe_namespace

Type annotations for `boto3.client("quicksight").describe_namespace` method.

[Client.describe_namespace documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_namespace)

```python
def describe_namespace(
    self,
    AwsAccountId: str,
    Namespace: str
) -> DescribeNamespaceResponseTypeDef:
    pass
```

### describe_template

Type annotations for `boto3.client("quicksight").describe_template` method.

[Client.describe_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_template)

```python
def describe_template(
    self,
    AwsAccountId: str,
    TemplateId: str,
    VersionNumber: int = None,
    AliasName: str = None
) -> DescribeTemplateResponseTypeDef:
    pass
```

### describe_template_alias

Type annotations for `boto3.client("quicksight").describe_template_alias` method.

[Client.describe_template_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_template_alias)

```python
def describe_template_alias(
    self,
    AwsAccountId: str,
    TemplateId: str,
    AliasName: str
) -> DescribeTemplateAliasResponseTypeDef:
    pass
```

### describe_template_permissions

Type annotations for `boto3.client("quicksight").describe_template_permissions` method.

[Client.describe_template_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_template_permissions)

```python
def describe_template_permissions(
    self,
    AwsAccountId: str,
    TemplateId: str
) -> DescribeTemplatePermissionsResponseTypeDef:
    pass
```

### describe_theme

Type annotations for `boto3.client("quicksight").describe_theme` method.

[Client.describe_theme documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_theme)

```python
def describe_theme(
    self,
    AwsAccountId: str,
    ThemeId: str,
    VersionNumber: int = None,
    AliasName: str = None
) -> DescribeThemeResponseTypeDef:
    pass
```

### describe_theme_alias

Type annotations for `boto3.client("quicksight").describe_theme_alias` method.

[Client.describe_theme_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_theme_alias)

```python
def describe_theme_alias(
    self,
    AwsAccountId: str,
    ThemeId: str,
    AliasName: str
) -> DescribeThemeAliasResponseTypeDef:
    pass
```

### describe_theme_permissions

Type annotations for `boto3.client("quicksight").describe_theme_permissions` method.

[Client.describe_theme_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_theme_permissions)

```python
def describe_theme_permissions(
    self,
    AwsAccountId: str,
    ThemeId: str
) -> DescribeThemePermissionsResponseTypeDef:
    pass
```

### describe_user

Type annotations for `boto3.client("quicksight").describe_user` method.

[Client.describe_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_user)

```python
def describe_user(
    self,
    UserName: str,
    AwsAccountId: str,
    Namespace: str
) -> DescribeUserResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("quicksight").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.generate_presigned_url)

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

### get_dashboard_embed_url

Type annotations for `boto3.client("quicksight").get_dashboard_embed_url` method.

[Client.get_dashboard_embed_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_dashboard_embed_url)

```python
def get_dashboard_embed_url(
    self,
    AwsAccountId: str,
    DashboardId: str,
    IdentityType: EmbeddingIdentityType,
    SessionLifetimeInMinutes: int = None,
    UndoRedoDisabled: bool = None,
    ResetDisabled: bool = None,
    StatePersistenceEnabled: bool = None,
    UserArn: str = None,
    Namespace: str = None,
    AdditionalDashboardIds: List[str] = None
) -> GetDashboardEmbedUrlResponseTypeDef:
    pass
```

### get_session_embed_url

Type annotations for `boto3.client("quicksight").get_session_embed_url` method.

[Client.get_session_embed_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_session_embed_url)

```python
def get_session_embed_url(
    self,
    AwsAccountId: str,
    EntryPoint: str = None,
    SessionLifetimeInMinutes: int = None,
    UserArn: str = None
) -> GetSessionEmbedUrlResponseTypeDef:
    pass
```

### list_analyses

Type annotations for `boto3.client("quicksight").list_analyses` method.

[Client.list_analyses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_analyses)

```python
def list_analyses(
    self,
    AwsAccountId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListAnalysesResponseTypeDef:
    pass
```

### list_dashboard_versions

Type annotations for `boto3.client("quicksight").list_dashboard_versions` method.

[Client.list_dashboard_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_dashboard_versions)

```python
def list_dashboard_versions(
    self,
    AwsAccountId: str,
    DashboardId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListDashboardVersionsResponseTypeDef:
    pass
```

### list_dashboards

Type annotations for `boto3.client("quicksight").list_dashboards` method.

[Client.list_dashboards documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_dashboards)

```python
def list_dashboards(
    self,
    AwsAccountId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListDashboardsResponseTypeDef:
    pass
```

### list_data_sets

Type annotations for `boto3.client("quicksight").list_data_sets` method.

[Client.list_data_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_data_sets)

```python
def list_data_sets(
    self,
    AwsAccountId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListDataSetsResponseTypeDef:
    pass
```

### list_data_sources

Type annotations for `boto3.client("quicksight").list_data_sources` method.

[Client.list_data_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_data_sources)

```python
def list_data_sources(
    self,
    AwsAccountId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListDataSourcesResponseTypeDef:
    pass
```

### list_group_memberships

Type annotations for `boto3.client("quicksight").list_group_memberships` method.

[Client.list_group_memberships documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_group_memberships)

```python
def list_group_memberships(
    self,
    GroupName: str,
    AwsAccountId: str,
    Namespace: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListGroupMembershipsResponseTypeDef:
    pass
```

### list_groups

Type annotations for `boto3.client("quicksight").list_groups` method.

[Client.list_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_groups)

```python
def list_groups(
    self,
    AwsAccountId: str,
    Namespace: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListGroupsResponseTypeDef:
    pass
```

### list_iam_policy_assignments

Type annotations for `boto3.client("quicksight").list_iam_policy_assignments` method.

[Client.list_iam_policy_assignments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_iam_policy_assignments)

```python
def list_iam_policy_assignments(
    self,
    AwsAccountId: str,
    Namespace: str,
    AssignmentStatus: AssignmentStatus = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListIAMPolicyAssignmentsResponseTypeDef:
    pass
```

### list_iam_policy_assignments_for_user

Type annotations for `boto3.client("quicksight").list_iam_policy_assignments_for_user` method.

[Client.list_iam_policy_assignments_for_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_iam_policy_assignments_for_user)

```python
def list_iam_policy_assignments_for_user(
    self,
    AwsAccountId: str,
    UserName: str,
    Namespace: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListIAMPolicyAssignmentsForUserResponseTypeDef:
    pass
```

### list_ingestions

Type annotations for `boto3.client("quicksight").list_ingestions` method.

[Client.list_ingestions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_ingestions)

```python
def list_ingestions(
    self,
    DataSetId: str,
    AwsAccountId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListIngestionsResponseTypeDef:
    pass
```

### list_namespaces

Type annotations for `boto3.client("quicksight").list_namespaces` method.

[Client.list_namespaces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_namespaces)

```python
def list_namespaces(
    self,
    AwsAccountId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListNamespacesResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("quicksight").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_template_aliases

Type annotations for `boto3.client("quicksight").list_template_aliases` method.

[Client.list_template_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_template_aliases)

```python
def list_template_aliases(
    self,
    AwsAccountId: str,
    TemplateId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListTemplateAliasesResponseTypeDef:
    pass
```

### list_template_versions

Type annotations for `boto3.client("quicksight").list_template_versions` method.

[Client.list_template_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_template_versions)

```python
def list_template_versions(
    self,
    AwsAccountId: str,
    TemplateId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListTemplateVersionsResponseTypeDef:
    pass
```

### list_templates

Type annotations for `boto3.client("quicksight").list_templates` method.

[Client.list_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_templates)

```python
def list_templates(
    self,
    AwsAccountId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListTemplatesResponseTypeDef:
    pass
```

### list_theme_aliases

Type annotations for `boto3.client("quicksight").list_theme_aliases` method.

[Client.list_theme_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_theme_aliases)

```python
def list_theme_aliases(
    self,
    AwsAccountId: str,
    ThemeId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListThemeAliasesResponseTypeDef:
    pass
```

### list_theme_versions

Type annotations for `boto3.client("quicksight").list_theme_versions` method.

[Client.list_theme_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_theme_versions)

```python
def list_theme_versions(
    self,
    AwsAccountId: str,
    ThemeId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListThemeVersionsResponseTypeDef:
    pass
```

### list_themes

Type annotations for `boto3.client("quicksight").list_themes` method.

[Client.list_themes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_themes)

```python
def list_themes(
    self,
    AwsAccountId: str,
    NextToken: str = None,
    MaxResults: int = None,
    Type: ThemeType = None
) -> ListThemesResponseTypeDef:
    pass
```

### list_user_groups

Type annotations for `boto3.client("quicksight").list_user_groups` method.

[Client.list_user_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_user_groups)

```python
def list_user_groups(
    self,
    UserName: str,
    AwsAccountId: str,
    Namespace: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListUserGroupsResponseTypeDef:
    pass
```

### list_users

Type annotations for `boto3.client("quicksight").list_users` method.

[Client.list_users documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_users)

```python
def list_users(
    self,
    AwsAccountId: str,
    Namespace: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListUsersResponseTypeDef:
    pass
```

### register_user

Type annotations for `boto3.client("quicksight").register_user` method.

[Client.register_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.register_user)

```python
def register_user(
    self,
    IdentityType: IdentityType,
    Email: str,
    UserRole: UserRole,
    AwsAccountId: str,
    Namespace: str,
    IamArn: str = None,
    SessionName: str = None,
    UserName: str = None,
    CustomPermissionsName: str = None
) -> RegisterUserResponseTypeDef:
    pass
```

### restore_analysis

Type annotations for `boto3.client("quicksight").restore_analysis` method.

[Client.restore_analysis documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.restore_analysis)

```python
def restore_analysis(
    self,
    AwsAccountId: str,
    AnalysisId: str
) -> RestoreAnalysisResponseTypeDef:
    pass
```

### search_analyses

Type annotations for `boto3.client("quicksight").search_analyses` method.

[Client.search_analyses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.search_analyses)

```python
def search_analyses(
    self,
    AwsAccountId: str,
    Filters: List[AnalysisSearchFilterTypeDef],
    NextToken: str = None,
    MaxResults: int = None
) -> SearchAnalysesResponseTypeDef:
    pass
```

### search_dashboards

Type annotations for `boto3.client("quicksight").search_dashboards` method.

[Client.search_dashboards documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.search_dashboards)

```python
def search_dashboards(
    self,
    AwsAccountId: str,
    Filters: List[DashboardSearchFilterTypeDef],
    NextToken: str = None,
    MaxResults: int = None
) -> SearchDashboardsResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("quicksight").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: List["TagTypeDef"]
) -> TagResourceResponseTypeDef:
    pass
```

### untag_resource

Type annotations for `boto3.client("quicksight").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> UntagResourceResponseTypeDef:
    pass
```

### update_account_customization

Type annotations for `boto3.client("quicksight").update_account_customization` method.

[Client.update_account_customization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_account_customization)

```python
def update_account_customization(
    self,
    AwsAccountId: str,
    AccountCustomization: "AccountCustomizationTypeDef",
    Namespace: str = None
) -> UpdateAccountCustomizationResponseTypeDef:
    pass
```

### update_account_settings

Type annotations for `boto3.client("quicksight").update_account_settings` method.

[Client.update_account_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_account_settings)

```python
def update_account_settings(
    self,
    AwsAccountId: str,
    DefaultNamespace: str,
    NotificationEmail: str = None
) -> UpdateAccountSettingsResponseTypeDef:
    pass
```

### update_analysis

Type annotations for `boto3.client("quicksight").update_analysis` method.

[Client.update_analysis documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_analysis)

```python
def update_analysis(
    self,
    AwsAccountId: str,
    AnalysisId: str,
    Name: str,
    SourceEntity: AnalysisSourceEntityTypeDef,
    Parameters: ParametersTypeDef = None,
    ThemeArn: str = None
) -> UpdateAnalysisResponseTypeDef:
    pass
```

### update_analysis_permissions

Type annotations for `boto3.client("quicksight").update_analysis_permissions` method.

[Client.update_analysis_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_analysis_permissions)

```python
def update_analysis_permissions(
    self,
    AwsAccountId: str,
    AnalysisId: str,
    GrantPermissions: List["ResourcePermissionTypeDef"] = None,
    RevokePermissions: List["ResourcePermissionTypeDef"] = None
) -> UpdateAnalysisPermissionsResponseTypeDef:
    pass
```

### update_dashboard

Type annotations for `boto3.client("quicksight").update_dashboard` method.

[Client.update_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_dashboard)

```python
def update_dashboard(
    self,
    AwsAccountId: str,
    DashboardId: str,
    Name: str,
    SourceEntity: DashboardSourceEntityTypeDef,
    Parameters: ParametersTypeDef = None,
    VersionDescription: str = None,
    DashboardPublishOptions: DashboardPublishOptionsTypeDef = None,
    ThemeArn: str = None
) -> UpdateDashboardResponseTypeDef:
    pass
```

### update_dashboard_permissions

Type annotations for `boto3.client("quicksight").update_dashboard_permissions` method.

[Client.update_dashboard_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_dashboard_permissions)

```python
def update_dashboard_permissions(
    self,
    AwsAccountId: str,
    DashboardId: str,
    GrantPermissions: List["ResourcePermissionTypeDef"] = None,
    RevokePermissions: List["ResourcePermissionTypeDef"] = None
) -> UpdateDashboardPermissionsResponseTypeDef:
    pass
```

### update_dashboard_published_version

Type annotations for `boto3.client("quicksight").update_dashboard_published_version` method.

[Client.update_dashboard_published_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_dashboard_published_version)

```python
def update_dashboard_published_version(
    self,
    AwsAccountId: str,
    DashboardId: str,
    VersionNumber: int
) -> UpdateDashboardPublishedVersionResponseTypeDef:
    pass
```

### update_data_set

Type annotations for `boto3.client("quicksight").update_data_set` method.

[Client.update_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_data_set)

```python
def update_data_set(
    self,
    AwsAccountId: str,
    DataSetId: str,
    Name: str,
    PhysicalTableMap: Dict[str, "PhysicalTableTypeDef"],
    ImportMode: DataSetImportMode,
    LogicalTableMap: Dict[str, "LogicalTableTypeDef"] = None,
    ColumnGroups: List["ColumnGroupTypeDef"] = None,
    FieldFolders: Dict[str, "FieldFolderTypeDef"] = None,
    RowLevelPermissionDataSet: "RowLevelPermissionDataSetTypeDef" = None,
    ColumnLevelPermissionRules: List["ColumnLevelPermissionRuleTypeDef"] = None
) -> UpdateDataSetResponseTypeDef:
    pass
```

### update_data_set_permissions

Type annotations for `boto3.client("quicksight").update_data_set_permissions` method.

[Client.update_data_set_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_data_set_permissions)

```python
def update_data_set_permissions(
    self,
    AwsAccountId: str,
    DataSetId: str,
    GrantPermissions: List["ResourcePermissionTypeDef"] = None,
    RevokePermissions: List["ResourcePermissionTypeDef"] = None
) -> UpdateDataSetPermissionsResponseTypeDef:
    pass
```

### update_data_source

Type annotations for `boto3.client("quicksight").update_data_source` method.

[Client.update_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_data_source)

```python
def update_data_source(
    self,
    AwsAccountId: str,
    DataSourceId: str,
    Name: str,
    DataSourceParameters: "DataSourceParametersTypeDef" = None,
    Credentials: DataSourceCredentialsTypeDef = None,
    VpcConnectionProperties: "VpcConnectionPropertiesTypeDef" = None,
    SslProperties: "SslPropertiesTypeDef" = None
) -> UpdateDataSourceResponseTypeDef:
    pass
```

### update_data_source_permissions

Type annotations for `boto3.client("quicksight").update_data_source_permissions` method.

[Client.update_data_source_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_data_source_permissions)

```python
def update_data_source_permissions(
    self,
    AwsAccountId: str,
    DataSourceId: str,
    GrantPermissions: List["ResourcePermissionTypeDef"] = None,
    RevokePermissions: List["ResourcePermissionTypeDef"] = None
) -> UpdateDataSourcePermissionsResponseTypeDef:
    pass
```

### update_group

Type annotations for `boto3.client("quicksight").update_group` method.

[Client.update_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_group)

```python
def update_group(
    self,
    GroupName: str,
    AwsAccountId: str,
    Namespace: str,
    Description: str = None
) -> UpdateGroupResponseTypeDef:
    pass
```

### update_iam_policy_assignment

Type annotations for `boto3.client("quicksight").update_iam_policy_assignment` method.

[Client.update_iam_policy_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_iam_policy_assignment)

```python
def update_iam_policy_assignment(
    self,
    AwsAccountId: str,
    AssignmentName: str,
    Namespace: str,
    AssignmentStatus: AssignmentStatus = None,
    PolicyArn: str = None,
    Identities: Dict[str, List[str]] = None
) -> UpdateIAMPolicyAssignmentResponseTypeDef:
    pass
```

### update_template

Type annotations for `boto3.client("quicksight").update_template` method.

[Client.update_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_template)

```python
def update_template(
    self,
    AwsAccountId: str,
    TemplateId: str,
    SourceEntity: TemplateSourceEntityTypeDef,
    VersionDescription: str = None,
    Name: str = None
) -> UpdateTemplateResponseTypeDef:
    pass
```

### update_template_alias

Type annotations for `boto3.client("quicksight").update_template_alias` method.

[Client.update_template_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_template_alias)

```python
def update_template_alias(
    self,
    AwsAccountId: str,
    TemplateId: str,
    AliasName: str,
    TemplateVersionNumber: int
) -> UpdateTemplateAliasResponseTypeDef:
    pass
```

### update_template_permissions

Type annotations for `boto3.client("quicksight").update_template_permissions` method.

[Client.update_template_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_template_permissions)

```python
def update_template_permissions(
    self,
    AwsAccountId: str,
    TemplateId: str,
    GrantPermissions: List["ResourcePermissionTypeDef"] = None,
    RevokePermissions: List["ResourcePermissionTypeDef"] = None
) -> UpdateTemplatePermissionsResponseTypeDef:
    pass
```

### update_theme

Type annotations for `boto3.client("quicksight").update_theme` method.

[Client.update_theme documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_theme)

```python
def update_theme(
    self,
    AwsAccountId: str,
    ThemeId: str,
    BaseThemeId: str,
    Name: str = None,
    VersionDescription: str = None,
    Configuration: "ThemeConfigurationTypeDef" = None
) -> UpdateThemeResponseTypeDef:
    pass
```

### update_theme_alias

Type annotations for `boto3.client("quicksight").update_theme_alias` method.

[Client.update_theme_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_theme_alias)

```python
def update_theme_alias(
    self,
    AwsAccountId: str,
    ThemeId: str,
    AliasName: str,
    ThemeVersionNumber: int
) -> UpdateThemeAliasResponseTypeDef:
    pass
```

### update_theme_permissions

Type annotations for `boto3.client("quicksight").update_theme_permissions` method.

[Client.update_theme_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_theme_permissions)

```python
def update_theme_permissions(
    self,
    AwsAccountId: str,
    ThemeId: str,
    GrantPermissions: List["ResourcePermissionTypeDef"] = None,
    RevokePermissions: List["ResourcePermissionTypeDef"] = None
) -> UpdateThemePermissionsResponseTypeDef:
    pass
```

### update_user

Type annotations for `boto3.client("quicksight").update_user` method.

[Client.update_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_user)

```python
def update_user(
    self,
    UserName: str,
    AwsAccountId: str,
    Namespace: str,
    Email: str,
    Role: UserRole,
    CustomPermissionsName: str = None,
    UnapplyCustomPermissions: bool = None
) -> UpdateUserResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("quicksight").get_paginator` method with overloads.

- `client.get_paginator("list_analyses")` -> [ListAnalysesPaginator](./paginators.md#listanalysespaginator)
- `client.get_paginator("list_dashboard_versions")` -> [ListDashboardVersionsPaginator](./paginators.md#listdashboardversionspaginator)
- `client.get_paginator("list_dashboards")` -> [ListDashboardsPaginator](./paginators.md#listdashboardspaginator)
- `client.get_paginator("list_data_sets")` -> [ListDataSetsPaginator](./paginators.md#listdatasetspaginator)
- `client.get_paginator("list_data_sources")` -> [ListDataSourcesPaginator](./paginators.md#listdatasourcespaginator)
- `client.get_paginator("list_ingestions")` -> [ListIngestionsPaginator](./paginators.md#listingestionspaginator)
- `client.get_paginator("list_namespaces")` -> [ListNamespacesPaginator](./paginators.md#listnamespacespaginator)
- `client.get_paginator("list_template_aliases")` -> [ListTemplateAliasesPaginator](./paginators.md#listtemplatealiasespaginator)
- `client.get_paginator("list_template_versions")` -> [ListTemplateVersionsPaginator](./paginators.md#listtemplateversionspaginator)
- `client.get_paginator("list_templates")` -> [ListTemplatesPaginator](./paginators.md#listtemplatespaginator)
- `client.get_paginator("list_theme_versions")` -> [ListThemeVersionsPaginator](./paginators.md#listthemeversionspaginator)
- `client.get_paginator("list_themes")` -> [ListThemesPaginator](./paginators.md#listthemespaginator)
- `client.get_paginator("search_analyses")` -> [SearchAnalysesPaginator](./paginators.md#searchanalysespaginator)
- `client.get_paginator("search_dashboards")` -> [SearchDashboardsPaginator](./paginators.md#searchdashboardspaginator)


