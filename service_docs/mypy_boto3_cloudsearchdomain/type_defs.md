# Structures for boto3 CloudSearchDomain module

> [Index](../index.md) > [CloudSearchDomain](./index.md) > Structures

Auto-generated documentation for [CloudSearchDomain](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearchdomain.html#CloudSearchDomain)
type annotations stubs module [mypy_boto3_cloudsearchdomain](https://pypi.org/project/mypy-boto3-cloudsearchdomain/).

- [Structures for boto3 CloudSearchDomain module](#structures-for-boto3-cloudsearchdomain-module)
  - [BucketInfoTypeDef](#bucketinfotypedef)
  - [BucketTypeDef](#buckettypedef)
  - [DocumentServiceWarningTypeDef](#documentservicewarningtypedef)
  - [FieldStatsTypeDef](#fieldstatstypedef)
  - [HitTypeDef](#hittypedef)
  - [HitsTypeDef](#hitstypedef)
  - [SearchResponseTypeDef](#searchresponsetypedef)
  - [SearchStatusTypeDef](#searchstatustypedef)
  - [SuggestModelTypeDef](#suggestmodeltypedef)
  - [SuggestResponseTypeDef](#suggestresponsetypedef)
  - [SuggestStatusTypeDef](#suggeststatustypedef)
  - [SuggestionMatchTypeDef](#suggestionmatchtypedef)
  - [UploadDocumentsResponseTypeDef](#uploaddocumentsresponsetypedef)

## BucketInfoTypeDef

```python
from mypy_boto3_cloudsearchdomain.type_defs import BucketInfoTypeDef
```




Optional fields:
- `buckets`: `List["BucketTypeDef"]`


## BucketTypeDef

```python
from mypy_boto3_cloudsearchdomain.type_defs import BucketTypeDef
```




Optional fields:
- `value`: `str`
- `count`: `int`


## DocumentServiceWarningTypeDef

```python
from mypy_boto3_cloudsearchdomain.type_defs import DocumentServiceWarningTypeDef
```




Optional fields:
- `message`: `str`


## FieldStatsTypeDef

```python
from mypy_boto3_cloudsearchdomain.type_defs import FieldStatsTypeDef
```




Optional fields:
- `min`: `str`
- `max`: `str`
- `count`: `int`
- `missing`: `int`
- `sum`: `float`
- `sumOfSquares`: `float`
- `mean`: `str`
- `stddev`: `float`


## HitTypeDef

```python
from mypy_boto3_cloudsearchdomain.type_defs import HitTypeDef
```




Optional fields:
- `id`: `str`
- `fields`: `Dict[str, List[str]]`
- `exprs`: `Dict[str, str]`
- `highlights`: `Dict[str, str]`


## HitsTypeDef

```python
from mypy_boto3_cloudsearchdomain.type_defs import HitsTypeDef
```




Optional fields:
- `found`: `int`
- `start`: `int`
- `cursor`: `str`
- `hit`: `List["HitTypeDef"]`


## SearchResponseTypeDef

```python
from mypy_boto3_cloudsearchdomain.type_defs import SearchResponseTypeDef
```




Optional fields:
- `status`: `"SearchStatusTypeDef"`
- `hits`: `"HitsTypeDef"`
- `facets`: `Dict[str, "BucketInfoTypeDef"]`
- `stats`: `Dict[str, "FieldStatsTypeDef"]`


## SearchStatusTypeDef

```python
from mypy_boto3_cloudsearchdomain.type_defs import SearchStatusTypeDef
```




Optional fields:
- `timems`: `int`
- `rid`: `str`


## SuggestModelTypeDef

```python
from mypy_boto3_cloudsearchdomain.type_defs import SuggestModelTypeDef
```




Optional fields:
- `query`: `str`
- `found`: `int`
- `suggestions`: `List["SuggestionMatchTypeDef"]`


## SuggestResponseTypeDef

```python
from mypy_boto3_cloudsearchdomain.type_defs import SuggestResponseTypeDef
```




Optional fields:
- `status`: `"SuggestStatusTypeDef"`
- `suggest`: `"SuggestModelTypeDef"`


## SuggestStatusTypeDef

```python
from mypy_boto3_cloudsearchdomain.type_defs import SuggestStatusTypeDef
```




Optional fields:
- `timems`: `int`
- `rid`: `str`


## SuggestionMatchTypeDef

```python
from mypy_boto3_cloudsearchdomain.type_defs import SuggestionMatchTypeDef
```




Optional fields:
- `suggestion`: `str`
- `score`: `int`
- `id`: `str`


## UploadDocumentsResponseTypeDef

```python
from mypy_boto3_cloudsearchdomain.type_defs import UploadDocumentsResponseTypeDef
```




Optional fields:
- `status`: `str`
- `adds`: `int`
- `deletes`: `int`
- `warnings`: `List["DocumentServiceWarningTypeDef"]`

