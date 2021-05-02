# LookoutMetricsClient for boto3 LookoutMetrics module

> [Index](../index.md) > [LookoutMetrics](./index.md) > LookoutMetricsClient

Auto-generated documentation for [LookoutMetrics](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics)
type annotations stubs module [mypy_boto3_lookoutmetrics](https://pypi.org/project/mypy-boto3-lookoutmetrics/).

- [LookoutMetricsClient for boto3 LookoutMetrics module](#lookoutmetricsclient-for-boto3-lookoutmetrics-module)
  - [LookoutMetricsClient](#lookoutmetricsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [activate_anomaly_detector](#activate_anomaly_detector)
    - [back_test_anomaly_detector](#back_test_anomaly_detector)
    - [can_paginate](#can_paginate)
    - [create_alert](#create_alert)
    - [create_anomaly_detector](#create_anomaly_detector)
    - [create_metric_set](#create_metric_set)
    - [delete_alert](#delete_alert)
    - [delete_anomaly_detector](#delete_anomaly_detector)
    - [describe_alert](#describe_alert)
    - [describe_anomaly_detection_executions](#describe_anomaly_detection_executions)
    - [describe_anomaly_detector](#describe_anomaly_detector)
    - [describe_metric_set](#describe_metric_set)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_anomaly_group](#get_anomaly_group)
    - [get_feedback](#get_feedback)
    - [get_sample_data](#get_sample_data)
    - [list_alerts](#list_alerts)
    - [list_anomaly_detectors](#list_anomaly_detectors)
    - [list_anomaly_group_summaries](#list_anomaly_group_summaries)
    - [list_anomaly_group_time_series](#list_anomaly_group_time_series)
    - [list_metric_sets](#list_metric_sets)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [put_feedback](#put_feedback)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_anomaly_detector](#update_anomaly_detector)
    - [update_metric_set](#update_metric_set)

## LookoutMetricsClient

Type annotations for `boto3.client("lookoutmetrics")`

Can be used directly:

```python
from mypy_boto3_lookoutmetrics.client import LookoutMetricsClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_lookoutmetrics.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.TooManyRequestsException`
- `Exceptions.ValidationException`


## Methods


### activate_anomaly_detector

Type annotations for `boto3.client("lookoutmetrics").activate_anomaly_detector` method.

[Client.activate_anomaly_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics.Client.activate_anomaly_detector)

```python
def activate_anomaly_detector(
    self,
    AnomalyDetectorArn: str
) -> Dict[str, Any]:
    pass
```

### back_test_anomaly_detector

Type annotations for `boto3.client("lookoutmetrics").back_test_anomaly_detector` method.

[Client.back_test_anomaly_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics.Client.back_test_anomaly_detector)

```python
def back_test_anomaly_detector(
    self,
    AnomalyDetectorArn: str
) -> Dict[str, Any]:
    pass
```

### can_paginate

Type annotations for `boto3.client("lookoutmetrics").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_alert

Type annotations for `boto3.client("lookoutmetrics").create_alert` method.

[Client.create_alert documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics.Client.create_alert)

```python
def create_alert(
    self,
    AlertName: str,
    AlertSensitivityThreshold: int,
    AnomalyDetectorArn: str,
    Action: "ActionTypeDef",
    AlertDescription: str = None,
    Tags: Dict[str, str] = None
) -> CreateAlertResponseTypeDef:
    pass
```

### create_anomaly_detector

Type annotations for `boto3.client("lookoutmetrics").create_anomaly_detector` method.

[Client.create_anomaly_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics.Client.create_anomaly_detector)

```python
def create_anomaly_detector(
    self,
    AnomalyDetectorName: str,
    AnomalyDetectorConfig: AnomalyDetectorConfigTypeDef,
    AnomalyDetectorDescription: str = None,
    KmsKeyArn: str = None,
    Tags: Dict[str, str] = None
) -> CreateAnomalyDetectorResponseTypeDef:
    pass
```

### create_metric_set

Type annotations for `boto3.client("lookoutmetrics").create_metric_set` method.

[Client.create_metric_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics.Client.create_metric_set)

```python
def create_metric_set(
    self,
    AnomalyDetectorArn: str,
    MetricSetName: str,
    MetricList: List["MetricTypeDef"],
    MetricSource: "MetricSourceTypeDef",
    MetricSetDescription: str = None,
    Offset: int = None,
    TimestampColumn: "TimestampColumnTypeDef" = None,
    DimensionList: List[str] = None,
    MetricSetFrequency: Frequency = None,
    Timezone: str = None,
    Tags: Dict[str, str] = None
) -> CreateMetricSetResponseTypeDef:
    pass
```

### delete_alert

Type annotations for `boto3.client("lookoutmetrics").delete_alert` method.

[Client.delete_alert documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics.Client.delete_alert)

```python
def delete_alert(
    self,
    AlertArn: str
) -> Dict[str, Any]:
    pass
```

### delete_anomaly_detector

Type annotations for `boto3.client("lookoutmetrics").delete_anomaly_detector` method.

[Client.delete_anomaly_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics.Client.delete_anomaly_detector)

```python
def delete_anomaly_detector(
    self,
    AnomalyDetectorArn: str
) -> Dict[str, Any]:
    pass
```

### describe_alert

Type annotations for `boto3.client("lookoutmetrics").describe_alert` method.

[Client.describe_alert documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics.Client.describe_alert)

```python
def describe_alert(
    self,
    AlertArn: str
) -> DescribeAlertResponseTypeDef:
    pass
```

### describe_anomaly_detection_executions

Type annotations for `boto3.client("lookoutmetrics").describe_anomaly_detection_executions` method.

[Client.describe_anomaly_detection_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics.Client.describe_anomaly_detection_executions)

```python
def describe_anomaly_detection_executions(
    self,
    AnomalyDetectorArn: str,
    Timestamp: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeAnomalyDetectionExecutionsResponseTypeDef:
    pass
```

### describe_anomaly_detector

Type annotations for `boto3.client("lookoutmetrics").describe_anomaly_detector` method.

[Client.describe_anomaly_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics.Client.describe_anomaly_detector)

```python
def describe_anomaly_detector(
    self,
    AnomalyDetectorArn: str
) -> DescribeAnomalyDetectorResponseTypeDef:
    pass
```

### describe_metric_set

Type annotations for `boto3.client("lookoutmetrics").describe_metric_set` method.

[Client.describe_metric_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics.Client.describe_metric_set)

```python
def describe_metric_set(
    self,
    MetricSetArn: str
) -> DescribeMetricSetResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("lookoutmetrics").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics.Client.generate_presigned_url)

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

### get_anomaly_group

Type annotations for `boto3.client("lookoutmetrics").get_anomaly_group` method.

[Client.get_anomaly_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics.Client.get_anomaly_group)

```python
def get_anomaly_group(
    self,
    AnomalyGroupId: str,
    AnomalyDetectorArn: str
) -> GetAnomalyGroupResponseTypeDef:
    pass
```

### get_feedback

Type annotations for `boto3.client("lookoutmetrics").get_feedback` method.

[Client.get_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics.Client.get_feedback)

```python
def get_feedback(
    self,
    AnomalyDetectorArn: str,
    AnomalyGroupTimeSeriesFeedback: AnomalyGroupTimeSeriesTypeDef,
    MaxResults: int = None,
    NextToken: str = None
) -> GetFeedbackResponseTypeDef:
    pass
```

### get_sample_data

Type annotations for `boto3.client("lookoutmetrics").get_sample_data` method.

[Client.get_sample_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics.Client.get_sample_data)

```python
def get_sample_data(
    self,
    S3SourceConfig: SampleDataS3SourceConfigTypeDef = None
) -> GetSampleDataResponseTypeDef:
    pass
```

### list_alerts

Type annotations for `boto3.client("lookoutmetrics").list_alerts` method.

[Client.list_alerts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics.Client.list_alerts)

```python
def list_alerts(
    self,
    AnomalyDetectorArn: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListAlertsResponseTypeDef:
    pass
```

### list_anomaly_detectors

Type annotations for `boto3.client("lookoutmetrics").list_anomaly_detectors` method.

[Client.list_anomaly_detectors documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics.Client.list_anomaly_detectors)

```python
def list_anomaly_detectors(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListAnomalyDetectorsResponseTypeDef:
    pass
```

### list_anomaly_group_summaries

Type annotations for `boto3.client("lookoutmetrics").list_anomaly_group_summaries` method.

[Client.list_anomaly_group_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics.Client.list_anomaly_group_summaries)

```python
def list_anomaly_group_summaries(
    self,
    AnomalyDetectorArn: str,
    SensitivityThreshold: int,
    MaxResults: int = None,
    NextToken: str = None
) -> ListAnomalyGroupSummariesResponseTypeDef:
    pass
```

### list_anomaly_group_time_series

Type annotations for `boto3.client("lookoutmetrics").list_anomaly_group_time_series` method.

[Client.list_anomaly_group_time_series documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics.Client.list_anomaly_group_time_series)

```python
def list_anomaly_group_time_series(
    self,
    AnomalyDetectorArn: str,
    AnomalyGroupId: str,
    MetricName: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListAnomalyGroupTimeSeriesResponseTypeDef:
    pass
```

### list_metric_sets

Type annotations for `boto3.client("lookoutmetrics").list_metric_sets` method.

[Client.list_metric_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics.Client.list_metric_sets)

```python
def list_metric_sets(
    self,
    AnomalyDetectorArn: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListMetricSetsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("lookoutmetrics").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### put_feedback

Type annotations for `boto3.client("lookoutmetrics").put_feedback` method.

[Client.put_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics.Client.put_feedback)

```python
def put_feedback(
    self,
    AnomalyDetectorArn: str,
    AnomalyGroupTimeSeriesFeedback: AnomalyGroupTimeSeriesFeedbackTypeDef
) -> Dict[str, Any]:
    pass
```

### tag_resource

Type annotations for `boto3.client("lookoutmetrics").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("lookoutmetrics").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_anomaly_detector

Type annotations for `boto3.client("lookoutmetrics").update_anomaly_detector` method.

[Client.update_anomaly_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics.Client.update_anomaly_detector)

```python
def update_anomaly_detector(
    self,
    AnomalyDetectorArn: str,
    KmsKeyArn: str = None,
    AnomalyDetectorDescription: str = None,
    AnomalyDetectorConfig: AnomalyDetectorConfigTypeDef = None
) -> UpdateAnomalyDetectorResponseTypeDef:
    pass
```

### update_metric_set

Type annotations for `boto3.client("lookoutmetrics").update_metric_set` method.

[Client.update_metric_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html#LookoutMetrics.Client.update_metric_set)

```python
def update_metric_set(
    self,
    MetricSetArn: str,
    MetricSetDescription: str = None,
    MetricList: List["MetricTypeDef"] = None,
    Offset: int = None,
    TimestampColumn: "TimestampColumnTypeDef" = None,
    DimensionList: List[str] = None,
    MetricSetFrequency: Frequency = None,
    MetricSource: "MetricSourceTypeDef" = None
) -> UpdateMetricSetResponseTypeDef:
    pass
```



