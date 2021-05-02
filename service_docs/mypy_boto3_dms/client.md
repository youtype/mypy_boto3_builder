# DatabaseMigrationServiceClient for boto3 DatabaseMigrationService module

> [Index](../index.md) > [DatabaseMigrationService](./index.md) > DatabaseMigrationServiceClient

Auto-generated documentation for [DatabaseMigrationService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService)
type annotations stubs module [mypy_boto3_dms](https://pypi.org/project/mypy-boto3-dms/).

- [DatabaseMigrationServiceClient for boto3 DatabaseMigrationService module](#databasemigrationserviceclient-for-boto3-databasemigrationservice-module)
  - [DatabaseMigrationServiceClient](#databasemigrationserviceclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_tags_to_resource](#add_tags_to_resource)
    - [apply_pending_maintenance_action](#apply_pending_maintenance_action)
    - [can_paginate](#can_paginate)
    - [cancel_replication_task_assessment_run](#cancel_replication_task_assessment_run)
    - [create_endpoint](#create_endpoint)
    - [create_event_subscription](#create_event_subscription)
    - [create_replication_instance](#create_replication_instance)
    - [create_replication_subnet_group](#create_replication_subnet_group)
    - [create_replication_task](#create_replication_task)
    - [delete_certificate](#delete_certificate)
    - [delete_connection](#delete_connection)
    - [delete_endpoint](#delete_endpoint)
    - [delete_event_subscription](#delete_event_subscription)
    - [delete_replication_instance](#delete_replication_instance)
    - [delete_replication_subnet_group](#delete_replication_subnet_group)
    - [delete_replication_task](#delete_replication_task)
    - [delete_replication_task_assessment_run](#delete_replication_task_assessment_run)
    - [describe_account_attributes](#describe_account_attributes)
    - [describe_applicable_individual_assessments](#describe_applicable_individual_assessments)
    - [describe_certificates](#describe_certificates)
    - [describe_connections](#describe_connections)
    - [describe_endpoint_settings](#describe_endpoint_settings)
    - [describe_endpoint_types](#describe_endpoint_types)
    - [describe_endpoints](#describe_endpoints)
    - [describe_event_categories](#describe_event_categories)
    - [describe_event_subscriptions](#describe_event_subscriptions)
    - [describe_events](#describe_events)
    - [describe_orderable_replication_instances](#describe_orderable_replication_instances)
    - [describe_pending_maintenance_actions](#describe_pending_maintenance_actions)
    - [describe_refresh_schemas_status](#describe_refresh_schemas_status)
    - [describe_replication_instance_task_logs](#describe_replication_instance_task_logs)
    - [describe_replication_instances](#describe_replication_instances)
    - [describe_replication_subnet_groups](#describe_replication_subnet_groups)
    - [describe_replication_task_assessment_results](#describe_replication_task_assessment_results)
    - [describe_replication_task_assessment_runs](#describe_replication_task_assessment_runs)
    - [describe_replication_task_individual_assessments](#describe_replication_task_individual_assessments)
    - [describe_replication_tasks](#describe_replication_tasks)
    - [describe_schemas](#describe_schemas)
    - [describe_table_statistics](#describe_table_statistics)
    - [generate_presigned_url](#generate_presigned_url)
    - [import_certificate](#import_certificate)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [modify_endpoint](#modify_endpoint)
    - [modify_event_subscription](#modify_event_subscription)
    - [modify_replication_instance](#modify_replication_instance)
    - [modify_replication_subnet_group](#modify_replication_subnet_group)
    - [modify_replication_task](#modify_replication_task)
    - [move_replication_task](#move_replication_task)
    - [reboot_replication_instance](#reboot_replication_instance)
    - [refresh_schemas](#refresh_schemas)
    - [reload_tables](#reload_tables)
    - [remove_tags_from_resource](#remove_tags_from_resource)
    - [start_replication_task](#start_replication_task)
    - [start_replication_task_assessment](#start_replication_task_assessment)
    - [start_replication_task_assessment_run](#start_replication_task_assessment_run)
    - [stop_replication_task](#stop_replication_task)
    - [test_connection](#test_connection)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)
    - [get_paginator](#get_paginator-8)
    - [get_paginator](#get_paginator-9)
    - [get_paginator](#get_paginator-10)
    - [get_paginator](#get_paginator-11)
    - [get_paginator](#get_paginator-12)
    - [get_waiter](#get_waiter)
    - [get_waiter](#get_waiter-1)
    - [get_waiter](#get_waiter-2)
    - [get_waiter](#get_waiter-3)
    - [get_waiter](#get_waiter-4)
    - [get_waiter](#get_waiter-5)
    - [get_waiter](#get_waiter-6)
    - [get_waiter](#get_waiter-7)

## DatabaseMigrationServiceClient

Type annotations for `boto3.client("dms")`

Can be used directly:

```python
from mypy_boto3_dms.client import DatabaseMigrationServiceClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_dms.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedFault) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedFault`
- `Exceptions.ClientError`
- `Exceptions.InsufficientResourceCapacityFault`
- `Exceptions.InvalidCertificateFault`
- `Exceptions.InvalidResourceStateFault`
- `Exceptions.InvalidSubnet`
- `Exceptions.KMSAccessDeniedFault`
- `Exceptions.KMSDisabledFault`
- `Exceptions.KMSFault`
- `Exceptions.KMSInvalidStateFault`
- `Exceptions.KMSKeyNotAccessibleFault`
- `Exceptions.KMSNotFoundFault`
- `Exceptions.KMSThrottlingFault`
- `Exceptions.ReplicationSubnetGroupDoesNotCoverEnoughAZs`
- `Exceptions.ResourceAlreadyExistsFault`
- `Exceptions.ResourceNotFoundFault`
- `Exceptions.ResourceQuotaExceededFault`
- `Exceptions.S3AccessDeniedFault`
- `Exceptions.S3ResourceNotFoundFault`
- `Exceptions.SNSInvalidTopicFault`
- `Exceptions.SNSNoAuthorizationFault`
- `Exceptions.StorageQuotaExceededFault`
- `Exceptions.SubnetAlreadyInUse`
- `Exceptions.UpgradeDependencyFailureFault`


## Methods


### add_tags_to_resource

Type annotations for `boto3.client("dms").add_tags_to_resource` method.

[Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.add_tags_to_resource)

```python
def add_tags_to_resource(
    self,
    ResourceArn: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### apply_pending_maintenance_action

Type annotations for `boto3.client("dms").apply_pending_maintenance_action` method.

[Client.apply_pending_maintenance_action documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.apply_pending_maintenance_action)

```python
def apply_pending_maintenance_action(
    self,
    ReplicationInstanceArn: str,
    ApplyAction: str,
    OptInType: str
) -> ApplyPendingMaintenanceActionResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("dms").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_replication_task_assessment_run

Type annotations for `boto3.client("dms").cancel_replication_task_assessment_run` method.

[Client.cancel_replication_task_assessment_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.cancel_replication_task_assessment_run)

```python
def cancel_replication_task_assessment_run(
    self,
    ReplicationTaskAssessmentRunArn: str
) -> CancelReplicationTaskAssessmentRunResponseTypeDef:
    pass
```

### create_endpoint

Type annotations for `boto3.client("dms").create_endpoint` method.

[Client.create_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.create_endpoint)

```python
def create_endpoint(
    self,
    EndpointIdentifier: str,
    EndpointType: ReplicationEndpointTypeValue,
    EngineName: str,
    Username: str = None,
    Password: str = None,
    ServerName: str = None,
    Port: int = None,
    DatabaseName: str = None,
    ExtraConnectionAttributes: str = None,
    KmsKeyId: str = None,
    Tags: List["TagTypeDef"] = None,
    CertificateArn: str = None,
    SslMode: DmsSslModeValue = None,
    ServiceAccessRoleArn: str = None,
    ExternalTableDefinition: str = None,
    DynamoDbSettings: "DynamoDbSettingsTypeDef" = None,
    S3Settings: "S3SettingsTypeDef" = None,
    DmsTransferSettings: "DmsTransferSettingsTypeDef" = None,
    MongoDbSettings: "MongoDbSettingsTypeDef" = None,
    KinesisSettings: "KinesisSettingsTypeDef" = None,
    KafkaSettings: "KafkaSettingsTypeDef" = None,
    ElasticsearchSettings: "ElasticsearchSettingsTypeDef" = None,
    NeptuneSettings: "NeptuneSettingsTypeDef" = None,
    RedshiftSettings: "RedshiftSettingsTypeDef" = None,
    PostgreSQLSettings: "PostgreSQLSettingsTypeDef" = None,
    MySQLSettings: "MySQLSettingsTypeDef" = None,
    OracleSettings: "OracleSettingsTypeDef" = None,
    SybaseSettings: "SybaseSettingsTypeDef" = None,
    MicrosoftSQLServerSettings: "MicrosoftSQLServerSettingsTypeDef" = None,
    IBMDb2Settings: "IBMDb2SettingsTypeDef" = None,
    ResourceIdentifier: str = None,
    DocDbSettings: "DocDbSettingsTypeDef" = None
) -> CreateEndpointResponseTypeDef:
    pass
```

### create_event_subscription

Type annotations for `boto3.client("dms").create_event_subscription` method.

[Client.create_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.create_event_subscription)

```python
def create_event_subscription(
    self,
    SubscriptionName: str,
    SnsTopicArn: str,
    SourceType: str = None,
    EventCategories: List[str] = None,
    SourceIds: List[str] = None,
    Enabled: bool = None,
    Tags: List["TagTypeDef"] = None
) -> CreateEventSubscriptionResponseTypeDef:
    pass
```

### create_replication_instance

Type annotations for `boto3.client("dms").create_replication_instance` method.

[Client.create_replication_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.create_replication_instance)

```python
def create_replication_instance(
    self,
    ReplicationInstanceIdentifier: str,
    ReplicationInstanceClass: str,
    AllocatedStorage: int = None,
    VpcSecurityGroupIds: List[str] = None,
    AvailabilityZone: str = None,
    ReplicationSubnetGroupIdentifier: str = None,
    PreferredMaintenanceWindow: str = None,
    MultiAZ: bool = None,
    EngineVersion: str = None,
    AutoMinorVersionUpgrade: bool = None,
    Tags: List["TagTypeDef"] = None,
    KmsKeyId: str = None,
    PubliclyAccessible: bool = None,
    DnsNameServers: str = None,
    ResourceIdentifier: str = None
) -> CreateReplicationInstanceResponseTypeDef:
    pass
```

### create_replication_subnet_group

Type annotations for `boto3.client("dms").create_replication_subnet_group` method.

[Client.create_replication_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.create_replication_subnet_group)

```python
def create_replication_subnet_group(
    self,
    ReplicationSubnetGroupIdentifier: str,
    ReplicationSubnetGroupDescription: str,
    SubnetIds: List[str],
    Tags: List["TagTypeDef"] = None
) -> CreateReplicationSubnetGroupResponseTypeDef:
    pass
```

### create_replication_task

Type annotations for `boto3.client("dms").create_replication_task` method.

[Client.create_replication_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.create_replication_task)

```python
def create_replication_task(
    self,
    ReplicationTaskIdentifier: str,
    SourceEndpointArn: str,
    TargetEndpointArn: str,
    ReplicationInstanceArn: str,
    MigrationType: MigrationTypeValue,
    TableMappings: str,
    ReplicationTaskSettings: str = None,
    CdcStartTime: datetime = None,
    CdcStartPosition: str = None,
    CdcStopPosition: str = None,
    Tags: List["TagTypeDef"] = None,
    TaskData: str = None,
    ResourceIdentifier: str = None
) -> CreateReplicationTaskResponseTypeDef:
    pass
```

### delete_certificate

Type annotations for `boto3.client("dms").delete_certificate` method.

[Client.delete_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.delete_certificate)

```python
def delete_certificate(
    self,
    CertificateArn: str
) -> DeleteCertificateResponseTypeDef:
    pass
```

### delete_connection

Type annotations for `boto3.client("dms").delete_connection` method.

[Client.delete_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.delete_connection)

```python
def delete_connection(
    self,
    EndpointArn: str,
    ReplicationInstanceArn: str
) -> DeleteConnectionResponseTypeDef:
    pass
```

### delete_endpoint

Type annotations for `boto3.client("dms").delete_endpoint` method.

[Client.delete_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.delete_endpoint)

```python
def delete_endpoint(
    self,
    EndpointArn: str
) -> DeleteEndpointResponseTypeDef:
    pass
```

### delete_event_subscription

Type annotations for `boto3.client("dms").delete_event_subscription` method.

[Client.delete_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.delete_event_subscription)

```python
def delete_event_subscription(
    self,
    SubscriptionName: str
) -> DeleteEventSubscriptionResponseTypeDef:
    pass
```

### delete_replication_instance

Type annotations for `boto3.client("dms").delete_replication_instance` method.

[Client.delete_replication_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.delete_replication_instance)

```python
def delete_replication_instance(
    self,
    ReplicationInstanceArn: str
) -> DeleteReplicationInstanceResponseTypeDef:
    pass
```

### delete_replication_subnet_group

Type annotations for `boto3.client("dms").delete_replication_subnet_group` method.

[Client.delete_replication_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.delete_replication_subnet_group)

```python
def delete_replication_subnet_group(
    self,
    ReplicationSubnetGroupIdentifier: str
) -> Dict[str, Any]:
    pass
```

### delete_replication_task

Type annotations for `boto3.client("dms").delete_replication_task` method.

[Client.delete_replication_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.delete_replication_task)

```python
def delete_replication_task(
    self,
    ReplicationTaskArn: str
) -> DeleteReplicationTaskResponseTypeDef:
    pass
```

### delete_replication_task_assessment_run

Type annotations for `boto3.client("dms").delete_replication_task_assessment_run` method.

[Client.delete_replication_task_assessment_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.delete_replication_task_assessment_run)

```python
def delete_replication_task_assessment_run(
    self,
    ReplicationTaskAssessmentRunArn: str
) -> DeleteReplicationTaskAssessmentRunResponseTypeDef:
    pass
```

### describe_account_attributes

Type annotations for `boto3.client("dms").describe_account_attributes` method.

[Client.describe_account_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_account_attributes)

```python
def describe_account_attributes(
    self
) -> DescribeAccountAttributesResponseTypeDef:
    pass
```

### describe_applicable_individual_assessments

Type annotations for `boto3.client("dms").describe_applicable_individual_assessments` method.

[Client.describe_applicable_individual_assessments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_applicable_individual_assessments)

```python
def describe_applicable_individual_assessments(
    self,
    ReplicationTaskArn: str = None,
    ReplicationInstanceArn: str = None,
    SourceEngineName: str = None,
    TargetEngineName: str = None,
    MigrationType: MigrationTypeValue = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DescribeApplicableIndividualAssessmentsResponseTypeDef:
    pass
```

### describe_certificates

Type annotations for `boto3.client("dms").describe_certificates` method.

[Client.describe_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_certificates)

```python
def describe_certificates(
    self,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DescribeCertificatesResponseTypeDef:
    pass
```

### describe_connections

Type annotations for `boto3.client("dms").describe_connections` method.

[Client.describe_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_connections)

```python
def describe_connections(
    self,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DescribeConnectionsResponseTypeDef:
    pass
```

### describe_endpoint_settings

Type annotations for `boto3.client("dms").describe_endpoint_settings` method.

[Client.describe_endpoint_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_endpoint_settings)

```python
def describe_endpoint_settings(
    self,
    EngineName: str,
    MaxRecords: int = None,
    Marker: str = None
) -> DescribeEndpointSettingsResponseTypeDef:
    pass
```

### describe_endpoint_types

Type annotations for `boto3.client("dms").describe_endpoint_types` method.

[Client.describe_endpoint_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_endpoint_types)

```python
def describe_endpoint_types(
    self,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DescribeEndpointTypesResponseTypeDef:
    pass
```

### describe_endpoints

Type annotations for `boto3.client("dms").describe_endpoints` method.

[Client.describe_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_endpoints)

```python
def describe_endpoints(
    self,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DescribeEndpointsResponseTypeDef:
    pass
```

### describe_event_categories

Type annotations for `boto3.client("dms").describe_event_categories` method.

[Client.describe_event_categories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_event_categories)

```python
def describe_event_categories(
    self,
    SourceType: str = None,
    Filters: List[FilterTypeDef] = None
) -> DescribeEventCategoriesResponseTypeDef:
    pass
```

### describe_event_subscriptions

Type annotations for `boto3.client("dms").describe_event_subscriptions` method.

[Client.describe_event_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_event_subscriptions)

```python
def describe_event_subscriptions(
    self,
    SubscriptionName: str = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DescribeEventSubscriptionsResponseTypeDef:
    pass
```

### describe_events

Type annotations for `boto3.client("dms").describe_events` method.

[Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_events)

```python
def describe_events(
    self,
    SourceIdentifier: str = None,
    SourceType: SourceType = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    Duration: int = None,
    EventCategories: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DescribeEventsResponseTypeDef:
    pass
```

### describe_orderable_replication_instances

Type annotations for `boto3.client("dms").describe_orderable_replication_instances` method.

[Client.describe_orderable_replication_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_orderable_replication_instances)

```python
def describe_orderable_replication_instances(
    self,
    MaxRecords: int = None,
    Marker: str = None
) -> DescribeOrderableReplicationInstancesResponseTypeDef:
    pass
```

### describe_pending_maintenance_actions

Type annotations for `boto3.client("dms").describe_pending_maintenance_actions` method.

[Client.describe_pending_maintenance_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_pending_maintenance_actions)

```python
def describe_pending_maintenance_actions(
    self,
    ReplicationInstanceArn: str = None,
    Filters: List[FilterTypeDef] = None,
    Marker: str = None,
    MaxRecords: int = None
) -> DescribePendingMaintenanceActionsResponseTypeDef:
    pass
```

### describe_refresh_schemas_status

Type annotations for `boto3.client("dms").describe_refresh_schemas_status` method.

[Client.describe_refresh_schemas_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_refresh_schemas_status)

```python
def describe_refresh_schemas_status(
    self,
    EndpointArn: str
) -> DescribeRefreshSchemasStatusResponseTypeDef:
    pass
```

### describe_replication_instance_task_logs

Type annotations for `boto3.client("dms").describe_replication_instance_task_logs` method.

[Client.describe_replication_instance_task_logs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_instance_task_logs)

```python
def describe_replication_instance_task_logs(
    self,
    ReplicationInstanceArn: str,
    MaxRecords: int = None,
    Marker: str = None
) -> DescribeReplicationInstanceTaskLogsResponseTypeDef:
    pass
```

### describe_replication_instances

Type annotations for `boto3.client("dms").describe_replication_instances` method.

[Client.describe_replication_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_instances)

```python
def describe_replication_instances(
    self,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DescribeReplicationInstancesResponseTypeDef:
    pass
```

### describe_replication_subnet_groups

Type annotations for `boto3.client("dms").describe_replication_subnet_groups` method.

[Client.describe_replication_subnet_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_subnet_groups)

```python
def describe_replication_subnet_groups(
    self,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DescribeReplicationSubnetGroupsResponseTypeDef:
    pass
```

### describe_replication_task_assessment_results

Type annotations for `boto3.client("dms").describe_replication_task_assessment_results` method.

[Client.describe_replication_task_assessment_results documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_task_assessment_results)

```python
def describe_replication_task_assessment_results(
    self,
    ReplicationTaskArn: str = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DescribeReplicationTaskAssessmentResultsResponseTypeDef:
    pass
```

### describe_replication_task_assessment_runs

Type annotations for `boto3.client("dms").describe_replication_task_assessment_runs` method.

[Client.describe_replication_task_assessment_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_task_assessment_runs)

```python
def describe_replication_task_assessment_runs(
    self,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DescribeReplicationTaskAssessmentRunsResponseTypeDef:
    pass
```

### describe_replication_task_individual_assessments

Type annotations for `boto3.client("dms").describe_replication_task_individual_assessments` method.

[Client.describe_replication_task_individual_assessments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_task_individual_assessments)

```python
def describe_replication_task_individual_assessments(
    self,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None
) -> DescribeReplicationTaskIndividualAssessmentsResponseTypeDef:
    pass
```

### describe_replication_tasks

Type annotations for `boto3.client("dms").describe_replication_tasks` method.

[Client.describe_replication_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_tasks)

```python
def describe_replication_tasks(
    self,
    Filters: List[FilterTypeDef] = None,
    MaxRecords: int = None,
    Marker: str = None,
    WithoutSettings: bool = None
) -> DescribeReplicationTasksResponseTypeDef:
    pass
```

### describe_schemas

Type annotations for `boto3.client("dms").describe_schemas` method.

[Client.describe_schemas documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_schemas)

```python
def describe_schemas(
    self,
    EndpointArn: str,
    MaxRecords: int = None,
    Marker: str = None
) -> DescribeSchemasResponseTypeDef:
    pass
```

### describe_table_statistics

Type annotations for `boto3.client("dms").describe_table_statistics` method.

[Client.describe_table_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.describe_table_statistics)

```python
def describe_table_statistics(
    self,
    ReplicationTaskArn: str,
    MaxRecords: int = None,
    Marker: str = None,
    Filters: List[FilterTypeDef] = None
) -> DescribeTableStatisticsResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("dms").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.generate_presigned_url)

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

### import_certificate

Type annotations for `boto3.client("dms").import_certificate` method.

[Client.import_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.import_certificate)

```python
def import_certificate(
    self,
    CertificateIdentifier: str,
    CertificatePem: str = None,
    CertificateWallet: Union[bytes, IO[bytes]] = None,
    Tags: List["TagTypeDef"] = None
) -> ImportCertificateResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("dms").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### modify_endpoint

Type annotations for `boto3.client("dms").modify_endpoint` method.

[Client.modify_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.modify_endpoint)

```python
def modify_endpoint(
    self,
    EndpointArn: str,
    EndpointIdentifier: str = None,
    EndpointType: ReplicationEndpointTypeValue = None,
    EngineName: str = None,
    Username: str = None,
    Password: str = None,
    ServerName: str = None,
    Port: int = None,
    DatabaseName: str = None,
    ExtraConnectionAttributes: str = None,
    CertificateArn: str = None,
    SslMode: DmsSslModeValue = None,
    ServiceAccessRoleArn: str = None,
    ExternalTableDefinition: str = None,
    DynamoDbSettings: "DynamoDbSettingsTypeDef" = None,
    S3Settings: "S3SettingsTypeDef" = None,
    DmsTransferSettings: "DmsTransferSettingsTypeDef" = None,
    MongoDbSettings: "MongoDbSettingsTypeDef" = None,
    KinesisSettings: "KinesisSettingsTypeDef" = None,
    KafkaSettings: "KafkaSettingsTypeDef" = None,
    ElasticsearchSettings: "ElasticsearchSettingsTypeDef" = None,
    NeptuneSettings: "NeptuneSettingsTypeDef" = None,
    RedshiftSettings: "RedshiftSettingsTypeDef" = None,
    PostgreSQLSettings: "PostgreSQLSettingsTypeDef" = None,
    MySQLSettings: "MySQLSettingsTypeDef" = None,
    OracleSettings: "OracleSettingsTypeDef" = None,
    SybaseSettings: "SybaseSettingsTypeDef" = None,
    MicrosoftSQLServerSettings: "MicrosoftSQLServerSettingsTypeDef" = None,
    IBMDb2Settings: "IBMDb2SettingsTypeDef" = None,
    DocDbSettings: "DocDbSettingsTypeDef" = None
) -> ModifyEndpointResponseTypeDef:
    pass
```

### modify_event_subscription

Type annotations for `boto3.client("dms").modify_event_subscription` method.

[Client.modify_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.modify_event_subscription)

```python
def modify_event_subscription(
    self,
    SubscriptionName: str,
    SnsTopicArn: str = None,
    SourceType: str = None,
    EventCategories: List[str] = None,
    Enabled: bool = None
) -> ModifyEventSubscriptionResponseTypeDef:
    pass
```

### modify_replication_instance

Type annotations for `boto3.client("dms").modify_replication_instance` method.

[Client.modify_replication_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.modify_replication_instance)

```python
def modify_replication_instance(
    self,
    ReplicationInstanceArn: str,
    AllocatedStorage: int = None,
    ApplyImmediately: bool = None,
    ReplicationInstanceClass: str = None,
    VpcSecurityGroupIds: List[str] = None,
    PreferredMaintenanceWindow: str = None,
    MultiAZ: bool = None,
    EngineVersion: str = None,
    AllowMajorVersionUpgrade: bool = None,
    AutoMinorVersionUpgrade: bool = None,
    ReplicationInstanceIdentifier: str = None
) -> ModifyReplicationInstanceResponseTypeDef:
    pass
```

### modify_replication_subnet_group

Type annotations for `boto3.client("dms").modify_replication_subnet_group` method.

[Client.modify_replication_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.modify_replication_subnet_group)

```python
def modify_replication_subnet_group(
    self,
    ReplicationSubnetGroupIdentifier: str,
    SubnetIds: List[str],
    ReplicationSubnetGroupDescription: str = None
) -> ModifyReplicationSubnetGroupResponseTypeDef:
    pass
```

### modify_replication_task

Type annotations for `boto3.client("dms").modify_replication_task` method.

[Client.modify_replication_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.modify_replication_task)

```python
def modify_replication_task(
    self,
    ReplicationTaskArn: str,
    ReplicationTaskIdentifier: str = None,
    MigrationType: MigrationTypeValue = None,
    TableMappings: str = None,
    ReplicationTaskSettings: str = None,
    CdcStartTime: datetime = None,
    CdcStartPosition: str = None,
    CdcStopPosition: str = None,
    TaskData: str = None
) -> ModifyReplicationTaskResponseTypeDef:
    pass
```

### move_replication_task

Type annotations for `boto3.client("dms").move_replication_task` method.

[Client.move_replication_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.move_replication_task)

```python
def move_replication_task(
    self,
    ReplicationTaskArn: str,
    TargetReplicationInstanceArn: str
) -> MoveReplicationTaskResponseTypeDef:
    pass
```

### reboot_replication_instance

Type annotations for `boto3.client("dms").reboot_replication_instance` method.

[Client.reboot_replication_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.reboot_replication_instance)

```python
def reboot_replication_instance(
    self,
    ReplicationInstanceArn: str,
    ForceFailover: bool = None
) -> RebootReplicationInstanceResponseTypeDef:
    pass
```

### refresh_schemas

Type annotations for `boto3.client("dms").refresh_schemas` method.

[Client.refresh_schemas documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.refresh_schemas)

```python
def refresh_schemas(
    self,
    EndpointArn: str,
    ReplicationInstanceArn: str
) -> RefreshSchemasResponseTypeDef:
    pass
```

### reload_tables

Type annotations for `boto3.client("dms").reload_tables` method.

[Client.reload_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.reload_tables)

```python
def reload_tables(
    self,
    ReplicationTaskArn: str,
    TablesToReload: List[TableToReloadTypeDef],
    ReloadOption: ReloadOptionValue = None
) -> ReloadTablesResponseTypeDef:
    pass
```

### remove_tags_from_resource

Type annotations for `boto3.client("dms").remove_tags_from_resource` method.

[Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.remove_tags_from_resource)

```python
def remove_tags_from_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### start_replication_task

Type annotations for `boto3.client("dms").start_replication_task` method.

[Client.start_replication_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.start_replication_task)

```python
def start_replication_task(
    self,
    ReplicationTaskArn: str,
    StartReplicationTaskType: StartReplicationTaskTypeValue,
    CdcStartTime: datetime = None,
    CdcStartPosition: str = None,
    CdcStopPosition: str = None
) -> StartReplicationTaskResponseTypeDef:
    pass
```

### start_replication_task_assessment

Type annotations for `boto3.client("dms").start_replication_task_assessment` method.

[Client.start_replication_task_assessment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.start_replication_task_assessment)

```python
def start_replication_task_assessment(
    self,
    ReplicationTaskArn: str
) -> StartReplicationTaskAssessmentResponseTypeDef:
    pass
```

### start_replication_task_assessment_run

Type annotations for `boto3.client("dms").start_replication_task_assessment_run` method.

[Client.start_replication_task_assessment_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.start_replication_task_assessment_run)

```python
def start_replication_task_assessment_run(
    self,
    ReplicationTaskArn: str,
    ServiceAccessRoleArn: str,
    ResultLocationBucket: str,
    AssessmentRunName: str,
    ResultLocationFolder: str = None,
    ResultEncryptionMode: str = None,
    ResultKmsKeyArn: str = None,
    IncludeOnly: List[str] = None,
    Exclude: List[str] = None
) -> StartReplicationTaskAssessmentRunResponseTypeDef:
    pass
```

### stop_replication_task

Type annotations for `boto3.client("dms").stop_replication_task` method.

[Client.stop_replication_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.stop_replication_task)

```python
def stop_replication_task(
    self,
    ReplicationTaskArn: str
) -> StopReplicationTaskResponseTypeDef:
    pass
```

### test_connection

Type annotations for `boto3.client("dms").test_connection` method.

[Client.test_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client.test_connection)

```python
def test_connection(
    self,
    ReplicationInstanceArn: str,
    EndpointArn: str
) -> TestConnectionResponseTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("dms").get_paginator` method.

[Paginator.DescribeCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeCertificates)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeCertificatesPaginatorName
) -> DescribeCertificatesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("dms").get_paginator` method.

[Paginator.DescribeConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeConnections)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeConnectionsPaginatorName
) -> DescribeConnectionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("dms").get_paginator` method.

[Paginator.DescribeEndpointTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEndpointTypes)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeEndpointTypesPaginatorName
) -> DescribeEndpointTypesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("dms").get_paginator` method.

[Paginator.DescribeEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEndpoints)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeEndpointsPaginatorName
) -> DescribeEndpointsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("dms").get_paginator` method.

[Paginator.DescribeEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEventSubscriptions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeEventSubscriptionsPaginatorName
) -> DescribeEventSubscriptionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("dms").get_paginator` method.

[Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEvents)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeEventsPaginatorName
) -> DescribeEventsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("dms").get_paginator` method.

[Paginator.DescribeOrderableReplicationInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeOrderableReplicationInstances)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeOrderableReplicationInstancesPaginatorName
) -> DescribeOrderableReplicationInstancesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("dms").get_paginator` method.

[Paginator.DescribeReplicationInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationInstances)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeReplicationInstancesPaginatorName
) -> DescribeReplicationInstancesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("dms").get_paginator` method.

[Paginator.DescribeReplicationSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationSubnetGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeReplicationSubnetGroupsPaginatorName
) -> DescribeReplicationSubnetGroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("dms").get_paginator` method.

[Paginator.DescribeReplicationTaskAssessmentResults documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationTaskAssessmentResults)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeReplicationTaskAssessmentResultsPaginatorName
) -> DescribeReplicationTaskAssessmentResultsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("dms").get_paginator` method.

[Paginator.DescribeReplicationTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationTasks)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeReplicationTasksPaginatorName
) -> DescribeReplicationTasksPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("dms").get_paginator` method.

[Paginator.DescribeSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeSchemas)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeSchemasPaginatorName
) -> DescribeSchemasPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("dms").get_paginator` method.

[Paginator.DescribeTableStatistics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeTableStatistics)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeTableStatisticsPaginatorName
) -> DescribeTableStatisticsPaginator:
    pass
```

### get_waiter

Type annotations for `boto3.client("dms").get_waiter` method.

[Waiter.EndpointDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Waiter.EndpointDeleted)

```python
@overload
def get_waiter(
    self,
    waiter_name: EndpointDeletedWaiterName
) -> EndpointDeletedWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("dms").get_waiter` method.

[Waiter.ReplicationInstanceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationInstanceAvailable)

```python
@overload
def get_waiter(
    self,
    waiter_name: ReplicationInstanceAvailableWaiterName
) -> ReplicationInstanceAvailableWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("dms").get_waiter` method.

[Waiter.ReplicationInstanceDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationInstanceDeleted)

```python
@overload
def get_waiter(
    self,
    waiter_name: ReplicationInstanceDeletedWaiterName
) -> ReplicationInstanceDeletedWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("dms").get_waiter` method.

[Waiter.ReplicationTaskDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskDeleted)

```python
@overload
def get_waiter(
    self,
    waiter_name: ReplicationTaskDeletedWaiterName
) -> ReplicationTaskDeletedWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("dms").get_waiter` method.

[Waiter.ReplicationTaskReady documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskReady)

```python
@overload
def get_waiter(
    self,
    waiter_name: ReplicationTaskReadyWaiterName
) -> ReplicationTaskReadyWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("dms").get_waiter` method.

[Waiter.ReplicationTaskRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskRunning)

```python
@overload
def get_waiter(
    self,
    waiter_name: ReplicationTaskRunningWaiterName
) -> ReplicationTaskRunningWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("dms").get_waiter` method.

[Waiter.ReplicationTaskStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskStopped)

```python
@overload
def get_waiter(
    self,
    waiter_name: ReplicationTaskStoppedWaiterName
) -> ReplicationTaskStoppedWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("dms").get_waiter` method.

[Waiter.TestConnectionSucceeds documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Waiter.TestConnectionSucceeds)

```python
@overload
def get_waiter(
    self,
    waiter_name: TestConnectionSucceedsWaiterName
) -> TestConnectionSucceedsWaiter:
    pass
```