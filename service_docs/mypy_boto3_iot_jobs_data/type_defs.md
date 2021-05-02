# Structures for boto3 IoTJobsDataPlane module

> [Index](../index.md) > [IoTJobsDataPlane](./index.md) > Structures

Auto-generated documentation for [IoTJobsDataPlane](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-jobs-data.html#IoTJobsDataPlane)
type annotations stubs module [mypy_boto3_iot_jobs_data](https://pypi.org/project/mypy-boto3-iot-jobs-data/).

- [Structures for boto3 IoTJobsDataPlane module](#structures-for-boto3-iotjobsdataplane-module)
  - [DescribeJobExecutionResponseTypeDef](#describejobexecutionresponsetypedef)
  - [GetPendingJobExecutionsResponseTypeDef](#getpendingjobexecutionsresponsetypedef)
  - [JobExecutionStateTypeDef](#jobexecutionstatetypedef)
  - [JobExecutionSummaryTypeDef](#jobexecutionsummarytypedef)
  - [JobExecutionTypeDef](#jobexecutiontypedef)
  - [StartNextPendingJobExecutionResponseTypeDef](#startnextpendingjobexecutionresponsetypedef)
  - [UpdateJobExecutionResponseTypeDef](#updatejobexecutionresponsetypedef)

## DescribeJobExecutionResponseTypeDef

```python
from mypy_boto3_iot_jobs_data.type_defs import DescribeJobExecutionResponseTypeDef
```




Optional fields:
- `execution`: `"JobExecutionTypeDef"`


## GetPendingJobExecutionsResponseTypeDef

```python
from mypy_boto3_iot_jobs_data.type_defs import GetPendingJobExecutionsResponseTypeDef
```




Optional fields:
- `inProgressJobs`: `List["JobExecutionSummaryTypeDef"]`
- `queuedJobs`: `List["JobExecutionSummaryTypeDef"]`


## JobExecutionStateTypeDef

```python
from mypy_boto3_iot_jobs_data.type_defs import JobExecutionStateTypeDef
```




Optional fields:
- `status`: `JobExecutionStatus`
- `statusDetails`: `Dict[str, str]`
- `versionNumber`: `int`


## JobExecutionSummaryTypeDef

```python
from mypy_boto3_iot_jobs_data.type_defs import JobExecutionSummaryTypeDef
```




Optional fields:
- `jobId`: `str`
- `queuedAt`: `int`
- `startedAt`: `int`
- `lastUpdatedAt`: `int`
- `versionNumber`: `int`
- `executionNumber`: `int`


## JobExecutionTypeDef

```python
from mypy_boto3_iot_jobs_data.type_defs import JobExecutionTypeDef
```




Optional fields:
- `jobId`: `str`
- `thingName`: `str`
- `status`: `JobExecutionStatus`
- `statusDetails`: `Dict[str, str]`
- `queuedAt`: `int`
- `startedAt`: `int`
- `lastUpdatedAt`: `int`
- `approximateSecondsBeforeTimedOut`: `int`
- `versionNumber`: `int`
- `executionNumber`: `int`
- `jobDocument`: `str`


## StartNextPendingJobExecutionResponseTypeDef

```python
from mypy_boto3_iot_jobs_data.type_defs import StartNextPendingJobExecutionResponseTypeDef
```




Optional fields:
- `execution`: `"JobExecutionTypeDef"`


## UpdateJobExecutionResponseTypeDef

```python
from mypy_boto3_iot_jobs_data.type_defs import UpdateJobExecutionResponseTypeDef
```




Optional fields:
- `executionState`: `"JobExecutionStateTypeDef"`
- `jobDocument`: `str`

