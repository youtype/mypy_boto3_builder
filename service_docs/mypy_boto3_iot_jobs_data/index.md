# Type annotations for boto3 IoTJobsDataPlane module

> [Index](../index.md) > IoTJobsDataPlane

Auto-generated documentation for [IoTJobsDataPlane](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-jobs-data.html#IoTJobsDataPlane)
type annotations stubs module [mypy_boto3_iot_jobs_data](https://pypi.org/project/mypy-boto3-iot-jobs-data/).

```bash
pip install mypy-boto3-iot-jobs-data
```

- [Type annotations for boto3 IoTJobsDataPlane module](#type-annotations-for-boto3-iotjobsdataplane-module)
  - [IoTJobsDataPlaneClient](#iotjobsdataplaneclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## IoTJobsDataPlaneClient

Type annotations for  `boto3.client("iot-jobs-data")` as [IoTJobsDataPlaneClient](./client.md)

Can be used directly:

```python
from mypy_boto3_iot_jobs_data.client import IoTJobsDataPlaneClient
```


IoTJobsDataPlaneClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [describe_job_execution](./client.md#describe-job-execution)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_pending_job_executions](./client.md#get-pending-job-executions)
- [start_next_pending_job_execution](./client.md#start-next-pending-job-execution)
- [update_job_execution](./client.md#update-job-execution)




### Exceptions
- [CertificateValidationException](./client.md#certificatevalidationexception)
- [ClientError](./client.md#clienterror)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [InvalidStateTransitionException](./client.md#invalidstatetransitionexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)
- [TerminalStateException](./client.md#terminalstateexception)
- [ThrottlingException](./client.md#throttlingexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_iot_jobs_data.literals import JobExecutionStatus, ...
```

- [JobExecutionStatus](./literals.md#jobexecutionstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_iot_jobs_data.type_defs import JobExecutionStateTypeDef, ...
```

- [JobExecutionStateTypeDef](./type_defs.md#jobexecutionstatetypedef)
- [JobExecutionSummaryTypeDef](./type_defs.md#jobexecutionsummarytypedef)
- [JobExecutionTypeDef](./type_defs.md#jobexecutiontypedef)
- [DescribeJobExecutionResponseTypeDef](./type_defs.md#describejobexecutionresponsetypedef)
- [GetPendingJobExecutionsResponseTypeDef](./type_defs.md#getpendingjobexecutionsresponsetypedef)
- [StartNextPendingJobExecutionResponseTypeDef](./type_defs.md#startnextpendingjobexecutionresponsetypedef)
- [UpdateJobExecutionResponseTypeDef](./type_defs.md#updatejobexecutionresponsetypedef)
