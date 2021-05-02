# Literals for boto3 LexModelsV2 module

> [Index](../index.md) > [LexModelsV2](./index.md) > Literals

Auto-generated documentation for [LexModelsV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2)
type annotations stubs module [mypy_boto3_lexv2_models](https://pypi.org/project/mypy-boto3-lexv2-models/).

- [Literals for boto3 LexModelsV2 module](#literals-for-boto3-lexmodelsv2-module)
  - [BotAliasStatus](#botaliasstatus)
  - [BotFilterName](#botfiltername)
  - [BotFilterOperator](#botfilteroperator)
  - [BotLocaleFilterName](#botlocalefiltername)
  - [BotLocaleFilterOperator](#botlocalefilteroperator)
  - [BotLocaleSortAttribute](#botlocalesortattribute)
  - [BotLocaleStatus](#botlocalestatus)
  - [BotSortAttribute](#botsortattribute)
  - [BotStatus](#botstatus)
  - [BotVersionSortAttribute](#botversionsortattribute)
  - [BuiltInIntentSortAttribute](#builtinintentsortattribute)
  - [BuiltInSlotTypeSortAttribute](#builtinslottypesortattribute)
  - [IntentFilterName](#intentfiltername)
  - [IntentFilterOperator](#intentfilteroperator)
  - [IntentSortAttribute](#intentsortattribute)
  - [ObfuscationSettingType](#obfuscationsettingtype)
  - [SlotConstraint](#slotconstraint)
  - [SlotFilterName](#slotfiltername)
  - [SlotFilterOperator](#slotfilteroperator)
  - [SlotSortAttribute](#slotsortattribute)
  - [SlotTypeFilterName](#slottypefiltername)
  - [SlotTypeFilterOperator](#slottypefilteroperator)
  - [SlotTypeSortAttribute](#slottypesortattribute)
  - [SlotValueResolutionStrategy](#slotvalueresolutionstrategy)
  - [SortOrder](#sortorder)

## BotAliasStatus

```python
from mypy_boto3_lexv2_models.literals import BotAliasStatus
```

Values:

- `Available`
- `Creating`
- `Deleting`
- `Failed`

## BotFilterName

```python
from mypy_boto3_lexv2_models.literals import BotFilterName
```

Values:

- `BotName`

## BotFilterOperator

```python
from mypy_boto3_lexv2_models.literals import BotFilterOperator
```

Values:

- `CO`
- `EQ`

## BotLocaleFilterName

```python
from mypy_boto3_lexv2_models.literals import BotLocaleFilterName
```

Values:

- `BotLocaleName`

## BotLocaleFilterOperator

```python
from mypy_boto3_lexv2_models.literals import BotLocaleFilterOperator
```

Values:

- `CO`
- `EQ`

## BotLocaleSortAttribute

```python
from mypy_boto3_lexv2_models.literals import BotLocaleSortAttribute
```

Values:

- `BotLocaleName`

## BotLocaleStatus

```python
from mypy_boto3_lexv2_models.literals import BotLocaleStatus
```

Values:

- `Building`
- `Built`
- `Creating`
- `Deleting`
- `Failed`
- `NotBuilt`
- `ReadyExpressTesting`

## BotSortAttribute

```python
from mypy_boto3_lexv2_models.literals import BotSortAttribute
```

Values:

- `BotName`

## BotStatus

```python
from mypy_boto3_lexv2_models.literals import BotStatus
```

Values:

- `Available`
- `Creating`
- `Deleting`
- `Failed`
- `Inactive`
- `Versioning`

## BotVersionSortAttribute

```python
from mypy_boto3_lexv2_models.literals import BotVersionSortAttribute
```

Values:

- `BotVersion`

## BuiltInIntentSortAttribute

```python
from mypy_boto3_lexv2_models.literals import BuiltInIntentSortAttribute
```

Values:

- `IntentSignature`

## BuiltInSlotTypeSortAttribute

```python
from mypy_boto3_lexv2_models.literals import BuiltInSlotTypeSortAttribute
```

Values:

- `SlotTypeSignature`

## IntentFilterName

```python
from mypy_boto3_lexv2_models.literals import IntentFilterName
```

Values:

- `IntentName`

## IntentFilterOperator

```python
from mypy_boto3_lexv2_models.literals import IntentFilterOperator
```

Values:

- `CO`
- `EQ`

## IntentSortAttribute

```python
from mypy_boto3_lexv2_models.literals import IntentSortAttribute
```

Values:

- `IntentName`
- `LastUpdatedDateTime`

## ObfuscationSettingType

```python
from mypy_boto3_lexv2_models.literals import ObfuscationSettingType
```

Values:

- `DefaultObfuscation`
- `None`

## SlotConstraint

```python
from mypy_boto3_lexv2_models.literals import SlotConstraint
```

Values:

- `Optional`
- `Required`

## SlotFilterName

```python
from mypy_boto3_lexv2_models.literals import SlotFilterName
```

Values:

- `SlotName`

## SlotFilterOperator

```python
from mypy_boto3_lexv2_models.literals import SlotFilterOperator
```

Values:

- `CO`
- `EQ`

## SlotSortAttribute

```python
from mypy_boto3_lexv2_models.literals import SlotSortAttribute
```

Values:

- `LastUpdatedDateTime`
- `SlotName`

## SlotTypeFilterName

```python
from mypy_boto3_lexv2_models.literals import SlotTypeFilterName
```

Values:

- `SlotTypeName`

## SlotTypeFilterOperator

```python
from mypy_boto3_lexv2_models.literals import SlotTypeFilterOperator
```

Values:

- `CO`
- `EQ`

## SlotTypeSortAttribute

```python
from mypy_boto3_lexv2_models.literals import SlotTypeSortAttribute
```

Values:

- `LastUpdatedDateTime`
- `SlotTypeName`

## SlotValueResolutionStrategy

```python
from mypy_boto3_lexv2_models.literals import SlotValueResolutionStrategy
```

Values:

- `OriginalValue`
- `TopResolution`

## SortOrder

```python
from mypy_boto3_lexv2_models.literals import SortOrder
```

Values:

- `Ascending`
- `Descending`
