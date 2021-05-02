# Literals for boto3 AccessAnalyzer module

> [Index](../index.md) > [AccessAnalyzer](./index.md) > Literals

Auto-generated documentation for [AccessAnalyzer](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer)
type annotations stubs module [mypy_boto3_accessanalyzer](https://pypi.org/project/mypy-boto3-accessanalyzer/).

- [Literals for boto3 AccessAnalyzer module](#literals-for-boto3-accessanalyzer-module)
  - [AccessPreviewStatus](#accesspreviewstatus)
  - [AccessPreviewStatusReasonCode](#accesspreviewstatusreasoncode)
  - [AclPermission](#aclpermission)
  - [AnalyzerStatus](#analyzerstatus)
  - [FindingChangeType](#findingchangetype)
  - [FindingSourceType](#findingsourcetype)
  - [FindingStatus](#findingstatus)
  - [FindingStatusUpdate](#findingstatusupdate)
  - [JobErrorCode](#joberrorcode)
  - [JobStatus](#jobstatus)
  - [KmsGrantOperation](#kmsgrantoperation)
  - [ListAccessPreviewFindingsPaginatorName](#listaccesspreviewfindingspaginatorname)
  - [ListAccessPreviewsPaginatorName](#listaccesspreviewspaginatorname)
  - [ListAnalyzedResourcesPaginatorName](#listanalyzedresourcespaginatorname)
  - [ListAnalyzersPaginatorName](#listanalyzerspaginatorname)
  - [ListArchiveRulesPaginatorName](#listarchiverulespaginatorname)
  - [ListFindingsPaginatorName](#listfindingspaginatorname)
  - [ListPolicyGenerationsPaginatorName](#listpolicygenerationspaginatorname)
  - [Locale](#locale)
  - [OrderBy](#orderby)
  - [PolicyType](#policytype)
  - [ReasonCode](#reasoncode)
  - [ResourceType](#resourcetype)
  - [TypeType](#typetype)
  - [ValidatePolicyFindingType](#validatepolicyfindingtype)
  - [ValidatePolicyPaginatorName](#validatepolicypaginatorname)

## AccessPreviewStatus

```python
from mypy_boto3_accessanalyzer.literals import AccessPreviewStatus
```

Values:

- `COMPLETED`
- `CREATING`
- `FAILED`

## AccessPreviewStatusReasonCode

```python
from mypy_boto3_accessanalyzer.literals import AccessPreviewStatusReasonCode
```

Values:

- `INTERNAL_ERROR`
- `INVALID_CONFIGURATION`

## AclPermission

```python
from mypy_boto3_accessanalyzer.literals import AclPermission
```

Values:

- `FULL_CONTROL`
- `READ`
- `READ_ACP`
- `WRITE`
- `WRITE_ACP`

## AnalyzerStatus

```python
from mypy_boto3_accessanalyzer.literals import AnalyzerStatus
```

Values:

- `ACTIVE`
- `CREATING`
- `DISABLED`
- `FAILED`

## FindingChangeType

```python
from mypy_boto3_accessanalyzer.literals import FindingChangeType
```

Values:

- `CHANGED`
- `NEW`
- `UNCHANGED`

## FindingSourceType

```python
from mypy_boto3_accessanalyzer.literals import FindingSourceType
```

Values:

- `BUCKET_ACL`
- `POLICY`
- `S3_ACCESS_POINT`

## FindingStatus

```python
from mypy_boto3_accessanalyzer.literals import FindingStatus
```

Values:

- `ACTIVE`
- `ARCHIVED`
- `RESOLVED`

## FindingStatusUpdate

```python
from mypy_boto3_accessanalyzer.literals import FindingStatusUpdate
```

Values:

- `ACTIVE`
- `ARCHIVED`

## JobErrorCode

```python
from mypy_boto3_accessanalyzer.literals import JobErrorCode
```

Values:

- `AUTHORIZATION_ERROR`
- `RESOURCE_NOT_FOUND_ERROR`
- `SERVICE_ERROR`
- `SERVICE_QUOTA_EXCEEDED_ERROR`

## JobStatus

```python
from mypy_boto3_accessanalyzer.literals import JobStatus
```

Values:

- `CANCELED`
- `FAILED`
- `IN_PROGRESS`
- `SUCCEEDED`

## KmsGrantOperation

```python
from mypy_boto3_accessanalyzer.literals import KmsGrantOperation
```

Values:

- `CreateGrant`
- `Decrypt`
- `DescribeKey`
- `Encrypt`
- `GenerateDataKey`
- `GenerateDataKeyPair`
- `GenerateDataKeyPairWithoutPlaintext`
- `GenerateDataKeyWithoutPlaintext`
- `GetPublicKey`
- `ReEncryptFrom`
- `ReEncryptTo`
- `RetireGrant`
- `Sign`
- `Verify`

## ListAccessPreviewFindingsPaginatorName

```python
from mypy_boto3_accessanalyzer.literals import ListAccessPreviewFindingsPaginatorName
```

Values:

- `list_access_preview_findings`

## ListAccessPreviewsPaginatorName

```python
from mypy_boto3_accessanalyzer.literals import ListAccessPreviewsPaginatorName
```

Values:

- `list_access_previews`

## ListAnalyzedResourcesPaginatorName

```python
from mypy_boto3_accessanalyzer.literals import ListAnalyzedResourcesPaginatorName
```

Values:

- `list_analyzed_resources`

## ListAnalyzersPaginatorName

```python
from mypy_boto3_accessanalyzer.literals import ListAnalyzersPaginatorName
```

Values:

- `list_analyzers`

## ListArchiveRulesPaginatorName

```python
from mypy_boto3_accessanalyzer.literals import ListArchiveRulesPaginatorName
```

Values:

- `list_archive_rules`

## ListFindingsPaginatorName

```python
from mypy_boto3_accessanalyzer.literals import ListFindingsPaginatorName
```

Values:

- `list_findings`

## ListPolicyGenerationsPaginatorName

```python
from mypy_boto3_accessanalyzer.literals import ListPolicyGenerationsPaginatorName
```

Values:

- `list_policy_generations`

## Locale

```python
from mypy_boto3_accessanalyzer.literals import Locale
```

Values:

- `DE`
- `EN`
- `ES`
- `FR`
- `IT`
- `JA`
- `KO`
- `PT_BR`
- `ZH_CN`
- `ZH_TW`

## OrderBy

```python
from mypy_boto3_accessanalyzer.literals import OrderBy
```

Values:

- `ASC`
- `DESC`

## PolicyType

```python
from mypy_boto3_accessanalyzer.literals import PolicyType
```

Values:

- `IDENTITY_POLICY`
- `RESOURCE_POLICY`
- `SERVICE_CONTROL_POLICY`

## ReasonCode

```python
from mypy_boto3_accessanalyzer.literals import ReasonCode
```

Values:

- `AWS_SERVICE_ACCESS_DISABLED`
- `DELEGATED_ADMINISTRATOR_DEREGISTERED`
- `ORGANIZATION_DELETED`
- `SERVICE_LINKED_ROLE_CREATION_FAILED`

## ResourceType

```python
from mypy_boto3_accessanalyzer.literals import ResourceType
```

Values:

- `AWS::IAM::Role`
- `AWS::KMS::Key`
- `AWS::Lambda::Function`
- `AWS::Lambda::LayerVersion`
- `AWS::S3::Bucket`
- `AWS::SecretsManager::Secret`
- `AWS::SQS::Queue`

## TypeType

```python
from mypy_boto3_accessanalyzer.literals import TypeType
```

Values:

- `ACCOUNT`
- `ORGANIZATION`

## ValidatePolicyFindingType

```python
from mypy_boto3_accessanalyzer.literals import ValidatePolicyFindingType
```

Values:

- `ERROR`
- `SECURITY_WARNING`
- `SUGGESTION`
- `WARNING`

## ValidatePolicyPaginatorName

```python
from mypy_boto3_accessanalyzer.literals import ValidatePolicyPaginatorName
```

Values:

- `validate_policy`
