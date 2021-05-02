# Structures for boto3 AccessAnalyzer module

> [Index](../index.md) > [AccessAnalyzer](./index.md) > Structures

Auto-generated documentation for [AccessAnalyzer](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer)
type annotations stubs module [mypy_boto3_accessanalyzer](https://pypi.org/project/mypy-boto3-accessanalyzer/).

- [Structures for boto3 AccessAnalyzer module](#structures-for-boto3-accessanalyzer-module)
  - [AccessPreviewFindingTypeDef](#accesspreviewfindingtypedef)
  - [AccessPreviewStatusReasonTypeDef](#accesspreviewstatusreasontypedef)
  - [AccessPreviewSummaryTypeDef](#accesspreviewsummarytypedef)
  - [AccessPreviewTypeDef](#accesspreviewtypedef)
  - [AclGranteeTypeDef](#aclgranteetypedef)
  - [AnalyzedResourceSummaryTypeDef](#analyzedresourcesummarytypedef)
  - [AnalyzedResourceTypeDef](#analyzedresourcetypedef)
  - [AnalyzerSummaryTypeDef](#analyzersummarytypedef)
  - [ArchiveRuleSummaryTypeDef](#archiverulesummarytypedef)
  - [CloudTrailDetailsTypeDef](#cloudtraildetailstypedef)
  - [CloudTrailPropertiesTypeDef](#cloudtrailpropertiestypedef)
  - [ConfigurationTypeDef](#configurationtypedef)
  - [CreateAccessPreviewResponseTypeDef](#createaccesspreviewresponsetypedef)
  - [CreateAnalyzerResponseTypeDef](#createanalyzerresponsetypedef)
  - [CriterionTypeDef](#criteriontypedef)
  - [FindingSourceDetailTypeDef](#findingsourcedetailtypedef)
  - [FindingSourceTypeDef](#findingsourcetypedef)
  - [FindingSummaryTypeDef](#findingsummarytypedef)
  - [FindingTypeDef](#findingtypedef)
  - [GeneratedPolicyPropertiesTypeDef](#generatedpolicypropertiestypedef)
  - [GeneratedPolicyResultTypeDef](#generatedpolicyresulttypedef)
  - [GeneratedPolicyTypeDef](#generatedpolicytypedef)
  - [GetAccessPreviewResponseTypeDef](#getaccesspreviewresponsetypedef)
  - [GetAnalyzedResourceResponseTypeDef](#getanalyzedresourceresponsetypedef)
  - [GetAnalyzerResponseTypeDef](#getanalyzerresponsetypedef)
  - [GetArchiveRuleResponseTypeDef](#getarchiveruleresponsetypedef)
  - [GetFindingResponseTypeDef](#getfindingresponsetypedef)
  - [GetGeneratedPolicyResponseTypeDef](#getgeneratedpolicyresponsetypedef)
  - [IamRoleConfigurationTypeDef](#iamroleconfigurationtypedef)
  - [InlineArchiveRuleTypeDef](#inlinearchiveruletypedef)
  - [JobDetailsTypeDef](#jobdetailstypedef)
  - [JobErrorTypeDef](#joberrortypedef)
  - [KmsGrantConfigurationTypeDef](#kmsgrantconfigurationtypedef)
  - [KmsGrantConstraintsTypeDef](#kmsgrantconstraintstypedef)
  - [KmsKeyConfigurationTypeDef](#kmskeyconfigurationtypedef)
  - [ListAccessPreviewFindingsResponseTypeDef](#listaccesspreviewfindingsresponsetypedef)
  - [ListAccessPreviewsResponseTypeDef](#listaccesspreviewsresponsetypedef)
  - [ListAnalyzedResourcesResponseTypeDef](#listanalyzedresourcesresponsetypedef)
  - [ListAnalyzersResponseTypeDef](#listanalyzersresponsetypedef)
  - [ListArchiveRulesResponseTypeDef](#listarchiverulesresponsetypedef)
  - [ListFindingsResponseTypeDef](#listfindingsresponsetypedef)
  - [ListPolicyGenerationsResponseTypeDef](#listpolicygenerationsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [LocationTypeDef](#locationtypedef)
  - [NetworkOriginConfigurationTypeDef](#networkoriginconfigurationtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PathElementTypeDef](#pathelementtypedef)
  - [PolicyGenerationDetailsTypeDef](#policygenerationdetailstypedef)
  - [PolicyGenerationTypeDef](#policygenerationtypedef)
  - [PositionTypeDef](#positiontypedef)
  - [S3AccessPointConfigurationTypeDef](#s3accesspointconfigurationtypedef)
  - [S3BucketAclGrantConfigurationTypeDef](#s3bucketaclgrantconfigurationtypedef)
  - [S3BucketConfigurationTypeDef](#s3bucketconfigurationtypedef)
  - [S3PublicAccessBlockConfigurationTypeDef](#s3publicaccessblockconfigurationtypedef)
  - [SecretsManagerSecretConfigurationTypeDef](#secretsmanagersecretconfigurationtypedef)
  - [SortCriteriaTypeDef](#sortcriteriatypedef)
  - [SpanTypeDef](#spantypedef)
  - [SqsQueueConfigurationTypeDef](#sqsqueueconfigurationtypedef)
  - [StartPolicyGenerationResponseTypeDef](#startpolicygenerationresponsetypedef)
  - [StatusReasonTypeDef](#statusreasontypedef)
  - [SubstringTypeDef](#substringtypedef)
  - [TrailPropertiesTypeDef](#trailpropertiestypedef)
  - [TrailTypeDef](#trailtypedef)
  - [ValidatePolicyFindingTypeDef](#validatepolicyfindingtypedef)
  - [ValidatePolicyResponseTypeDef](#validatepolicyresponsetypedef)
  - [VpcConfigurationTypeDef](#vpcconfigurationtypedef)

## AccessPreviewFindingTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import AccessPreviewFindingTypeDef
```


Required fields:
- `changeType`: `FindingChangeType`
- `createdAt`: `datetime`
- `id`: `str`
- `resourceOwnerAccount`: `str`
- `resourceType`: `ResourceType`
- `status`: `FindingStatus`



Optional fields:
- `action`: `List[str]`
- `condition`: `Dict[str, str]`
- `error`: `str`
- `existingFindingId`: `str`
- `existingFindingStatus`: `FindingStatus`
- `isPublic`: `bool`
- `principal`: `Dict[str, str]`
- `resource`: `str`
- `sources`: `List["FindingSourceTypeDef"]`


## AccessPreviewStatusReasonTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import AccessPreviewStatusReasonTypeDef
```


Required fields:
- `code`: `AccessPreviewStatusReasonCode`




## AccessPreviewSummaryTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import AccessPreviewSummaryTypeDef
```


Required fields:
- `analyzerArn`: `str`
- `createdAt`: `datetime`
- `id`: `str`
- `status`: `AccessPreviewStatus`



Optional fields:
- `statusReason`: `"AccessPreviewStatusReasonTypeDef"`


## AccessPreviewTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import AccessPreviewTypeDef
```


Required fields:
- `analyzerArn`: `str`
- `configurations`: `Dict[str, "ConfigurationTypeDef"]`
- `createdAt`: `datetime`
- `id`: `str`
- `status`: `AccessPreviewStatus`



Optional fields:
- `statusReason`: `"AccessPreviewStatusReasonTypeDef"`


## AclGranteeTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import AclGranteeTypeDef
```




Optional fields:
- `id`: `str`
- `uri`: `str`


## AnalyzedResourceSummaryTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import AnalyzedResourceSummaryTypeDef
```


Required fields:
- `resourceArn`: `str`
- `resourceOwnerAccount`: `str`
- `resourceType`: `ResourceType`




## AnalyzedResourceTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import AnalyzedResourceTypeDef
```


Required fields:
- `analyzedAt`: `datetime`
- `createdAt`: `datetime`
- `isPublic`: `bool`
- `resourceArn`: `str`
- `resourceOwnerAccount`: `str`
- `resourceType`: `ResourceType`
- `updatedAt`: `datetime`



Optional fields:
- `actions`: `List[str]`
- `error`: `str`
- `sharedVia`: `List[str]`
- `status`: `FindingStatus`


## AnalyzerSummaryTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import AnalyzerSummaryTypeDef
```


Required fields:
- `arn`: `str`
- `createdAt`: `datetime`
- `name`: `str`
- `status`: `AnalyzerStatus`
- `type`: `TypeType`



Optional fields:
- `lastResourceAnalyzed`: `str`
- `lastResourceAnalyzedAt`: `datetime`
- `statusReason`: `"StatusReasonTypeDef"`
- `tags`: `Dict[str, str]`


## ArchiveRuleSummaryTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import ArchiveRuleSummaryTypeDef
```


Required fields:
- `createdAt`: `datetime`
- `filter`: `Dict[str, "CriterionTypeDef"]`
- `ruleName`: `str`
- `updatedAt`: `datetime`




## CloudTrailDetailsTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import CloudTrailDetailsTypeDef
```


Required fields:
- `accessRole`: `str`
- `startTime`: `datetime`
- `trails`: `List["TrailTypeDef"]`



Optional fields:
- `endTime`: `datetime`


## CloudTrailPropertiesTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import CloudTrailPropertiesTypeDef
```


Required fields:
- `endTime`: `datetime`
- `startTime`: `datetime`
- `trailProperties`: `List["TrailPropertiesTypeDef"]`




## ConfigurationTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import ConfigurationTypeDef
```




Optional fields:
- `iamRole`: `"IamRoleConfigurationTypeDef"`
- `kmsKey`: `"KmsKeyConfigurationTypeDef"`
- `s3Bucket`: `"S3BucketConfigurationTypeDef"`
- `secretsManagerSecret`: `"SecretsManagerSecretConfigurationTypeDef"`
- `sqsQueue`: `"SqsQueueConfigurationTypeDef"`


## CreateAccessPreviewResponseTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import CreateAccessPreviewResponseTypeDef
```


Required fields:
- `id`: `str`




## CreateAnalyzerResponseTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import CreateAnalyzerResponseTypeDef
```




Optional fields:
- `arn`: `str`


## CriterionTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import CriterionTypeDef
```




Optional fields:
- `contains`: `List[str]`
- `eq`: `List[str]`
- `exists`: `bool`
- `neq`: `List[str]`


## FindingSourceDetailTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import FindingSourceDetailTypeDef
```




Optional fields:
- `accessPointArn`: `str`


## FindingSourceTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import FindingSourceTypeDef
```


Required fields:
- `type`: `FindingSourceType`



Optional fields:
- `detail`: `"FindingSourceDetailTypeDef"`


## FindingSummaryTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import FindingSummaryTypeDef
```


Required fields:
- `analyzedAt`: `datetime`
- `condition`: `Dict[str, str]`
- `createdAt`: `datetime`
- `id`: `str`
- `resourceOwnerAccount`: `str`
- `resourceType`: `ResourceType`
- `status`: `FindingStatus`
- `updatedAt`: `datetime`



Optional fields:
- `action`: `List[str]`
- `error`: `str`
- `isPublic`: `bool`
- `principal`: `Dict[str, str]`
- `resource`: `str`
- `sources`: `List["FindingSourceTypeDef"]`


## FindingTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import FindingTypeDef
```


Required fields:
- `analyzedAt`: `datetime`
- `condition`: `Dict[str, str]`
- `createdAt`: `datetime`
- `id`: `str`
- `resourceOwnerAccount`: `str`
- `resourceType`: `ResourceType`
- `status`: `FindingStatus`
- `updatedAt`: `datetime`



Optional fields:
- `action`: `List[str]`
- `error`: `str`
- `isPublic`: `bool`
- `principal`: `Dict[str, str]`
- `resource`: `str`
- `sources`: `List["FindingSourceTypeDef"]`


## GeneratedPolicyPropertiesTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import GeneratedPolicyPropertiesTypeDef
```


Required fields:
- `principalArn`: `str`



Optional fields:
- `cloudTrailProperties`: `"CloudTrailPropertiesTypeDef"`
- `isComplete`: `bool`


## GeneratedPolicyResultTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import GeneratedPolicyResultTypeDef
```


Required fields:
- `properties`: `"GeneratedPolicyPropertiesTypeDef"`



Optional fields:
- `generatedPolicies`: `List["GeneratedPolicyTypeDef"]`


## GeneratedPolicyTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import GeneratedPolicyTypeDef
```


Required fields:
- `policy`: `str`




## GetAccessPreviewResponseTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import GetAccessPreviewResponseTypeDef
```


Required fields:
- `accessPreview`: `"AccessPreviewTypeDef"`




## GetAnalyzedResourceResponseTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import GetAnalyzedResourceResponseTypeDef
```




Optional fields:
- `resource`: `"AnalyzedResourceTypeDef"`


## GetAnalyzerResponseTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import GetAnalyzerResponseTypeDef
```


Required fields:
- `analyzer`: `"AnalyzerSummaryTypeDef"`




## GetArchiveRuleResponseTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import GetArchiveRuleResponseTypeDef
```


Required fields:
- `archiveRule`: `"ArchiveRuleSummaryTypeDef"`




## GetFindingResponseTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import GetFindingResponseTypeDef
```




Optional fields:
- `finding`: `"FindingTypeDef"`


## GetGeneratedPolicyResponseTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import GetGeneratedPolicyResponseTypeDef
```


Required fields:
- `generatedPolicyResult`: `"GeneratedPolicyResultTypeDef"`
- `jobDetails`: `"JobDetailsTypeDef"`




## IamRoleConfigurationTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import IamRoleConfigurationTypeDef
```




Optional fields:
- `trustPolicy`: `str`


## InlineArchiveRuleTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import InlineArchiveRuleTypeDef
```


Required fields:
- `filter`: `Dict[str, "CriterionTypeDef"]`
- `ruleName`: `str`




## JobDetailsTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import JobDetailsTypeDef
```


Required fields:
- `jobId`: `str`
- `startedOn`: `datetime`
- `status`: `JobStatus`



Optional fields:
- `completedOn`: `datetime`
- `jobError`: `"JobErrorTypeDef"`


## JobErrorTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import JobErrorTypeDef
```


Required fields:
- `code`: `JobErrorCode`
- `message`: `str`




## KmsGrantConfigurationTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import KmsGrantConfigurationTypeDef
```


Required fields:
- `granteePrincipal`: `str`
- `issuingAccount`: `str`
- `operations`: `List[KmsGrantOperation]`



Optional fields:
- `constraints`: `"KmsGrantConstraintsTypeDef"`
- `retiringPrincipal`: `str`


## KmsGrantConstraintsTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import KmsGrantConstraintsTypeDef
```




Optional fields:
- `encryptionContextEquals`: `Dict[str, str]`
- `encryptionContextSubset`: `Dict[str, str]`


## KmsKeyConfigurationTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import KmsKeyConfigurationTypeDef
```




Optional fields:
- `grants`: `List["KmsGrantConfigurationTypeDef"]`
- `keyPolicies`: `Dict[str, str]`


## ListAccessPreviewFindingsResponseTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import ListAccessPreviewFindingsResponseTypeDef
```


Required fields:
- `findings`: `List["AccessPreviewFindingTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListAccessPreviewsResponseTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import ListAccessPreviewsResponseTypeDef
```


Required fields:
- `accessPreviews`: `List["AccessPreviewSummaryTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListAnalyzedResourcesResponseTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import ListAnalyzedResourcesResponseTypeDef
```


Required fields:
- `analyzedResources`: `List["AnalyzedResourceSummaryTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListAnalyzersResponseTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import ListAnalyzersResponseTypeDef
```


Required fields:
- `analyzers`: `List["AnalyzerSummaryTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListArchiveRulesResponseTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import ListArchiveRulesResponseTypeDef
```


Required fields:
- `archiveRules`: `List["ArchiveRuleSummaryTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListFindingsResponseTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import ListFindingsResponseTypeDef
```


Required fields:
- `findings`: `List["FindingSummaryTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListPolicyGenerationsResponseTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import ListPolicyGenerationsResponseTypeDef
```


Required fields:
- `policyGenerations`: `List["PolicyGenerationTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `Dict[str, str]`


## LocationTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import LocationTypeDef
```


Required fields:
- `path`: `List["PathElementTypeDef"]`
- `span`: `"SpanTypeDef"`




## NetworkOriginConfigurationTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import NetworkOriginConfigurationTypeDef
```




Optional fields:
- `internetConfiguration`: `Dict[str, Any]`
- `vpcConfiguration`: `"VpcConfigurationTypeDef"`


## PaginatorConfigTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PathElementTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import PathElementTypeDef
```




Optional fields:
- `index`: `int`
- `key`: `str`
- `substring`: `"SubstringTypeDef"`
- `value`: `str`


## PolicyGenerationDetailsTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import PolicyGenerationDetailsTypeDef
```


Required fields:
- `principalArn`: `str`




## PolicyGenerationTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import PolicyGenerationTypeDef
```


Required fields:
- `jobId`: `str`
- `principalArn`: `str`
- `startedOn`: `datetime`
- `status`: `JobStatus`



Optional fields:
- `completedOn`: `datetime`


## PositionTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import PositionTypeDef
```


Required fields:
- `column`: `int`
- `line`: `int`
- `offset`: `int`




## S3AccessPointConfigurationTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import S3AccessPointConfigurationTypeDef
```




Optional fields:
- `accessPointPolicy`: `str`
- `networkOrigin`: `"NetworkOriginConfigurationTypeDef"`
- `publicAccessBlock`: `"S3PublicAccessBlockConfigurationTypeDef"`


## S3BucketAclGrantConfigurationTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import S3BucketAclGrantConfigurationTypeDef
```


Required fields:
- `grantee`: `"AclGranteeTypeDef"`
- `permission`: `AclPermission`




## S3BucketConfigurationTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import S3BucketConfigurationTypeDef
```




Optional fields:
- `accessPoints`: `Dict[str, "S3AccessPointConfigurationTypeDef"]`
- `bucketAclGrants`: `List["S3BucketAclGrantConfigurationTypeDef"]`
- `bucketPolicy`: `str`
- `bucketPublicAccessBlock`: `"S3PublicAccessBlockConfigurationTypeDef"`


## S3PublicAccessBlockConfigurationTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import S3PublicAccessBlockConfigurationTypeDef
```


Required fields:
- `ignorePublicAcls`: `bool`
- `restrictPublicBuckets`: `bool`




## SecretsManagerSecretConfigurationTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import SecretsManagerSecretConfigurationTypeDef
```




Optional fields:
- `kmsKeyId`: `str`
- `secretPolicy`: `str`


## SortCriteriaTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import SortCriteriaTypeDef
```




Optional fields:
- `attributeName`: `str`
- `orderBy`: `OrderBy`


## SpanTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import SpanTypeDef
```


Required fields:
- `end`: `"PositionTypeDef"`
- `start`: `"PositionTypeDef"`




## SqsQueueConfigurationTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import SqsQueueConfigurationTypeDef
```




Optional fields:
- `queuePolicy`: `str`


## StartPolicyGenerationResponseTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import StartPolicyGenerationResponseTypeDef
```


Required fields:
- `jobId`: `str`




## StatusReasonTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import StatusReasonTypeDef
```


Required fields:
- `code`: `ReasonCode`




## SubstringTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import SubstringTypeDef
```


Required fields:
- `length`: `int`
- `start`: `int`




## TrailPropertiesTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import TrailPropertiesTypeDef
```


Required fields:
- `cloudTrailArn`: `str`



Optional fields:
- `allRegions`: `bool`
- `regions`: `List[str]`


## TrailTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import TrailTypeDef
```


Required fields:
- `cloudTrailArn`: `str`



Optional fields:
- `allRegions`: `bool`
- `regions`: `List[str]`


## ValidatePolicyFindingTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import ValidatePolicyFindingTypeDef
```


Required fields:
- `findingDetails`: `str`
- `findingType`: `ValidatePolicyFindingType`
- `issueCode`: `str`
- `learnMoreLink`: `str`
- `locations`: `List["LocationTypeDef"]`




## ValidatePolicyResponseTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import ValidatePolicyResponseTypeDef
```


Required fields:
- `findings`: `List["ValidatePolicyFindingTypeDef"]`



Optional fields:
- `nextToken`: `str`


## VpcConfigurationTypeDef

```python
from mypy_boto3_accessanalyzer.type_defs import VpcConfigurationTypeDef
```


Required fields:
- `vpcId`: `str`



