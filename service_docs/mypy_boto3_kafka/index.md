# Type annotations for boto3 Kafka module

> [Index](../index.md) > Kafka

Auto-generated documentation for [Kafka](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka)
type annotations stubs module [mypy_boto3_kafka](https://pypi.org/project/mypy-boto3-kafka/).

```bash
pip install mypy-boto3-kafka
```

- [Type annotations for boto3 Kafka module](#type-annotations-for-boto3-kafka-module)
  - [KafkaClient](#kafkaclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## KafkaClient

Type annotations for  `boto3.client("kafka")` as [KafkaClient](./client.md)

Can be used directly:

```python
from mypy_boto3_kafka.client import KafkaClient
```


KafkaClient [exceptions](./client.md#exceptions)



### Methods
- [batch_associate_scram_secret](./client.md#batch-associate-scram-secret)
- [batch_disassociate_scram_secret](./client.md#batch-disassociate-scram-secret)
- [can_paginate](./client.md#can-paginate)
- [create_cluster](./client.md#create-cluster)
- [create_configuration](./client.md#create-configuration)
- [delete_cluster](./client.md#delete-cluster)
- [delete_configuration](./client.md#delete-configuration)
- [describe_cluster](./client.md#describe-cluster)
- [describe_cluster_operation](./client.md#describe-cluster-operation)
- [describe_configuration](./client.md#describe-configuration)
- [describe_configuration_revision](./client.md#describe-configuration-revision)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_bootstrap_brokers](./client.md#get-bootstrap-brokers)
- [get_compatible_kafka_versions](./client.md#get-compatible-kafka-versions)
- [get_paginator](./client.md#get-paginator)
- [list_cluster_operations](./client.md#list-cluster-operations)
- [list_clusters](./client.md#list-clusters)
- [list_configuration_revisions](./client.md#list-configuration-revisions)
- [list_configurations](./client.md#list-configurations)
- [list_kafka_versions](./client.md#list-kafka-versions)
- [list_nodes](./client.md#list-nodes)
- [list_scram_secrets](./client.md#list-scram-secrets)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [reboot_broker](./client.md#reboot-broker)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_broker_count](./client.md#update-broker-count)
- [update_broker_storage](./client.md#update-broker-storage)
- [update_broker_type](./client.md#update-broker-type)
- [update_cluster_configuration](./client.md#update-cluster-configuration)
- [update_cluster_kafka_version](./client.md#update-cluster-kafka-version)
- [update_configuration](./client.md#update-configuration)
- [update_monitoring](./client.md#update-monitoring)




### Exceptions
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [ForbiddenException](./client.md#forbiddenexception)
- [InternalServerErrorException](./client.md#internalservererrorexception)
- [NotFoundException](./client.md#notfoundexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)
- [UnauthorizedException](./client.md#unauthorizedexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("kafka").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_kafka.paginators import ListClusterOperationsPaginator, ...
```

- [ListClusterOperationsPaginator](./paginators.md#listclusteroperationspaginator)
- [ListClustersPaginator](./paginators.md#listclusterspaginator)
- [ListConfigurationRevisionsPaginator](./paginators.md#listconfigurationrevisionspaginator)
- [ListConfigurationsPaginator](./paginators.md#listconfigurationspaginator)
- [ListKafkaVersionsPaginator](./paginators.md#listkafkaversionspaginator)
- [ListNodesPaginator](./paginators.md#listnodespaginator)
- [ListScramSecretsPaginator](./paginators.md#listscramsecretspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_kafka.literals import BrokerAZDistribution, ...
```

- [BrokerAZDistribution](./literals.md#brokerazdistribution)
- [ClientBroker](./literals.md#clientbroker)
- [ClusterState](./literals.md#clusterstate)
- [ConfigurationState](./literals.md#configurationstate)
- [EnhancedMonitoring](./literals.md#enhancedmonitoring)
- [KafkaVersionStatus](./literals.md#kafkaversionstatus)
- [ListClusterOperationsPaginatorName](./literals.md#listclusteroperationspaginatorname)
- [ListClustersPaginatorName](./literals.md#listclusterspaginatorname)
- [ListConfigurationRevisionsPaginatorName](./literals.md#listconfigurationrevisionspaginatorname)
- [ListConfigurationsPaginatorName](./literals.md#listconfigurationspaginatorname)
- [ListKafkaVersionsPaginatorName](./literals.md#listkafkaversionspaginatorname)
- [ListNodesPaginatorName](./literals.md#listnodespaginatorname)
- [ListScramSecretsPaginatorName](./literals.md#listscramsecretspaginatorname)
- [NodeType](./literals.md#nodetype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_kafka.type_defs import BrokerEBSVolumeInfoTypeDef, ...
```

- [BrokerEBSVolumeInfoTypeDef](./type_defs.md#brokerebsvolumeinfotypedef)
- [BrokerLogsTypeDef](./type_defs.md#brokerlogstypedef)
- [BrokerNodeGroupInfoTypeDef](./type_defs.md#brokernodegroupinfotypedef)
- [BrokerNodeInfoTypeDef](./type_defs.md#brokernodeinfotypedef)
- [BrokerSoftwareInfoTypeDef](./type_defs.md#brokersoftwareinfotypedef)
- [ClientAuthenticationTypeDef](./type_defs.md#clientauthenticationtypedef)
- [CloudWatchLogsTypeDef](./type_defs.md#cloudwatchlogstypedef)
- [ClusterInfoTypeDef](./type_defs.md#clusterinfotypedef)
- [ClusterOperationInfoTypeDef](./type_defs.md#clusteroperationinfotypedef)
- [ClusterOperationStepInfoTypeDef](./type_defs.md#clusteroperationstepinfotypedef)
- [ClusterOperationStepTypeDef](./type_defs.md#clusteroperationsteptypedef)
- [CompatibleKafkaVersionTypeDef](./type_defs.md#compatiblekafkaversiontypedef)
- [ConfigurationInfoTypeDef](./type_defs.md#configurationinfotypedef)
- [ConfigurationRevisionTypeDef](./type_defs.md#configurationrevisiontypedef)
- [ConfigurationTypeDef](./type_defs.md#configurationtypedef)
- [EBSStorageInfoTypeDef](./type_defs.md#ebsstorageinfotypedef)
- [EncryptionAtRestTypeDef](./type_defs.md#encryptionatresttypedef)
- [EncryptionInTransitTypeDef](./type_defs.md#encryptionintransittypedef)
- [EncryptionInfoTypeDef](./type_defs.md#encryptioninfotypedef)
- [ErrorInfoTypeDef](./type_defs.md#errorinfotypedef)
- [FirehoseTypeDef](./type_defs.md#firehosetypedef)
- [JmxExporterInfoTypeDef](./type_defs.md#jmxexporterinfotypedef)
- [JmxExporterTypeDef](./type_defs.md#jmxexportertypedef)
- [KafkaVersionTypeDef](./type_defs.md#kafkaversiontypedef)
- [LoggingInfoTypeDef](./type_defs.md#logginginfotypedef)
- [MutableClusterInfoTypeDef](./type_defs.md#mutableclusterinfotypedef)
- [NodeExporterInfoTypeDef](./type_defs.md#nodeexporterinfotypedef)
- [NodeExporterTypeDef](./type_defs.md#nodeexportertypedef)
- [NodeInfoTypeDef](./type_defs.md#nodeinfotypedef)
- [OpenMonitoringTypeDef](./type_defs.md#openmonitoringtypedef)
- [PrometheusInfoTypeDef](./type_defs.md#prometheusinfotypedef)
- [PrometheusTypeDef](./type_defs.md#prometheustypedef)
- [S3TypeDef](./type_defs.md#s3typedef)
- [SaslTypeDef](./type_defs.md#sasltypedef)
- [ScramTypeDef](./type_defs.md#scramtypedef)
- [StateInfoTypeDef](./type_defs.md#stateinfotypedef)
- [StorageInfoTypeDef](./type_defs.md#storageinfotypedef)
- [TlsTypeDef](./type_defs.md#tlstypedef)
- [UnprocessedScramSecretTypeDef](./type_defs.md#unprocessedscramsecrettypedef)
- [ZookeeperNodeInfoTypeDef](./type_defs.md#zookeepernodeinfotypedef)
- [BatchAssociateScramSecretResponseTypeDef](./type_defs.md#batchassociatescramsecretresponsetypedef)
- [BatchDisassociateScramSecretResponseTypeDef](./type_defs.md#batchdisassociatescramsecretresponsetypedef)
- [CreateClusterResponseTypeDef](./type_defs.md#createclusterresponsetypedef)
- [CreateConfigurationResponseTypeDef](./type_defs.md#createconfigurationresponsetypedef)
- [DeleteClusterResponseTypeDef](./type_defs.md#deleteclusterresponsetypedef)
- [DeleteConfigurationResponseTypeDef](./type_defs.md#deleteconfigurationresponsetypedef)
- [DescribeClusterOperationResponseTypeDef](./type_defs.md#describeclusteroperationresponsetypedef)
- [DescribeClusterResponseTypeDef](./type_defs.md#describeclusterresponsetypedef)
- [DescribeConfigurationResponseTypeDef](./type_defs.md#describeconfigurationresponsetypedef)
- [DescribeConfigurationRevisionResponseTypeDef](./type_defs.md#describeconfigurationrevisionresponsetypedef)
- [GetBootstrapBrokersResponseTypeDef](./type_defs.md#getbootstrapbrokersresponsetypedef)
- [GetCompatibleKafkaVersionsResponseTypeDef](./type_defs.md#getcompatiblekafkaversionsresponsetypedef)
- [ListClusterOperationsResponseTypeDef](./type_defs.md#listclusteroperationsresponsetypedef)
- [ListClustersResponseTypeDef](./type_defs.md#listclustersresponsetypedef)
- [ListConfigurationRevisionsResponseTypeDef](./type_defs.md#listconfigurationrevisionsresponsetypedef)
- [ListConfigurationsResponseTypeDef](./type_defs.md#listconfigurationsresponsetypedef)
- [ListKafkaVersionsResponseTypeDef](./type_defs.md#listkafkaversionsresponsetypedef)
- [ListNodesResponseTypeDef](./type_defs.md#listnodesresponsetypedef)
- [ListScramSecretsResponseTypeDef](./type_defs.md#listscramsecretsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [OpenMonitoringInfoTypeDef](./type_defs.md#openmonitoringinfotypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [RebootBrokerResponseTypeDef](./type_defs.md#rebootbrokerresponsetypedef)
- [UpdateBrokerCountResponseTypeDef](./type_defs.md#updatebrokercountresponsetypedef)
- [UpdateBrokerStorageResponseTypeDef](./type_defs.md#updatebrokerstorageresponsetypedef)
- [UpdateBrokerTypeResponseTypeDef](./type_defs.md#updatebrokertyperesponsetypedef)
- [UpdateClusterConfigurationResponseTypeDef](./type_defs.md#updateclusterconfigurationresponsetypedef)
- [UpdateClusterKafkaVersionResponseTypeDef](./type_defs.md#updateclusterkafkaversionresponsetypedef)
- [UpdateConfigurationResponseTypeDef](./type_defs.md#updateconfigurationresponsetypedef)
- [UpdateMonitoringResponseTypeDef](./type_defs.md#updatemonitoringresponsetypedef)
