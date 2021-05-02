# Literals for boto3 DirectoryService module

> [Index](../index.md) > [DirectoryService](./index.md) > Literals

Auto-generated documentation for [DirectoryService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService)
type annotations stubs module [mypy_boto3_ds](https://pypi.org/project/mypy-boto3-ds/).

- [Literals for boto3 DirectoryService module](#literals-for-boto3-directoryservice-module)
  - [CertificateState](#certificatestate)
  - [CertificateType](#certificatetype)
  - [ClientAuthenticationType](#clientauthenticationtype)
  - [DescribeDirectoriesPaginatorName](#describedirectoriespaginatorname)
  - [DescribeDomainControllersPaginatorName](#describedomaincontrollerspaginatorname)
  - [DescribeSharedDirectoriesPaginatorName](#describeshareddirectoriespaginatorname)
  - [DescribeSnapshotsPaginatorName](#describesnapshotspaginatorname)
  - [DescribeTrustsPaginatorName](#describetrustspaginatorname)
  - [DirectoryEdition](#directoryedition)
  - [DirectorySize](#directorysize)
  - [DirectoryStage](#directorystage)
  - [DirectoryType](#directorytype)
  - [DomainControllerStatus](#domaincontrollerstatus)
  - [IpRouteStatusMsg](#iproutestatusmsg)
  - [LDAPSStatus](#ldapsstatus)
  - [LDAPSType](#ldapstype)
  - [ListIpRoutesPaginatorName](#listiproutespaginatorname)
  - [ListLogSubscriptionsPaginatorName](#listlogsubscriptionspaginatorname)
  - [ListSchemaExtensionsPaginatorName](#listschemaextensionspaginatorname)
  - [ListTagsForResourcePaginatorName](#listtagsforresourcepaginatorname)
  - [RadiusAuthenticationProtocol](#radiusauthenticationprotocol)
  - [RadiusStatus](#radiusstatus)
  - [RegionType](#regiontype)
  - [ReplicationScope](#replicationscope)
  - [SchemaExtensionStatus](#schemaextensionstatus)
  - [SelectiveAuth](#selectiveauth)
  - [ShareMethod](#sharemethod)
  - [ShareStatus](#sharestatus)
  - [SnapshotStatus](#snapshotstatus)
  - [SnapshotType](#snapshottype)
  - [TargetType](#targettype)
  - [TopicStatus](#topicstatus)
  - [TrustDirection](#trustdirection)
  - [TrustState](#truststate)
  - [TrustType](#trusttype)

## CertificateState

```python
from mypy_boto3_ds.literals import CertificateState
```

Values:

- `Deregistered`
- `DeregisterFailed`
- `Deregistering`
- `Registered`
- `RegisterFailed`
- `Registering`

## CertificateType

```python
from mypy_boto3_ds.literals import CertificateType
```

Values:

- `ClientCertAuth`
- `ClientLDAPS`

## ClientAuthenticationType

```python
from mypy_boto3_ds.literals import ClientAuthenticationType
```

Values:

- `SmartCard`

## DescribeDirectoriesPaginatorName

```python
from mypy_boto3_ds.literals import DescribeDirectoriesPaginatorName
```

Values:

- `describe_directories`

## DescribeDomainControllersPaginatorName

```python
from mypy_boto3_ds.literals import DescribeDomainControllersPaginatorName
```

Values:

- `describe_domain_controllers`

## DescribeSharedDirectoriesPaginatorName

```python
from mypy_boto3_ds.literals import DescribeSharedDirectoriesPaginatorName
```

Values:

- `describe_shared_directories`

## DescribeSnapshotsPaginatorName

```python
from mypy_boto3_ds.literals import DescribeSnapshotsPaginatorName
```

Values:

- `describe_snapshots`

## DescribeTrustsPaginatorName

```python
from mypy_boto3_ds.literals import DescribeTrustsPaginatorName
```

Values:

- `describe_trusts`

## DirectoryEdition

```python
from mypy_boto3_ds.literals import DirectoryEdition
```

Values:

- `Enterprise`
- `Standard`

## DirectorySize

```python
from mypy_boto3_ds.literals import DirectorySize
```

Values:

- `Large`
- `Small`

## DirectoryStage

```python
from mypy_boto3_ds.literals import DirectoryStage
```

Values:

- `Active`
- `Created`
- `Creating`
- `Deleted`
- `Deleting`
- `Failed`
- `Impaired`
- `Inoperable`
- `Requested`
- `RestoreFailed`
- `Restoring`

## DirectoryType

```python
from mypy_boto3_ds.literals import DirectoryType
```

Values:

- `ADConnector`
- `MicrosoftAD`
- `SharedMicrosoftAD`
- `SimpleAD`

## DomainControllerStatus

```python
from mypy_boto3_ds.literals import DomainControllerStatus
```

Values:

- `Active`
- `Creating`
- `Deleted`
- `Deleting`
- `Failed`
- `Impaired`
- `Restoring`

## IpRouteStatusMsg

```python
from mypy_boto3_ds.literals import IpRouteStatusMsg
```

Values:

- `Added`
- `AddFailed`
- `Adding`
- `Removed`
- `RemoveFailed`
- `Removing`

## LDAPSStatus

```python
from mypy_boto3_ds.literals import LDAPSStatus
```

Values:

- `Disabled`
- `Enabled`
- `EnableFailed`
- `Enabling`

## LDAPSType

```python
from mypy_boto3_ds.literals import LDAPSType
```

Values:

- `Client`

## ListIpRoutesPaginatorName

```python
from mypy_boto3_ds.literals import ListIpRoutesPaginatorName
```

Values:

- `list_ip_routes`

## ListLogSubscriptionsPaginatorName

```python
from mypy_boto3_ds.literals import ListLogSubscriptionsPaginatorName
```

Values:

- `list_log_subscriptions`

## ListSchemaExtensionsPaginatorName

```python
from mypy_boto3_ds.literals import ListSchemaExtensionsPaginatorName
```

Values:

- `list_schema_extensions`

## ListTagsForResourcePaginatorName

```python
from mypy_boto3_ds.literals import ListTagsForResourcePaginatorName
```

Values:

- `list_tags_for_resource`

## RadiusAuthenticationProtocol

```python
from mypy_boto3_ds.literals import RadiusAuthenticationProtocol
```

Values:

- `CHAP`
- `MS-CHAPv1`
- `MS-CHAPv2`
- `PAP`

## RadiusStatus

```python
from mypy_boto3_ds.literals import RadiusStatus
```

Values:

- `Completed`
- `Creating`
- `Failed`

## RegionType

```python
from mypy_boto3_ds.literals import RegionType
```

Values:

- `Additional`
- `Primary`

## ReplicationScope

```python
from mypy_boto3_ds.literals import ReplicationScope
```

Values:

- `Domain`

## SchemaExtensionStatus

```python
from mypy_boto3_ds.literals import SchemaExtensionStatus
```

Values:

- `CancelInProgress`
- `Cancelled`
- `Completed`
- `CreatingSnapshot`
- `Failed`
- `Initializing`
- `Replicating`
- `RollbackInProgress`
- `UpdatingSchema`

## SelectiveAuth

```python
from mypy_boto3_ds.literals import SelectiveAuth
```

Values:

- `Disabled`
- `Enabled`

## ShareMethod

```python
from mypy_boto3_ds.literals import ShareMethod
```

Values:

- `HANDSHAKE`
- `ORGANIZATIONS`

## ShareStatus

```python
from mypy_boto3_ds.literals import ShareStatus
```

Values:

- `Deleted`
- `Deleting`
- `PendingAcceptance`
- `Rejected`
- `RejectFailed`
- `Rejecting`
- `Shared`
- `ShareFailed`
- `Sharing`

## SnapshotStatus

```python
from mypy_boto3_ds.literals import SnapshotStatus
```

Values:

- `Completed`
- `Creating`
- `Failed`

## SnapshotType

```python
from mypy_boto3_ds.literals import SnapshotType
```

Values:

- `Auto`
- `Manual`

## TargetType

```python
from mypy_boto3_ds.literals import TargetType
```

Values:

- `ACCOUNT`

## TopicStatus

```python
from mypy_boto3_ds.literals import TopicStatus
```

Values:

- `Deleted`
- `Failed`
- `Registered`
- `Topic not found`

## TrustDirection

```python
from mypy_boto3_ds.literals import TrustDirection
```

Values:

- `One-Way: Incoming`
- `One-Way: Outgoing`
- `Two-Way`

## TrustState

```python
from mypy_boto3_ds.literals import TrustState
```

Values:

- `Created`
- `Creating`
- `Deleted`
- `Deleting`
- `Failed`
- `Updated`
- `UpdateFailed`
- `Updating`
- `Verified`
- `VerifyFailed`
- `Verifying`

## TrustType

```python
from mypy_boto3_ds.literals import TrustType
```

Values:

- `External`
- `Forest`
