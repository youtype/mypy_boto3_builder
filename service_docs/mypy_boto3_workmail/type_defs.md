# Structures for boto3 WorkMail module

> [Index](../index.md) > [WorkMail](./index.md) > Structures

Auto-generated documentation for [WorkMail](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail)
type annotations stubs module [mypy_boto3_workmail](https://pypi.org/project/mypy-boto3-workmail/).

- [Structures for boto3 WorkMail module](#structures-for-boto3-workmail-module)
  - [AccessControlRuleTypeDef](#accesscontrolruletypedef)
  - [BookingOptionsTypeDef](#bookingoptionstypedef)
  - [CreateGroupResponseTypeDef](#creategroupresponsetypedef)
  - [CreateMobileDeviceAccessRuleResponseTypeDef](#createmobiledeviceaccessruleresponsetypedef)
  - [CreateOrganizationResponseTypeDef](#createorganizationresponsetypedef)
  - [CreateResourceResponseTypeDef](#createresourceresponsetypedef)
  - [CreateUserResponseTypeDef](#createuserresponsetypedef)
  - [DelegateTypeDef](#delegatetypedef)
  - [DeleteOrganizationResponseTypeDef](#deleteorganizationresponsetypedef)
  - [DescribeGroupResponseTypeDef](#describegroupresponsetypedef)
  - [DescribeMailboxExportJobResponseTypeDef](#describemailboxexportjobresponsetypedef)
  - [DescribeOrganizationResponseTypeDef](#describeorganizationresponsetypedef)
  - [DescribeResourceResponseTypeDef](#describeresourceresponsetypedef)
  - [DescribeUserResponseTypeDef](#describeuserresponsetypedef)
  - [DomainTypeDef](#domaintypedef)
  - [FolderConfigurationTypeDef](#folderconfigurationtypedef)
  - [GetAccessControlEffectResponseTypeDef](#getaccesscontroleffectresponsetypedef)
  - [GetDefaultRetentionPolicyResponseTypeDef](#getdefaultretentionpolicyresponsetypedef)
  - [GetMailboxDetailsResponseTypeDef](#getmailboxdetailsresponsetypedef)
  - [GetMobileDeviceAccessEffectResponseTypeDef](#getmobiledeviceaccesseffectresponsetypedef)
  - [GroupTypeDef](#grouptypedef)
  - [ListAccessControlRulesResponseTypeDef](#listaccesscontrolrulesresponsetypedef)
  - [ListAliasesResponseTypeDef](#listaliasesresponsetypedef)
  - [ListGroupMembersResponseTypeDef](#listgroupmembersresponsetypedef)
  - [ListGroupsResponseTypeDef](#listgroupsresponsetypedef)
  - [ListMailboxExportJobsResponseTypeDef](#listmailboxexportjobsresponsetypedef)
  - [ListMailboxPermissionsResponseTypeDef](#listmailboxpermissionsresponsetypedef)
  - [ListMobileDeviceAccessRulesResponseTypeDef](#listmobiledeviceaccessrulesresponsetypedef)
  - [ListOrganizationsResponseTypeDef](#listorganizationsresponsetypedef)
  - [ListResourceDelegatesResponseTypeDef](#listresourcedelegatesresponsetypedef)
  - [ListResourcesResponseTypeDef](#listresourcesresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListUsersResponseTypeDef](#listusersresponsetypedef)
  - [MailboxExportJobTypeDef](#mailboxexportjobtypedef)
  - [MemberTypeDef](#membertypedef)
  - [MobileDeviceAccessMatchedRuleTypeDef](#mobiledeviceaccessmatchedruletypedef)
  - [MobileDeviceAccessRuleTypeDef](#mobiledeviceaccessruletypedef)
  - [OrganizationSummaryTypeDef](#organizationsummarytypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PermissionTypeDef](#permissiontypedef)
  - [ResourceTypeDef](#resourcetypedef)
  - [StartMailboxExportJobResponseTypeDef](#startmailboxexportjobresponsetypedef)
  - [TagTypeDef](#tagtypedef)
  - [UserTypeDef](#usertypedef)

## AccessControlRuleTypeDef

```python
from mypy_boto3_workmail.type_defs import AccessControlRuleTypeDef
```




Optional fields:
- `Name`: `str`
- `Effect`: `AccessControlRuleEffect`
- `Description`: `str`
- `IpRanges`: `List[str]`
- `NotIpRanges`: `List[str]`
- `Actions`: `List[str]`
- `NotActions`: `List[str]`
- `UserIds`: `List[str]`
- `NotUserIds`: `List[str]`
- `DateCreated`: `datetime`
- `DateModified`: `datetime`


## BookingOptionsTypeDef

```python
from mypy_boto3_workmail.type_defs import BookingOptionsTypeDef
```




Optional fields:
- `AutoAcceptRequests`: `bool`
- `AutoDeclineRecurringRequests`: `bool`
- `AutoDeclineConflictingRequests`: `bool`


## CreateGroupResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import CreateGroupResponseTypeDef
```




Optional fields:
- `GroupId`: `str`


## CreateMobileDeviceAccessRuleResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import CreateMobileDeviceAccessRuleResponseTypeDef
```




Optional fields:
- `MobileDeviceAccessRuleId`: `str`


## CreateOrganizationResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import CreateOrganizationResponseTypeDef
```




Optional fields:
- `OrganizationId`: `str`


## CreateResourceResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import CreateResourceResponseTypeDef
```




Optional fields:
- `ResourceId`: `str`


## CreateUserResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import CreateUserResponseTypeDef
```




Optional fields:
- `UserId`: `str`


## DelegateTypeDef

```python
from mypy_boto3_workmail.type_defs import DelegateTypeDef
```


Required fields:
- `Id`: `str`
- `Type`: `MemberType`




## DeleteOrganizationResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import DeleteOrganizationResponseTypeDef
```




Optional fields:
- `OrganizationId`: `str`
- `State`: `str`


## DescribeGroupResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import DescribeGroupResponseTypeDef
```




Optional fields:
- `GroupId`: `str`
- `Name`: `str`
- `Email`: `str`
- `State`: `EntityState`
- `EnabledDate`: `datetime`
- `DisabledDate`: `datetime`


## DescribeMailboxExportJobResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import DescribeMailboxExportJobResponseTypeDef
```




Optional fields:
- `EntityId`: `str`
- `Description`: `str`
- `RoleArn`: `str`
- `KmsKeyArn`: `str`
- `S3BucketName`: `str`
- `S3Prefix`: `str`
- `S3Path`: `str`
- `EstimatedProgress`: `int`
- `State`: `MailboxExportJobState`
- `ErrorInfo`: `str`
- `StartTime`: `datetime`
- `EndTime`: `datetime`


## DescribeOrganizationResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import DescribeOrganizationResponseTypeDef
```




Optional fields:
- `OrganizationId`: `str`
- `Alias`: `str`
- `State`: `str`
- `DirectoryId`: `str`
- `DirectoryType`: `str`
- `DefaultMailDomain`: `str`
- `CompletedDate`: `datetime`
- `ErrorMessage`: `str`
- `ARN`: `str`


## DescribeResourceResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import DescribeResourceResponseTypeDef
```




Optional fields:
- `ResourceId`: `str`
- `Email`: `str`
- `Name`: `str`
- `Type`: `ResourceType`
- `BookingOptions`: `"BookingOptionsTypeDef"`
- `State`: `EntityState`
- `EnabledDate`: `datetime`
- `DisabledDate`: `datetime`


## DescribeUserResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import DescribeUserResponseTypeDef
```




Optional fields:
- `UserId`: `str`
- `Name`: `str`
- `Email`: `str`
- `DisplayName`: `str`
- `State`: `EntityState`
- `UserRole`: `UserRole`
- `EnabledDate`: `datetime`
- `DisabledDate`: `datetime`


## DomainTypeDef

```python
from mypy_boto3_workmail.type_defs import DomainTypeDef
```




Optional fields:
- `DomainName`: `str`
- `HostedZoneId`: `str`


## FolderConfigurationTypeDef

```python
from mypy_boto3_workmail.type_defs import FolderConfigurationTypeDef
```


Required fields:
- `Name`: `FolderName`
- `Action`: `RetentionAction`



Optional fields:
- `Period`: `int`


## GetAccessControlEffectResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import GetAccessControlEffectResponseTypeDef
```




Optional fields:
- `Effect`: `AccessControlRuleEffect`
- `MatchedRules`: `List[str]`


## GetDefaultRetentionPolicyResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import GetDefaultRetentionPolicyResponseTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `Description`: `str`
- `FolderConfigurations`: `List["FolderConfigurationTypeDef"]`


## GetMailboxDetailsResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import GetMailboxDetailsResponseTypeDef
```




Optional fields:
- `MailboxQuota`: `int`
- `MailboxSize`: `float`


## GetMobileDeviceAccessEffectResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import GetMobileDeviceAccessEffectResponseTypeDef
```




Optional fields:
- `Effect`: `MobileDeviceAccessRuleEffect`
- `MatchedRules`: `List["MobileDeviceAccessMatchedRuleTypeDef"]`


## GroupTypeDef

```python
from mypy_boto3_workmail.type_defs import GroupTypeDef
```




Optional fields:
- `Id`: `str`
- `Email`: `str`
- `Name`: `str`
- `State`: `EntityState`
- `EnabledDate`: `datetime`
- `DisabledDate`: `datetime`


## ListAccessControlRulesResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import ListAccessControlRulesResponseTypeDef
```




Optional fields:
- `Rules`: `List["AccessControlRuleTypeDef"]`


## ListAliasesResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import ListAliasesResponseTypeDef
```




Optional fields:
- `Aliases`: `List[str]`
- `NextToken`: `str`


## ListGroupMembersResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import ListGroupMembersResponseTypeDef
```




Optional fields:
- `Members`: `List["MemberTypeDef"]`
- `NextToken`: `str`


## ListGroupsResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import ListGroupsResponseTypeDef
```




Optional fields:
- `Groups`: `List["GroupTypeDef"]`
- `NextToken`: `str`


## ListMailboxExportJobsResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import ListMailboxExportJobsResponseTypeDef
```




Optional fields:
- `Jobs`: `List["MailboxExportJobTypeDef"]`
- `NextToken`: `str`


## ListMailboxPermissionsResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import ListMailboxPermissionsResponseTypeDef
```




Optional fields:
- `Permissions`: `List["PermissionTypeDef"]`
- `NextToken`: `str`


## ListMobileDeviceAccessRulesResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import ListMobileDeviceAccessRulesResponseTypeDef
```




Optional fields:
- `Rules`: `List["MobileDeviceAccessRuleTypeDef"]`


## ListOrganizationsResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import ListOrganizationsResponseTypeDef
```




Optional fields:
- `OrganizationSummaries`: `List["OrganizationSummaryTypeDef"]`
- `NextToken`: `str`


## ListResourceDelegatesResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import ListResourceDelegatesResponseTypeDef
```




Optional fields:
- `Delegates`: `List["DelegateTypeDef"]`
- `NextToken`: `str`


## ListResourcesResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import ListResourcesResponseTypeDef
```




Optional fields:
- `Resources`: `List["ResourceTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`


## ListUsersResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import ListUsersResponseTypeDef
```




Optional fields:
- `Users`: `List["UserTypeDef"]`
- `NextToken`: `str`


## MailboxExportJobTypeDef

```python
from mypy_boto3_workmail.type_defs import MailboxExportJobTypeDef
```




Optional fields:
- `JobId`: `str`
- `EntityId`: `str`
- `Description`: `str`
- `S3BucketName`: `str`
- `S3Path`: `str`
- `EstimatedProgress`: `int`
- `State`: `MailboxExportJobState`
- `StartTime`: `datetime`
- `EndTime`: `datetime`


## MemberTypeDef

```python
from mypy_boto3_workmail.type_defs import MemberTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `Type`: `MemberType`
- `State`: `EntityState`
- `EnabledDate`: `datetime`
- `DisabledDate`: `datetime`


## MobileDeviceAccessMatchedRuleTypeDef

```python
from mypy_boto3_workmail.type_defs import MobileDeviceAccessMatchedRuleTypeDef
```




Optional fields:
- `MobileDeviceAccessRuleId`: `str`
- `Name`: `str`


## MobileDeviceAccessRuleTypeDef

```python
from mypy_boto3_workmail.type_defs import MobileDeviceAccessRuleTypeDef
```




Optional fields:
- `MobileDeviceAccessRuleId`: `str`
- `Name`: `str`
- `Description`: `str`
- `Effect`: `MobileDeviceAccessRuleEffect`
- `DeviceTypes`: `List[str]`
- `NotDeviceTypes`: `List[str]`
- `DeviceModels`: `List[str]`
- `NotDeviceModels`: `List[str]`
- `DeviceOperatingSystems`: `List[str]`
- `NotDeviceOperatingSystems`: `List[str]`
- `DeviceUserAgents`: `List[str]`
- `NotDeviceUserAgents`: `List[str]`
- `DateCreated`: `datetime`
- `DateModified`: `datetime`


## OrganizationSummaryTypeDef

```python
from mypy_boto3_workmail.type_defs import OrganizationSummaryTypeDef
```




Optional fields:
- `OrganizationId`: `str`
- `Alias`: `str`
- `DefaultMailDomain`: `str`
- `ErrorMessage`: `str`
- `State`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_workmail.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PermissionTypeDef

```python
from mypy_boto3_workmail.type_defs import PermissionTypeDef
```


Required fields:
- `GranteeId`: `str`
- `GranteeType`: `MemberType`
- `PermissionValues`: `List[PermissionType]`




## ResourceTypeDef

```python
from mypy_boto3_workmail.type_defs import ResourceTypeDef
```




Optional fields:
- `Id`: `str`
- `Email`: `str`
- `Name`: `str`
- `Type`: `ResourceType`
- `State`: `EntityState`
- `EnabledDate`: `datetime`
- `DisabledDate`: `datetime`


## StartMailboxExportJobResponseTypeDef

```python
from mypy_boto3_workmail.type_defs import StartMailboxExportJobResponseTypeDef
```




Optional fields:
- `JobId`: `str`


## TagTypeDef

```python
from mypy_boto3_workmail.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## UserTypeDef

```python
from mypy_boto3_workmail.type_defs import UserTypeDef
```




Optional fields:
- `Id`: `str`
- `Email`: `str`
- `Name`: `str`
- `DisplayName`: `str`
- `State`: `EntityState`
- `UserRole`: `UserRole`
- `EnabledDate`: `datetime`
- `DisabledDate`: `datetime`

