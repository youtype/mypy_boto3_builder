# Literals for boto3 Lightsail module

> [Index](../index.md) > [Lightsail](./index.md) > Literals

Auto-generated documentation for [Lightsail](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail)
type annotations stubs module [mypy_boto3_lightsail](https://pypi.org/project/mypy-boto3-lightsail/).

- [Literals for boto3 Lightsail module](#literals-for-boto3-lightsail-module)
  - [AccessDirection](#accessdirection)
  - [AddOnType](#addontype)
  - [AlarmState](#alarmstate)
  - [AutoSnapshotStatus](#autosnapshotstatus)
  - [BehaviorEnum](#behaviorenum)
  - [BlueprintType](#blueprinttype)
  - [CertificateStatus](#certificatestatus)
  - [CloudFormationStackRecordSourceType](#cloudformationstackrecordsourcetype)
  - [ComparisonOperator](#comparisonoperator)
  - [ContactMethodStatus](#contactmethodstatus)
  - [ContactMethodVerificationProtocol](#contactmethodverificationprotocol)
  - [ContactProtocol](#contactprotocol)
  - [ContainerServiceDeploymentState](#containerservicedeploymentstate)
  - [ContainerServiceMetricName](#containerservicemetricname)
  - [ContainerServicePowerName](#containerservicepowername)
  - [ContainerServiceProtocol](#containerserviceprotocol)
  - [ContainerServiceState](#containerservicestate)
  - [ContainerServiceStateDetailCode](#containerservicestatedetailcode)
  - [DiskSnapshotState](#disksnapshotstate)
  - [DiskState](#diskstate)
  - [DistributionMetricName](#distributionmetricname)
  - [ExportSnapshotRecordSourceType](#exportsnapshotrecordsourcetype)
  - [ForwardValues](#forwardvalues)
  - [GetActiveNamesPaginatorName](#getactivenamespaginatorname)
  - [GetBlueprintsPaginatorName](#getblueprintspaginatorname)
  - [GetBundlesPaginatorName](#getbundlespaginatorname)
  - [GetCloudFormationStackRecordsPaginatorName](#getcloudformationstackrecordspaginatorname)
  - [GetDiskSnapshotsPaginatorName](#getdisksnapshotspaginatorname)
  - [GetDisksPaginatorName](#getdiskspaginatorname)
  - [GetDomainsPaginatorName](#getdomainspaginatorname)
  - [GetExportSnapshotRecordsPaginatorName](#getexportsnapshotrecordspaginatorname)
  - [GetInstanceSnapshotsPaginatorName](#getinstancesnapshotspaginatorname)
  - [GetInstancesPaginatorName](#getinstancespaginatorname)
  - [GetKeyPairsPaginatorName](#getkeypairspaginatorname)
  - [GetLoadBalancersPaginatorName](#getloadbalancerspaginatorname)
  - [GetOperationsPaginatorName](#getoperationspaginatorname)
  - [GetRelationalDatabaseBlueprintsPaginatorName](#getrelationaldatabaseblueprintspaginatorname)
  - [GetRelationalDatabaseBundlesPaginatorName](#getrelationaldatabasebundlespaginatorname)
  - [GetRelationalDatabaseEventsPaginatorName](#getrelationaldatabaseeventspaginatorname)
  - [GetRelationalDatabaseParametersPaginatorName](#getrelationaldatabaseparameterspaginatorname)
  - [GetRelationalDatabaseSnapshotsPaginatorName](#getrelationaldatabasesnapshotspaginatorname)
  - [GetRelationalDatabasesPaginatorName](#getrelationaldatabasespaginatorname)
  - [GetStaticIpsPaginatorName](#getstaticipspaginatorname)
  - [HeaderEnum](#headerenum)
  - [InstanceAccessProtocol](#instanceaccessprotocol)
  - [InstanceHealthReason](#instancehealthreason)
  - [InstanceHealthState](#instancehealthstate)
  - [InstanceMetricName](#instancemetricname)
  - [InstancePlatform](#instanceplatform)
  - [InstanceSnapshotState](#instancesnapshotstate)
  - [IpAddressType](#ipaddresstype)
  - [LoadBalancerAttributeName](#loadbalancerattributename)
  - [LoadBalancerMetricName](#loadbalancermetricname)
  - [LoadBalancerProtocol](#loadbalancerprotocol)
  - [LoadBalancerState](#loadbalancerstate)
  - [LoadBalancerTlsCertificateDomainStatus](#loadbalancertlscertificatedomainstatus)
  - [LoadBalancerTlsCertificateFailureReason](#loadbalancertlscertificatefailurereason)
  - [LoadBalancerTlsCertificateRenewalStatus](#loadbalancertlscertificaterenewalstatus)
  - [LoadBalancerTlsCertificateRevocationReason](#loadbalancertlscertificaterevocationreason)
  - [LoadBalancerTlsCertificateStatus](#loadbalancertlscertificatestatus)
  - [MetricName](#metricname)
  - [MetricStatistic](#metricstatistic)
  - [MetricUnit](#metricunit)
  - [NetworkProtocol](#networkprotocol)
  - [OperationStatus](#operationstatus)
  - [OperationType](#operationtype)
  - [OriginProtocolPolicyEnum](#originprotocolpolicyenum)
  - [PortAccessType](#portaccesstype)
  - [PortInfoSourceType](#portinfosourcetype)
  - [PortState](#portstate)
  - [RecordState](#recordstate)
  - [RegionName](#regionname)
  - [RelationalDatabaseEngine](#relationaldatabaseengine)
  - [RelationalDatabaseMetricName](#relationaldatabasemetricname)
  - [RelationalDatabasePasswordVersion](#relationaldatabasepasswordversion)
  - [RenewalStatus](#renewalstatus)
  - [ResourceType](#resourcetype)
  - [TreatMissingData](#treatmissingdata)

## AccessDirection

```python
from mypy_boto3_lightsail.literals import AccessDirection
```

Values:

- `inbound`
- `outbound`

## AddOnType

```python
from mypy_boto3_lightsail.literals import AddOnType
```

Values:

- `AutoSnapshot`

## AlarmState

```python
from mypy_boto3_lightsail.literals import AlarmState
```

Values:

- `ALARM`
- `INSUFFICIENT_DATA`
- `OK`

## AutoSnapshotStatus

```python
from mypy_boto3_lightsail.literals import AutoSnapshotStatus
```

Values:

- `Failed`
- `InProgress`
- `NotFound`
- `Success`

## BehaviorEnum

```python
from mypy_boto3_lightsail.literals import BehaviorEnum
```

Values:

- `cache`
- `dont-cache`

## BlueprintType

```python
from mypy_boto3_lightsail.literals import BlueprintType
```

Values:

- `app`
- `os`

## CertificateStatus

```python
from mypy_boto3_lightsail.literals import CertificateStatus
```

Values:

- `EXPIRED`
- `FAILED`
- `INACTIVE`
- `ISSUED`
- `PENDING_VALIDATION`
- `REVOKED`
- `VALIDATION_TIMED_OUT`

## CloudFormationStackRecordSourceType

```python
from mypy_boto3_lightsail.literals import CloudFormationStackRecordSourceType
```

Values:

- `ExportSnapshotRecord`

## ComparisonOperator

```python
from mypy_boto3_lightsail.literals import ComparisonOperator
```

Values:

- `GreaterThanOrEqualToThreshold`
- `GreaterThanThreshold`
- `LessThanOrEqualToThreshold`
- `LessThanThreshold`

## ContactMethodStatus

```python
from mypy_boto3_lightsail.literals import ContactMethodStatus
```

Values:

- `Invalid`
- `PendingVerification`
- `Valid`

## ContactMethodVerificationProtocol

```python
from mypy_boto3_lightsail.literals import ContactMethodVerificationProtocol
```

Values:

- `Email`

## ContactProtocol

```python
from mypy_boto3_lightsail.literals import ContactProtocol
```

Values:

- `Email`
- `SMS`

## ContainerServiceDeploymentState

```python
from mypy_boto3_lightsail.literals import ContainerServiceDeploymentState
```

Values:

- `ACTIVATING`
- `ACTIVE`
- `FAILED`
- `INACTIVE`

## ContainerServiceMetricName

```python
from mypy_boto3_lightsail.literals import ContainerServiceMetricName
```

Values:

- `CPUUtilization`
- `MemoryUtilization`

## ContainerServicePowerName

```python
from mypy_boto3_lightsail.literals import ContainerServicePowerName
```

Values:

- `large`
- `medium`
- `micro`
- `nano`
- `small`
- `xlarge`

## ContainerServiceProtocol

```python
from mypy_boto3_lightsail.literals import ContainerServiceProtocol
```

Values:

- `HTTP`
- `HTTPS`
- `TCP`
- `UDP`

## ContainerServiceState

```python
from mypy_boto3_lightsail.literals import ContainerServiceState
```

Values:

- `DELETING`
- `DEPLOYING`
- `DISABLED`
- `PENDING`
- `READY`
- `RUNNING`
- `UPDATING`

## ContainerServiceStateDetailCode

```python
from mypy_boto3_lightsail.literals import ContainerServiceStateDetailCode
```

Values:

- `ACTIVATING_DEPLOYMENT`
- `CERTIFICATE_LIMIT_EXCEEDED`
- `CREATING_DEPLOYMENT`
- `CREATING_NETWORK_INFRASTRUCTURE`
- `CREATING_SYSTEM_RESOURCES`
- `EVALUATING_HEALTH_CHECK`
- `PROVISIONING_CERTIFICATE`
- `PROVISIONING_SERVICE`
- `UNKNOWN_ERROR`

## DiskSnapshotState

```python
from mypy_boto3_lightsail.literals import DiskSnapshotState
```

Values:

- `completed`
- `error`
- `pending`
- `unknown`

## DiskState

```python
from mypy_boto3_lightsail.literals import DiskState
```

Values:

- `available`
- `error`
- `in-use`
- `pending`
- `unknown`

## DistributionMetricName

```python
from mypy_boto3_lightsail.literals import DistributionMetricName
```

Values:

- `BytesDownloaded`
- `BytesUploaded`
- `Http4xxErrorRate`
- `Http5xxErrorRate`
- `Requests`
- `TotalErrorRate`

## ExportSnapshotRecordSourceType

```python
from mypy_boto3_lightsail.literals import ExportSnapshotRecordSourceType
```

Values:

- `DiskSnapshot`
- `InstanceSnapshot`

## ForwardValues

```python
from mypy_boto3_lightsail.literals import ForwardValues
```

Values:

- `all`
- `allow-list`
- `none`

## GetActiveNamesPaginatorName

```python
from mypy_boto3_lightsail.literals import GetActiveNamesPaginatorName
```

Values:

- `get_active_names`

## GetBlueprintsPaginatorName

```python
from mypy_boto3_lightsail.literals import GetBlueprintsPaginatorName
```

Values:

- `get_blueprints`

## GetBundlesPaginatorName

```python
from mypy_boto3_lightsail.literals import GetBundlesPaginatorName
```

Values:

- `get_bundles`

## GetCloudFormationStackRecordsPaginatorName

```python
from mypy_boto3_lightsail.literals import GetCloudFormationStackRecordsPaginatorName
```

Values:

- `get_cloud_formation_stack_records`

## GetDiskSnapshotsPaginatorName

```python
from mypy_boto3_lightsail.literals import GetDiskSnapshotsPaginatorName
```

Values:

- `get_disk_snapshots`

## GetDisksPaginatorName

```python
from mypy_boto3_lightsail.literals import GetDisksPaginatorName
```

Values:

- `get_disks`

## GetDomainsPaginatorName

```python
from mypy_boto3_lightsail.literals import GetDomainsPaginatorName
```

Values:

- `get_domains`

## GetExportSnapshotRecordsPaginatorName

```python
from mypy_boto3_lightsail.literals import GetExportSnapshotRecordsPaginatorName
```

Values:

- `get_export_snapshot_records`

## GetInstanceSnapshotsPaginatorName

```python
from mypy_boto3_lightsail.literals import GetInstanceSnapshotsPaginatorName
```

Values:

- `get_instance_snapshots`

## GetInstancesPaginatorName

```python
from mypy_boto3_lightsail.literals import GetInstancesPaginatorName
```

Values:

- `get_instances`

## GetKeyPairsPaginatorName

```python
from mypy_boto3_lightsail.literals import GetKeyPairsPaginatorName
```

Values:

- `get_key_pairs`

## GetLoadBalancersPaginatorName

```python
from mypy_boto3_lightsail.literals import GetLoadBalancersPaginatorName
```

Values:

- `get_load_balancers`

## GetOperationsPaginatorName

```python
from mypy_boto3_lightsail.literals import GetOperationsPaginatorName
```

Values:

- `get_operations`

## GetRelationalDatabaseBlueprintsPaginatorName

```python
from mypy_boto3_lightsail.literals import GetRelationalDatabaseBlueprintsPaginatorName
```

Values:

- `get_relational_database_blueprints`

## GetRelationalDatabaseBundlesPaginatorName

```python
from mypy_boto3_lightsail.literals import GetRelationalDatabaseBundlesPaginatorName
```

Values:

- `get_relational_database_bundles`

## GetRelationalDatabaseEventsPaginatorName

```python
from mypy_boto3_lightsail.literals import GetRelationalDatabaseEventsPaginatorName
```

Values:

- `get_relational_database_events`

## GetRelationalDatabaseParametersPaginatorName

```python
from mypy_boto3_lightsail.literals import GetRelationalDatabaseParametersPaginatorName
```

Values:

- `get_relational_database_parameters`

## GetRelationalDatabaseSnapshotsPaginatorName

```python
from mypy_boto3_lightsail.literals import GetRelationalDatabaseSnapshotsPaginatorName
```

Values:

- `get_relational_database_snapshots`

## GetRelationalDatabasesPaginatorName

```python
from mypy_boto3_lightsail.literals import GetRelationalDatabasesPaginatorName
```

Values:

- `get_relational_databases`

## GetStaticIpsPaginatorName

```python
from mypy_boto3_lightsail.literals import GetStaticIpsPaginatorName
```

Values:

- `get_static_ips`

## HeaderEnum

```python
from mypy_boto3_lightsail.literals import HeaderEnum
```

Values:

- `Accept`
- `Accept-Charset`
- `Accept-Datetime`
- `Accept-Encoding`
- `Accept-Language`
- `Authorization`
- `CloudFront-Forwarded-Proto`
- `CloudFront-Is-Desktop-Viewer`
- `CloudFront-Is-Mobile-Viewer`
- `CloudFront-Is-SmartTV-Viewer`
- `CloudFront-Is-Tablet-Viewer`
- `CloudFront-Viewer-Country`
- `Host`
- `Origin`
- `Referer`

## InstanceAccessProtocol

```python
from mypy_boto3_lightsail.literals import InstanceAccessProtocol
```

Values:

- `rdp`
- `ssh`

## InstanceHealthReason

```python
from mypy_boto3_lightsail.literals import InstanceHealthReason
```

Values:

- `Instance.DeregistrationInProgress`
- `Instance.FailedHealthChecks`
- `Instance.InvalidState`
- `Instance.IpUnusable`
- `Instance.NotInUse`
- `Instance.NotRegistered`
- `Instance.ResponseCodeMismatch`
- `Instance.Timeout`
- `Lb.InitialHealthChecking`
- `Lb.InternalError`
- `Lb.RegistrationInProgress`

## InstanceHealthState

```python
from mypy_boto3_lightsail.literals import InstanceHealthState
```

Values:

- `draining`
- `healthy`
- `initial`
- `unavailable`
- `unhealthy`
- `unused`

## InstanceMetricName

```python
from mypy_boto3_lightsail.literals import InstanceMetricName
```

Values:

- `BurstCapacityPercentage`
- `BurstCapacityTime`
- `CPUUtilization`
- `NetworkIn`
- `NetworkOut`
- `StatusCheckFailed`
- `StatusCheckFailed_Instance`
- `StatusCheckFailed_System`

## InstancePlatform

```python
from mypy_boto3_lightsail.literals import InstancePlatform
```

Values:

- `LINUX_UNIX`
- `WINDOWS`

## InstanceSnapshotState

```python
from mypy_boto3_lightsail.literals import InstanceSnapshotState
```

Values:

- `available`
- `error`
- `pending`

## IpAddressType

```python
from mypy_boto3_lightsail.literals import IpAddressType
```

Values:

- `dualstack`
- `ipv4`

## LoadBalancerAttributeName

```python
from mypy_boto3_lightsail.literals import LoadBalancerAttributeName
```

Values:

- `HealthCheckPath`
- `SessionStickiness_LB_CookieDurationSeconds`
- `SessionStickinessEnabled`

## LoadBalancerMetricName

```python
from mypy_boto3_lightsail.literals import LoadBalancerMetricName
```

Values:

- `ClientTLSNegotiationErrorCount`
- `HealthyHostCount`
- `HTTPCode_Instance_2XX_Count`
- `HTTPCode_Instance_3XX_Count`
- `HTTPCode_Instance_4XX_Count`
- `HTTPCode_Instance_5XX_Count`
- `HTTPCode_LB_4XX_Count`
- `HTTPCode_LB_5XX_Count`
- `InstanceResponseTime`
- `RejectedConnectionCount`
- `RequestCount`
- `UnhealthyHostCount`

## LoadBalancerProtocol

```python
from mypy_boto3_lightsail.literals import LoadBalancerProtocol
```

Values:

- `HTTP`
- `HTTP_HTTPS`

## LoadBalancerState

```python
from mypy_boto3_lightsail.literals import LoadBalancerState
```

Values:

- `active`
- `active_impaired`
- `failed`
- `provisioning`
- `unknown`

## LoadBalancerTlsCertificateDomainStatus

```python
from mypy_boto3_lightsail.literals import LoadBalancerTlsCertificateDomainStatus
```

Values:

- `FAILED`
- `PENDING_VALIDATION`
- `SUCCESS`

## LoadBalancerTlsCertificateFailureReason

```python
from mypy_boto3_lightsail.literals import LoadBalancerTlsCertificateFailureReason
```

Values:

- `ADDITIONAL_VERIFICATION_REQUIRED`
- `DOMAIN_NOT_ALLOWED`
- `INVALID_PUBLIC_DOMAIN`
- `NO_AVAILABLE_CONTACTS`
- `OTHER`

## LoadBalancerTlsCertificateRenewalStatus

```python
from mypy_boto3_lightsail.literals import LoadBalancerTlsCertificateRenewalStatus
```

Values:

- `FAILED`
- `PENDING_AUTO_RENEWAL`
- `PENDING_VALIDATION`
- `SUCCESS`

## LoadBalancerTlsCertificateRevocationReason

```python
from mypy_boto3_lightsail.literals import LoadBalancerTlsCertificateRevocationReason
```

Values:

- `A_A_COMPROMISE`
- `AFFILIATION_CHANGED`
- `CA_COMPROMISE`
- `CERTIFICATE_HOLD`
- `CESSATION_OF_OPERATION`
- `KEY_COMPROMISE`
- `PRIVILEGE_WITHDRAWN`
- `REMOVE_FROM_CRL`
- `SUPERCEDED`
- `UNSPECIFIED`

## LoadBalancerTlsCertificateStatus

```python
from mypy_boto3_lightsail.literals import LoadBalancerTlsCertificateStatus
```

Values:

- `EXPIRED`
- `FAILED`
- `INACTIVE`
- `ISSUED`
- `PENDING_VALIDATION`
- `REVOKED`
- `UNKNOWN`
- `VALIDATION_TIMED_OUT`

## MetricName

```python
from mypy_boto3_lightsail.literals import MetricName
```

Values:

- `BurstCapacityPercentage`
- `BurstCapacityTime`
- `ClientTLSNegotiationErrorCount`
- `CPUUtilization`
- `DatabaseConnections`
- `DiskQueueDepth`
- `FreeStorageSpace`
- `HealthyHostCount`
- `HTTPCode_Instance_2XX_Count`
- `HTTPCode_Instance_3XX_Count`
- `HTTPCode_Instance_4XX_Count`
- `HTTPCode_Instance_5XX_Count`
- `HTTPCode_LB_4XX_Count`
- `HTTPCode_LB_5XX_Count`
- `InstanceResponseTime`
- `NetworkIn`
- `NetworkOut`
- `NetworkReceiveThroughput`
- `NetworkTransmitThroughput`
- `RejectedConnectionCount`
- `RequestCount`
- `StatusCheckFailed`
- `StatusCheckFailed_Instance`
- `StatusCheckFailed_System`
- `UnhealthyHostCount`

## MetricStatistic

```python
from mypy_boto3_lightsail.literals import MetricStatistic
```

Values:

- `Average`
- `Maximum`
- `Minimum`
- `SampleCount`
- `Sum`

## MetricUnit

```python
from mypy_boto3_lightsail.literals import MetricUnit
```

Values:

- `Bits`
- `Bits/Second`
- `Bytes`
- `Bytes/Second`
- `Count`
- `Count/Second`
- `Gigabits`
- `Gigabits/Second`
- `Gigabytes`
- `Gigabytes/Second`
- `Kilobits`
- `Kilobits/Second`
- `Kilobytes`
- `Kilobytes/Second`
- `Megabits`
- `Megabits/Second`
- `Megabytes`
- `Megabytes/Second`
- `Microseconds`
- `Milliseconds`
- `None`
- `Percent`
- `Seconds`
- `Terabits`
- `Terabits/Second`
- `Terabytes`
- `Terabytes/Second`

## NetworkProtocol

```python
from mypy_boto3_lightsail.literals import NetworkProtocol
```

Values:

- `all`
- `icmp`
- `tcp`
- `udp`

## OperationStatus

```python
from mypy_boto3_lightsail.literals import OperationStatus
```

Values:

- `Completed`
- `Failed`
- `NotStarted`
- `Started`
- `Succeeded`

## OperationType

```python
from mypy_boto3_lightsail.literals import OperationType
```

Values:

- `AllocateStaticIp`
- `AttachCertificateToDistribution`
- `AttachDisk`
- `AttachInstancesToLoadBalancer`
- `AttachLoadBalancerTlsCertificate`
- `AttachStaticIp`
- `CloseInstancePublicPorts`
- `CreateCertificate`
- `CreateContactMethod`
- `CreateContainerService`
- `CreateContainerServiceDeployment`
- `CreateContainerServiceRegistryLogin`
- `CreateDisk`
- `CreateDiskFromSnapshot`
- `CreateDiskSnapshot`
- `CreateDistribution`
- `CreateDomain`
- `CreateInstance`
- `CreateInstancesFromSnapshot`
- `CreateInstanceSnapshot`
- `CreateLoadBalancer`
- `CreateLoadBalancerTlsCertificate`
- `CreateRelationalDatabase`
- `CreateRelationalDatabaseFromSnapshot`
- `CreateRelationalDatabaseSnapshot`
- `DeleteAlarm`
- `DeleteCertificate`
- `DeleteContactMethod`
- `DeleteContainerImage`
- `DeleteContainerService`
- `DeleteDisk`
- `DeleteDiskSnapshot`
- `DeleteDistribution`
- `DeleteDomain`
- `DeleteDomainEntry`
- `DeleteInstance`
- `DeleteInstanceSnapshot`
- `DeleteKnownHostKeys`
- `DeleteLoadBalancer`
- `DeleteLoadBalancerTlsCertificate`
- `DeleteRelationalDatabase`
- `DeleteRelationalDatabaseSnapshot`
- `DetachCertificateFromDistribution`
- `DetachDisk`
- `DetachInstancesFromLoadBalancer`
- `DetachStaticIp`
- `DisableAddOn`
- `EnableAddOn`
- `GetAlarms`
- `GetContactMethods`
- `OpenInstancePublicPorts`
- `PutAlarm`
- `PutInstancePublicPorts`
- `RebootInstance`
- `RebootRelationalDatabase`
- `RegisterContainerImage`
- `ReleaseStaticIp`
- `ResetDistributionCache`
- `SendContactMethodVerification`
- `SetIpAddressType`
- `StartInstance`
- `StartRelationalDatabase`
- `StopInstance`
- `StopRelationalDatabase`
- `TestAlarm`
- `UpdateContainerService`
- `UpdateDistribution`
- `UpdateDistributionBundle`
- `UpdateDomainEntry`
- `UpdateLoadBalancerAttribute`
- `UpdateRelationalDatabase`
- `UpdateRelationalDatabaseParameters`

## OriginProtocolPolicyEnum

```python
from mypy_boto3_lightsail.literals import OriginProtocolPolicyEnum
```

Values:

- `http-only`
- `https-only`

## PortAccessType

```python
from mypy_boto3_lightsail.literals import PortAccessType
```

Values:

- `Private`
- `Public`

## PortInfoSourceType

```python
from mypy_boto3_lightsail.literals import PortInfoSourceType
```

Values:

- `CLOSED`
- `DEFAULT`
- `INSTANCE`
- `NONE`

## PortState

```python
from mypy_boto3_lightsail.literals import PortState
```

Values:

- `closed`
- `open`

## RecordState

```python
from mypy_boto3_lightsail.literals import RecordState
```

Values:

- `Failed`
- `Started`
- `Succeeded`

## RegionName

```python
from mypy_boto3_lightsail.literals import RegionName
```

Values:

- `ap-northeast-1`
- `ap-northeast-2`
- `ap-south-1`
- `ap-southeast-1`
- `ap-southeast-2`
- `ca-central-1`
- `eu-central-1`
- `eu-west-1`
- `eu-west-2`
- `eu-west-3`
- `us-east-1`
- `us-east-2`
- `us-west-1`
- `us-west-2`

## RelationalDatabaseEngine

```python
from mypy_boto3_lightsail.literals import RelationalDatabaseEngine
```

Values:

- `mysql`

## RelationalDatabaseMetricName

```python
from mypy_boto3_lightsail.literals import RelationalDatabaseMetricName
```

Values:

- `CPUUtilization`
- `DatabaseConnections`
- `DiskQueueDepth`
- `FreeStorageSpace`
- `NetworkReceiveThroughput`
- `NetworkTransmitThroughput`

## RelationalDatabasePasswordVersion

```python
from mypy_boto3_lightsail.literals import RelationalDatabasePasswordVersion
```

Values:

- `CURRENT`
- `PENDING`
- `PREVIOUS`

## RenewalStatus

```python
from mypy_boto3_lightsail.literals import RenewalStatus
```

Values:

- `Failed`
- `PendingAutoRenewal`
- `PendingValidation`
- `Success`

## ResourceType

```python
from mypy_boto3_lightsail.literals import ResourceType
```

Values:

- `Alarm`
- `Certificate`
- `CloudFormationStackRecord`
- `ContactMethod`
- `ContainerService`
- `Disk`
- `DiskSnapshot`
- `Distribution`
- `Domain`
- `ExportSnapshotRecord`
- `Instance`
- `InstanceSnapshot`
- `KeyPair`
- `LoadBalancer`
- `LoadBalancerTlsCertificate`
- `PeeredVpc`
- `RelationalDatabase`
- `RelationalDatabaseSnapshot`
- `StaticIp`

## TreatMissingData

```python
from mypy_boto3_lightsail.literals import TreatMissingData
```

Values:

- `breaching`
- `ignore`
- `missing`
- `notBreaching`
