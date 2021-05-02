# ComprehendMedicalClient for boto3 ComprehendMedical module

> [Index](../index.md) > [ComprehendMedical](./index.md) > ComprehendMedicalClient

Auto-generated documentation for [ComprehendMedical](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html#ComprehendMedical)
type annotations stubs module [mypy_boto3_comprehendmedical](https://pypi.org/project/mypy-boto3-comprehendmedical/).

- [ComprehendMedicalClient for boto3 ComprehendMedical module](#comprehendmedicalclient-for-boto3-comprehendmedical-module)
  - [ComprehendMedicalClient](#comprehendmedicalclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [describe_entities_detection_v2_job](#describe_entities_detection_v2_job)
    - [describe_icd10_cm_inference_job](#describe_icd10_cm_inference_job)
    - [describe_phi_detection_job](#describe_phi_detection_job)
    - [describe_rx_norm_inference_job](#describe_rx_norm_inference_job)
    - [detect_entities](#detect_entities)
    - [detect_entities_v2](#detect_entities_v2)
    - [detect_phi](#detect_phi)
    - [generate_presigned_url](#generate_presigned_url)
    - [infer_icd10_cm](#infer_icd10_cm)
    - [infer_rx_norm](#infer_rx_norm)
    - [list_entities_detection_v2_jobs](#list_entities_detection_v2_jobs)
    - [list_icd10_cm_inference_jobs](#list_icd10_cm_inference_jobs)
    - [list_phi_detection_jobs](#list_phi_detection_jobs)
    - [list_rx_norm_inference_jobs](#list_rx_norm_inference_jobs)
    - [start_entities_detection_v2_job](#start_entities_detection_v2_job)
    - [start_icd10_cm_inference_job](#start_icd10_cm_inference_job)
    - [start_phi_detection_job](#start_phi_detection_job)
    - [start_rx_norm_inference_job](#start_rx_norm_inference_job)
    - [stop_entities_detection_v2_job](#stop_entities_detection_v2_job)
    - [stop_icd10_cm_inference_job](#stop_icd10_cm_inference_job)
    - [stop_phi_detection_job](#stop_phi_detection_job)
    - [stop_rx_norm_inference_job](#stop_rx_norm_inference_job)

## ComprehendMedicalClient

Type annotations for `boto3.client("comprehendmedical")`

Can be used directly:

```python
from mypy_boto3_comprehendmedical.client import ComprehendMedicalClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_comprehendmedical.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InternalServerException`
- `Exceptions.InvalidEncodingException`
- `Exceptions.InvalidRequestException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceUnavailableException`
- `Exceptions.TextSizeLimitExceededException`
- `Exceptions.TooManyRequestsException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("comprehendmedical").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html#ComprehendMedical.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### describe_entities_detection_v2_job

Type annotations for `boto3.client("comprehendmedical").describe_entities_detection_v2_job` method.

[Client.describe_entities_detection_v2_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html#ComprehendMedical.Client.describe_entities_detection_v2_job)

```python
def describe_entities_detection_v2_job(
    self,
    JobId: str
) -> DescribeEntitiesDetectionV2JobResponseTypeDef:
    pass
```

### describe_icd10_cm_inference_job

Type annotations for `boto3.client("comprehendmedical").describe_icd10_cm_inference_job` method.

[Client.describe_icd10_cm_inference_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html#ComprehendMedical.Client.describe_icd10_cm_inference_job)

```python
def describe_icd10_cm_inference_job(
    self,
    JobId: str
) -> DescribeICD10CMInferenceJobResponseTypeDef:
    pass
```

### describe_phi_detection_job

Type annotations for `boto3.client("comprehendmedical").describe_phi_detection_job` method.

[Client.describe_phi_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html#ComprehendMedical.Client.describe_phi_detection_job)

```python
def describe_phi_detection_job(
    self,
    JobId: str
) -> DescribePHIDetectionJobResponseTypeDef:
    pass
```

### describe_rx_norm_inference_job

Type annotations for `boto3.client("comprehendmedical").describe_rx_norm_inference_job` method.

[Client.describe_rx_norm_inference_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html#ComprehendMedical.Client.describe_rx_norm_inference_job)

```python
def describe_rx_norm_inference_job(
    self,
    JobId: str
) -> DescribeRxNormInferenceJobResponseTypeDef:
    pass
```

### detect_entities

Type annotations for `boto3.client("comprehendmedical").detect_entities` method.

[Client.detect_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html#ComprehendMedical.Client.detect_entities)

```python
def detect_entities(
    self,
    Text: str
) -> DetectEntitiesResponseTypeDef:
    pass
```

### detect_entities_v2

Type annotations for `boto3.client("comprehendmedical").detect_entities_v2` method.

[Client.detect_entities_v2 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html#ComprehendMedical.Client.detect_entities_v2)

```python
def detect_entities_v2(
    self,
    Text: str
) -> DetectEntitiesV2ResponseTypeDef:
    pass
```

### detect_phi

Type annotations for `boto3.client("comprehendmedical").detect_phi` method.

[Client.detect_phi documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html#ComprehendMedical.Client.detect_phi)

```python
def detect_phi(
    self,
    Text: str
) -> DetectPHIResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("comprehendmedical").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html#ComprehendMedical.Client.generate_presigned_url)

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

### infer_icd10_cm

Type annotations for `boto3.client("comprehendmedical").infer_icd10_cm` method.

[Client.infer_icd10_cm documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html#ComprehendMedical.Client.infer_icd10_cm)

```python
def infer_icd10_cm(
    self,
    Text: str
) -> InferICD10CMResponseTypeDef:
    pass
```

### infer_rx_norm

Type annotations for `boto3.client("comprehendmedical").infer_rx_norm` method.

[Client.infer_rx_norm documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html#ComprehendMedical.Client.infer_rx_norm)

```python
def infer_rx_norm(
    self,
    Text: str
) -> InferRxNormResponseTypeDef:
    pass
```

### list_entities_detection_v2_jobs

Type annotations for `boto3.client("comprehendmedical").list_entities_detection_v2_jobs` method.

[Client.list_entities_detection_v2_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html#ComprehendMedical.Client.list_entities_detection_v2_jobs)

```python
def list_entities_detection_v2_jobs(
    self,
    Filter: ComprehendMedicalAsyncJobFilterTypeDef = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListEntitiesDetectionV2JobsResponseTypeDef:
    pass
```

### list_icd10_cm_inference_jobs

Type annotations for `boto3.client("comprehendmedical").list_icd10_cm_inference_jobs` method.

[Client.list_icd10_cm_inference_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html#ComprehendMedical.Client.list_icd10_cm_inference_jobs)

```python
def list_icd10_cm_inference_jobs(
    self,
    Filter: ComprehendMedicalAsyncJobFilterTypeDef = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListICD10CMInferenceJobsResponseTypeDef:
    pass
```

### list_phi_detection_jobs

Type annotations for `boto3.client("comprehendmedical").list_phi_detection_jobs` method.

[Client.list_phi_detection_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html#ComprehendMedical.Client.list_phi_detection_jobs)

```python
def list_phi_detection_jobs(
    self,
    Filter: ComprehendMedicalAsyncJobFilterTypeDef = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListPHIDetectionJobsResponseTypeDef:
    pass
```

### list_rx_norm_inference_jobs

Type annotations for `boto3.client("comprehendmedical").list_rx_norm_inference_jobs` method.

[Client.list_rx_norm_inference_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html#ComprehendMedical.Client.list_rx_norm_inference_jobs)

```python
def list_rx_norm_inference_jobs(
    self,
    Filter: ComprehendMedicalAsyncJobFilterTypeDef = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListRxNormInferenceJobsResponseTypeDef:
    pass
```

### start_entities_detection_v2_job

Type annotations for `boto3.client("comprehendmedical").start_entities_detection_v2_job` method.

[Client.start_entities_detection_v2_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html#ComprehendMedical.Client.start_entities_detection_v2_job)

```python
def start_entities_detection_v2_job(
    self,
    InputDataConfig: "InputDataConfigTypeDef",
    OutputDataConfig: "OutputDataConfigTypeDef",
    DataAccessRoleArn: str,
    LanguageCode: Literal['en'],
    JobName: str = None,
    ClientRequestToken: str = None,
    KMSKey: str = None
) -> StartEntitiesDetectionV2JobResponseTypeDef:
    pass
```

### start_icd10_cm_inference_job

Type annotations for `boto3.client("comprehendmedical").start_icd10_cm_inference_job` method.

[Client.start_icd10_cm_inference_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html#ComprehendMedical.Client.start_icd10_cm_inference_job)

```python
def start_icd10_cm_inference_job(
    self,
    InputDataConfig: "InputDataConfigTypeDef",
    OutputDataConfig: "OutputDataConfigTypeDef",
    DataAccessRoleArn: str,
    LanguageCode: Literal['en'],
    JobName: str = None,
    ClientRequestToken: str = None,
    KMSKey: str = None
) -> StartICD10CMInferenceJobResponseTypeDef:
    pass
```

### start_phi_detection_job

Type annotations for `boto3.client("comprehendmedical").start_phi_detection_job` method.

[Client.start_phi_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html#ComprehendMedical.Client.start_phi_detection_job)

```python
def start_phi_detection_job(
    self,
    InputDataConfig: "InputDataConfigTypeDef",
    OutputDataConfig: "OutputDataConfigTypeDef",
    DataAccessRoleArn: str,
    LanguageCode: Literal['en'],
    JobName: str = None,
    ClientRequestToken: str = None,
    KMSKey: str = None
) -> StartPHIDetectionJobResponseTypeDef:
    pass
```

### start_rx_norm_inference_job

Type annotations for `boto3.client("comprehendmedical").start_rx_norm_inference_job` method.

[Client.start_rx_norm_inference_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html#ComprehendMedical.Client.start_rx_norm_inference_job)

```python
def start_rx_norm_inference_job(
    self,
    InputDataConfig: "InputDataConfigTypeDef",
    OutputDataConfig: "OutputDataConfigTypeDef",
    DataAccessRoleArn: str,
    LanguageCode: Literal['en'],
    JobName: str = None,
    ClientRequestToken: str = None,
    KMSKey: str = None
) -> StartRxNormInferenceJobResponseTypeDef:
    pass
```

### stop_entities_detection_v2_job

Type annotations for `boto3.client("comprehendmedical").stop_entities_detection_v2_job` method.

[Client.stop_entities_detection_v2_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html#ComprehendMedical.Client.stop_entities_detection_v2_job)

```python
def stop_entities_detection_v2_job(
    self,
    JobId: str
) -> StopEntitiesDetectionV2JobResponseTypeDef:
    pass
```

### stop_icd10_cm_inference_job

Type annotations for `boto3.client("comprehendmedical").stop_icd10_cm_inference_job` method.

[Client.stop_icd10_cm_inference_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html#ComprehendMedical.Client.stop_icd10_cm_inference_job)

```python
def stop_icd10_cm_inference_job(
    self,
    JobId: str
) -> StopICD10CMInferenceJobResponseTypeDef:
    pass
```

### stop_phi_detection_job

Type annotations for `boto3.client("comprehendmedical").stop_phi_detection_job` method.

[Client.stop_phi_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html#ComprehendMedical.Client.stop_phi_detection_job)

```python
def stop_phi_detection_job(
    self,
    JobId: str
) -> StopPHIDetectionJobResponseTypeDef:
    pass
```

### stop_rx_norm_inference_job

Type annotations for `boto3.client("comprehendmedical").stop_rx_norm_inference_job` method.

[Client.stop_rx_norm_inference_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html#ComprehendMedical.Client.stop_rx_norm_inference_job)

```python
def stop_rx_norm_inference_job(
    self,
    JobId: str
) -> StopRxNormInferenceJobResponseTypeDef:
    pass
```



