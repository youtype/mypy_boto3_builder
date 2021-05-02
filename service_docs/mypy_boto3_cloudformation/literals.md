# Literals for boto3 CloudFormation module

> [Index](../index.md) > [CloudFormation](./index.md) > Literals

Auto-generated documentation for [CloudFormation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation)
type annotations stubs module [mypy_boto3_cloudformation](https://pypi.org/project/mypy-boto3-cloudformation/).

- [Literals for boto3 CloudFormation module](#literals-for-boto3-cloudformation-module)
  - [AccountGateStatus](#accountgatestatus)
  - [CallAs](#callas)
  - [Capability](#capability)
  - [ChangeAction](#changeaction)
  - [ChangeSetCreateCompleteWaiterName](#changesetcreatecompletewaitername)
  - [ChangeSetStatus](#changesetstatus)
  - [ChangeSetType](#changesettype)
  - [ChangeSource](#changesource)
  - [ChangeType](#changetype)
  - [DeprecatedStatus](#deprecatedstatus)
  - [DescribeAccountLimitsPaginatorName](#describeaccountlimitspaginatorname)
  - [DescribeChangeSetPaginatorName](#describechangesetpaginatorname)
  - [DescribeStackEventsPaginatorName](#describestackeventspaginatorname)
  - [DescribeStacksPaginatorName](#describestackspaginatorname)
  - [DifferenceType](#differencetype)
  - [EvaluationType](#evaluationtype)
  - [ExecutionStatus](#executionstatus)
  - [HandlerErrorCode](#handlererrorcode)
  - [ListChangeSetsPaginatorName](#listchangesetspaginatorname)
  - [ListExportsPaginatorName](#listexportspaginatorname)
  - [ListImportsPaginatorName](#listimportspaginatorname)
  - [ListStackInstancesPaginatorName](#liststackinstancespaginatorname)
  - [ListStackResourcesPaginatorName](#liststackresourcespaginatorname)
  - [ListStackSetOperationResultsPaginatorName](#liststacksetoperationresultspaginatorname)
  - [ListStackSetOperationsPaginatorName](#liststacksetoperationspaginatorname)
  - [ListStackSetsPaginatorName](#liststacksetspaginatorname)
  - [ListStacksPaginatorName](#liststackspaginatorname)
  - [OnFailure](#onfailure)
  - [OperationStatus](#operationstatus)
  - [PermissionModels](#permissionmodels)
  - [ProvisioningType](#provisioningtype)
  - [RegionConcurrencyType](#regionconcurrencytype)
  - [RegistrationStatus](#registrationstatus)
  - [RegistryType](#registrytype)
  - [Replacement](#replacement)
  - [RequiresRecreation](#requiresrecreation)
  - [ResourceAttribute](#resourceattribute)
  - [ResourceSignalStatus](#resourcesignalstatus)
  - [ResourceStatus](#resourcestatus)
  - [StackCreateCompleteWaiterName](#stackcreatecompletewaitername)
  - [StackDeleteCompleteWaiterName](#stackdeletecompletewaitername)
  - [StackDriftDetectionStatus](#stackdriftdetectionstatus)
  - [StackDriftStatus](#stackdriftstatus)
  - [StackExistsWaiterName](#stackexistswaitername)
  - [StackImportCompleteWaiterName](#stackimportcompletewaitername)
  - [StackInstanceDetailedStatus](#stackinstancedetailedstatus)
  - [StackInstanceFilterName](#stackinstancefiltername)
  - [StackInstanceStatus](#stackinstancestatus)
  - [StackResourceDriftStatus](#stackresourcedriftstatus)
  - [StackRollbackCompleteWaiterName](#stackrollbackcompletewaitername)
  - [StackSetDriftDetectionStatus](#stacksetdriftdetectionstatus)
  - [StackSetDriftStatus](#stacksetdriftstatus)
  - [StackSetOperationAction](#stacksetoperationaction)
  - [StackSetOperationResultStatus](#stacksetoperationresultstatus)
  - [StackSetOperationStatus](#stacksetoperationstatus)
  - [StackSetStatus](#stacksetstatus)
  - [StackStatus](#stackstatus)
  - [StackUpdateCompleteWaiterName](#stackupdatecompletewaitername)
  - [TemplateStage](#templatestage)
  - [TypeRegistrationCompleteWaiterName](#typeregistrationcompletewaitername)
  - [Visibility](#visibility)

## AccountGateStatus

```python
from mypy_boto3_cloudformation.literals import AccountGateStatus
```

Values:

- `FAILED`
- `SKIPPED`
- `SUCCEEDED`

## CallAs

```python
from mypy_boto3_cloudformation.literals import CallAs
```

Values:

- `DELEGATED_ADMIN`
- `SELF`

## Capability

```python
from mypy_boto3_cloudformation.literals import Capability
```

Values:

- `CAPABILITY_AUTO_EXPAND`
- `CAPABILITY_IAM`
- `CAPABILITY_NAMED_IAM`

## ChangeAction

```python
from mypy_boto3_cloudformation.literals import ChangeAction
```

Values:

- `Add`
- `Dynamic`
- `Import`
- `Modify`
- `Remove`

## ChangeSetCreateCompleteWaiterName

```python
from mypy_boto3_cloudformation.literals import ChangeSetCreateCompleteWaiterName
```

Values:

- `change_set_create_complete`

## ChangeSetStatus

```python
from mypy_boto3_cloudformation.literals import ChangeSetStatus
```

Values:

- `CREATE_COMPLETE`
- `CREATE_IN_PROGRESS`
- `CREATE_PENDING`
- `DELETE_COMPLETE`
- `DELETE_FAILED`
- `DELETE_IN_PROGRESS`
- `DELETE_PENDING`
- `FAILED`

## ChangeSetType

```python
from mypy_boto3_cloudformation.literals import ChangeSetType
```

Values:

- `CREATE`
- `IMPORT`
- `UPDATE`

## ChangeSource

```python
from mypy_boto3_cloudformation.literals import ChangeSource
```

Values:

- `Automatic`
- `DirectModification`
- `ParameterReference`
- `ResourceAttribute`
- `ResourceReference`

## ChangeType

```python
from mypy_boto3_cloudformation.literals import ChangeType
```

Values:

- `Resource`

## DeprecatedStatus

```python
from mypy_boto3_cloudformation.literals import DeprecatedStatus
```

Values:

- `DEPRECATED`
- `LIVE`

## DescribeAccountLimitsPaginatorName

```python
from mypy_boto3_cloudformation.literals import DescribeAccountLimitsPaginatorName
```

Values:

- `describe_account_limits`

## DescribeChangeSetPaginatorName

```python
from mypy_boto3_cloudformation.literals import DescribeChangeSetPaginatorName
```

Values:

- `describe_change_set`

## DescribeStackEventsPaginatorName

```python
from mypy_boto3_cloudformation.literals import DescribeStackEventsPaginatorName
```

Values:

- `describe_stack_events`

## DescribeStacksPaginatorName

```python
from mypy_boto3_cloudformation.literals import DescribeStacksPaginatorName
```

Values:

- `describe_stacks`

## DifferenceType

```python
from mypy_boto3_cloudformation.literals import DifferenceType
```

Values:

- `ADD`
- `NOT_EQUAL`
- `REMOVE`

## EvaluationType

```python
from mypy_boto3_cloudformation.literals import EvaluationType
```

Values:

- `Dynamic`
- `Static`

## ExecutionStatus

```python
from mypy_boto3_cloudformation.literals import ExecutionStatus
```

Values:

- `AVAILABLE`
- `EXECUTE_COMPLETE`
- `EXECUTE_FAILED`
- `EXECUTE_IN_PROGRESS`
- `OBSOLETE`
- `UNAVAILABLE`

## HandlerErrorCode

```python
from mypy_boto3_cloudformation.literals import HandlerErrorCode
```

Values:

- `AccessDenied`
- `AlreadyExists`
- `GeneralServiceException`
- `InternalFailure`
- `InvalidCredentials`
- `InvalidRequest`
- `NetworkFailure`
- `NotFound`
- `NotStabilized`
- `NotUpdatable`
- `ResourceConflict`
- `ServiceInternalError`
- `ServiceLimitExceeded`
- `Throttling`

## ListChangeSetsPaginatorName

```python
from mypy_boto3_cloudformation.literals import ListChangeSetsPaginatorName
```

Values:

- `list_change_sets`

## ListExportsPaginatorName

```python
from mypy_boto3_cloudformation.literals import ListExportsPaginatorName
```

Values:

- `list_exports`

## ListImportsPaginatorName

```python
from mypy_boto3_cloudformation.literals import ListImportsPaginatorName
```

Values:

- `list_imports`

## ListStackInstancesPaginatorName

```python
from mypy_boto3_cloudformation.literals import ListStackInstancesPaginatorName
```

Values:

- `list_stack_instances`

## ListStackResourcesPaginatorName

```python
from mypy_boto3_cloudformation.literals import ListStackResourcesPaginatorName
```

Values:

- `list_stack_resources`

## ListStackSetOperationResultsPaginatorName

```python
from mypy_boto3_cloudformation.literals import ListStackSetOperationResultsPaginatorName
```

Values:

- `list_stack_set_operation_results`

## ListStackSetOperationsPaginatorName

```python
from mypy_boto3_cloudformation.literals import ListStackSetOperationsPaginatorName
```

Values:

- `list_stack_set_operations`

## ListStackSetsPaginatorName

```python
from mypy_boto3_cloudformation.literals import ListStackSetsPaginatorName
```

Values:

- `list_stack_sets`

## ListStacksPaginatorName

```python
from mypy_boto3_cloudformation.literals import ListStacksPaginatorName
```

Values:

- `list_stacks`

## OnFailure

```python
from mypy_boto3_cloudformation.literals import OnFailure
```

Values:

- `DELETE`
- `DO_NOTHING`
- `ROLLBACK`

## OperationStatus

```python
from mypy_boto3_cloudformation.literals import OperationStatus
```

Values:

- `FAILED`
- `IN_PROGRESS`
- `PENDING`
- `SUCCESS`

## PermissionModels

```python
from mypy_boto3_cloudformation.literals import PermissionModels
```

Values:

- `SELF_MANAGED`
- `SERVICE_MANAGED`

## ProvisioningType

```python
from mypy_boto3_cloudformation.literals import ProvisioningType
```

Values:

- `FULLY_MUTABLE`
- `IMMUTABLE`
- `NON_PROVISIONABLE`

## RegionConcurrencyType

```python
from mypy_boto3_cloudformation.literals import RegionConcurrencyType
```

Values:

- `PARALLEL`
- `SEQUENTIAL`

## RegistrationStatus

```python
from mypy_boto3_cloudformation.literals import RegistrationStatus
```

Values:

- `COMPLETE`
- `FAILED`
- `IN_PROGRESS`

## RegistryType

```python
from mypy_boto3_cloudformation.literals import RegistryType
```

Values:

- `MODULE`
- `RESOURCE`

## Replacement

```python
from mypy_boto3_cloudformation.literals import Replacement
```

Values:

- `Conditional`
- `False`
- `True`

## RequiresRecreation

```python
from mypy_boto3_cloudformation.literals import RequiresRecreation
```

Values:

- `Always`
- `Conditionally`
- `Never`

## ResourceAttribute

```python
from mypy_boto3_cloudformation.literals import ResourceAttribute
```

Values:

- `CreationPolicy`
- `DeletionPolicy`
- `Metadata`
- `Properties`
- `Tags`
- `UpdatePolicy`

## ResourceSignalStatus

```python
from mypy_boto3_cloudformation.literals import ResourceSignalStatus
```

Values:

- `FAILURE`
- `SUCCESS`

## ResourceStatus

```python
from mypy_boto3_cloudformation.literals import ResourceStatus
```

Values:

- `CREATE_COMPLETE`
- `CREATE_FAILED`
- `CREATE_IN_PROGRESS`
- `DELETE_COMPLETE`
- `DELETE_FAILED`
- `DELETE_IN_PROGRESS`
- `DELETE_SKIPPED`
- `IMPORT_COMPLETE`
- `IMPORT_FAILED`
- `IMPORT_IN_PROGRESS`
- `IMPORT_ROLLBACK_COMPLETE`
- `IMPORT_ROLLBACK_FAILED`
- `IMPORT_ROLLBACK_IN_PROGRESS`
- `UPDATE_COMPLETE`
- `UPDATE_FAILED`
- `UPDATE_IN_PROGRESS`

## StackCreateCompleteWaiterName

```python
from mypy_boto3_cloudformation.literals import StackCreateCompleteWaiterName
```

Values:

- `stack_create_complete`

## StackDeleteCompleteWaiterName

```python
from mypy_boto3_cloudformation.literals import StackDeleteCompleteWaiterName
```

Values:

- `stack_delete_complete`

## StackDriftDetectionStatus

```python
from mypy_boto3_cloudformation.literals import StackDriftDetectionStatus
```

Values:

- `DETECTION_COMPLETE`
- `DETECTION_FAILED`
- `DETECTION_IN_PROGRESS`

## StackDriftStatus

```python
from mypy_boto3_cloudformation.literals import StackDriftStatus
```

Values:

- `DRIFTED`
- `IN_SYNC`
- `NOT_CHECKED`
- `UNKNOWN`

## StackExistsWaiterName

```python
from mypy_boto3_cloudformation.literals import StackExistsWaiterName
```

Values:

- `stack_exists`

## StackImportCompleteWaiterName

```python
from mypy_boto3_cloudformation.literals import StackImportCompleteWaiterName
```

Values:

- `stack_import_complete`

## StackInstanceDetailedStatus

```python
from mypy_boto3_cloudformation.literals import StackInstanceDetailedStatus
```

Values:

- `CANCELLED`
- `FAILED`
- `INOPERABLE`
- `PENDING`
- `RUNNING`
- `SUCCEEDED`

## StackInstanceFilterName

```python
from mypy_boto3_cloudformation.literals import StackInstanceFilterName
```

Values:

- `DETAILED_STATUS`

## StackInstanceStatus

```python
from mypy_boto3_cloudformation.literals import StackInstanceStatus
```

Values:

- `CURRENT`
- `INOPERABLE`
- `OUTDATED`

## StackResourceDriftStatus

```python
from mypy_boto3_cloudformation.literals import StackResourceDriftStatus
```

Values:

- `DELETED`
- `IN_SYNC`
- `MODIFIED`
- `NOT_CHECKED`

## StackRollbackCompleteWaiterName

```python
from mypy_boto3_cloudformation.literals import StackRollbackCompleteWaiterName
```

Values:

- `stack_rollback_complete`

## StackSetDriftDetectionStatus

```python
from mypy_boto3_cloudformation.literals import StackSetDriftDetectionStatus
```

Values:

- `COMPLETED`
- `FAILED`
- `IN_PROGRESS`
- `PARTIAL_SUCCESS`
- `STOPPED`

## StackSetDriftStatus

```python
from mypy_boto3_cloudformation.literals import StackSetDriftStatus
```

Values:

- `DRIFTED`
- `IN_SYNC`
- `NOT_CHECKED`

## StackSetOperationAction

```python
from mypy_boto3_cloudformation.literals import StackSetOperationAction
```

Values:

- `CREATE`
- `DELETE`
- `DETECT_DRIFT`
- `UPDATE`

## StackSetOperationResultStatus

```python
from mypy_boto3_cloudformation.literals import StackSetOperationResultStatus
```

Values:

- `CANCELLED`
- `FAILED`
- `PENDING`
- `RUNNING`
- `SUCCEEDED`

## StackSetOperationStatus

```python
from mypy_boto3_cloudformation.literals import StackSetOperationStatus
```

Values:

- `FAILED`
- `QUEUED`
- `RUNNING`
- `STOPPED`
- `STOPPING`
- `SUCCEEDED`

## StackSetStatus

```python
from mypy_boto3_cloudformation.literals import StackSetStatus
```

Values:

- `ACTIVE`
- `DELETED`

## StackStatus

```python
from mypy_boto3_cloudformation.literals import StackStatus
```

Values:

- `CREATE_COMPLETE`
- `CREATE_FAILED`
- `CREATE_IN_PROGRESS`
- `DELETE_COMPLETE`
- `DELETE_FAILED`
- `DELETE_IN_PROGRESS`
- `IMPORT_COMPLETE`
- `IMPORT_IN_PROGRESS`
- `IMPORT_ROLLBACK_COMPLETE`
- `IMPORT_ROLLBACK_FAILED`
- `IMPORT_ROLLBACK_IN_PROGRESS`
- `REVIEW_IN_PROGRESS`
- `ROLLBACK_COMPLETE`
- `ROLLBACK_FAILED`
- `ROLLBACK_IN_PROGRESS`
- `UPDATE_COMPLETE`
- `UPDATE_COMPLETE_CLEANUP_IN_PROGRESS`
- `UPDATE_IN_PROGRESS`
- `UPDATE_ROLLBACK_COMPLETE`
- `UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS`
- `UPDATE_ROLLBACK_FAILED`
- `UPDATE_ROLLBACK_IN_PROGRESS`

## StackUpdateCompleteWaiterName

```python
from mypy_boto3_cloudformation.literals import StackUpdateCompleteWaiterName
```

Values:

- `stack_update_complete`

## TemplateStage

```python
from mypy_boto3_cloudformation.literals import TemplateStage
```

Values:

- `Original`
- `Processed`

## TypeRegistrationCompleteWaiterName

```python
from mypy_boto3_cloudformation.literals import TypeRegistrationCompleteWaiterName
```

Values:

- `type_registration_complete`

## Visibility

```python
from mypy_boto3_cloudformation.literals import Visibility
```

Values:

- `PRIVATE`
- `PUBLIC`
