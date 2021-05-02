# Structures for boto3 Kafka module

> [Index](../index.md) > [Kafka](./index.md) > Structures

Auto-generated documentation for [Kafka](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka)
type annotations stubs module [mypy_boto3_kafka](https://pypi.org/project/mypy-boto3-kafka/).

- [Structures for boto3 Kafka module](#structures-for-boto3-kafka-module)
  - [BrokerEBSVolumeInfoTypeDef](#brokerebsvolumeinfotypedef)
  - [BrokerLogsTypeDef](#brokerlogstypedef)
  - [BrokerNodeGroupInfoTypeDef](#brokernodegroupinfotypedef)
  - [BrokerNodeInfoTypeDef](#brokernodeinfotypedef)
  - [BrokerSoftwareInfoTypeDef](#brokersoftwareinfotypedef)
  - [ClientAuthenticationTypeDef](#clientauthenticationtypedef)
  - [CloudWatchLogsTypeDef](#cloudwatchlogstypedef)
  - [ClusterInfoTypeDef](#clusterinfotypedef)
  - [ClusterOperationInfoTypeDef](#clusteroperationinfotypedef)
  - [ClusterOperationStepInfoTypeDef](#clusteroperationstepinfotypedef)
  - [ClusterOperationStepTypeDef](#clusteroperationsteptypedef)
  - [CompatibleKafkaVersionTypeDef](#compatiblekafkaversiontypedef)
  - [ConfigurationInfoTypeDef](#configurationinfotypedef)
  - [ConfigurationRevisionTypeDef](#configurationrevisiontypedef)
  - [ConfigurationTypeDef](#configurationtypedef)
  - [EBSStorageInfoTypeDef](#ebsstorageinfotypedef)
  - [EncryptionAtRestTypeDef](#encryptionatresttypedef)
  - [EncryptionInTransitTypeDef](#encryptionintransittypedef)
  - [EncryptionInfoTypeDef](#encryptioninfotypedef)
  - [ErrorInfoTypeDef](#errorinfotypedef)
  - [FirehoseTypeDef](#firehosetypedef)
  - [JmxExporterInfoTypeDef](#jmxexporterinfotypedef)
  - [JmxExporterTypeDef](#jmxexportertypedef)
  - [KafkaVersionTypeDef](#kafkaversiontypedef)
  - [LoggingInfoTypeDef](#logginginfotypedef)
  - [MutableClusterInfoTypeDef](#mutableclusterinfotypedef)
  - [NodeExporterInfoTypeDef](#nodeexporterinfotypedef)
  - [NodeExporterTypeDef](#nodeexportertypedef)
  - [NodeInfoTypeDef](#nodeinfotypedef)
  - [OpenMonitoringTypeDef](#openmonitoringtypedef)
  - [PrometheusInfoTypeDef](#prometheusinfotypedef)
  - [PrometheusTypeDef](#prometheustypedef)
  - [S3TypeDef](#s3typedef)
  - [SaslTypeDef](#sasltypedef)
  - [ScramTypeDef](#scramtypedef)
  - [StateInfoTypeDef](#stateinfotypedef)
  - [StorageInfoTypeDef](#storageinfotypedef)
  - [TlsTypeDef](#tlstypedef)
  - [UnprocessedScramSecretTypeDef](#unprocessedscramsecrettypedef)
  - [ZookeeperNodeInfoTypeDef](#zookeepernodeinfotypedef)
  - [BatchAssociateScramSecretResponseTypeDef](#batchassociatescramsecretresponsetypedef)
  - [BatchDisassociateScramSecretResponseTypeDef](#batchdisassociatescramsecretresponsetypedef)
  - [CreateClusterResponseTypeDef](#createclusterresponsetypedef)
  - [CreateConfigurationResponseTypeDef](#createconfigurationresponsetypedef)
  - [DeleteClusterResponseTypeDef](#deleteclusterresponsetypedef)
  - [DeleteConfigurationResponseTypeDef](#deleteconfigurationresponsetypedef)
  - [DescribeClusterOperationResponseTypeDef](#describeclusteroperationresponsetypedef)
  - [DescribeClusterResponseTypeDef](#describeclusterresponsetypedef)
  - [DescribeConfigurationResponseTypeDef](#describeconfigurationresponsetypedef)
  - [DescribeConfigurationRevisionResponseTypeDef](#describeconfigurationrevisionresponsetypedef)
  - [GetBootstrapBrokersResponseTypeDef](#getbootstrapbrokersresponsetypedef)
  - [GetCompatibleKafkaVersionsResponseTypeDef](#getcompatiblekafkaversionsresponsetypedef)
  - [ListClusterOperationsResponseTypeDef](#listclusteroperationsresponsetypedef)
  - [ListClustersResponseTypeDef](#listclustersresponsetypedef)
  - [ListConfigurationRevisionsResponseTypeDef](#listconfigurationrevisionsresponsetypedef)
  - [ListConfigurationsResponseTypeDef](#listconfigurationsresponsetypedef)
  - [ListKafkaVersionsResponseTypeDef](#listkafkaversionsresponsetypedef)
  - [ListNodesResponseTypeDef](#listnodesresponsetypedef)
  - [ListScramSecretsResponseTypeDef](#listscramsecretsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [OpenMonitoringInfoTypeDef](#openmonitoringinfotypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [RebootBrokerResponseTypeDef](#rebootbrokerresponsetypedef)
  - [UpdateBrokerCountResponseTypeDef](#updatebrokercountresponsetypedef)
  - [UpdateBrokerStorageResponseTypeDef](#updatebrokerstorageresponsetypedef)
  - [UpdateBrokerTypeResponseTypeDef](#updatebrokertyperesponsetypedef)
  - [UpdateClusterConfigurationResponseTypeDef](#updateclusterconfigurationresponsetypedef)
  - [UpdateClusterKafkaVersionResponseTypeDef](#updateclusterkafkaversionresponsetypedef)
  - [UpdateConfigurationResponseTypeDef](#updateconfigurationresponsetypedef)
  - [UpdateMonitoringResponseTypeDef](#updatemonitoringresponsetypedef)

## BrokerEBSVolumeInfoTypeDef

```python
from mypy_boto3_kafka.type_defs import BrokerEBSVolumeInfoTypeDef
```


Required fields:
- `KafkaBrokerNodeId`: `str`
- `VolumeSizeGB`: `int`




## BrokerLogsTypeDef

```python
from mypy_boto3_kafka.type_defs import BrokerLogsTypeDef
```




Optional fields:
- `CloudWatchLogs`: `"CloudWatchLogsTypeDef"`
- `Firehose`: `"FirehoseTypeDef"`
- `S3`: `"S3TypeDef"`


## BrokerNodeGroupInfoTypeDef

```python
from mypy_boto3_kafka.type_defs import BrokerNodeGroupInfoTypeDef
```


Required fields:
- `ClientSubnets`: `List[str]`
- `InstanceType`: `str`



Optional fields:
- `BrokerAZDistribution`: `BrokerAZDistribution`
- `SecurityGroups`: `List[str]`
- `StorageInfo`: `"StorageInfoTypeDef"`


## BrokerNodeInfoTypeDef

```python
from mypy_boto3_kafka.type_defs import BrokerNodeInfoTypeDef
```




Optional fields:
- `AttachedENIId`: `str`
- `BrokerId`: `float`
- `ClientSubnet`: `str`
- `ClientVpcIpAddress`: `str`
- `CurrentBrokerSoftwareInfo`: `"BrokerSoftwareInfoTypeDef"`
- `Endpoints`: `List[str]`


## BrokerSoftwareInfoTypeDef

```python
from mypy_boto3_kafka.type_defs import BrokerSoftwareInfoTypeDef
```




Optional fields:
- `ConfigurationArn`: `str`
- `ConfigurationRevision`: `int`
- `KafkaVersion`: `str`


## ClientAuthenticationTypeDef

```python
from mypy_boto3_kafka.type_defs import ClientAuthenticationTypeDef
```




Optional fields:
- `Sasl`: `"SaslTypeDef"`
- `Tls`: `"TlsTypeDef"`


## CloudWatchLogsTypeDef

```python
from mypy_boto3_kafka.type_defs import CloudWatchLogsTypeDef
```


Required fields:
- `Enabled`: `bool`



Optional fields:
- `LogGroup`: `str`


## ClusterInfoTypeDef

```python
from mypy_boto3_kafka.type_defs import ClusterInfoTypeDef
```




Optional fields:
- `ActiveOperationArn`: `str`
- `BrokerNodeGroupInfo`: `"BrokerNodeGroupInfoTypeDef"`
- `ClientAuthentication`: `"ClientAuthenticationTypeDef"`
- `ClusterArn`: `str`
- `ClusterName`: `str`
- `CreationTime`: `datetime`
- `CurrentBrokerSoftwareInfo`: `"BrokerSoftwareInfoTypeDef"`
- `CurrentVersion`: `str`
- `EncryptionInfo`: `"EncryptionInfoTypeDef"`
- `EnhancedMonitoring`: `EnhancedMonitoring`
- `OpenMonitoring`: `"OpenMonitoringTypeDef"`
- `LoggingInfo`: `"LoggingInfoTypeDef"`
- `NumberOfBrokerNodes`: `int`
- `State`: `ClusterState`
- `StateInfo`: `"StateInfoTypeDef"`
- `Tags`: `Dict[str, str]`
- `ZookeeperConnectString`: `str`
- `ZookeeperConnectStringTls`: `str`


## ClusterOperationInfoTypeDef

```python
from mypy_boto3_kafka.type_defs import ClusterOperationInfoTypeDef
```




Optional fields:
- `ClientRequestId`: `str`
- `ClusterArn`: `str`
- `CreationTime`: `datetime`
- `EndTime`: `datetime`
- `ErrorInfo`: `"ErrorInfoTypeDef"`
- `OperationArn`: `str`
- `OperationState`: `str`
- `OperationSteps`: `List["ClusterOperationStepTypeDef"]`
- `OperationType`: `str`
- `SourceClusterInfo`: `"MutableClusterInfoTypeDef"`
- `TargetClusterInfo`: `"MutableClusterInfoTypeDef"`


## ClusterOperationStepInfoTypeDef

```python
from mypy_boto3_kafka.type_defs import ClusterOperationStepInfoTypeDef
```




Optional fields:
- `StepStatus`: `str`


## ClusterOperationStepTypeDef

```python
from mypy_boto3_kafka.type_defs import ClusterOperationStepTypeDef
```




Optional fields:
- `StepInfo`: `"ClusterOperationStepInfoTypeDef"`
- `StepName`: `str`


## CompatibleKafkaVersionTypeDef

```python
from mypy_boto3_kafka.type_defs import CompatibleKafkaVersionTypeDef
```




Optional fields:
- `SourceVersion`: `str`
- `TargetVersions`: `List[str]`


## ConfigurationInfoTypeDef

```python
from mypy_boto3_kafka.type_defs import ConfigurationInfoTypeDef
```


Required fields:
- `Arn`: `str`
- `Revision`: `int`




## ConfigurationRevisionTypeDef

```python
from mypy_boto3_kafka.type_defs import ConfigurationRevisionTypeDef
```


Required fields:
- `CreationTime`: `datetime`
- `Revision`: `int`



Optional fields:
- `Description`: `str`


## ConfigurationTypeDef

```python
from mypy_boto3_kafka.type_defs import ConfigurationTypeDef
```


Required fields:
- `Arn`: `str`
- `CreationTime`: `datetime`
- `Description`: `str`
- `KafkaVersions`: `List[str]`
- `LatestRevision`: `"ConfigurationRevisionTypeDef"`
- `Name`: `str`
- `State`: `ConfigurationState`




## EBSStorageInfoTypeDef

```python
from mypy_boto3_kafka.type_defs import EBSStorageInfoTypeDef
```




Optional fields:
- `VolumeSize`: `int`


## EncryptionAtRestTypeDef

```python
from mypy_boto3_kafka.type_defs import EncryptionAtRestTypeDef
```


Required fields:
- `DataVolumeKMSKeyId`: `str`




## EncryptionInTransitTypeDef

```python
from mypy_boto3_kafka.type_defs import EncryptionInTransitTypeDef
```




Optional fields:
- `ClientBroker`: `ClientBroker`
- `InCluster`: `bool`


## EncryptionInfoTypeDef

```python
from mypy_boto3_kafka.type_defs import EncryptionInfoTypeDef
```




Optional fields:
- `EncryptionAtRest`: `"EncryptionAtRestTypeDef"`
- `EncryptionInTransit`: `"EncryptionInTransitTypeDef"`


## ErrorInfoTypeDef

```python
from mypy_boto3_kafka.type_defs import ErrorInfoTypeDef
```




Optional fields:
- `ErrorCode`: `str`
- `ErrorString`: `str`


## FirehoseTypeDef

```python
from mypy_boto3_kafka.type_defs import FirehoseTypeDef
```


Required fields:
- `Enabled`: `bool`



Optional fields:
- `DeliveryStream`: `str`


## JmxExporterInfoTypeDef

```python
from mypy_boto3_kafka.type_defs import JmxExporterInfoTypeDef
```


Required fields:
- `EnabledInBroker`: `bool`




## JmxExporterTypeDef

```python
from mypy_boto3_kafka.type_defs import JmxExporterTypeDef
```


Required fields:
- `EnabledInBroker`: `bool`




## KafkaVersionTypeDef

```python
from mypy_boto3_kafka.type_defs import KafkaVersionTypeDef
```




Optional fields:
- `Version`: `str`
- `Status`: `KafkaVersionStatus`


## LoggingInfoTypeDef

```python
from mypy_boto3_kafka.type_defs import LoggingInfoTypeDef
```


Required fields:
- `BrokerLogs`: `"BrokerLogsTypeDef"`




## MutableClusterInfoTypeDef

```python
from mypy_boto3_kafka.type_defs import MutableClusterInfoTypeDef
```




Optional fields:
- `BrokerEBSVolumeInfo`: `List["BrokerEBSVolumeInfoTypeDef"]`
- `ConfigurationInfo`: `"ConfigurationInfoTypeDef"`
- `NumberOfBrokerNodes`: `int`
- `EnhancedMonitoring`: `EnhancedMonitoring`
- `OpenMonitoring`: `"OpenMonitoringTypeDef"`
- `KafkaVersion`: `str`
- `LoggingInfo`: `"LoggingInfoTypeDef"`
- `InstanceType`: `str`


## NodeExporterInfoTypeDef

```python
from mypy_boto3_kafka.type_defs import NodeExporterInfoTypeDef
```


Required fields:
- `EnabledInBroker`: `bool`




## NodeExporterTypeDef

```python
from mypy_boto3_kafka.type_defs import NodeExporterTypeDef
```


Required fields:
- `EnabledInBroker`: `bool`




## NodeInfoTypeDef

```python
from mypy_boto3_kafka.type_defs import NodeInfoTypeDef
```




Optional fields:
- `AddedToClusterTime`: `str`
- `BrokerNodeInfo`: `"BrokerNodeInfoTypeDef"`
- `InstanceType`: `str`
- `NodeARN`: `str`
- `NodeType`: `NodeType`
- `ZookeeperNodeInfo`: `"ZookeeperNodeInfoTypeDef"`


## OpenMonitoringTypeDef

```python
from mypy_boto3_kafka.type_defs import OpenMonitoringTypeDef
```


Required fields:
- `Prometheus`: `"PrometheusTypeDef"`




## PrometheusInfoTypeDef

```python
from mypy_boto3_kafka.type_defs import PrometheusInfoTypeDef
```




Optional fields:
- `JmxExporter`: `"JmxExporterInfoTypeDef"`
- `NodeExporter`: `"NodeExporterInfoTypeDef"`


## PrometheusTypeDef

```python
from mypy_boto3_kafka.type_defs import PrometheusTypeDef
```




Optional fields:
- `JmxExporter`: `"JmxExporterTypeDef"`
- `NodeExporter`: `"NodeExporterTypeDef"`


## S3TypeDef

```python
from mypy_boto3_kafka.type_defs import S3TypeDef
```


Required fields:
- `Enabled`: `bool`



Optional fields:
- `Bucket`: `str`
- `Prefix`: `str`


## SaslTypeDef

```python
from mypy_boto3_kafka.type_defs import SaslTypeDef
```




Optional fields:
- `Scram`: `"ScramTypeDef"`


## ScramTypeDef

```python
from mypy_boto3_kafka.type_defs import ScramTypeDef
```




Optional fields:
- `Enabled`: `bool`


## StateInfoTypeDef

```python
from mypy_boto3_kafka.type_defs import StateInfoTypeDef
```




Optional fields:
- `Code`: `str`
- `Message`: `str`


## StorageInfoTypeDef

```python
from mypy_boto3_kafka.type_defs import StorageInfoTypeDef
```




Optional fields:
- `EbsStorageInfo`: `"EBSStorageInfoTypeDef"`


## TlsTypeDef

```python
from mypy_boto3_kafka.type_defs import TlsTypeDef
```




Optional fields:
- `CertificateAuthorityArnList`: `List[str]`


## UnprocessedScramSecretTypeDef

```python
from mypy_boto3_kafka.type_defs import UnprocessedScramSecretTypeDef
```




Optional fields:
- `ErrorCode`: `str`
- `ErrorMessage`: `str`
- `SecretArn`: `str`


## ZookeeperNodeInfoTypeDef

```python
from mypy_boto3_kafka.type_defs import ZookeeperNodeInfoTypeDef
```




Optional fields:
- `AttachedENIId`: `str`
- `ClientVpcIpAddress`: `str`
- `Endpoints`: `List[str]`
- `ZookeeperId`: `float`
- `ZookeeperVersion`: `str`


## BatchAssociateScramSecretResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import BatchAssociateScramSecretResponseTypeDef
```




Optional fields:
- `ClusterArn`: `str`
- `UnprocessedScramSecrets`: `List["UnprocessedScramSecretTypeDef"]`


## BatchDisassociateScramSecretResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import BatchDisassociateScramSecretResponseTypeDef
```




Optional fields:
- `ClusterArn`: `str`
- `UnprocessedScramSecrets`: `List["UnprocessedScramSecretTypeDef"]`


## CreateClusterResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import CreateClusterResponseTypeDef
```




Optional fields:
- `ClusterArn`: `str`
- `ClusterName`: `str`
- `State`: `ClusterState`


## CreateConfigurationResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import CreateConfigurationResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `CreationTime`: `datetime`
- `LatestRevision`: `"ConfigurationRevisionTypeDef"`
- `Name`: `str`
- `State`: `ConfigurationState`


## DeleteClusterResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import DeleteClusterResponseTypeDef
```




Optional fields:
- `ClusterArn`: `str`
- `State`: `ClusterState`


## DeleteConfigurationResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import DeleteConfigurationResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `State`: `ConfigurationState`


## DescribeClusterOperationResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import DescribeClusterOperationResponseTypeDef
```




Optional fields:
- `ClusterOperationInfo`: `"ClusterOperationInfoTypeDef"`


## DescribeClusterResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import DescribeClusterResponseTypeDef
```




Optional fields:
- `ClusterInfo`: `"ClusterInfoTypeDef"`


## DescribeConfigurationResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import DescribeConfigurationResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `CreationTime`: `datetime`
- `Description`: `str`
- `KafkaVersions`: `List[str]`
- `LatestRevision`: `"ConfigurationRevisionTypeDef"`
- `Name`: `str`
- `State`: `ConfigurationState`


## DescribeConfigurationRevisionResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import DescribeConfigurationRevisionResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `CreationTime`: `datetime`
- `Description`: `str`
- `Revision`: `int`
- `ServerProperties`: `Union[bytes, IO[bytes]]`


## GetBootstrapBrokersResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import GetBootstrapBrokersResponseTypeDef
```




Optional fields:
- `BootstrapBrokerString`: `str`
- `BootstrapBrokerStringTls`: `str`
- `BootstrapBrokerStringSaslScram`: `str`


## GetCompatibleKafkaVersionsResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import GetCompatibleKafkaVersionsResponseTypeDef
```




Optional fields:
- `CompatibleKafkaVersions`: `List["CompatibleKafkaVersionTypeDef"]`


## ListClusterOperationsResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import ListClusterOperationsResponseTypeDef
```




Optional fields:
- `ClusterOperationInfoList`: `List["ClusterOperationInfoTypeDef"]`
- `NextToken`: `str`


## ListClustersResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import ListClustersResponseTypeDef
```




Optional fields:
- `ClusterInfoList`: `List["ClusterInfoTypeDef"]`
- `NextToken`: `str`


## ListConfigurationRevisionsResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import ListConfigurationRevisionsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Revisions`: `List["ConfigurationRevisionTypeDef"]`


## ListConfigurationsResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import ListConfigurationsResponseTypeDef
```




Optional fields:
- `Configurations`: `List["ConfigurationTypeDef"]`
- `NextToken`: `str`


## ListKafkaVersionsResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import ListKafkaVersionsResponseTypeDef
```




Optional fields:
- `KafkaVersions`: `List["KafkaVersionTypeDef"]`
- `NextToken`: `str`


## ListNodesResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import ListNodesResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `NodeInfoList`: `List["NodeInfoTypeDef"]`


## ListScramSecretsResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import ListScramSecretsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `SecretArnList`: `List[str]`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`


## OpenMonitoringInfoTypeDef

```python
from mypy_boto3_kafka.type_defs import OpenMonitoringInfoTypeDef
```


Required fields:
- `Prometheus`: `"PrometheusInfoTypeDef"`




## PaginatorConfigTypeDef

```python
from mypy_boto3_kafka.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## RebootBrokerResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import RebootBrokerResponseTypeDef
```




Optional fields:
- `ClusterArn`: `str`
- `ClusterOperationArn`: `str`


## UpdateBrokerCountResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import UpdateBrokerCountResponseTypeDef
```




Optional fields:
- `ClusterArn`: `str`
- `ClusterOperationArn`: `str`


## UpdateBrokerStorageResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import UpdateBrokerStorageResponseTypeDef
```




Optional fields:
- `ClusterArn`: `str`
- `ClusterOperationArn`: `str`


## UpdateBrokerTypeResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import UpdateBrokerTypeResponseTypeDef
```




Optional fields:
- `ClusterArn`: `str`
- `ClusterOperationArn`: `str`


## UpdateClusterConfigurationResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import UpdateClusterConfigurationResponseTypeDef
```




Optional fields:
- `ClusterArn`: `str`
- `ClusterOperationArn`: `str`


## UpdateClusterKafkaVersionResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import UpdateClusterKafkaVersionResponseTypeDef
```




Optional fields:
- `ClusterArn`: `str`
- `ClusterOperationArn`: `str`


## UpdateConfigurationResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import UpdateConfigurationResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `LatestRevision`: `"ConfigurationRevisionTypeDef"`


## UpdateMonitoringResponseTypeDef

```python
from mypy_boto3_kafka.type_defs import UpdateMonitoringResponseTypeDef
```




Optional fields:
- `ClusterArn`: `str`
- `ClusterOperationArn`: `str`

