# Literals for boto3 Imagebuilder module

> [Index](../index.md) > [Imagebuilder](./index.md) > Literals

Auto-generated documentation for [Imagebuilder](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder)
type annotations stubs module [mypy_boto3_imagebuilder](https://pypi.org/project/mypy-boto3-imagebuilder/).

- [Literals for boto3 Imagebuilder module](#literals-for-boto3-imagebuilder-module)
  - [ComponentFormat](#componentformat)
  - [ComponentType](#componenttype)
  - [ContainerRepositoryService](#containerrepositoryservice)
  - [ContainerType](#containertype)
  - [EbsVolumeType](#ebsvolumetype)
  - [ImageStatus](#imagestatus)
  - [ImageType](#imagetype)
  - [Ownership](#ownership)
  - [PipelineExecutionStartCondition](#pipelineexecutionstartcondition)
  - [PipelineStatus](#pipelinestatus)
  - [Platform](#platform)

## ComponentFormat

```python
from mypy_boto3_imagebuilder.literals import ComponentFormat
```

Values:

- `SHELL`

## ComponentType

```python
from mypy_boto3_imagebuilder.literals import ComponentType
```

Values:

- `BUILD`
- `TEST`

## ContainerRepositoryService

```python
from mypy_boto3_imagebuilder.literals import ContainerRepositoryService
```

Values:

- `ECR`

## ContainerType

```python
from mypy_boto3_imagebuilder.literals import ContainerType
```

Values:

- `DOCKER`

## EbsVolumeType

```python
from mypy_boto3_imagebuilder.literals import EbsVolumeType
```

Values:

- `gp2`
- `gp3`
- `io1`
- `io2`
- `sc1`
- `st1`
- `standard`

## ImageStatus

```python
from mypy_boto3_imagebuilder.literals import ImageStatus
```

Values:

- `AVAILABLE`
- `BUILDING`
- `CANCELLED`
- `CREATING`
- `DELETED`
- `DEPRECATED`
- `DISTRIBUTING`
- `FAILED`
- `INTEGRATING`
- `PENDING`
- `TESTING`

## ImageType

```python
from mypy_boto3_imagebuilder.literals import ImageType
```

Values:

- `AMI`
- `DOCKER`

## Ownership

```python
from mypy_boto3_imagebuilder.literals import Ownership
```

Values:

- `Amazon`
- `Self`
- `Shared`

## PipelineExecutionStartCondition

```python
from mypy_boto3_imagebuilder.literals import PipelineExecutionStartCondition
```

Values:

- `EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE`
- `EXPRESSION_MATCH_ONLY`

## PipelineStatus

```python
from mypy_boto3_imagebuilder.literals import PipelineStatus
```

Values:

- `DISABLED`
- `ENABLED`

## Platform

```python
from mypy_boto3_imagebuilder.literals import Platform
```

Values:

- `Linux`
- `Windows`
