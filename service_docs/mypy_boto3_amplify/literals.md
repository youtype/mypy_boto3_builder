# Literals for boto3 Amplify module

> [Index](../index.md) > [Amplify](./index.md) > Literals

Auto-generated documentation for [Amplify](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify)
type annotations stubs module [mypy_boto3_amplify](https://pypi.org/project/mypy-boto3-amplify/).

- [Literals for boto3 Amplify module](#literals-for-boto3-amplify-module)
  - [DomainStatus](#domainstatus)
  - [JobStatus](#jobstatus)
  - [JobType](#jobtype)
  - [ListAppsPaginatorName](#listappspaginatorname)
  - [ListBranchesPaginatorName](#listbranchespaginatorname)
  - [ListDomainAssociationsPaginatorName](#listdomainassociationspaginatorname)
  - [ListJobsPaginatorName](#listjobspaginatorname)
  - [Platform](#platform)
  - [Stage](#stage)

## DomainStatus

```python
from mypy_boto3_amplify.literals import DomainStatus
```

Values:

- `AVAILABLE`
- `CREATING`
- `FAILED`
- `IN_PROGRESS`
- `PENDING_DEPLOYMENT`
- `PENDING_VERIFICATION`
- `REQUESTING_CERTIFICATE`
- `UPDATING`

## JobStatus

```python
from mypy_boto3_amplify.literals import JobStatus
```

Values:

- `CANCELLED`
- `CANCELLING`
- `FAILED`
- `PENDING`
- `PROVISIONING`
- `RUNNING`
- `SUCCEED`

## JobType

```python
from mypy_boto3_amplify.literals import JobType
```

Values:

- `MANUAL`
- `RELEASE`
- `RETRY`
- `WEB_HOOK`

## ListAppsPaginatorName

```python
from mypy_boto3_amplify.literals import ListAppsPaginatorName
```

Values:

- `list_apps`

## ListBranchesPaginatorName

```python
from mypy_boto3_amplify.literals import ListBranchesPaginatorName
```

Values:

- `list_branches`

## ListDomainAssociationsPaginatorName

```python
from mypy_boto3_amplify.literals import ListDomainAssociationsPaginatorName
```

Values:

- `list_domain_associations`

## ListJobsPaginatorName

```python
from mypy_boto3_amplify.literals import ListJobsPaginatorName
```

Values:

- `list_jobs`

## Platform

```python
from mypy_boto3_amplify.literals import Platform
```

Values:

- `WEB`

## Stage

```python
from mypy_boto3_amplify.literals import Stage
```

Values:

- `BETA`
- `DEVELOPMENT`
- `EXPERIMENTAL`
- `PRODUCTION`
- `PULL_REQUEST`
