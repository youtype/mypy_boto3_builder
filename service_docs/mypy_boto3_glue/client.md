# GlueClient for boto3 Glue module

> [Index](../index.md) > [Glue](./index.md) > GlueClient

Auto-generated documentation for [Glue](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue)
type annotations stubs module [mypy_boto3_glue](https://pypi.org/project/mypy-boto3-glue/).

- [GlueClient for boto3 Glue module](#glueclient-for-boto3-glue-module)
  - [GlueClient](#glueclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [batch_create_partition](#batch_create_partition)
    - [batch_delete_connection](#batch_delete_connection)
    - [batch_delete_partition](#batch_delete_partition)
    - [batch_delete_table](#batch_delete_table)
    - [batch_delete_table_version](#batch_delete_table_version)
    - [batch_get_crawlers](#batch_get_crawlers)
    - [batch_get_dev_endpoints](#batch_get_dev_endpoints)
    - [batch_get_jobs](#batch_get_jobs)
    - [batch_get_partition](#batch_get_partition)
    - [batch_get_triggers](#batch_get_triggers)
    - [batch_get_workflows](#batch_get_workflows)
    - [batch_stop_job_run](#batch_stop_job_run)
    - [batch_update_partition](#batch_update_partition)
    - [can_paginate](#can_paginate)
    - [cancel_ml_task_run](#cancel_ml_task_run)
    - [check_schema_version_validity](#check_schema_version_validity)
    - [create_classifier](#create_classifier)
    - [create_connection](#create_connection)
    - [create_crawler](#create_crawler)
    - [create_database](#create_database)
    - [create_dev_endpoint](#create_dev_endpoint)
    - [create_job](#create_job)
    - [create_ml_transform](#create_ml_transform)
    - [create_partition](#create_partition)
    - [create_partition_index](#create_partition_index)
    - [create_registry](#create_registry)
    - [create_schema](#create_schema)
    - [create_script](#create_script)
    - [create_security_configuration](#create_security_configuration)
    - [create_table](#create_table)
    - [create_trigger](#create_trigger)
    - [create_user_defined_function](#create_user_defined_function)
    - [create_workflow](#create_workflow)
    - [delete_classifier](#delete_classifier)
    - [delete_column_statistics_for_partition](#delete_column_statistics_for_partition)
    - [delete_column_statistics_for_table](#delete_column_statistics_for_table)
    - [delete_connection](#delete_connection)
    - [delete_crawler](#delete_crawler)
    - [delete_database](#delete_database)
    - [delete_dev_endpoint](#delete_dev_endpoint)
    - [delete_job](#delete_job)
    - [delete_ml_transform](#delete_ml_transform)
    - [delete_partition](#delete_partition)
    - [delete_partition_index](#delete_partition_index)
    - [delete_registry](#delete_registry)
    - [delete_resource_policy](#delete_resource_policy)
    - [delete_schema](#delete_schema)
    - [delete_schema_versions](#delete_schema_versions)
    - [delete_security_configuration](#delete_security_configuration)
    - [delete_table](#delete_table)
    - [delete_table_version](#delete_table_version)
    - [delete_trigger](#delete_trigger)
    - [delete_user_defined_function](#delete_user_defined_function)
    - [delete_workflow](#delete_workflow)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_catalog_import_status](#get_catalog_import_status)
    - [get_classifier](#get_classifier)
    - [get_classifiers](#get_classifiers)
    - [get_column_statistics_for_partition](#get_column_statistics_for_partition)
    - [get_column_statistics_for_table](#get_column_statistics_for_table)
    - [get_connection](#get_connection)
    - [get_connections](#get_connections)
    - [get_crawler](#get_crawler)
    - [get_crawler_metrics](#get_crawler_metrics)
    - [get_crawlers](#get_crawlers)
    - [get_data_catalog_encryption_settings](#get_data_catalog_encryption_settings)
    - [get_database](#get_database)
    - [get_databases](#get_databases)
    - [get_dataflow_graph](#get_dataflow_graph)
    - [get_dev_endpoint](#get_dev_endpoint)
    - [get_dev_endpoints](#get_dev_endpoints)
    - [get_job](#get_job)
    - [get_job_bookmark](#get_job_bookmark)
    - [get_job_run](#get_job_run)
    - [get_job_runs](#get_job_runs)
    - [get_jobs](#get_jobs)
    - [get_mapping](#get_mapping)
    - [get_ml_task_run](#get_ml_task_run)
    - [get_ml_task_runs](#get_ml_task_runs)
    - [get_ml_transform](#get_ml_transform)
    - [get_ml_transforms](#get_ml_transforms)
    - [get_partition](#get_partition)
    - [get_partition_indexes](#get_partition_indexes)
    - [get_partitions](#get_partitions)
    - [get_plan](#get_plan)
    - [get_registry](#get_registry)
    - [get_resource_policies](#get_resource_policies)
    - [get_resource_policy](#get_resource_policy)
    - [get_schema](#get_schema)
    - [get_schema_by_definition](#get_schema_by_definition)
    - [get_schema_version](#get_schema_version)
    - [get_schema_versions_diff](#get_schema_versions_diff)
    - [get_security_configuration](#get_security_configuration)
    - [get_security_configurations](#get_security_configurations)
    - [get_table](#get_table)
    - [get_table_version](#get_table_version)
    - [get_table_versions](#get_table_versions)
    - [get_tables](#get_tables)
    - [get_tags](#get_tags)
    - [get_trigger](#get_trigger)
    - [get_triggers](#get_triggers)
    - [get_user_defined_function](#get_user_defined_function)
    - [get_user_defined_functions](#get_user_defined_functions)
    - [get_workflow](#get_workflow)
    - [get_workflow_run](#get_workflow_run)
    - [get_workflow_run_properties](#get_workflow_run_properties)
    - [get_workflow_runs](#get_workflow_runs)
    - [import_catalog_to_glue](#import_catalog_to_glue)
    - [list_crawlers](#list_crawlers)
    - [list_dev_endpoints](#list_dev_endpoints)
    - [list_jobs](#list_jobs)
    - [list_ml_transforms](#list_ml_transforms)
    - [list_registries](#list_registries)
    - [list_schema_versions](#list_schema_versions)
    - [list_schemas](#list_schemas)
    - [list_triggers](#list_triggers)
    - [list_workflows](#list_workflows)
    - [put_data_catalog_encryption_settings](#put_data_catalog_encryption_settings)
    - [put_resource_policy](#put_resource_policy)
    - [put_schema_version_metadata](#put_schema_version_metadata)
    - [put_workflow_run_properties](#put_workflow_run_properties)
    - [query_schema_version_metadata](#query_schema_version_metadata)
    - [register_schema_version](#register_schema_version)
    - [remove_schema_version_metadata](#remove_schema_version_metadata)
    - [reset_job_bookmark](#reset_job_bookmark)
    - [resume_workflow_run](#resume_workflow_run)
    - [search_tables](#search_tables)
    - [start_crawler](#start_crawler)
    - [start_crawler_schedule](#start_crawler_schedule)
    - [start_export_labels_task_run](#start_export_labels_task_run)
    - [start_import_labels_task_run](#start_import_labels_task_run)
    - [start_job_run](#start_job_run)
    - [start_ml_evaluation_task_run](#start_ml_evaluation_task_run)
    - [start_ml_labeling_set_generation_task_run](#start_ml_labeling_set_generation_task_run)
    - [start_trigger](#start_trigger)
    - [start_workflow_run](#start_workflow_run)
    - [stop_crawler](#stop_crawler)
    - [stop_crawler_schedule](#stop_crawler_schedule)
    - [stop_trigger](#stop_trigger)
    - [stop_workflow_run](#stop_workflow_run)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_classifier](#update_classifier)
    - [update_column_statistics_for_partition](#update_column_statistics_for_partition)
    - [update_column_statistics_for_table](#update_column_statistics_for_table)
    - [update_connection](#update_connection)
    - [update_crawler](#update_crawler)
    - [update_crawler_schedule](#update_crawler_schedule)
    - [update_database](#update_database)
    - [update_dev_endpoint](#update_dev_endpoint)
    - [update_job](#update_job)
    - [update_ml_transform](#update_ml_transform)
    - [update_partition](#update_partition)
    - [update_registry](#update_registry)
    - [update_schema](#update_schema)
    - [update_table](#update_table)
    - [update_trigger](#update_trigger)
    - [update_user_defined_function](#update_user_defined_function)
    - [update_workflow](#update_workflow)
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
    - [get_paginator](#get_paginator-13)
    - [get_paginator](#get_paginator-14)
    - [get_paginator](#get_paginator-15)
    - [get_paginator](#get_paginator-16)
    - [get_paginator](#get_paginator-17)
    - [get_paginator](#get_paginator-18)

## GlueClient

Type annotations for `boto3.client("glue")`

Can be used directly:

```python
from mypy_boto3_glue.client import GlueClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_glue.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.AlreadyExistsException`
- `Exceptions.ClientError`
- `Exceptions.ConcurrentModificationException`
- `Exceptions.ConcurrentRunsExceededException`
- `Exceptions.ConditionCheckFailureException`
- `Exceptions.ConflictException`
- `Exceptions.CrawlerNotRunningException`
- `Exceptions.CrawlerRunningException`
- `Exceptions.CrawlerStoppingException`
- `Exceptions.EntityNotFoundException`
- `Exceptions.GlueEncryptionException`
- `Exceptions.IdempotentParameterMismatchException`
- `Exceptions.IllegalWorkflowStateException`
- `Exceptions.InternalServiceException`
- `Exceptions.InvalidInputException`
- `Exceptions.MLTransformNotReadyException`
- `Exceptions.NoScheduleException`
- `Exceptions.OperationTimeoutException`
- `Exceptions.ResourceNumberLimitExceededException`
- `Exceptions.SchedulerNotRunningException`
- `Exceptions.SchedulerRunningException`
- `Exceptions.SchedulerTransitioningException`
- `Exceptions.ValidationException`
- `Exceptions.VersionMismatchException`


## Methods


### batch_create_partition

Type annotations for `boto3.client("glue").batch_create_partition` method.

[Client.batch_create_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.batch_create_partition)

```python
def batch_create_partition(
    self,
    DatabaseName: str,
    TableName: str,
    PartitionInputList: List["PartitionInputTypeDef"],
    CatalogId: str = None
) -> BatchCreatePartitionResponseTypeDef:
    pass
```

### batch_delete_connection

Type annotations for `boto3.client("glue").batch_delete_connection` method.

[Client.batch_delete_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.batch_delete_connection)

```python
def batch_delete_connection(
    self,
    ConnectionNameList: List[str],
    CatalogId: str = None
) -> BatchDeleteConnectionResponseTypeDef:
    pass
```

### batch_delete_partition

Type annotations for `boto3.client("glue").batch_delete_partition` method.

[Client.batch_delete_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.batch_delete_partition)

```python
def batch_delete_partition(
    self,
    DatabaseName: str,
    TableName: str,
    PartitionsToDelete: List["PartitionValueListTypeDef"],
    CatalogId: str = None
) -> BatchDeletePartitionResponseTypeDef:
    pass
```

### batch_delete_table

Type annotations for `boto3.client("glue").batch_delete_table` method.

[Client.batch_delete_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.batch_delete_table)

```python
def batch_delete_table(
    self,
    DatabaseName: str,
    TablesToDelete: List[str],
    CatalogId: str = None
) -> BatchDeleteTableResponseTypeDef:
    pass
```

### batch_delete_table_version

Type annotations for `boto3.client("glue").batch_delete_table_version` method.

[Client.batch_delete_table_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.batch_delete_table_version)

```python
def batch_delete_table_version(
    self,
    DatabaseName: str,
    TableName: str,
    VersionIds: List[str],
    CatalogId: str = None
) -> BatchDeleteTableVersionResponseTypeDef:
    pass
```

### batch_get_crawlers

Type annotations for `boto3.client("glue").batch_get_crawlers` method.

[Client.batch_get_crawlers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.batch_get_crawlers)

```python
def batch_get_crawlers(
    self,
    CrawlerNames: List[str]
) -> BatchGetCrawlersResponseTypeDef:
    pass
```

### batch_get_dev_endpoints

Type annotations for `boto3.client("glue").batch_get_dev_endpoints` method.

[Client.batch_get_dev_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.batch_get_dev_endpoints)

```python
def batch_get_dev_endpoints(
    self,
    DevEndpointNames: List[str]
) -> BatchGetDevEndpointsResponseTypeDef:
    pass
```

### batch_get_jobs

Type annotations for `boto3.client("glue").batch_get_jobs` method.

[Client.batch_get_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.batch_get_jobs)

```python
def batch_get_jobs(
    self,
    JobNames: List[str]
) -> BatchGetJobsResponseTypeDef:
    pass
```

### batch_get_partition

Type annotations for `boto3.client("glue").batch_get_partition` method.

[Client.batch_get_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.batch_get_partition)

```python
def batch_get_partition(
    self,
    DatabaseName: str,
    TableName: str,
    PartitionsToGet: List["PartitionValueListTypeDef"],
    CatalogId: str = None
) -> BatchGetPartitionResponseTypeDef:
    pass
```

### batch_get_triggers

Type annotations for `boto3.client("glue").batch_get_triggers` method.

[Client.batch_get_triggers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.batch_get_triggers)

```python
def batch_get_triggers(
    self,
    TriggerNames: List[str]
) -> BatchGetTriggersResponseTypeDef:
    pass
```

### batch_get_workflows

Type annotations for `boto3.client("glue").batch_get_workflows` method.

[Client.batch_get_workflows documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.batch_get_workflows)

```python
def batch_get_workflows(
    self,
    Names: List[str],
    IncludeGraph: bool = None
) -> BatchGetWorkflowsResponseTypeDef:
    pass
```

### batch_stop_job_run

Type annotations for `boto3.client("glue").batch_stop_job_run` method.

[Client.batch_stop_job_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.batch_stop_job_run)

```python
def batch_stop_job_run(
    self,
    JobName: str,
    JobRunIds: List[str]
) -> BatchStopJobRunResponseTypeDef:
    pass
```

### batch_update_partition

Type annotations for `boto3.client("glue").batch_update_partition` method.

[Client.batch_update_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.batch_update_partition)

```python
def batch_update_partition(
    self,
    DatabaseName: str,
    TableName: str,
    Entries: List[BatchUpdatePartitionRequestEntryTypeDef],
    CatalogId: str = None
) -> BatchUpdatePartitionResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("glue").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_ml_task_run

Type annotations for `boto3.client("glue").cancel_ml_task_run` method.

[Client.cancel_ml_task_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.cancel_ml_task_run)

```python
def cancel_ml_task_run(
    self,
    TransformId: str,
    TaskRunId: str
) -> CancelMLTaskRunResponseTypeDef:
    pass
```

### check_schema_version_validity

Type annotations for `boto3.client("glue").check_schema_version_validity` method.

[Client.check_schema_version_validity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.check_schema_version_validity)

```python
def check_schema_version_validity(
    self,
    DataFormat: DataFormat,
    SchemaDefinition: str
) -> CheckSchemaVersionValidityResponseTypeDef:
    pass
```

### create_classifier

Type annotations for `boto3.client("glue").create_classifier` method.

[Client.create_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.create_classifier)

```python
def create_classifier(
    self,
    GrokClassifier: CreateGrokClassifierRequestTypeDef = None,
    XMLClassifier: CreateXMLClassifierRequestTypeDef = None,
    JsonClassifier: CreateJsonClassifierRequestTypeDef = None,
    CsvClassifier: CreateCsvClassifierRequestTypeDef = None
) -> Dict[str, Any]:
    pass
```

### create_connection

Type annotations for `boto3.client("glue").create_connection` method.

[Client.create_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.create_connection)

```python
def create_connection(
    self,
    ConnectionInput: ConnectionInputTypeDef,
    CatalogId: str = None
) -> Dict[str, Any]:
    pass
```

### create_crawler

Type annotations for `boto3.client("glue").create_crawler` method.

[Client.create_crawler documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.create_crawler)

```python
def create_crawler(
    self,
    Name: str,
    Role: str,
    Targets: "CrawlerTargetsTypeDef",
    DatabaseName: str = None,
    Description: str = None,
    Schedule: str = None,
    Classifiers: List[str] = None,
    TablePrefix: str = None,
    SchemaChangePolicy: "SchemaChangePolicyTypeDef" = None,
    RecrawlPolicy: "RecrawlPolicyTypeDef" = None,
    LineageConfiguration: "LineageConfigurationTypeDef" = None,
    Configuration: str = None,
    CrawlerSecurityConfiguration: str = None,
    Tags: Dict[str, str] = None
) -> Dict[str, Any]:
    pass
```

### create_database

Type annotations for `boto3.client("glue").create_database` method.

[Client.create_database documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.create_database)

```python
def create_database(
    self,
    DatabaseInput: DatabaseInputTypeDef,
    CatalogId: str = None
) -> Dict[str, Any]:
    pass
```

### create_dev_endpoint

Type annotations for `boto3.client("glue").create_dev_endpoint` method.

[Client.create_dev_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.create_dev_endpoint)

```python
def create_dev_endpoint(
    self,
    EndpointName: str,
    RoleArn: str,
    SecurityGroupIds: List[str] = None,
    SubnetId: str = None,
    PublicKey: str = None,
    PublicKeys: List[str] = None,
    NumberOfNodes: int = None,
    WorkerType: WorkerType = None,
    GlueVersion: str = None,
    NumberOfWorkers: int = None,
    ExtraPythonLibsS3Path: str = None,
    ExtraJarsS3Path: str = None,
    SecurityConfiguration: str = None,
    Tags: Dict[str, str] = None,
    Arguments: Dict[str, str] = None
) -> CreateDevEndpointResponseTypeDef:
    pass
```

### create_job

Type annotations for `boto3.client("glue").create_job` method.

[Client.create_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.create_job)

```python
def create_job(
    self,
    Name: str,
    Role: str,
    Command: "JobCommandTypeDef",
    Description: str = None,
    LogUri: str = None,
    ExecutionProperty: "ExecutionPropertyTypeDef" = None,
    DefaultArguments: Dict[str, str] = None,
    NonOverridableArguments: Dict[str, str] = None,
    Connections: "ConnectionsListTypeDef" = None,
    MaxRetries: int = None,
    AllocatedCapacity: int = None,
    Timeout: int = None,
    MaxCapacity: float = None,
    SecurityConfiguration: str = None,
    Tags: Dict[str, str] = None,
    NotificationProperty: "NotificationPropertyTypeDef" = None,
    GlueVersion: str = None,
    NumberOfWorkers: int = None,
    WorkerType: WorkerType = None
) -> CreateJobResponseTypeDef:
    pass
```

### create_ml_transform

Type annotations for `boto3.client("glue").create_ml_transform` method.

[Client.create_ml_transform documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.create_ml_transform)

```python
def create_ml_transform(
    self,
    Name: str,
    InputRecordTables: List["GlueTableTypeDef"],
    Parameters: "TransformParametersTypeDef",
    Role: str,
    Description: str = None,
    GlueVersion: str = None,
    MaxCapacity: float = None,
    WorkerType: WorkerType = None,
    NumberOfWorkers: int = None,
    Timeout: int = None,
    MaxRetries: int = None,
    Tags: Dict[str, str] = None,
    TransformEncryption: "TransformEncryptionTypeDef" = None
) -> CreateMLTransformResponseTypeDef:
    pass
```

### create_partition

Type annotations for `boto3.client("glue").create_partition` method.

[Client.create_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.create_partition)

```python
def create_partition(
    self,
    DatabaseName: str,
    TableName: str,
    PartitionInput: "PartitionInputTypeDef",
    CatalogId: str = None
) -> Dict[str, Any]:
    pass
```

### create_partition_index

Type annotations for `boto3.client("glue").create_partition_index` method.

[Client.create_partition_index documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.create_partition_index)

```python
def create_partition_index(
    self,
    DatabaseName: str,
    TableName: str,
    PartitionIndex: PartitionIndexTypeDef,
    CatalogId: str = None
) -> Dict[str, Any]:
    pass
```

### create_registry

Type annotations for `boto3.client("glue").create_registry` method.

[Client.create_registry documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.create_registry)

```python
def create_registry(
    self,
    RegistryName: str,
    Description: str = None,
    Tags: Dict[str, str] = None
) -> CreateRegistryResponseTypeDef:
    pass
```

### create_schema

Type annotations for `boto3.client("glue").create_schema` method.

[Client.create_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.create_schema)

```python
def create_schema(
    self,
    SchemaName: str,
    DataFormat: DataFormat,
    RegistryId: RegistryIdTypeDef = None,
    Compatibility: Compatibility = None,
    Description: str = None,
    Tags: Dict[str, str] = None,
    SchemaDefinition: str = None
) -> CreateSchemaResponseTypeDef:
    pass
```

### create_script

Type annotations for `boto3.client("glue").create_script` method.

[Client.create_script documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.create_script)

```python
def create_script(
    self,
    DagNodes: List["CodeGenNodeTypeDef"] = None,
    DagEdges: List["CodeGenEdgeTypeDef"] = None,
    Language: Language = None
) -> CreateScriptResponseTypeDef:
    pass
```

### create_security_configuration

Type annotations for `boto3.client("glue").create_security_configuration` method.

[Client.create_security_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.create_security_configuration)

```python
def create_security_configuration(
    self,
    Name: str,
    EncryptionConfiguration: "EncryptionConfigurationTypeDef"
) -> CreateSecurityConfigurationResponseTypeDef:
    pass
```

### create_table

Type annotations for `boto3.client("glue").create_table` method.

[Client.create_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.create_table)

```python
def create_table(
    self,
    DatabaseName: str,
    TableInput: TableInputTypeDef,
    CatalogId: str = None,
    PartitionIndexes: List[PartitionIndexTypeDef] = None
) -> Dict[str, Any]:
    pass
```

### create_trigger

Type annotations for `boto3.client("glue").create_trigger` method.

[Client.create_trigger documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.create_trigger)

```python
def create_trigger(
    self,
    Name: str,
    Type: TriggerType,
    Actions: List["ActionTypeDef"],
    WorkflowName: str = None,
    Schedule: str = None,
    Predicate: "PredicateTypeDef" = None,
    Description: str = None,
    StartOnCreation: bool = None,
    Tags: Dict[str, str] = None
) -> CreateTriggerResponseTypeDef:
    pass
```

### create_user_defined_function

Type annotations for `boto3.client("glue").create_user_defined_function` method.

[Client.create_user_defined_function documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.create_user_defined_function)

```python
def create_user_defined_function(
    self,
    DatabaseName: str,
    FunctionInput: UserDefinedFunctionInputTypeDef,
    CatalogId: str = None
) -> Dict[str, Any]:
    pass
```

### create_workflow

Type annotations for `boto3.client("glue").create_workflow` method.

[Client.create_workflow documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.create_workflow)

```python
def create_workflow(
    self,
    Name: str,
    Description: str = None,
    DefaultRunProperties: Dict[str, str] = None,
    Tags: Dict[str, str] = None,
    MaxConcurrentRuns: int = None
) -> CreateWorkflowResponseTypeDef:
    pass
```

### delete_classifier

Type annotations for `boto3.client("glue").delete_classifier` method.

[Client.delete_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.delete_classifier)

```python
def delete_classifier(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### delete_column_statistics_for_partition

Type annotations for `boto3.client("glue").delete_column_statistics_for_partition` method.

[Client.delete_column_statistics_for_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.delete_column_statistics_for_partition)

```python
def delete_column_statistics_for_partition(
    self,
    DatabaseName: str,
    TableName: str,
    PartitionValues: List[str],
    ColumnName: str,
    CatalogId: str = None
) -> Dict[str, Any]:
    pass
```

### delete_column_statistics_for_table

Type annotations for `boto3.client("glue").delete_column_statistics_for_table` method.

[Client.delete_column_statistics_for_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.delete_column_statistics_for_table)

```python
def delete_column_statistics_for_table(
    self,
    DatabaseName: str,
    TableName: str,
    ColumnName: str,
    CatalogId: str = None
) -> Dict[str, Any]:
    pass
```

### delete_connection

Type annotations for `boto3.client("glue").delete_connection` method.

[Client.delete_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.delete_connection)

```python
def delete_connection(
    self,
    ConnectionName: str,
    CatalogId: str = None
) -> Dict[str, Any]:
    pass
```

### delete_crawler

Type annotations for `boto3.client("glue").delete_crawler` method.

[Client.delete_crawler documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.delete_crawler)

```python
def delete_crawler(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### delete_database

Type annotations for `boto3.client("glue").delete_database` method.

[Client.delete_database documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.delete_database)

```python
def delete_database(
    self,
    Name: str,
    CatalogId: str = None
) -> Dict[str, Any]:
    pass
```

### delete_dev_endpoint

Type annotations for `boto3.client("glue").delete_dev_endpoint` method.

[Client.delete_dev_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.delete_dev_endpoint)

```python
def delete_dev_endpoint(
    self,
    EndpointName: str
) -> Dict[str, Any]:
    pass
```

### delete_job

Type annotations for `boto3.client("glue").delete_job` method.

[Client.delete_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.delete_job)

```python
def delete_job(
    self,
    JobName: str
) -> DeleteJobResponseTypeDef:
    pass
```

### delete_ml_transform

Type annotations for `boto3.client("glue").delete_ml_transform` method.

[Client.delete_ml_transform documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.delete_ml_transform)

```python
def delete_ml_transform(
    self,
    TransformId: str
) -> DeleteMLTransformResponseTypeDef:
    pass
```

### delete_partition

Type annotations for `boto3.client("glue").delete_partition` method.

[Client.delete_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.delete_partition)

```python
def delete_partition(
    self,
    DatabaseName: str,
    TableName: str,
    PartitionValues: List[str],
    CatalogId: str = None
) -> Dict[str, Any]:
    pass
```

### delete_partition_index

Type annotations for `boto3.client("glue").delete_partition_index` method.

[Client.delete_partition_index documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.delete_partition_index)

```python
def delete_partition_index(
    self,
    DatabaseName: str,
    TableName: str,
    IndexName: str,
    CatalogId: str = None
) -> Dict[str, Any]:
    pass
```

### delete_registry

Type annotations for `boto3.client("glue").delete_registry` method.

[Client.delete_registry documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.delete_registry)

```python
def delete_registry(
    self,
    RegistryId: RegistryIdTypeDef
) -> DeleteRegistryResponseTypeDef:
    pass
```

### delete_resource_policy

Type annotations for `boto3.client("glue").delete_resource_policy` method.

[Client.delete_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.delete_resource_policy)

```python
def delete_resource_policy(
    self,
    PolicyHashCondition: str = None,
    ResourceArn: str = None
) -> Dict[str, Any]:
    pass
```

### delete_schema

Type annotations for `boto3.client("glue").delete_schema` method.

[Client.delete_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.delete_schema)

```python
def delete_schema(
    self,
    SchemaId: "SchemaIdTypeDef"
) -> DeleteSchemaResponseTypeDef:
    pass
```

### delete_schema_versions

Type annotations for `boto3.client("glue").delete_schema_versions` method.

[Client.delete_schema_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.delete_schema_versions)

```python
def delete_schema_versions(
    self,
    SchemaId: "SchemaIdTypeDef",
    Versions: str
) -> DeleteSchemaVersionsResponseTypeDef:
    pass
```

### delete_security_configuration

Type annotations for `boto3.client("glue").delete_security_configuration` method.

[Client.delete_security_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.delete_security_configuration)

```python
def delete_security_configuration(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### delete_table

Type annotations for `boto3.client("glue").delete_table` method.

[Client.delete_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.delete_table)

```python
def delete_table(
    self,
    DatabaseName: str,
    Name: str,
    CatalogId: str = None
) -> Dict[str, Any]:
    pass
```

### delete_table_version

Type annotations for `boto3.client("glue").delete_table_version` method.

[Client.delete_table_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.delete_table_version)

```python
def delete_table_version(
    self,
    DatabaseName: str,
    TableName: str,
    VersionId: str,
    CatalogId: str = None
) -> Dict[str, Any]:
    pass
```

### delete_trigger

Type annotations for `boto3.client("glue").delete_trigger` method.

[Client.delete_trigger documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.delete_trigger)

```python
def delete_trigger(
    self,
    Name: str
) -> DeleteTriggerResponseTypeDef:
    pass
```

### delete_user_defined_function

Type annotations for `boto3.client("glue").delete_user_defined_function` method.

[Client.delete_user_defined_function documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.delete_user_defined_function)

```python
def delete_user_defined_function(
    self,
    DatabaseName: str,
    FunctionName: str,
    CatalogId: str = None
) -> Dict[str, Any]:
    pass
```

### delete_workflow

Type annotations for `boto3.client("glue").delete_workflow` method.

[Client.delete_workflow documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.delete_workflow)

```python
def delete_workflow(
    self,
    Name: str
) -> DeleteWorkflowResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("glue").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.generate_presigned_url)

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

### get_catalog_import_status

Type annotations for `boto3.client("glue").get_catalog_import_status` method.

[Client.get_catalog_import_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_catalog_import_status)

```python
def get_catalog_import_status(
    self,
    CatalogId: str = None
) -> GetCatalogImportStatusResponseTypeDef:
    pass
```

### get_classifier

Type annotations for `boto3.client("glue").get_classifier` method.

[Client.get_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_classifier)

```python
def get_classifier(
    self,
    Name: str
) -> GetClassifierResponseTypeDef:
    pass
```

### get_classifiers

Type annotations for `boto3.client("glue").get_classifiers` method.

[Client.get_classifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_classifiers)

```python
def get_classifiers(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> GetClassifiersResponseTypeDef:
    pass
```

### get_column_statistics_for_partition

Type annotations for `boto3.client("glue").get_column_statistics_for_partition` method.

[Client.get_column_statistics_for_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_column_statistics_for_partition)

```python
def get_column_statistics_for_partition(
    self,
    DatabaseName: str,
    TableName: str,
    PartitionValues: List[str],
    ColumnNames: List[str],
    CatalogId: str = None
) -> GetColumnStatisticsForPartitionResponseTypeDef:
    pass
```

### get_column_statistics_for_table

Type annotations for `boto3.client("glue").get_column_statistics_for_table` method.

[Client.get_column_statistics_for_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_column_statistics_for_table)

```python
def get_column_statistics_for_table(
    self,
    DatabaseName: str,
    TableName: str,
    ColumnNames: List[str],
    CatalogId: str = None
) -> GetColumnStatisticsForTableResponseTypeDef:
    pass
```

### get_connection

Type annotations for `boto3.client("glue").get_connection` method.

[Client.get_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_connection)

```python
def get_connection(
    self,
    Name: str,
    CatalogId: str = None,
    HidePassword: bool = None
) -> GetConnectionResponseTypeDef:
    pass
```

### get_connections

Type annotations for `boto3.client("glue").get_connections` method.

[Client.get_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_connections)

```python
def get_connections(
    self,
    CatalogId: str = None,
    Filter: GetConnectionsFilterTypeDef = None,
    HidePassword: bool = None,
    NextToken: str = None,
    MaxResults: int = None
) -> GetConnectionsResponseTypeDef:
    pass
```

### get_crawler

Type annotations for `boto3.client("glue").get_crawler` method.

[Client.get_crawler documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_crawler)

```python
def get_crawler(
    self,
    Name: str
) -> GetCrawlerResponseTypeDef:
    pass
```

### get_crawler_metrics

Type annotations for `boto3.client("glue").get_crawler_metrics` method.

[Client.get_crawler_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_crawler_metrics)

```python
def get_crawler_metrics(
    self,
    CrawlerNameList: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> GetCrawlerMetricsResponseTypeDef:
    pass
```

### get_crawlers

Type annotations for `boto3.client("glue").get_crawlers` method.

[Client.get_crawlers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_crawlers)

```python
def get_crawlers(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> GetCrawlersResponseTypeDef:
    pass
```

### get_data_catalog_encryption_settings

Type annotations for `boto3.client("glue").get_data_catalog_encryption_settings` method.

[Client.get_data_catalog_encryption_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_data_catalog_encryption_settings)

```python
def get_data_catalog_encryption_settings(
    self,
    CatalogId: str = None
) -> GetDataCatalogEncryptionSettingsResponseTypeDef:
    pass
```

### get_database

Type annotations for `boto3.client("glue").get_database` method.

[Client.get_database documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_database)

```python
def get_database(
    self,
    Name: str,
    CatalogId: str = None
) -> GetDatabaseResponseTypeDef:
    pass
```

### get_databases

Type annotations for `boto3.client("glue").get_databases` method.

[Client.get_databases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_databases)

```python
def get_databases(
    self,
    CatalogId: str = None,
    NextToken: str = None,
    MaxResults: int = None,
    ResourceShareType: ResourceShareType = None
) -> GetDatabasesResponseTypeDef:
    pass
```

### get_dataflow_graph

Type annotations for `boto3.client("glue").get_dataflow_graph` method.

[Client.get_dataflow_graph documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_dataflow_graph)

```python
def get_dataflow_graph(
    self,
    PythonScript: str = None
) -> GetDataflowGraphResponseTypeDef:
    pass
```

### get_dev_endpoint

Type annotations for `boto3.client("glue").get_dev_endpoint` method.

[Client.get_dev_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_dev_endpoint)

```python
def get_dev_endpoint(
    self,
    EndpointName: str
) -> GetDevEndpointResponseTypeDef:
    pass
```

### get_dev_endpoints

Type annotations for `boto3.client("glue").get_dev_endpoints` method.

[Client.get_dev_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_dev_endpoints)

```python
def get_dev_endpoints(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> GetDevEndpointsResponseTypeDef:
    pass
```

### get_job

Type annotations for `boto3.client("glue").get_job` method.

[Client.get_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_job)

```python
def get_job(
    self,
    JobName: str
) -> GetJobResponseTypeDef:
    pass
```

### get_job_bookmark

Type annotations for `boto3.client("glue").get_job_bookmark` method.

[Client.get_job_bookmark documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_job_bookmark)

```python
def get_job_bookmark(
    self,
    JobName: str,
    RunId: str = None
) -> GetJobBookmarkResponseTypeDef:
    pass
```

### get_job_run

Type annotations for `boto3.client("glue").get_job_run` method.

[Client.get_job_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_job_run)

```python
def get_job_run(
    self,
    JobName: str,
    RunId: str,
    PredecessorsIncluded: bool = None
) -> GetJobRunResponseTypeDef:
    pass
```

### get_job_runs

Type annotations for `boto3.client("glue").get_job_runs` method.

[Client.get_job_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_job_runs)

```python
def get_job_runs(
    self,
    JobName: str,
    NextToken: str = None,
    MaxResults: int = None
) -> GetJobRunsResponseTypeDef:
    pass
```

### get_jobs

Type annotations for `boto3.client("glue").get_jobs` method.

[Client.get_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_jobs)

```python
def get_jobs(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> GetJobsResponseTypeDef:
    pass
```

### get_mapping

Type annotations for `boto3.client("glue").get_mapping` method.

[Client.get_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_mapping)

```python
def get_mapping(
    self,
    Source: CatalogEntryTypeDef,
    Sinks: List[CatalogEntryTypeDef] = None,
    Location: LocationTypeDef = None
) -> GetMappingResponseTypeDef:
    pass
```

### get_ml_task_run

Type annotations for `boto3.client("glue").get_ml_task_run` method.

[Client.get_ml_task_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_ml_task_run)

```python
def get_ml_task_run(
    self,
    TransformId: str,
    TaskRunId: str
) -> GetMLTaskRunResponseTypeDef:
    pass
```

### get_ml_task_runs

Type annotations for `boto3.client("glue").get_ml_task_runs` method.

[Client.get_ml_task_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_ml_task_runs)

```python
def get_ml_task_runs(
    self,
    TransformId: str,
    NextToken: str = None,
    MaxResults: int = None,
    Filter: TaskRunFilterCriteriaTypeDef = None,
    Sort: TaskRunSortCriteriaTypeDef = None
) -> GetMLTaskRunsResponseTypeDef:
    pass
```

### get_ml_transform

Type annotations for `boto3.client("glue").get_ml_transform` method.

[Client.get_ml_transform documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_ml_transform)

```python
def get_ml_transform(
    self,
    TransformId: str
) -> GetMLTransformResponseTypeDef:
    pass
```

### get_ml_transforms

Type annotations for `boto3.client("glue").get_ml_transforms` method.

[Client.get_ml_transforms documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_ml_transforms)

```python
def get_ml_transforms(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    Filter: TransformFilterCriteriaTypeDef = None,
    Sort: TransformSortCriteriaTypeDef = None
) -> GetMLTransformsResponseTypeDef:
    pass
```

### get_partition

Type annotations for `boto3.client("glue").get_partition` method.

[Client.get_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_partition)

```python
def get_partition(
    self,
    DatabaseName: str,
    TableName: str,
    PartitionValues: List[str],
    CatalogId: str = None
) -> GetPartitionResponseTypeDef:
    pass
```

### get_partition_indexes

Type annotations for `boto3.client("glue").get_partition_indexes` method.

[Client.get_partition_indexes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_partition_indexes)

```python
def get_partition_indexes(
    self,
    DatabaseName: str,
    TableName: str,
    CatalogId: str = None,
    NextToken: str = None
) -> GetPartitionIndexesResponseTypeDef:
    pass
```

### get_partitions

Type annotations for `boto3.client("glue").get_partitions` method.

[Client.get_partitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_partitions)

```python
def get_partitions(
    self,
    DatabaseName: str,
    TableName: str,
    CatalogId: str = None,
    Expression: str = None,
    NextToken: str = None,
    Segment: SegmentTypeDef = None,
    MaxResults: int = None,
    ExcludeColumnSchema: bool = None
) -> GetPartitionsResponseTypeDef:
    pass
```

### get_plan

Type annotations for `boto3.client("glue").get_plan` method.

[Client.get_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_plan)

```python
def get_plan(
    self,
    Mapping: List["MappingEntryTypeDef"],
    Source: CatalogEntryTypeDef,
    Sinks: List[CatalogEntryTypeDef] = None,
    Location: LocationTypeDef = None,
    Language: Language = None,
    AdditionalPlanOptionsMap: Dict[str, str] = None
) -> GetPlanResponseTypeDef:
    pass
```

### get_registry

Type annotations for `boto3.client("glue").get_registry` method.

[Client.get_registry documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_registry)

```python
def get_registry(
    self,
    RegistryId: RegistryIdTypeDef
) -> GetRegistryResponseTypeDef:
    pass
```

### get_resource_policies

Type annotations for `boto3.client("glue").get_resource_policies` method.

[Client.get_resource_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_resource_policies)

```python
def get_resource_policies(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> GetResourcePoliciesResponseTypeDef:
    pass
```

### get_resource_policy

Type annotations for `boto3.client("glue").get_resource_policy` method.

[Client.get_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_resource_policy)

```python
def get_resource_policy(
    self,
    ResourceArn: str = None
) -> GetResourcePolicyResponseTypeDef:
    pass
```

### get_schema

Type annotations for `boto3.client("glue").get_schema` method.

[Client.get_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_schema)

```python
def get_schema(
    self,
    SchemaId: "SchemaIdTypeDef"
) -> GetSchemaResponseTypeDef:
    pass
```

### get_schema_by_definition

Type annotations for `boto3.client("glue").get_schema_by_definition` method.

[Client.get_schema_by_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_schema_by_definition)

```python
def get_schema_by_definition(
    self,
    SchemaId: "SchemaIdTypeDef",
    SchemaDefinition: str
) -> GetSchemaByDefinitionResponseTypeDef:
    pass
```

### get_schema_version

Type annotations for `boto3.client("glue").get_schema_version` method.

[Client.get_schema_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_schema_version)

```python
def get_schema_version(
    self,
    SchemaId: "SchemaIdTypeDef" = None,
    SchemaVersionId: str = None,
    SchemaVersionNumber: SchemaVersionNumberTypeDef = None
) -> GetSchemaVersionResponseTypeDef:
    pass
```

### get_schema_versions_diff

Type annotations for `boto3.client("glue").get_schema_versions_diff` method.

[Client.get_schema_versions_diff documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_schema_versions_diff)

```python
def get_schema_versions_diff(
    self,
    SchemaId: "SchemaIdTypeDef",
    FirstSchemaVersionNumber: SchemaVersionNumberTypeDef,
    SecondSchemaVersionNumber: SchemaVersionNumberTypeDef,
    SchemaDiffType: SchemaDiffType
) -> GetSchemaVersionsDiffResponseTypeDef:
    pass
```

### get_security_configuration

Type annotations for `boto3.client("glue").get_security_configuration` method.

[Client.get_security_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_security_configuration)

```python
def get_security_configuration(
    self,
    Name: str
) -> GetSecurityConfigurationResponseTypeDef:
    pass
```

### get_security_configurations

Type annotations for `boto3.client("glue").get_security_configurations` method.

[Client.get_security_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_security_configurations)

```python
def get_security_configurations(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> GetSecurityConfigurationsResponseTypeDef:
    pass
```

### get_table

Type annotations for `boto3.client("glue").get_table` method.

[Client.get_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_table)

```python
def get_table(
    self,
    DatabaseName: str,
    Name: str,
    CatalogId: str = None
) -> GetTableResponseTypeDef:
    pass
```

### get_table_version

Type annotations for `boto3.client("glue").get_table_version` method.

[Client.get_table_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_table_version)

```python
def get_table_version(
    self,
    DatabaseName: str,
    TableName: str,
    CatalogId: str = None,
    VersionId: str = None
) -> GetTableVersionResponseTypeDef:
    pass
```

### get_table_versions

Type annotations for `boto3.client("glue").get_table_versions` method.

[Client.get_table_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_table_versions)

```python
def get_table_versions(
    self,
    DatabaseName: str,
    TableName: str,
    CatalogId: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> GetTableVersionsResponseTypeDef:
    pass
```

### get_tables

Type annotations for `boto3.client("glue").get_tables` method.

[Client.get_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_tables)

```python
def get_tables(
    self,
    DatabaseName: str,
    CatalogId: str = None,
    Expression: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> GetTablesResponseTypeDef:
    pass
```

### get_tags

Type annotations for `boto3.client("glue").get_tags` method.

[Client.get_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_tags)

```python
def get_tags(
    self,
    ResourceArn: str
) -> GetTagsResponseTypeDef:
    pass
```

### get_trigger

Type annotations for `boto3.client("glue").get_trigger` method.

[Client.get_trigger documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_trigger)

```python
def get_trigger(
    self,
    Name: str
) -> GetTriggerResponseTypeDef:
    pass
```

### get_triggers

Type annotations for `boto3.client("glue").get_triggers` method.

[Client.get_triggers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_triggers)

```python
def get_triggers(
    self,
    NextToken: str = None,
    DependentJobName: str = None,
    MaxResults: int = None
) -> GetTriggersResponseTypeDef:
    pass
```

### get_user_defined_function

Type annotations for `boto3.client("glue").get_user_defined_function` method.

[Client.get_user_defined_function documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_user_defined_function)

```python
def get_user_defined_function(
    self,
    DatabaseName: str,
    FunctionName: str,
    CatalogId: str = None
) -> GetUserDefinedFunctionResponseTypeDef:
    pass
```

### get_user_defined_functions

Type annotations for `boto3.client("glue").get_user_defined_functions` method.

[Client.get_user_defined_functions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_user_defined_functions)

```python
def get_user_defined_functions(
    self,
    Pattern: str,
    CatalogId: str = None,
    DatabaseName: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> GetUserDefinedFunctionsResponseTypeDef:
    pass
```

### get_workflow

Type annotations for `boto3.client("glue").get_workflow` method.

[Client.get_workflow documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_workflow)

```python
def get_workflow(
    self,
    Name: str,
    IncludeGraph: bool = None
) -> GetWorkflowResponseTypeDef:
    pass
```

### get_workflow_run

Type annotations for `boto3.client("glue").get_workflow_run` method.

[Client.get_workflow_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_workflow_run)

```python
def get_workflow_run(
    self,
    Name: str,
    RunId: str,
    IncludeGraph: bool = None
) -> GetWorkflowRunResponseTypeDef:
    pass
```

### get_workflow_run_properties

Type annotations for `boto3.client("glue").get_workflow_run_properties` method.

[Client.get_workflow_run_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_workflow_run_properties)

```python
def get_workflow_run_properties(
    self,
    Name: str,
    RunId: str
) -> GetWorkflowRunPropertiesResponseTypeDef:
    pass
```

### get_workflow_runs

Type annotations for `boto3.client("glue").get_workflow_runs` method.

[Client.get_workflow_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.get_workflow_runs)

```python
def get_workflow_runs(
    self,
    Name: str,
    IncludeGraph: bool = None,
    NextToken: str = None,
    MaxResults: int = None
) -> GetWorkflowRunsResponseTypeDef:
    pass
```

### import_catalog_to_glue

Type annotations for `boto3.client("glue").import_catalog_to_glue` method.

[Client.import_catalog_to_glue documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.import_catalog_to_glue)

```python
def import_catalog_to_glue(
    self,
    CatalogId: str = None
) -> Dict[str, Any]:
    pass
```

### list_crawlers

Type annotations for `boto3.client("glue").list_crawlers` method.

[Client.list_crawlers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.list_crawlers)

```python
def list_crawlers(
    self,
    MaxResults: int = None,
    NextToken: str = None,
    Tags: Dict[str, str] = None
) -> ListCrawlersResponseTypeDef:
    pass
```

### list_dev_endpoints

Type annotations for `boto3.client("glue").list_dev_endpoints` method.

[Client.list_dev_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.list_dev_endpoints)

```python
def list_dev_endpoints(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    Tags: Dict[str, str] = None
) -> ListDevEndpointsResponseTypeDef:
    pass
```

### list_jobs

Type annotations for `boto3.client("glue").list_jobs` method.

[Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.list_jobs)

```python
def list_jobs(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    Tags: Dict[str, str] = None
) -> ListJobsResponseTypeDef:
    pass
```

### list_ml_transforms

Type annotations for `boto3.client("glue").list_ml_transforms` method.

[Client.list_ml_transforms documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.list_ml_transforms)

```python
def list_ml_transforms(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    Filter: TransformFilterCriteriaTypeDef = None,
    Sort: TransformSortCriteriaTypeDef = None,
    Tags: Dict[str, str] = None
) -> ListMLTransformsResponseTypeDef:
    pass
```

### list_registries

Type annotations for `boto3.client("glue").list_registries` method.

[Client.list_registries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.list_registries)

```python
def list_registries(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListRegistriesResponseTypeDef:
    pass
```

### list_schema_versions

Type annotations for `boto3.client("glue").list_schema_versions` method.

[Client.list_schema_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.list_schema_versions)

```python
def list_schema_versions(
    self,
    SchemaId: "SchemaIdTypeDef",
    MaxResults: int = None,
    NextToken: str = None
) -> ListSchemaVersionsResponseTypeDef:
    pass
```

### list_schemas

Type annotations for `boto3.client("glue").list_schemas` method.

[Client.list_schemas documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.list_schemas)

```python
def list_schemas(
    self,
    RegistryId: RegistryIdTypeDef = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListSchemasResponseTypeDef:
    pass
```

### list_triggers

Type annotations for `boto3.client("glue").list_triggers` method.

[Client.list_triggers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.list_triggers)

```python
def list_triggers(
    self,
    NextToken: str = None,
    DependentJobName: str = None,
    MaxResults: int = None,
    Tags: Dict[str, str] = None
) -> ListTriggersResponseTypeDef:
    pass
```

### list_workflows

Type annotations for `boto3.client("glue").list_workflows` method.

[Client.list_workflows documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.list_workflows)

```python
def list_workflows(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListWorkflowsResponseTypeDef:
    pass
```

### put_data_catalog_encryption_settings

Type annotations for `boto3.client("glue").put_data_catalog_encryption_settings` method.

[Client.put_data_catalog_encryption_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.put_data_catalog_encryption_settings)

```python
def put_data_catalog_encryption_settings(
    self,
    DataCatalogEncryptionSettings: "DataCatalogEncryptionSettingsTypeDef",
    CatalogId: str = None
) -> Dict[str, Any]:
    pass
```

### put_resource_policy

Type annotations for `boto3.client("glue").put_resource_policy` method.

[Client.put_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.put_resource_policy)

```python
def put_resource_policy(
    self,
    PolicyInJson: str,
    ResourceArn: str = None,
    PolicyHashCondition: str = None,
    PolicyExistsCondition: ExistCondition = None,
    EnableHybrid: EnableHybridValues = None
) -> PutResourcePolicyResponseTypeDef:
    pass
```

### put_schema_version_metadata

Type annotations for `boto3.client("glue").put_schema_version_metadata` method.

[Client.put_schema_version_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.put_schema_version_metadata)

```python
def put_schema_version_metadata(
    self,
    MetadataKeyValue: MetadataKeyValuePairTypeDef,
    SchemaId: "SchemaIdTypeDef" = None,
    SchemaVersionNumber: SchemaVersionNumberTypeDef = None,
    SchemaVersionId: str = None
) -> PutSchemaVersionMetadataResponseTypeDef:
    pass
```

### put_workflow_run_properties

Type annotations for `boto3.client("glue").put_workflow_run_properties` method.

[Client.put_workflow_run_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.put_workflow_run_properties)

```python
def put_workflow_run_properties(
    self,
    Name: str,
    RunId: str,
    RunProperties: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### query_schema_version_metadata

Type annotations for `boto3.client("glue").query_schema_version_metadata` method.

[Client.query_schema_version_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.query_schema_version_metadata)

```python
def query_schema_version_metadata(
    self,
    SchemaId: "SchemaIdTypeDef" = None,
    SchemaVersionNumber: SchemaVersionNumberTypeDef = None,
    SchemaVersionId: str = None,
    MetadataList: List[MetadataKeyValuePairTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> QuerySchemaVersionMetadataResponseTypeDef:
    pass
```

### register_schema_version

Type annotations for `boto3.client("glue").register_schema_version` method.

[Client.register_schema_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.register_schema_version)

```python
def register_schema_version(
    self,
    SchemaId: "SchemaIdTypeDef",
    SchemaDefinition: str
) -> RegisterSchemaVersionResponseTypeDef:
    pass
```

### remove_schema_version_metadata

Type annotations for `boto3.client("glue").remove_schema_version_metadata` method.

[Client.remove_schema_version_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.remove_schema_version_metadata)

```python
def remove_schema_version_metadata(
    self,
    MetadataKeyValue: MetadataKeyValuePairTypeDef,
    SchemaId: "SchemaIdTypeDef" = None,
    SchemaVersionNumber: SchemaVersionNumberTypeDef = None,
    SchemaVersionId: str = None
) -> RemoveSchemaVersionMetadataResponseTypeDef:
    pass
```

### reset_job_bookmark

Type annotations for `boto3.client("glue").reset_job_bookmark` method.

[Client.reset_job_bookmark documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.reset_job_bookmark)

```python
def reset_job_bookmark(
    self,
    JobName: str,
    RunId: str = None
) -> ResetJobBookmarkResponseTypeDef:
    pass
```

### resume_workflow_run

Type annotations for `boto3.client("glue").resume_workflow_run` method.

[Client.resume_workflow_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.resume_workflow_run)

```python
def resume_workflow_run(
    self,
    Name: str,
    RunId: str,
    NodeIds: List[str]
) -> ResumeWorkflowRunResponseTypeDef:
    pass
```

### search_tables

Type annotations for `boto3.client("glue").search_tables` method.

[Client.search_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.search_tables)

```python
def search_tables(
    self,
    CatalogId: str = None,
    NextToken: str = None,
    Filters: List[PropertyPredicateTypeDef] = None,
    SearchText: str = None,
    SortCriteria: List[SortCriterionTypeDef] = None,
    MaxResults: int = None,
    ResourceShareType: ResourceShareType = None
) -> SearchTablesResponseTypeDef:
    pass
```

### start_crawler

Type annotations for `boto3.client("glue").start_crawler` method.

[Client.start_crawler documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.start_crawler)

```python
def start_crawler(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### start_crawler_schedule

Type annotations for `boto3.client("glue").start_crawler_schedule` method.

[Client.start_crawler_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.start_crawler_schedule)

```python
def start_crawler_schedule(
    self,
    CrawlerName: str
) -> Dict[str, Any]:
    pass
```

### start_export_labels_task_run

Type annotations for `boto3.client("glue").start_export_labels_task_run` method.

[Client.start_export_labels_task_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.start_export_labels_task_run)

```python
def start_export_labels_task_run(
    self,
    TransformId: str,
    OutputS3Path: str
) -> StartExportLabelsTaskRunResponseTypeDef:
    pass
```

### start_import_labels_task_run

Type annotations for `boto3.client("glue").start_import_labels_task_run` method.

[Client.start_import_labels_task_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.start_import_labels_task_run)

```python
def start_import_labels_task_run(
    self,
    TransformId: str,
    InputS3Path: str,
    ReplaceAllLabels: bool = None
) -> StartImportLabelsTaskRunResponseTypeDef:
    pass
```

### start_job_run

Type annotations for `boto3.client("glue").start_job_run` method.

[Client.start_job_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.start_job_run)

```python
def start_job_run(
    self,
    JobName: str,
    JobRunId: str = None,
    Arguments: Dict[str, str] = None,
    AllocatedCapacity: int = None,
    Timeout: int = None,
    MaxCapacity: float = None,
    SecurityConfiguration: str = None,
    NotificationProperty: "NotificationPropertyTypeDef" = None,
    WorkerType: WorkerType = None,
    NumberOfWorkers: int = None
) -> StartJobRunResponseTypeDef:
    pass
```

### start_ml_evaluation_task_run

Type annotations for `boto3.client("glue").start_ml_evaluation_task_run` method.

[Client.start_ml_evaluation_task_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.start_ml_evaluation_task_run)

```python
def start_ml_evaluation_task_run(
    self,
    TransformId: str
) -> StartMLEvaluationTaskRunResponseTypeDef:
    pass
```

### start_ml_labeling_set_generation_task_run

Type annotations for `boto3.client("glue").start_ml_labeling_set_generation_task_run` method.

[Client.start_ml_labeling_set_generation_task_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.start_ml_labeling_set_generation_task_run)

```python
def start_ml_labeling_set_generation_task_run(
    self,
    TransformId: str,
    OutputS3Path: str
) -> StartMLLabelingSetGenerationTaskRunResponseTypeDef:
    pass
```

### start_trigger

Type annotations for `boto3.client("glue").start_trigger` method.

[Client.start_trigger documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.start_trigger)

```python
def start_trigger(
    self,
    Name: str
) -> StartTriggerResponseTypeDef:
    pass
```

### start_workflow_run

Type annotations for `boto3.client("glue").start_workflow_run` method.

[Client.start_workflow_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.start_workflow_run)

```python
def start_workflow_run(
    self,
    Name: str
) -> StartWorkflowRunResponseTypeDef:
    pass
```

### stop_crawler

Type annotations for `boto3.client("glue").stop_crawler` method.

[Client.stop_crawler documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.stop_crawler)

```python
def stop_crawler(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### stop_crawler_schedule

Type annotations for `boto3.client("glue").stop_crawler_schedule` method.

[Client.stop_crawler_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.stop_crawler_schedule)

```python
def stop_crawler_schedule(
    self,
    CrawlerName: str
) -> Dict[str, Any]:
    pass
```

### stop_trigger

Type annotations for `boto3.client("glue").stop_trigger` method.

[Client.stop_trigger documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.stop_trigger)

```python
def stop_trigger(
    self,
    Name: str
) -> StopTriggerResponseTypeDef:
    pass
```

### stop_workflow_run

Type annotations for `boto3.client("glue").stop_workflow_run` method.

[Client.stop_workflow_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.stop_workflow_run)

```python
def stop_workflow_run(
    self,
    Name: str,
    RunId: str
) -> Dict[str, Any]:
    pass
```

### tag_resource

Type annotations for `boto3.client("glue").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    TagsToAdd: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("glue").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagsToRemove: List[str]
) -> Dict[str, Any]:
    pass
```

### update_classifier

Type annotations for `boto3.client("glue").update_classifier` method.

[Client.update_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.update_classifier)

```python
def update_classifier(
    self,
    GrokClassifier: UpdateGrokClassifierRequestTypeDef = None,
    XMLClassifier: UpdateXMLClassifierRequestTypeDef = None,
    JsonClassifier: UpdateJsonClassifierRequestTypeDef = None,
    CsvClassifier: UpdateCsvClassifierRequestTypeDef = None
) -> Dict[str, Any]:
    pass
```

### update_column_statistics_for_partition

Type annotations for `boto3.client("glue").update_column_statistics_for_partition` method.

[Client.update_column_statistics_for_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.update_column_statistics_for_partition)

```python
def update_column_statistics_for_partition(
    self,
    DatabaseName: str,
    TableName: str,
    PartitionValues: List[str],
    ColumnStatisticsList: List["ColumnStatisticsTypeDef"],
    CatalogId: str = None
) -> UpdateColumnStatisticsForPartitionResponseTypeDef:
    pass
```

### update_column_statistics_for_table

Type annotations for `boto3.client("glue").update_column_statistics_for_table` method.

[Client.update_column_statistics_for_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.update_column_statistics_for_table)

```python
def update_column_statistics_for_table(
    self,
    DatabaseName: str,
    TableName: str,
    ColumnStatisticsList: List["ColumnStatisticsTypeDef"],
    CatalogId: str = None
) -> UpdateColumnStatisticsForTableResponseTypeDef:
    pass
```

### update_connection

Type annotations for `boto3.client("glue").update_connection` method.

[Client.update_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.update_connection)

```python
def update_connection(
    self,
    Name: str,
    ConnectionInput: ConnectionInputTypeDef,
    CatalogId: str = None
) -> Dict[str, Any]:
    pass
```

### update_crawler

Type annotations for `boto3.client("glue").update_crawler` method.

[Client.update_crawler documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.update_crawler)

```python
def update_crawler(
    self,
    Name: str,
    Role: str = None,
    DatabaseName: str = None,
    Description: str = None,
    Targets: "CrawlerTargetsTypeDef" = None,
    Schedule: str = None,
    Classifiers: List[str] = None,
    TablePrefix: str = None,
    SchemaChangePolicy: "SchemaChangePolicyTypeDef" = None,
    RecrawlPolicy: "RecrawlPolicyTypeDef" = None,
    LineageConfiguration: "LineageConfigurationTypeDef" = None,
    Configuration: str = None,
    CrawlerSecurityConfiguration: str = None
) -> Dict[str, Any]:
    pass
```

### update_crawler_schedule

Type annotations for `boto3.client("glue").update_crawler_schedule` method.

[Client.update_crawler_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.update_crawler_schedule)

```python
def update_crawler_schedule(
    self,
    CrawlerName: str,
    Schedule: str = None
) -> Dict[str, Any]:
    pass
```

### update_database

Type annotations for `boto3.client("glue").update_database` method.

[Client.update_database documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.update_database)

```python
def update_database(
    self,
    Name: str,
    DatabaseInput: DatabaseInputTypeDef,
    CatalogId: str = None
) -> Dict[str, Any]:
    pass
```

### update_dev_endpoint

Type annotations for `boto3.client("glue").update_dev_endpoint` method.

[Client.update_dev_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.update_dev_endpoint)

```python
def update_dev_endpoint(
    self,
    EndpointName: str,
    PublicKey: str = None,
    AddPublicKeys: List[str] = None,
    DeletePublicKeys: List[str] = None,
    CustomLibraries: DevEndpointCustomLibrariesTypeDef = None,
    UpdateEtlLibraries: bool = None,
    DeleteArguments: List[str] = None,
    AddArguments: Dict[str, str] = None
) -> Dict[str, Any]:
    pass
```

### update_job

Type annotations for `boto3.client("glue").update_job` method.

[Client.update_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.update_job)

```python
def update_job(
    self,
    JobName: str,
    JobUpdate: JobUpdateTypeDef
) -> UpdateJobResponseTypeDef:
    pass
```

### update_ml_transform

Type annotations for `boto3.client("glue").update_ml_transform` method.

[Client.update_ml_transform documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.update_ml_transform)

```python
def update_ml_transform(
    self,
    TransformId: str,
    Name: str = None,
    Description: str = None,
    Parameters: "TransformParametersTypeDef" = None,
    Role: str = None,
    GlueVersion: str = None,
    MaxCapacity: float = None,
    WorkerType: WorkerType = None,
    NumberOfWorkers: int = None,
    Timeout: int = None,
    MaxRetries: int = None
) -> UpdateMLTransformResponseTypeDef:
    pass
```

### update_partition

Type annotations for `boto3.client("glue").update_partition` method.

[Client.update_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.update_partition)

```python
def update_partition(
    self,
    DatabaseName: str,
    TableName: str,
    PartitionValueList: List[str],
    PartitionInput: "PartitionInputTypeDef",
    CatalogId: str = None
) -> Dict[str, Any]:
    pass
```

### update_registry

Type annotations for `boto3.client("glue").update_registry` method.

[Client.update_registry documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.update_registry)

```python
def update_registry(
    self,
    RegistryId: RegistryIdTypeDef,
    Description: str
) -> UpdateRegistryResponseTypeDef:
    pass
```

### update_schema

Type annotations for `boto3.client("glue").update_schema` method.

[Client.update_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.update_schema)

```python
def update_schema(
    self,
    SchemaId: "SchemaIdTypeDef",
    SchemaVersionNumber: SchemaVersionNumberTypeDef = None,
    Compatibility: Compatibility = None,
    Description: str = None
) -> UpdateSchemaResponseTypeDef:
    pass
```

### update_table

Type annotations for `boto3.client("glue").update_table` method.

[Client.update_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.update_table)

```python
def update_table(
    self,
    DatabaseName: str,
    TableInput: TableInputTypeDef,
    CatalogId: str = None,
    SkipArchive: bool = None
) -> Dict[str, Any]:
    pass
```

### update_trigger

Type annotations for `boto3.client("glue").update_trigger` method.

[Client.update_trigger documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.update_trigger)

```python
def update_trigger(
    self,
    Name: str,
    TriggerUpdate: TriggerUpdateTypeDef
) -> UpdateTriggerResponseTypeDef:
    pass
```

### update_user_defined_function

Type annotations for `boto3.client("glue").update_user_defined_function` method.

[Client.update_user_defined_function documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.update_user_defined_function)

```python
def update_user_defined_function(
    self,
    DatabaseName: str,
    FunctionName: str,
    FunctionInput: UserDefinedFunctionInputTypeDef,
    CatalogId: str = None
) -> Dict[str, Any]:
    pass
```

### update_workflow

Type annotations for `boto3.client("glue").update_workflow` method.

[Client.update_workflow documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.update_workflow)

```python
def update_workflow(
    self,
    Name: str,
    Description: str = None,
    DefaultRunProperties: Dict[str, str] = None,
    MaxConcurrentRuns: int = None
) -> UpdateWorkflowResponseTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("glue").get_paginator` method.

[Paginator.GetClassifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetClassifiers)

```python
@overload
def get_paginator(
    self,
    operation_name: GetClassifiersPaginatorName
) -> GetClassifiersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("glue").get_paginator` method.

[Paginator.GetConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetConnections)

```python
@overload
def get_paginator(
    self,
    operation_name: GetConnectionsPaginatorName
) -> GetConnectionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("glue").get_paginator` method.

[Paginator.GetCrawlerMetrics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetCrawlerMetrics)

```python
@overload
def get_paginator(
    self,
    operation_name: GetCrawlerMetricsPaginatorName
) -> GetCrawlerMetricsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("glue").get_paginator` method.

[Paginator.GetCrawlers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetCrawlers)

```python
@overload
def get_paginator(
    self,
    operation_name: GetCrawlersPaginatorName
) -> GetCrawlersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("glue").get_paginator` method.

[Paginator.GetDatabases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetDatabases)

```python
@overload
def get_paginator(
    self,
    operation_name: GetDatabasesPaginatorName
) -> GetDatabasesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("glue").get_paginator` method.

[Paginator.GetDevEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetDevEndpoints)

```python
@overload
def get_paginator(
    self,
    operation_name: GetDevEndpointsPaginatorName
) -> GetDevEndpointsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("glue").get_paginator` method.

[Paginator.GetJobRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetJobRuns)

```python
@overload
def get_paginator(
    self,
    operation_name: GetJobRunsPaginatorName
) -> GetJobRunsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("glue").get_paginator` method.

[Paginator.GetJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetJobs)

```python
@overload
def get_paginator(
    self,
    operation_name: GetJobsPaginatorName
) -> GetJobsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("glue").get_paginator` method.

[Paginator.GetPartitionIndexes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetPartitionIndexes)

```python
@overload
def get_paginator(
    self,
    operation_name: GetPartitionIndexesPaginatorName
) -> GetPartitionIndexesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("glue").get_paginator` method.

[Paginator.GetPartitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetPartitions)

```python
@overload
def get_paginator(
    self,
    operation_name: GetPartitionsPaginatorName
) -> GetPartitionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("glue").get_paginator` method.

[Paginator.GetResourcePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetResourcePolicies)

```python
@overload
def get_paginator(
    self,
    operation_name: GetResourcePoliciesPaginatorName
) -> GetResourcePoliciesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("glue").get_paginator` method.

[Paginator.GetSecurityConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetSecurityConfigurations)

```python
@overload
def get_paginator(
    self,
    operation_name: GetSecurityConfigurationsPaginatorName
) -> GetSecurityConfigurationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("glue").get_paginator` method.

[Paginator.GetTableVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetTableVersions)

```python
@overload
def get_paginator(
    self,
    operation_name: GetTableVersionsPaginatorName
) -> GetTableVersionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("glue").get_paginator` method.

[Paginator.GetTables documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetTables)

```python
@overload
def get_paginator(
    self,
    operation_name: GetTablesPaginatorName
) -> GetTablesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("glue").get_paginator` method.

[Paginator.GetTriggers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetTriggers)

```python
@overload
def get_paginator(
    self,
    operation_name: GetTriggersPaginatorName
) -> GetTriggersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("glue").get_paginator` method.

[Paginator.GetUserDefinedFunctions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetUserDefinedFunctions)

```python
@overload
def get_paginator(
    self,
    operation_name: GetUserDefinedFunctionsPaginatorName
) -> GetUserDefinedFunctionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("glue").get_paginator` method.

[Paginator.ListRegistries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.ListRegistries)

```python
@overload
def get_paginator(
    self,
    operation_name: ListRegistriesPaginatorName
) -> ListRegistriesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("glue").get_paginator` method.

[Paginator.ListSchemaVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.ListSchemaVersions)

```python
@overload
def get_paginator(
    self,
    operation_name: ListSchemaVersionsPaginatorName
) -> ListSchemaVersionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("glue").get_paginator` method.

[Paginator.ListSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.ListSchemas)

```python
@overload
def get_paginator(
    self,
    operation_name: ListSchemasPaginatorName
) -> ListSchemasPaginator:
    pass
```