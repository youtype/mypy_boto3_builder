# Structures for boto3 ElasticBeanstalk module

> [Index](../index.md) > [ElasticBeanstalk](./index.md) > Structures

Auto-generated documentation for [ElasticBeanstalk](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk)
type annotations stubs module [mypy_boto3_elasticbeanstalk](https://pypi.org/project/mypy-boto3-elasticbeanstalk/).

- [Structures for boto3 ElasticBeanstalk module](#structures-for-boto3-elasticbeanstalk-module)
  - [ApplicationDescriptionTypeDef](#applicationdescriptiontypedef)
  - [ApplicationMetricsTypeDef](#applicationmetricstypedef)
  - [ApplicationResourceLifecycleConfigTypeDef](#applicationresourcelifecycleconfigtypedef)
  - [ApplicationVersionDescriptionTypeDef](#applicationversiondescriptiontypedef)
  - [ApplicationVersionLifecycleConfigTypeDef](#applicationversionlifecycleconfigtypedef)
  - [AutoScalingGroupTypeDef](#autoscalinggrouptypedef)
  - [BuilderTypeDef](#buildertypedef)
  - [CPUUtilizationTypeDef](#cpuutilizationtypedef)
  - [ConfigurationOptionDescriptionTypeDef](#configurationoptiondescriptiontypedef)
  - [ConfigurationOptionSettingTypeDef](#configurationoptionsettingtypedef)
  - [ConfigurationSettingsDescriptionTypeDef](#configurationsettingsdescriptiontypedef)
  - [CustomAmiTypeDef](#customamitypedef)
  - [DeploymentTypeDef](#deploymenttypedef)
  - [EnvironmentDescriptionTypeDef](#environmentdescriptiontypedef)
  - [EnvironmentInfoDescriptionTypeDef](#environmentinfodescriptiontypedef)
  - [EnvironmentLinkTypeDef](#environmentlinktypedef)
  - [EnvironmentResourceDescriptionTypeDef](#environmentresourcedescriptiontypedef)
  - [EnvironmentResourcesDescriptionTypeDef](#environmentresourcesdescriptiontypedef)
  - [EnvironmentTierTypeDef](#environmenttiertypedef)
  - [EventDescriptionTypeDef](#eventdescriptiontypedef)
  - [InstanceHealthSummaryTypeDef](#instancehealthsummarytypedef)
  - [InstanceTypeDef](#instancetypedef)
  - [LatencyTypeDef](#latencytypedef)
  - [LaunchConfigurationTypeDef](#launchconfigurationtypedef)
  - [LaunchTemplateTypeDef](#launchtemplatetypedef)
  - [ListenerTypeDef](#listenertypedef)
  - [LoadBalancerDescriptionTypeDef](#loadbalancerdescriptiontypedef)
  - [LoadBalancerTypeDef](#loadbalancertypedef)
  - [ManagedActionHistoryItemTypeDef](#managedactionhistoryitemtypedef)
  - [ManagedActionTypeDef](#managedactiontypedef)
  - [MaxAgeRuleTypeDef](#maxageruletypedef)
  - [MaxCountRuleTypeDef](#maxcountruletypedef)
  - [OptionRestrictionRegexTypeDef](#optionrestrictionregextypedef)
  - [PlatformBranchSummaryTypeDef](#platformbranchsummarytypedef)
  - [PlatformDescriptionTypeDef](#platformdescriptiontypedef)
  - [PlatformFrameworkTypeDef](#platformframeworktypedef)
  - [PlatformProgrammingLanguageTypeDef](#platformprogramminglanguagetypedef)
  - [PlatformSummaryTypeDef](#platformsummarytypedef)
  - [QueueTypeDef](#queuetypedef)
  - [ResourceQuotaTypeDef](#resourcequotatypedef)
  - [ResourceQuotasTypeDef](#resourcequotastypedef)
  - [S3LocationTypeDef](#s3locationtypedef)
  - [SingleInstanceHealthTypeDef](#singleinstancehealthtypedef)
  - [SolutionStackDescriptionTypeDef](#solutionstackdescriptiontypedef)
  - [SourceBuildInformationTypeDef](#sourcebuildinformationtypedef)
  - [StatusCodesTypeDef](#statuscodestypedef)
  - [SystemStatusTypeDef](#systemstatustypedef)
  - [TagTypeDef](#tagtypedef)
  - [TriggerTypeDef](#triggertypedef)
  - [ValidationMessageTypeDef](#validationmessagetypedef)
  - [ApplicationDescriptionMessageTypeDef](#applicationdescriptionmessagetypedef)
  - [ApplicationDescriptionsMessageTypeDef](#applicationdescriptionsmessagetypedef)
  - [ApplicationResourceLifecycleDescriptionMessageTypeDef](#applicationresourcelifecycledescriptionmessagetypedef)
  - [ApplicationVersionDescriptionMessageTypeDef](#applicationversiondescriptionmessagetypedef)
  - [ApplicationVersionDescriptionsMessageTypeDef](#applicationversiondescriptionsmessagetypedef)
  - [ApplyEnvironmentManagedActionResultTypeDef](#applyenvironmentmanagedactionresulttypedef)
  - [BuildConfigurationTypeDef](#buildconfigurationtypedef)
  - [CheckDNSAvailabilityResultMessageTypeDef](#checkdnsavailabilityresultmessagetypedef)
  - [ConfigurationOptionsDescriptionTypeDef](#configurationoptionsdescriptiontypedef)
  - [ConfigurationSettingsDescriptionsTypeDef](#configurationsettingsdescriptionstypedef)
  - [ConfigurationSettingsValidationMessagesTypeDef](#configurationsettingsvalidationmessagestypedef)
  - [CreatePlatformVersionResultTypeDef](#createplatformversionresulttypedef)
  - [CreateStorageLocationResultMessageTypeDef](#createstoragelocationresultmessagetypedef)
  - [DeletePlatformVersionResultTypeDef](#deleteplatformversionresulttypedef)
  - [DescribeAccountAttributesResultTypeDef](#describeaccountattributesresulttypedef)
  - [DescribeEnvironmentHealthResultTypeDef](#describeenvironmenthealthresulttypedef)
  - [DescribeEnvironmentManagedActionHistoryResultTypeDef](#describeenvironmentmanagedactionhistoryresulttypedef)
  - [DescribeEnvironmentManagedActionsResultTypeDef](#describeenvironmentmanagedactionsresulttypedef)
  - [DescribeInstancesHealthResultTypeDef](#describeinstanceshealthresulttypedef)
  - [DescribePlatformVersionResultTypeDef](#describeplatformversionresulttypedef)
  - [EnvironmentDescriptionsMessageTypeDef](#environmentdescriptionsmessagetypedef)
  - [EnvironmentResourceDescriptionsMessageTypeDef](#environmentresourcedescriptionsmessagetypedef)
  - [EventDescriptionsMessageTypeDef](#eventdescriptionsmessagetypedef)
  - [ListAvailableSolutionStacksResultMessageTypeDef](#listavailablesolutionstacksresultmessagetypedef)
  - [ListPlatformBranchesResultTypeDef](#listplatformbranchesresulttypedef)
  - [ListPlatformVersionsResultTypeDef](#listplatformversionsresulttypedef)
  - [OptionSpecificationTypeDef](#optionspecificationtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PlatformFilterTypeDef](#platformfiltertypedef)
  - [ResourceTagsDescriptionMessageTypeDef](#resourcetagsdescriptionmessagetypedef)
  - [RetrieveEnvironmentInfoResultMessageTypeDef](#retrieveenvironmentinforesultmessagetypedef)
  - [SearchFilterTypeDef](#searchfiltertypedef)
  - [SourceConfigurationTypeDef](#sourceconfigurationtypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## ApplicationDescriptionTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import ApplicationDescriptionTypeDef
```




Optional fields:
- `ApplicationArn`: `str`
- `ApplicationName`: `str`
- `Description`: `str`
- `DateCreated`: `datetime`
- `DateUpdated`: `datetime`
- `Versions`: `List[str]`
- `ConfigurationTemplates`: `List[str]`
- `ResourceLifecycleConfig`: `"ApplicationResourceLifecycleConfigTypeDef"`


## ApplicationMetricsTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import ApplicationMetricsTypeDef
```




Optional fields:
- `Duration`: `int`
- `RequestCount`: `int`
- `StatusCodes`: `"StatusCodesTypeDef"`
- `Latency`: `"LatencyTypeDef"`


## ApplicationResourceLifecycleConfigTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import ApplicationResourceLifecycleConfigTypeDef
```




Optional fields:
- `ServiceRole`: `str`
- `VersionLifecycleConfig`: `"ApplicationVersionLifecycleConfigTypeDef"`


## ApplicationVersionDescriptionTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import ApplicationVersionDescriptionTypeDef
```




Optional fields:
- `ApplicationVersionArn`: `str`
- `ApplicationName`: `str`
- `Description`: `str`
- `VersionLabel`: `str`
- `SourceBuildInformation`: `"SourceBuildInformationTypeDef"`
- `BuildArn`: `str`
- `SourceBundle`: `"S3LocationTypeDef"`
- `DateCreated`: `datetime`
- `DateUpdated`: `datetime`
- `Status`: `ApplicationVersionStatus`


## ApplicationVersionLifecycleConfigTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import ApplicationVersionLifecycleConfigTypeDef
```




Optional fields:
- `MaxCountRule`: `"MaxCountRuleTypeDef"`
- `MaxAgeRule`: `"MaxAgeRuleTypeDef"`


## AutoScalingGroupTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import AutoScalingGroupTypeDef
```




Optional fields:
- `Name`: `str`


## BuilderTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import BuilderTypeDef
```




Optional fields:
- `ARN`: `str`


## CPUUtilizationTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import CPUUtilizationTypeDef
```




Optional fields:
- `User`: `float`
- `Nice`: `float`
- `System`: `float`
- `Idle`: `float`
- `IOWait`: `float`
- `IRQ`: `float`
- `SoftIRQ`: `float`
- `Privileged`: `float`


## ConfigurationOptionDescriptionTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import ConfigurationOptionDescriptionTypeDef
```




Optional fields:
- `Namespace`: `str`
- `Name`: `str`
- `DefaultValue`: `str`
- `ChangeSeverity`: `str`
- `UserDefined`: `bool`
- `ValueType`: `ConfigurationOptionValueType`
- `ValueOptions`: `List[str]`
- `MinValue`: `int`
- `MaxValue`: `int`
- `MaxLength`: `int`
- `Regex`: `"OptionRestrictionRegexTypeDef"`


## ConfigurationOptionSettingTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import ConfigurationOptionSettingTypeDef
```




Optional fields:
- `ResourceName`: `str`
- `Namespace`: `str`
- `OptionName`: `str`
- `Value`: `str`


## ConfigurationSettingsDescriptionTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import ConfigurationSettingsDescriptionTypeDef
```




Optional fields:
- `SolutionStackName`: `str`
- `PlatformArn`: `str`
- `ApplicationName`: `str`
- `TemplateName`: `str`
- `Description`: `str`
- `EnvironmentName`: `str`
- `DeploymentStatus`: `ConfigurationDeploymentStatus`
- `DateCreated`: `datetime`
- `DateUpdated`: `datetime`
- `OptionSettings`: `List["ConfigurationOptionSettingTypeDef"]`


## CustomAmiTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import CustomAmiTypeDef
```




Optional fields:
- `VirtualizationType`: `str`
- `ImageId`: `str`


## DeploymentTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import DeploymentTypeDef
```




Optional fields:
- `VersionLabel`: `str`
- `DeploymentId`: `int`
- `Status`: `str`
- `DeploymentTime`: `datetime`


## EnvironmentDescriptionTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import EnvironmentDescriptionTypeDef
```




Optional fields:
- `EnvironmentName`: `str`
- `EnvironmentId`: `str`
- `ApplicationName`: `str`
- `VersionLabel`: `str`
- `SolutionStackName`: `str`
- `PlatformArn`: `str`
- `TemplateName`: `str`
- `Description`: `str`
- `EndpointURL`: `str`
- `CNAME`: `str`
- `DateCreated`: `datetime`
- `DateUpdated`: `datetime`
- `Status`: `EnvironmentStatus`
- `AbortableOperationInProgress`: `bool`
- `Health`: `EnvironmentHealth`
- `HealthStatus`: `EnvironmentHealthStatus`
- `Resources`: `"EnvironmentResourcesDescriptionTypeDef"`
- `Tier`: `"EnvironmentTierTypeDef"`
- `EnvironmentLinks`: `List["EnvironmentLinkTypeDef"]`
- `EnvironmentArn`: `str`
- `OperationsRole`: `str`


## EnvironmentInfoDescriptionTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import EnvironmentInfoDescriptionTypeDef
```




Optional fields:
- `InfoType`: `EnvironmentInfoType`
- `Ec2InstanceId`: `str`
- `SampleTimestamp`: `datetime`
- `Message`: `str`


## EnvironmentLinkTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import EnvironmentLinkTypeDef
```




Optional fields:
- `LinkName`: `str`
- `EnvironmentName`: `str`


## EnvironmentResourceDescriptionTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import EnvironmentResourceDescriptionTypeDef
```




Optional fields:
- `EnvironmentName`: `str`
- `AutoScalingGroups`: `List["AutoScalingGroupTypeDef"]`
- `Instances`: `List["InstanceTypeDef"]`
- `LaunchConfigurations`: `List["LaunchConfigurationTypeDef"]`
- `LaunchTemplates`: `List["LaunchTemplateTypeDef"]`
- `LoadBalancers`: `List["LoadBalancerTypeDef"]`
- `Triggers`: `List["TriggerTypeDef"]`
- `Queues`: `List["QueueTypeDef"]`


## EnvironmentResourcesDescriptionTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import EnvironmentResourcesDescriptionTypeDef
```




Optional fields:
- `LoadBalancer`: `"LoadBalancerDescriptionTypeDef"`


## EnvironmentTierTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import EnvironmentTierTypeDef
```




Optional fields:
- `Name`: `str`
- `Type`: `str`
- `Version`: `str`


## EventDescriptionTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import EventDescriptionTypeDef
```




Optional fields:
- `EventDate`: `datetime`
- `Message`: `str`
- `ApplicationName`: `str`
- `VersionLabel`: `str`
- `TemplateName`: `str`
- `EnvironmentName`: `str`
- `PlatformArn`: `str`
- `RequestId`: `str`
- `Severity`: `EventSeverity`


## InstanceHealthSummaryTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import InstanceHealthSummaryTypeDef
```




Optional fields:
- `NoData`: `int`
- `Unknown`: `int`
- `Pending`: `int`
- `Ok`: `int`
- `Info`: `int`
- `Warning`: `int`
- `Degraded`: `int`
- `Severe`: `int`


## InstanceTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import InstanceTypeDef
```




Optional fields:
- `Id`: `str`


## LatencyTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import LatencyTypeDef
```




Optional fields:
- `P999`: `float`
- `P99`: `float`
- `P95`: `float`
- `P90`: `float`
- `P85`: `float`
- `P75`: `float`
- `P50`: `float`
- `P10`: `float`


## LaunchConfigurationTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import LaunchConfigurationTypeDef
```




Optional fields:
- `Name`: `str`


## LaunchTemplateTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import LaunchTemplateTypeDef
```




Optional fields:
- `Id`: `str`


## ListenerTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import ListenerTypeDef
```




Optional fields:
- `Protocol`: `str`
- `Port`: `int`


## LoadBalancerDescriptionTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import LoadBalancerDescriptionTypeDef
```




Optional fields:
- `LoadBalancerName`: `str`
- `Domain`: `str`
- `Listeners`: `List["ListenerTypeDef"]`


## LoadBalancerTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import LoadBalancerTypeDef
```




Optional fields:
- `Name`: `str`


## ManagedActionHistoryItemTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import ManagedActionHistoryItemTypeDef
```




Optional fields:
- `ActionId`: `str`
- `ActionType`: `ActionType`
- `ActionDescription`: `str`
- `FailureType`: `FailureType`
- `Status`: `ActionHistoryStatus`
- `FailureDescription`: `str`
- `ExecutedTime`: `datetime`
- `FinishedTime`: `datetime`


## ManagedActionTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import ManagedActionTypeDef
```




Optional fields:
- `ActionId`: `str`
- `ActionDescription`: `str`
- `ActionType`: `ActionType`
- `Status`: `ActionStatus`
- `WindowStartTime`: `datetime`


## MaxAgeRuleTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import MaxAgeRuleTypeDef
```


Required fields:
- `Enabled`: `bool`



Optional fields:
- `MaxAgeInDays`: `int`
- `DeleteSourceFromS3`: `bool`


## MaxCountRuleTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import MaxCountRuleTypeDef
```


Required fields:
- `Enabled`: `bool`



Optional fields:
- `MaxCount`: `int`
- `DeleteSourceFromS3`: `bool`


## OptionRestrictionRegexTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import OptionRestrictionRegexTypeDef
```




Optional fields:
- `Pattern`: `str`
- `Label`: `str`


## PlatformBranchSummaryTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import PlatformBranchSummaryTypeDef
```




Optional fields:
- `PlatformName`: `str`
- `BranchName`: `str`
- `LifecycleState`: `str`
- `BranchOrder`: `int`
- `SupportedTierList`: `List[str]`


## PlatformDescriptionTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import PlatformDescriptionTypeDef
```




Optional fields:
- `PlatformArn`: `str`
- `PlatformOwner`: `str`
- `PlatformName`: `str`
- `PlatformVersion`: `str`
- `SolutionStackName`: `str`
- `PlatformStatus`: `PlatformStatus`
- `DateCreated`: `datetime`
- `DateUpdated`: `datetime`
- `PlatformCategory`: `str`
- `Description`: `str`
- `Maintainer`: `str`
- `OperatingSystemName`: `str`
- `OperatingSystemVersion`: `str`
- `ProgrammingLanguages`: `List["PlatformProgrammingLanguageTypeDef"]`
- `Frameworks`: `List["PlatformFrameworkTypeDef"]`
- `CustomAmiList`: `List["CustomAmiTypeDef"]`
- `SupportedTierList`: `List[str]`
- `SupportedAddonList`: `List[str]`
- `PlatformLifecycleState`: `str`
- `PlatformBranchName`: `str`
- `PlatformBranchLifecycleState`: `str`


## PlatformFrameworkTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import PlatformFrameworkTypeDef
```




Optional fields:
- `Name`: `str`
- `Version`: `str`


## PlatformProgrammingLanguageTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import PlatformProgrammingLanguageTypeDef
```




Optional fields:
- `Name`: `str`
- `Version`: `str`


## PlatformSummaryTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import PlatformSummaryTypeDef
```




Optional fields:
- `PlatformArn`: `str`
- `PlatformOwner`: `str`
- `PlatformStatus`: `PlatformStatus`
- `PlatformCategory`: `str`
- `OperatingSystemName`: `str`
- `OperatingSystemVersion`: `str`
- `SupportedTierList`: `List[str]`
- `SupportedAddonList`: `List[str]`
- `PlatformLifecycleState`: `str`
- `PlatformVersion`: `str`
- `PlatformBranchName`: `str`
- `PlatformBranchLifecycleState`: `str`


## QueueTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import QueueTypeDef
```




Optional fields:
- `Name`: `str`
- `URL`: `str`


## ResourceQuotaTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import ResourceQuotaTypeDef
```




Optional fields:
- `Maximum`: `int`


## ResourceQuotasTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import ResourceQuotasTypeDef
```




Optional fields:
- `ApplicationQuota`: `"ResourceQuotaTypeDef"`
- `ApplicationVersionQuota`: `"ResourceQuotaTypeDef"`
- `EnvironmentQuota`: `"ResourceQuotaTypeDef"`
- `ConfigurationTemplateQuota`: `"ResourceQuotaTypeDef"`
- `CustomPlatformQuota`: `"ResourceQuotaTypeDef"`


## S3LocationTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import S3LocationTypeDef
```




Optional fields:
- `S3Bucket`: `str`
- `S3Key`: `str`


## SingleInstanceHealthTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import SingleInstanceHealthTypeDef
```




Optional fields:
- `InstanceId`: `str`
- `HealthStatus`: `str`
- `Color`: `str`
- `Causes`: `List[str]`
- `LaunchedAt`: `datetime`
- `ApplicationMetrics`: `"ApplicationMetricsTypeDef"`
- `System`: `"SystemStatusTypeDef"`
- `Deployment`: `"DeploymentTypeDef"`
- `AvailabilityZone`: `str`
- `InstanceType`: `str`


## SolutionStackDescriptionTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import SolutionStackDescriptionTypeDef
```




Optional fields:
- `SolutionStackName`: `str`
- `PermittedFileTypes`: `List[str]`


## SourceBuildInformationTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import SourceBuildInformationTypeDef
```


Required fields:
- `SourceType`: `SourceType`
- `SourceRepository`: `SourceRepository`
- `SourceLocation`: `str`




## StatusCodesTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import StatusCodesTypeDef
```




Optional fields:
- `Status2xx`: `int`
- `Status3xx`: `int`
- `Status4xx`: `int`
- `Status5xx`: `int`


## SystemStatusTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import SystemStatusTypeDef
```




Optional fields:
- `CPUUtilization`: `"CPUUtilizationTypeDef"`
- `LoadAverage`: `List[float]`


## TagTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import TagTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## TriggerTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import TriggerTypeDef
```




Optional fields:
- `Name`: `str`


## ValidationMessageTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import ValidationMessageTypeDef
```




Optional fields:
- `Message`: `str`
- `Severity`: `ValidationSeverity`
- `Namespace`: `str`
- `OptionName`: `str`


## ApplicationDescriptionMessageTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import ApplicationDescriptionMessageTypeDef
```




Optional fields:
- `Application`: `"ApplicationDescriptionTypeDef"`


## ApplicationDescriptionsMessageTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import ApplicationDescriptionsMessageTypeDef
```




Optional fields:
- `Applications`: `List["ApplicationDescriptionTypeDef"]`


## ApplicationResourceLifecycleDescriptionMessageTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import ApplicationResourceLifecycleDescriptionMessageTypeDef
```




Optional fields:
- `ApplicationName`: `str`
- `ResourceLifecycleConfig`: `"ApplicationResourceLifecycleConfigTypeDef"`


## ApplicationVersionDescriptionMessageTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import ApplicationVersionDescriptionMessageTypeDef
```




Optional fields:
- `ApplicationVersion`: `"ApplicationVersionDescriptionTypeDef"`


## ApplicationVersionDescriptionsMessageTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import ApplicationVersionDescriptionsMessageTypeDef
```




Optional fields:
- `ApplicationVersions`: `List["ApplicationVersionDescriptionTypeDef"]`
- `NextToken`: `str`


## ApplyEnvironmentManagedActionResultTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import ApplyEnvironmentManagedActionResultTypeDef
```




Optional fields:
- `ActionId`: `str`
- `ActionDescription`: `str`
- `ActionType`: `ActionType`
- `Status`: `str`


## BuildConfigurationTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import BuildConfigurationTypeDef
```


Required fields:
- `CodeBuildServiceRole`: `str`
- `Image`: `str`



Optional fields:
- `ArtifactName`: `str`
- `ComputeType`: `ComputeType`
- `TimeoutInMinutes`: `int`


## CheckDNSAvailabilityResultMessageTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import CheckDNSAvailabilityResultMessageTypeDef
```




Optional fields:
- `Available`: `bool`
- `FullyQualifiedCNAME`: `str`


## ConfigurationOptionsDescriptionTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import ConfigurationOptionsDescriptionTypeDef
```




Optional fields:
- `SolutionStackName`: `str`
- `PlatformArn`: `str`
- `Options`: `List["ConfigurationOptionDescriptionTypeDef"]`


## ConfigurationSettingsDescriptionsTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import ConfigurationSettingsDescriptionsTypeDef
```




Optional fields:
- `ConfigurationSettings`: `List["ConfigurationSettingsDescriptionTypeDef"]`


## ConfigurationSettingsValidationMessagesTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import ConfigurationSettingsValidationMessagesTypeDef
```




Optional fields:
- `Messages`: `List["ValidationMessageTypeDef"]`


## CreatePlatformVersionResultTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import CreatePlatformVersionResultTypeDef
```




Optional fields:
- `PlatformSummary`: `"PlatformSummaryTypeDef"`
- `Builder`: `"BuilderTypeDef"`


## CreateStorageLocationResultMessageTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import CreateStorageLocationResultMessageTypeDef
```




Optional fields:
- `S3Bucket`: `str`


## DeletePlatformVersionResultTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import DeletePlatformVersionResultTypeDef
```




Optional fields:
- `PlatformSummary`: `"PlatformSummaryTypeDef"`


## DescribeAccountAttributesResultTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import DescribeAccountAttributesResultTypeDef
```




Optional fields:
- `ResourceQuotas`: `"ResourceQuotasTypeDef"`


## DescribeEnvironmentHealthResultTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import DescribeEnvironmentHealthResultTypeDef
```




Optional fields:
- `EnvironmentName`: `str`
- `HealthStatus`: `str`
- `Status`: `EnvironmentHealth`
- `Color`: `str`
- `Causes`: `List[str]`
- `ApplicationMetrics`: `"ApplicationMetricsTypeDef"`
- `InstancesHealth`: `"InstanceHealthSummaryTypeDef"`
- `RefreshedAt`: `datetime`


## DescribeEnvironmentManagedActionHistoryResultTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import DescribeEnvironmentManagedActionHistoryResultTypeDef
```




Optional fields:
- `ManagedActionHistoryItems`: `List["ManagedActionHistoryItemTypeDef"]`
- `NextToken`: `str`


## DescribeEnvironmentManagedActionsResultTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import DescribeEnvironmentManagedActionsResultTypeDef
```




Optional fields:
- `ManagedActions`: `List["ManagedActionTypeDef"]`


## DescribeInstancesHealthResultTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import DescribeInstancesHealthResultTypeDef
```




Optional fields:
- `InstanceHealthList`: `List["SingleInstanceHealthTypeDef"]`
- `RefreshedAt`: `datetime`
- `NextToken`: `str`


## DescribePlatformVersionResultTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import DescribePlatformVersionResultTypeDef
```




Optional fields:
- `PlatformDescription`: `"PlatformDescriptionTypeDef"`


## EnvironmentDescriptionsMessageTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import EnvironmentDescriptionsMessageTypeDef
```




Optional fields:
- `Environments`: `List["EnvironmentDescriptionTypeDef"]`
- `NextToken`: `str`


## EnvironmentResourceDescriptionsMessageTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import EnvironmentResourceDescriptionsMessageTypeDef
```




Optional fields:
- `EnvironmentResources`: `"EnvironmentResourceDescriptionTypeDef"`


## EventDescriptionsMessageTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import EventDescriptionsMessageTypeDef
```




Optional fields:
- `Events`: `List["EventDescriptionTypeDef"]`
- `NextToken`: `str`


## ListAvailableSolutionStacksResultMessageTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import ListAvailableSolutionStacksResultMessageTypeDef
```




Optional fields:
- `SolutionStacks`: `List[str]`
- `SolutionStackDetails`: `List["SolutionStackDescriptionTypeDef"]`


## ListPlatformBranchesResultTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import ListPlatformBranchesResultTypeDef
```




Optional fields:
- `PlatformBranchSummaryList`: `List["PlatformBranchSummaryTypeDef"]`
- `NextToken`: `str`


## ListPlatformVersionsResultTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import ListPlatformVersionsResultTypeDef
```




Optional fields:
- `PlatformSummaryList`: `List["PlatformSummaryTypeDef"]`
- `NextToken`: `str`


## OptionSpecificationTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import OptionSpecificationTypeDef
```




Optional fields:
- `ResourceName`: `str`
- `Namespace`: `str`
- `OptionName`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PlatformFilterTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import PlatformFilterTypeDef
```




Optional fields:
- `Type`: `str`
- `Operator`: `str`
- `Values`: `List[str]`


## ResourceTagsDescriptionMessageTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import ResourceTagsDescriptionMessageTypeDef
```




Optional fields:
- `ResourceArn`: `str`
- `ResourceTags`: `List["TagTypeDef"]`


## RetrieveEnvironmentInfoResultMessageTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import RetrieveEnvironmentInfoResultMessageTypeDef
```




Optional fields:
- `EnvironmentInfo`: `List["EnvironmentInfoDescriptionTypeDef"]`


## SearchFilterTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import SearchFilterTypeDef
```




Optional fields:
- `Attribute`: `str`
- `Operator`: `str`
- `Values`: `List[str]`


## SourceConfigurationTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import SourceConfigurationTypeDef
```




Optional fields:
- `ApplicationName`: `str`
- `TemplateName`: `str`


## WaiterConfigTypeDef

```python
from mypy_boto3_elasticbeanstalk.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

